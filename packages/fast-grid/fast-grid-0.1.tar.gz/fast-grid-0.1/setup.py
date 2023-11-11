from setuptools import setup, find_packages

setup(
    name="fast-grid",
    version="0.1",
    description="Fast grid calculation",
    author="Hyunsoo Park",
    author_email="hpark@ic.ac.uk",
    url="https://github.com/hspark1212/fast-grid.git",
    install_requires=[
        "numpy",
        "ase",
        "numba",
        "fire",
        "plotly",
        "pandas",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
)
