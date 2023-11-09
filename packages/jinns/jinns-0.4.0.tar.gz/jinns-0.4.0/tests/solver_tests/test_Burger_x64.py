import pytest

import jax
import jax.numpy as jnp
from jax import random
import equinox as eqx
import optax
import jinns


@pytest.fixture
def train_Burger_init():
    jax.config.update("jax_enable_x64", True)
    print(jax.config.FLAGS.jax_enable_x64)
    print(jax.devices())
    key = random.PRNGKey(2)
    eqx_list = [
        [eqx.nn.Linear, 2, 20],
        [jax.nn.tanh],
        [eqx.nn.Linear, 20, 20],
        [jax.nn.tanh],
        [eqx.nn.Linear, 20, 20],
        [jax.nn.tanh],
        [eqx.nn.Linear, 20, 1],
    ]
    key, subkey = random.split(key)
    init_param_fn, u = jinns.utils.create_PINN(subkey, eqx_list, "nonstatio_PDE", 1)

    init_nn_params = init_param_fn()

    n = 1000
    nt = 1000
    nb = 2
    omega_batch_size = 32
    temporal_batch_size = 20
    omega_border_batch_size = 1
    dim = 1
    xmin = -1
    xmax = 1
    tmin = 0
    tmax = 1
    Tmax = 1
    method = "uniform"

    train_data = jinns.data.CubicMeshPDENonStatio(
        subkey,
        n,
        nb,
        nt,
        omega_batch_size,
        omega_border_batch_size,
        temporal_batch_size,
        dim,
        (xmin,),
        (xmax,),
        tmin,
        tmax,
        method,
    )

    nu = 1 / (100 * jnp.pi)
    init_params = {"nn_params": init_nn_params, "eq_params": {"nu": nu}}

    def u0(x):
        return -jnp.sin(jnp.pi * x)

    be_loss = jinns.loss.BurgerEquation(Tmax=Tmax)

    loss_weights = {"dyn_loss": 1, "initial_condition": 5, "boundary_loss": 1}

    loss = jinns.loss.LossPDENonStatio(
        u=u,
        loss_weights=loss_weights,
        dynamic_loss=be_loss,
        omega_boundary_fun=lambda t, dx: 0,
        omega_boundary_condition="dirichlet",
        initial_condition_fun=u0,
    )

    return init_params, loss, train_data


@pytest.fixture
def train_Burger_10it(train_Burger_init):
    """
    Fixture that requests a fixture
    """
    init_params, loss, train_data = train_Burger_init

    # NOTE we need to waste one get_batch() here to stay synchronized with the
    # notebook
    _ = loss.evaluate(init_params, train_data.get_batch())[0]

    params = init_params

    tx = optax.adam(learning_rate=1e-3)
    n_iter = 10
    params, total_loss_list, loss_by_term_dict, _, _, _, _ = jinns.solve(
        init_params=params, data=train_data, optimizer=tx, loss=loss, n_iter=n_iter
    )
    return total_loss_list[9]


def test_initial_loss_Burger(train_Burger_init):
    init_params, loss, train_data = train_Burger_init
    assert jnp.round(
        loss.evaluate(init_params, train_data.get_batch())[0], 5
    ) == jnp.round(2.98864, 5)


def test_10it_Burger(train_Burger_10it):
    total_loss_val = train_Burger_10it
    assert jnp.round(total_loss_val, 5) == jnp.round(2.77797, 5)
