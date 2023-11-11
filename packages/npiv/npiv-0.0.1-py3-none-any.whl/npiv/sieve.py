import jax
import jax.numpy as jnp


@jax.jit
def identity_sieve(x):
    return x


@jax.jit
def basic_sieve(x):
    """
    Transforms a row vector to a row vector containing all original entries and 
    pairwise interaction effects. This includes own interaction effects, i.e.
    squares of the original entries. This is vectorized later via VMAP, which is
    the recommended way to build seive bases.
    
    Parameters
    ----------
    x: jax.Array (p, )
    
    Returns
    -------
    jax.Array (1 + p + p(p+1)/2, )
    """
    p, = x.shape
    assert p > 0

    output = jnp.zeros((1 + p + p * (p + 1) // 2, ))
    output = output.at[0].set(1)

    for i in range(p):
        output = output.at[1 + i].set(x[i])

    ctr = 0
    for i in range(p):
        for j in range(i, p):
            output = output.at[p + 1 + ctr].set(x[i] * x[j])
            ctr = ctr + 1

    return output


basic_sieve = jax.vmap(basic_sieve, in_axes=(0, ), out_axes=0)


def sieve_projection(x, sieve):
    """
    Returns the projection onto the seive space of x. P_(phi) in the paper
    """
    phi_x = sieve(x)
    return phi_x @ jnp.linalg.pinv(phi_x.T @ phi_x) @ phi_x.T