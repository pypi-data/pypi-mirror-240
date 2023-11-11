import jax
import jax.numpy as jnp
import jax.scipy.stats as jst
from jax import random, jit
from functools import partial


def make_paper_dgp_2(seed: random.PRNGKey, p: int, rho: float):
    """
    TODO(khemritolya): descriptions
    """
    h_01 = jax.nn.sigmoid
    h_02 = jnp.log1p

    @jax.jit
    def h_03(x):
        m = jnp.maximum(jnp.max(x, axis=1), 0.5)
        return (5 * jnp.power(x[:, 0], 3) + x[:, 1] * m +
                0.5 * jnp.exp(-x[:, p - 1]))

    z = random.normal(seed, shape=(p, ))
    cov = jnp.eye(p, ) + jnp.outer(z, z)
    cov = cov / (jnp.diag(cov)[:, None]**0.5) / (jnp.diag(cov)[None, :]**0.5)

    @partial(jax.jit, static_argnames=['n'])
    def dgp(seed: random.PRNGKey, n: int):
        keys = random.split(seed, 8)
        u_1 = random.normal(keys[0], shape=(n, ))
        u_2 = random.normal(keys[1], shape=(n, ))
        u_3 = random.normal(keys[2], shape=(n, ))
        v_2 = random.normal(keys[3], shape=(n, ))
        v_3 = random.normal(keys[4], shape=(n, ))
        v = random.normal(keys[5], shape=(n, ))

        x_1 = jst.norm.cdf(v_2)
        x_2 = random.uniform(keys[6], shape=(n, ))
        x_3 = jst.norm.cdf(v_3)
        sigma = jnp.sqrt((x_1**2 + x_2**2 + x_3**2) / 3.)
        u = (u_1 + u_2 + u_3) / 3. * sigma
        assert u.shape == (n, )

        r_1 = x_1 + 0.5 * u_2 + v
        r_2 = jst.norm.cdf(v_3 + 0.5 * u_3)

        x_bar = random.multivariate_normal(keys[7],
                                           jnp.zeros(p, ),
                                           cov=cov,
                                           shape=(n, ))
        assert x_bar.shape == (n, p)
        x_sig = (rho * (x_1 + x_2 + x_3))[:, None]
        assert x_sig.shape == (n, 1)
        x_bar = x_sig + jnp.sqrt(1 - jnp.square(rho)) * x_bar
        x_bar = jst.norm.cdf(x_bar)
        assert x_bar.shape == (n, p)

        assert u.shape == (n, )
        assert r_1.shape == (n, )
        assert h_03(x_bar).shape == (n, ), h_03(x_bar).shape
        y_1 = r_1 + h_01(r_2) + h_02(x_2) + h_03(x_bar) + u
        y_2 = jnp.hstack([r_1[:, None], r_2[:, None], x_2[:, None], x_bar])
        x = jnp.hstack([x_1[:, None], x_2[:, None], x_3[:, None], x_bar])

        assert y_1.shape == (n, )
        assert y_2.shape == (n, p + 3)
        assert x.shape == (n, p + 3)
        return y_1, y_2, x

    return dgp
