# TODO(khemritolya) force f32/f64 maybe? what about print options?
# from jax.config import config

# config.update("jax_enable_x64", False)
# config.update("jax_debug_nans", True)

# # import jax.tools.colab_tpu
# # jax.tools.colab_tpu.setup_tpu()

# jnp.set_printoptions(threshold=jnp.inf)
# jnp.set_printoptions(precision=5)

# print(jax.local_device_count())
from . import dgp
from . import estimators
from . import sieve
from . import nets