import jax
from jax import numpy as jnp
import jaxamp
from equinox import filter_jit
import equinox as eqx


class Net(eqx.Module):
    lin: eqx.nn.Linear
    bn: eqx.nn.BatchNorm

    def __init__(self):
        self.lin = eqx.nn.Linear(3,3, key=jax.random.PRNGKey(0))
        self.bn = eqx.nn.BatchNorm(3, axis_name="batch")

    def __call__(self, x, state):
        return self.bn(self.lin(x), state=state)

model, state = eqx.nn.make_with_state(Net)()

def run_model(model, state, x):
    print("compiling")
    return jax.vmap(model, in_axes=(0, None), out_axes=(0, None), axis_name="batch")(x, state)

f = filter_jit(run_model)

x = jnp.ones((1,3))
x, state = f(model, state, x)
x, state = f(model, state, x)
x, state = f(model, state, x)

# def foo(x, y):
#     print("compiling")
#     return x*y['k'], y, 1


# x = jnp.array([1,2,3])
# y = {'k': 4}

# f = filter_jit(jaxamp.amp(Net))
# # f = filter_jit(foo)
# print((x,y))
# x, y, z = f(x,y)
# print((x,y,z))
# x,y,z = f(x,y)
# print((x,y,z))
# x,y,z = f(x,y)
# print((x,y,z))
