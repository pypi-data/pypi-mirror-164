
<div align="center">
<img width="350px" src="assets/serketLogo.svg"></div>

<h2 align="center">The ✨Magical✨ JAX NN Library.</h2>
<h5 align = "center"> *Serket is the goddess of magic in Egyptian mythology </h5>

![Tests](https://github.com/ASEM000/serket/actions/workflows/tests.yml/badge.svg)
![pyver](https://img.shields.io/badge/python-3.7%203.8%203.9%203.10-red)
![codestyle](https://img.shields.io/badge/codestyle-black-lightgrey)
[![Downloads](https://pepy.tech/badge/serket)](https://pepy.tech/project/serket)
[![codecov](https://codecov.io/gh/ASEM000/serket/branch/main/graph/badge.svg?token=C6NXOK9EVS)](https://codecov.io/gh/ASEM000/serket)





## 🛠️ Installation<a id="Installation"></a>

```python
pip install serket
```


## 📖 Description<a id="Description"></a>
- `serket` aims to be the most intuitive and easy-to-use Neural network library in JAX.
- `serket` is built on top of [`pytreeclass`](https://github.com/ASEM000/pytreeclass)
- `serket` currently implements 
  - `Linear`, `FNN`
  - `Dropout`
  - `Sequential`
  - `Lambda`


## ⏩ Quick Example <a id="QuickExample">

Simple Fully connected neural network.

### Model definition
```python
import serket as sk 
import jax.numpy as jnp
import jax.random as jr


@sk.treeclass
class NN:
    def __init__(
        self, 
        in_features:int, 
        out_features:int, 
        hidden_features: int, key:jr.PRNGKey = jr.PRNGKey(0)):

        k1,k2,k3 = jr.split(key, 3)

        self.l1 = sk.nn.Linear(in_features, hidden_features, key=k1)
        self.l2 = sk.nn.Linear(hidden_features, hidden_features, key=k2)
        self.l3 = sk.nn.Linear(hidden_features, out_features, key=k3)
    
    def __call__(self, x):
        x = self.l1(x)
        x = jax.nn.relu(x)
        x = self.l2(x)
        x = jax.nn.relu(x)
        x = self.l3(x)
        return x


model = NN(
    in_features=1, 
    out_features=1, 
    hidden_features=128, 
    key=jr.PRNGKey(0))
```

```python
# `*` represents untrainable(static) nodes.
print(model.tree_diagram())
NN
    ├── l1=Linear
    │   ├── weight=f32[1,128]
    │   ├── bias=f32[128]
    │   ├*─ in_features=1
    │   ├*─ out_features=128
    │   ├*─ weight_init_func=init(key,shape,dtype)
    │   └*─ bias_init_func=Lambda(key,shape)    
    ├── l2=Linear
    │   ├── weight=f32[128,128]
    │   ├── bias=f32[128]
    │   ├*─ in_features=128
    │   ├*─ out_features=128
    │   ├*─ weight_init_func=init(key,shape,dtype)
    │   └*─ bias_init_func=Lambda(key,shape)    
    └── l3=Linear
        ├── weight=f32[128,1]
        ├── bias=f32[1]
        ├*─ in_features=128
        ├*─ out_features=1
        ├*─ weight_init_func=init(key,shape,dtype)
        └*─ bias_init_func=Lambda(key,shape) 
```

```python
>>> print(model.summary())
┌────┬──────┬─────────┬───────┬───────────────────┐
│Name│Type  │Param #  │Size   │Config             │
├────┼──────┼─────────┼───────┼───────────────────┤
│l1  │Linear│256(0)   │1.00KB │weight=f32[1,128]  │
│    │      │         │(0.00B)│bias=f32[128]      │
├────┼──────┼─────────┼───────┼───────────────────┤
│l2  │Linear│16,512(0)│64.50KB│weight=f32[128,128]│
│    │      │         │(0.00B)│bias=f32[128]      │
├────┼──────┼─────────┼───────┼───────────────────┤
│l3  │Linear│129(0)   │516.00B│weight=f32[128,1]  │
│    │      │         │(0.00B)│bias=f32[1]        │
└────┴──────┴─────────┴───────┴───────────────────┘
Total count :	16,897(0)
Dynamic count :	16,897(0)
Frozen count :	0(0)
---------------------------------------------------
Total size :	66.00KB(0.00B)
Dynamic size :	66.00KB(0.00B)
Frozen size :	0.00B(0.00B)
===================================================
```

### Train
```python
x = jnp.linspace(0,1,100)[:,None]
y = x**3 + jax.random.uniform(jax.random.PRNGKey(0),(100,1))*0.01

@jax.value_and_grad
def loss_func(model,x,y):
    return jnp.mean((model(x)-y)**2)

@jax.jit
def update(model,x,y):
    value,grad = loss_func(model,x,y)
    return value , model - 1e-3*grad

for _ in range(20_000):
    value,model = update(model,x,y)
```

### Filter
- Filter by (1)value, (2)`field` name, (3)`field` type, (4)`field` metadata
- See [here](https://github.com/ASEM000/PyTreeClass#%EF%B8%8F-filtering-with-at-) for more
