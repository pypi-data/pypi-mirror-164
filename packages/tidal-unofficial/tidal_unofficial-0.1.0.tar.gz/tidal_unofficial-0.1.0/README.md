# Unofficial Tidal API
This library gives access to several endpoints of the Tidal's api where the authorization is not required.

[![PyPI](https://img.shields.io/pypi/v/tidal-unofficial.svg)](https://pypi.org/project/tidal-unofficial/)
[![Python support](https://img.shields.io/pypi/pyversions/tidal-unofficial.svg)](https://pypi.org/project/tidal-unofficial/)

-------

## Installation

```
pip install tidal_unofficial
```

## Basic usage

```python
from tidal_unofficial import TidalUnofficial

tidal = TidalUnofficial({'user_agent': 'my_user_agent'})

print(tidal.get_artist('37277'))
```

## Documentation

The full documentation can be found at https://tidal-unofficial.readthedocs.io/.

## Disclaimer

This library is a python port of https://github.com/DaStormer/tidal-api and is not meant to bypass any Tidal restriction. It is meant for private use only, you should not use this library to act against Tidal's terms and conditions.
