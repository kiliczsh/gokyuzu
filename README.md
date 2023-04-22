# gokyuzu - bluesky python client

Gökyüzü - "sky" in Turkish - is a python client for the [bluesky](bsky.social) social network.

### Install

```bash
pip install gokyuzu
```

### Sample Usage

```python
from gokyuzu import Bluesky

bsky = Bluesky("handle.bsky.social", "PASSWORD")
response = bsky.resolveHandle("handle.bsky.social")
print(response.json())
```

### Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running tests

```bash
python -m unittest
```

### Publishing to PyPI

```bash
# Build for PyPI
python -m build

# Test PyPI
python -m twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ --no-deps gokyuzu

# PyPI
python -m twine upload dist/*
pip install gokyuzu
```