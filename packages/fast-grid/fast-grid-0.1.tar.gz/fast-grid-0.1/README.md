
<div align="center">

<h1> Fast Grid 🏁 </h1>

This package is designed to calculate voxel grids using numba. It is designed to be fast and easy to use.


</div>

## Installation

```bash
git clone https://github.com/hspark1212/fast-grid.git
cd fast-grid
pip install -e .
```

Arguments:

```bash
python calculate_grids.py --help
```

Run with the default parameters:

```bash
python calculate_grids.py --structure=examples/irmof-1.cif
```

Run with parameters:

```bash
python calculate_grids.py \
--structure=examples/irmof-1.cif \
--gird_size=30 \
--ff_type=UFF \
--potential=LJ \
--cutoff=12.8 \
--gas_epsilon=148.0 \
--gas_sigma=3.73 \
--visualize=True
```

![scheme_rl-01](./images/irmof-1.png)
