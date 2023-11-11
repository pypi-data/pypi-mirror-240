import jax
import jax.numpy as jnp
import optax
import flax.linen as nn
from tqdm import tqdm
from . import sieve

# TODO(khemritolya): give people a non scary good default optimizer
_base_optimizer = optax.adam(learning_rate=0.05)


def _general_loss(params, net, y_1, y_2, projection):
    """
    TODO(khemritolya): docstring, and the fact that the function below is code
    But there seems to be no good workaround if I want to JIT
    """
    n, = y_1.shape
    assert y_2.shape[0] == n, y_2.shape

    predictions = net.apply(params, y_2).reshape((n, ))
    residuals = y_1 - predictions
    assert predictions.shape == y_1.shape, predictions.shape
    assert residuals.shape == y_1.shape, residuals.shape
    assert projection.shape == (n, n), projection.shape

    projected_residuals = projection @ residuals
    assert projected_residuals.shape == y_1.shape, projected_residuals.shape
    return jnp.dot(projected_residuals, projected_residuals) / n


def _w_general_loss(params, net, y_1, y_2, projection, weighting_matrix):
    """
    TODO(khemritolya): Code duplication?
    """
    n, = y_1.shape
    assert y_2.shape[0] == n, y_2.shape

    predictions = net.apply(params, y_2).reshape((n, ))
    residuals = y_1 - predictions
    assert predictions.shape == y_1.shape, predictions.shape
    assert residuals.shape == y_1.shape, residuals.shape
    assert projection.shape == (n, n), projection.shape

    projected_residuals = projection @ residuals
    assert projected_residuals.shape == y_1.shape, projected_residuals.shape
    return jnp.dot(projected_residuals,
                   weighting_matrix @ projected_residuals) / n


class Estimator():

    def __init__(self, net, seive):
        self.net = net
        self.seive = seive
        self.is_fit = False
        self.params = None

    def fit(self,
            y_1: jax.Array,
            y_2: jax.Array,
            x: jax.Array,
            key: jax.random.PRNGKey,
            epochs=100,
            opt=_base_optimizer,
            progress=False):
        n, = y_1.shape
        assert y_2.shape[0] == n, y_2.shape
        assert x.shape[0] == n, x.shape
        assert epochs > 0
        return self._fit(y_1, y_2, x, key, epochs, opt, progress)

    def _fit(self,
             y_1: jax.Array,
             y_2: jax.Array,
             x: jax.Array,
             key: jax.random.PRNGKey,
             epochs=100,
             opt=_base_optimizer,
             progress=False):
        raise NotImplementedError("Called fit on an abstract estimator")

    def get_estimand(self, y_2: jax.Array):
        if not self.is_fit:
            raise RuntimeError(
                "Attempted to get an estimand on an unfitted estimator")
        return self._get_estimand(y_2)

    def _get_estimand(self, y_2):
        raise NotImplementedError("Called _get_estimand on abstract estimator")


class PluginEstimator(Estimator):

    def _fit(self,
             y_1: jax.Array,
             y_2: jax.Array,
             x: jax.Array,
             key: jax.random.PRNGKey,
             epochs=100,
             opt=_base_optimizer,
             progress=False):
        n, = y_1.shape

        self.params = self.net.init(key, y_2[0, :])
        opt_state = opt.init(self.params)
        projection = sieve.sieve_projection(x, self.seive)

        loss_grad = jax.value_and_grad(lambda params, y_1, y_2: _general_loss(
            params, self.net, y_1, y_2, projection))

        itr = range(epochs)
        if progress:
            itr = tqdm(itr)

        @jax.jit
        def training_step(params, opt_state):
            loss, grads = loss_grad(params, y_1, y_2)
            updates, opt_state = opt.update(grads, opt_state)
            params = optax.apply_updates(params, updates)
            return loss, params, opt_state

        for i in itr:
            loss, self.params, opt_state = training_step(
                self.params, opt_state)

            if progress:
                itr.set_description("nn loss: %.03f, epoch" % loss)

        self.is_fit = True

    def _get_estimand(self, y_2):
        n, p = y_2.shape

        def predict(y_2_i):
            return self.net.apply(self.params, y_2_i)[0]

        predict_gradient = jax.vmap(jax.grad(predict))
        predictions = predict_gradient(y_2)
        assert predictions.shape == (n, p), predictions.shape

        return jnp.mean(predictions[:, 0])
