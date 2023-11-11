"""Functions related to tangent vector field generation."""

import functools
from typing import List, Tuple

import jax
import jax.numpy as jnp

from fmmax import basis, fft, utils


def compute_field_jones_direct(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    fourier_loss_weight: float,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Compute tangent vector field using the Jones direct method."""
    return compute_tangent_field(
        arr=arr,
        expansion=expansion,
        primitive_lattice_vectors=primitive_lattice_vectors,
        use_jones_direct=True,
        fourier_loss_weight=fourier_loss_weight,
    )


def compute_field_pol(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    fourier_loss_weight: float,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Compute tangent vector field using the Pol method."""
    return compute_tangent_field(
        arr=arr,
        expansion=expansion,
        primitive_lattice_vectors=primitive_lattice_vectors,
        use_jones_direct=False,
        fourier_loss_weight=fourier_loss_weight,
    )


def compute_field_jones(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    fourier_loss_weight: float,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Compute tangent vector field using the Jones method."""
    tx, ty = compute_tangent_field(
        arr=arr,
        expansion=expansion,
        primitive_lattice_vectors=primitive_lattice_vectors,
        use_jones_direct=False,
        fourier_loss_weight=fourier_loss_weight,
    )
    jxjy = normalize_jones(jnp.stack([tx, ty], axis=-1))
    jx = jxjy[..., 0]
    jy = jxjy[..., 1]
    return jx, jy


def compute_field_normal(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    fourier_loss_weight: float,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Compute tangent vector field using the Normal method."""
    tx, ty = compute_tangent_field(
        arr=arr,
        expansion=expansion,
        primitive_lattice_vectors=primitive_lattice_vectors,
        use_jones_direct=False,
        fourier_loss_weight=fourier_loss_weight,
    )
    txty = normalize_elementwise(jnp.stack([tx, ty], axis=-1))
    tx = txty[..., 0]
    ty = txty[..., 1]
    return tx, ty


# -----------------------------------------------------------------------------
# Underlying functions used to compute all variants of the tangent fields.
# -----------------------------------------------------------------------------


def compute_tangent_field(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    use_jones_direct: bool,
    fourier_loss_weight: float,
    steps: int = 1,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Compute the tangent vector field for `arr`.

    The calculation finds the minimum of a quadratic loss function using a single
    Newton iteration. Rather than optimizing the real-space tangent field, the
    Fourier coefficients are directly optimized.

    Args:
        arr: The array for which the normal vector field is sought.
        expansion: The Fourier expansion for which the field is to be optimized.
        primitive_lattice_vectors: Define the unit cell coordinates.
        use_jones_direct: Specifies whether the complex Jones field is to be sought.
        fourier_loss_weight: Determines the weight of the loss term penalizing
            Fourier terms corresponding to high frequencies.
        steps: The number of Newton iterations to carry out. Generally, the default
            single iteration is sufficient to obtain converged fields.

    Returns:
        The normal field, `(tx, ty)`.
    """
    batch_shape = arr.shape[:-2]
    arr = utils.atleast_nd(arr, n=3)
    arr = arr.reshape((-1,) + arr.shape[-2:])

    field_fn = jax.vmap(
        functools.partial(
            _compute_tangent_field_no_batch,
            use_jones_direct=use_jones_direct,
            fourier_loss_weight=fourier_loss_weight,
            steps=steps,
        ),
        in_axes=(0, None, None),
    )
    field = field_fn(
        arr,
        expansion,
        primitive_lattice_vectors,
    )
    field = field.reshape(batch_shape + field.shape[-3:])
    tx = field[..., 0]
    ty = field[..., 1]
    return tx, ty


def _compute_tangent_field_no_batch(
    arr: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    use_jones_direct: bool,
    fourier_loss_weight: float,
    steps: int,
) -> jnp.ndarray:
    """Compute the tangent vector field for `arr` with no batch dimensions."""
    assert primitive_lattice_vectors.u.shape == (2,)
    assert arr.ndim == 2

    grid_shape: Tuple[int, int] = arr.shape[-2:]  # type: ignore[assignment]
    arr = _filter_and_adjust_resolution(arr, expansion)
    grad = compute_gradient(arr, primitive_lattice_vectors)

    # Normalize the gradient if its maximum magnitude exceeds unity.
    grad_magnitude = _field_magnitude(grad)
    norm = jnp.maximum(1.0, jnp.amax(grad_magnitude, axis=(-3, -2, -1), keepdims=True))
    grad /= norm

    elementwise_alignment_weight = _field_magnitude(grad)

    target_field = jnp.stack([grad[..., 1], -grad[..., 0]], axis=-1)
    target_field = normalize_elementwise(target_field)
    if use_jones_direct:
        target_field = normalize_jones(target_field)

    initial_field = target_field

    fourier_field = fft.fft(initial_field, expansion=expansion, axes=(-3, -2))
    flat_fourier_field = fourier_field.flatten()

    for _ in range(steps):
        _, jac, hessian = field_loss_value_jac_and_hessian(
            flat_fourier_field=flat_fourier_field,
            expansion=expansion,
            primitive_lattice_vectors=primitive_lattice_vectors,
            target_field=target_field,
            elementwise_alignment_loss_weight=elementwise_alignment_weight,
            fourier_loss_weight=fourier_loss_weight,
        )
        flat_fourier_field -= jnp.linalg.solve(hessian, jac.conj())

    fourier_field = flat_fourier_field.reshape((expansion.num_terms, 2))
    field = fft.ifft(fourier_field, expansion=expansion, shape=grid_shape, axis=-2)

    # Manually set the field in cases where `arr` is constant.
    grad_is_zero = jnp.all(jnp.isclose(grad, 0.0), axis=(-3, -2, -1), keepdims=True)
    field = jnp.where(grad_is_zero, jnp.ones_like(field), field)
    return normalize(field)


# -------------------------------------------------------------------------------------
# Normalization and transform functions.
# -------------------------------------------------------------------------------------


def normalize_jones(field: jnp.ndarray) -> jnp.ndarray:
    """Generates a Jones vector field following the "Jones" method of [2012 Liu]."""
    assert field.shape[-1] == 2
    field = normalize(field)
    magnitude = _field_magnitude(field)

    magnitude_near_zero = jnp.isclose(magnitude, 0.0)
    magnitude_safe = jnp.where(magnitude_near_zero, 1.0, magnitude)
    tx_norm = jnp.where(
        magnitude_near_zero,
        1 / jnp.sqrt(2),
        field[..., 0, jnp.newaxis] / magnitude_safe,
    )
    ty_norm = jnp.where(
        magnitude_near_zero,
        1 / jnp.sqrt(2),
        field[..., 1, jnp.newaxis] / magnitude_safe,
    )

    phi = jnp.pi / 8 * (1 + jnp.cos(jnp.pi * magnitude))
    theta = _angle(tx_norm + 1j * ty_norm)

    jx = jnp.exp(1j * theta) * (tx_norm * jnp.cos(phi) - ty_norm * 1j * jnp.sin(phi))
    jy = jnp.exp(1j * theta) * (ty_norm * jnp.cos(phi) + tx_norm * 1j * jnp.sin(phi))
    return jnp.concatenate([jx, jy], axis=-1)


def normalize_elementwise(field: jnp.ndarray) -> jnp.ndarray:
    """Normalize the elements of `field` to have magnitude `1` everywhere."""
    magnitude = _field_magnitude(field)
    magnitude_safe = jnp.where(jnp.isclose(magnitude, 0), 1, magnitude)
    return field / magnitude_safe


def normalize(field: jnp.ndarray) -> jnp.ndarray:
    """Normalize `field` so that it has maximum magnitude `1`."""
    max_magnitude = _max_field_magnitude(field)
    max_magnitude_safe = jnp.where(jnp.isclose(max_magnitude, 0), 1, max_magnitude)
    return field / max_magnitude_safe


def _field_magnitude(field: jnp.ndarray) -> jnp.ndarray:
    """Return the magnitude of `field`"""
    magnitude_squared = jnp.sum(jnp.abs(field) ** 2, axis=-1, keepdims=True)
    is_zero = magnitude_squared == 0
    magnitude_squared_safe = jnp.where(is_zero, 1.0, magnitude_squared)
    return jnp.where(is_zero, 0.0, jnp.sqrt(magnitude_squared_safe))


def _max_field_magnitude(field: jnp.ndarray) -> jnp.ndarray:
    """Returns the magnitude of the largest component in `field`."""
    return jnp.amax(_field_magnitude(field), axis=(-3, -2), keepdims=True)


def _angle(x: jnp.ndarray) -> jnp.ndarray:
    """Computes `angle(x)` with special logic for when `x` equals zero."""
    # Avoid taking the angle of an array with any near-zero elements, to avoid
    # `nan` in the gradients.
    is_near_zero = jnp.isclose(x, 0.0)
    x_safe = jnp.where(is_near_zero, (1.0 + 0.0j), x)
    return jnp.angle(x_safe)


def _filter_and_adjust_resolution(
    x: jnp.ndarray,
    expansion: basis.Expansion,
) -> jnp.ndarray:
    """Filter `x` and adjust its resolution for the given `expansion`."""
    y = fft.fft(x, expansion=expansion)
    min_shape = fft.min_array_shape_for_expansion(expansion)
    doubled_min_shape = (2 * min_shape[0], 2 * min_shape[1])
    return fft.ifft(y, expansion=expansion, shape=doubled_min_shape)


# -------------------------------------------------------------------------------------
# Loss function
# -------------------------------------------------------------------------------------


def field_loss_value_jac_and_hessian(
    flat_fourier_field: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    target_field: jnp.ndarray,
    elementwise_alignment_loss_weight: jnp.ndarray,
    fourier_loss_weight: float,
) -> Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray]:
    """Compute the value, Jacobian, and Hessian of the field loss."""
    assert flat_fourier_field.ndim == 1

    def fn(flat_fourier_field):
        fourier_field = jnp.reshape(flat_fourier_field, (-1, 2))
        value = _field_loss(
            fourier_field=fourier_field,
            expansion=expansion,
            primitive_lattice_vectors=primitive_lattice_vectors,
            target_field=target_field,
            elementwise_alignment_loss_weight=elementwise_alignment_loss_weight,
            fourier_loss_weight=fourier_loss_weight,
        )
        return value, value

    def jac_fn(flat_fourier_field):
        jac, value = jax.jacrev(fn, has_aux=True)(flat_fourier_field)
        return jac, (value, jac)

    hessian, (value, jac) = jax.jacrev(jac_fn, has_aux=True, holomorphic=True)(
        flat_fourier_field
    )

    return value, jac, hessian


def _field_loss(
    fourier_field: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
    target_field: jnp.ndarray,
    elementwise_alignment_loss_weight: jnp.ndarray,
    fourier_loss_weight: float,
) -> jnp.ndarray:
    """Compute loss that favors smooth"""
    shape: Tuple[int, int] = target_field.shape[-3:-1]  # type: ignore[assignment]
    field = fft.ifft(
        y=fourier_field,
        expansion=expansion,
        shape=shape,
        axis=-2,
    )
    alignment_loss = _alignment_loss(
        field, target_field, elementwise_alignment_loss_weight
    )

    fourier_loss = _fourier_loss(fourier_field, expansion, primitive_lattice_vectors)
    return alignment_loss + fourier_loss_weight * fourier_loss


def _alignment_loss(
    field: jnp.ndarray,
    target_field: jnp.ndarray,
    elementwise_alignment_loss_weight: jnp.ndarray,
) -> jnp.ndarray:
    """Compute loss that penalizes differences between `field` and `target_field`."""
    assert elementwise_alignment_loss_weight.ndim == field.ndim
    elementwise_loss = jnp.sum(
        jnp.abs(field - target_field) ** 2, axis=-1, keepdims=True
    )
    return jnp.mean(elementwise_alignment_loss_weight * elementwise_loss)


def _fourier_loss(
    fourier_field: jnp.ndarray,
    expansion: basis.Expansion,
    primitive_lattice_vectors: basis.LatticeVectors,
) -> jnp.ndarray:
    """Compute loss that penalizes high frequency Fourier components.

    The loss is scaled for the size of the unit cell, i.e. two unit cells with
    identical `fourier_field` and scaled `primitive_lattice_vectors` will have
    identical loss.

    Args:
        fourier_field: The Fourier field for which the loss is sought.
        expansion: The Fourier expansion for the field.
        primitive_lattice_vectors: Defines the unit cell coordinates.

    Returns:
        The scalar fourier loss value.
    """
    transverse_wavevectors = basis.transverse_wavevectors(
        primitive_lattice_vectors=primitive_lattice_vectors,
        expansion=expansion,
        in_plane_wavevector=jnp.zeros((2,)),
    )

    basis_vectors = jnp.stack(
        [primitive_lattice_vectors.u, primitive_lattice_vectors.v],
        axis=-1,
    )
    area = jnp.abs(jnp.linalg.det(basis_vectors))

    kt = jnp.linalg.norm(transverse_wavevectors, axis=-1) * jnp.sqrt(area)
    return jnp.sum(jnp.abs(fourier_field) ** 2 * kt[..., jnp.newaxis] ** 2)


# -------------------------------------------------------------------------------------
# Gradient calculation and transformation.
# -------------------------------------------------------------------------------------


def compute_gradient(
    arr: jnp.ndarray,
    primitive_lattice_vectors: basis.LatticeVectors,
) -> jnp.ndarray:
    """Computes the gradient of `arr`.

    The gradient is scaled for the size of the unit cell, i.e. two unit cells with
    identical `arr` and scaled `primitive_lattice_vectors` will have identical
    gradient.

    Args:
        arr: The array for which the gradient is sought.
        primitive_lattice_vectors: Defines the unit cell coordinates.

    Returns:
        The gradient, with shape `arr.shape + (2,)`.
    """
    basis_vectors = jnp.stack(
        [primitive_lattice_vectors.u, primitive_lattice_vectors.v],
        axis=-1,
    )

    area = jnp.abs(jnp.linalg.det(basis_vectors))
    basis_vectors /= jnp.sqrt(area)

    batch_dims = arr.ndim - 2
    pad_width = tuple([(0, 0)] * batch_dims + [(1, 1)] * 2)
    arr_padded = jnp.pad(arr, pad_width, mode="wrap")

    axes = tuple(range(-2, 0))
    partial_grad: List[jnp.ndarray]
    partial_grad = jnp.gradient(arr_padded, axis=axes)  # type: ignore[assignment]
    partial_grad = [_unpad(g, pad_width) for g in partial_grad]
    partial_grad = [g * arr.shape[ax] for g, ax in zip(partial_grad, axes)]
    return _transform_gradient(jnp.stack(partial_grad, axis=-1), basis_vectors)


def _transform_gradient(
    partial_grad: jnp.ndarray,
    basis_vectors: jnp.ndarray,
) -> jnp.ndarray:
    """Compute gradient from partial gradient with arbitrary basis vectors."""
    # https://en.wikipedia.org/wiki/Gradient#General_coordinates
    metric_tensor = _metric_tensor(basis_vectors)
    inverse_metric_tensor = jnp.linalg.inv(metric_tensor)
    result: jnp.ndarray = partial_grad @ inverse_metric_tensor @ basis_vectors.T
    return result


def _metric_tensor(basis_vectors: jnp.ndarray) -> jnp.ndarray:
    """Compute the metric tensor for a non-Cartesian, non-orthogonal basis."""
    return basis_vectors.T @ basis_vectors


def _unpad(arr: jnp.ndarray, pad_width: Tuple[Tuple[int, int], ...]) -> jnp.ndarray:
    """Undoes a pad operation."""
    slices = [slice(lo, size - hi) for (lo, hi), size in zip(pad_width, arr.shape)]
    return arr[tuple(slices)]
