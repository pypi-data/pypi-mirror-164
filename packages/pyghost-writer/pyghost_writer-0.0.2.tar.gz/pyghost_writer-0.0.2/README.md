# ghost_writer
![CI](https://github.com/grburgess/ghost_writer/workflows/CI/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/grburgess/ghost_writer/branch/master/graph/badge.svg)](https://codecov.io/gh/grburgess/ghost_writer)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3372456.svg)](https://doi.org/10.5281/zenodo.3372456)
![PyPI](https://img.shields.io/pypi/v/ghost_writer)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ghost_writer)

A simple package that allows you to build a class to parameterize scripts via
code generation.

A cmdline utility is add to convert python scripts into generators which can
later be modified.

## Installation

```bash
pip install ghost-writer
```

## Usage

Say you have a simple script that you want to parameterize for code generation.

```python
import os


for i in range(10):
    for j in range(20):
        pass

```

In the terminal run the ```scriptify_py``` command on the script

```bash
scriptify_py script.py
```

Now you will have a new file called ```generated_script.py``` which contains a class that can generate that script which can be run:

```python
from ghost_writer import ScriptGenerator


class NewGenerator(ScriptGenerator):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def _build_script(self) -> None:
        self._add_line('import os')
        self._end_line()
        self._end_line()
        self._add_line('for i in range(10):')
        self._add_line('for j in range(20):', indent_level=1)
        self._add_line('pass', indent_level=2)


```

We can now modify the class to be parameterized:


```python
from ghost_writer import ScriptGenerator


class MyGenerator(ScriptGenerator):
    def __init__(self, file_name: str, parameter: int) -> None:

        self._parameter = parameter

		super().__init__(file_name)

    def _build_script(self) -> None:
        self._add_line('import os')
        self._end_line()
        self._end_line()
        self._add_line('for i in range(10):')
        self._add_line('for j in range(20):', indent_level=1)
        self._add_line(f'print({parameter})', indent_level=2)


```

Now in python, we can import our class and run it:


```python

generator = MyGenerator("new_script.py", 4)

generator.write()

```

And now we have a generated script called ```new_script.py```


```python
import os


for i in range(10):
    for j in range(20):
        print(4)


```




* Free software: GNU General Public License v3
