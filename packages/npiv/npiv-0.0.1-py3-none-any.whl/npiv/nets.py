import flax.linen as nn


class BasicStructureEstimator(nn.Module):
    """
    A small network -- two hidden layers, 30 nodes each
    """

    @nn.compact
    def __call__(self, x):
        x = nn.relu(nn.Dense(30)(x))
        x = nn.relu(nn.Dense(30)(x))
        return nn.Dense(1)(x)