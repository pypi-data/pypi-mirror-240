# River Python bindings

A future home for River's Python bindings. For now, the [MyPI package is registered](https://pypi.org/project/riverqueue/), but nothing else is done.

``` sh
$ python3 -m pip install --upgrade build
$ python3 -m pip install --upgrade twine
```

``` sh
$ python3 -m build
$ python3 -m twine upload --repository pypi dist/*
```
