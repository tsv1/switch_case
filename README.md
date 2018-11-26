# switch_case

[![License](https://img.shields.io/github/license/nikitanovosibirsk/switch_case.svg)](https://github.com/nikitanovosibirsk/switch_case)
[![Travis](https://img.shields.io/travis/com/nikitanovosibirsk/switch_case/master.svg)](https://travis-ci.com/nikitanovosibirsk/switch_case)
[![Codecov](https://img.shields.io/codecov/c/github/nikitanovosibirsk/switch_case/master.svg)](https://codecov.io/gh/nikitanovosibirsk/switch_case)
[![PyPI](https://img.shields.io/pypi/v/switch_case.svg)](https://pypi.python.org/pypi/switch_case/)
[![Python Version](https://img.shields.io/pypi/pyversions/switch_case.svg)](https://pypi.python.org/pypi/switch_case/)

## Installation

```bash
pip3 install switch_case
```

## Usage

```python
from switch_case import *
reason = (
    switch
        | case(_ == 200) >> 'OK'
        | case(_ == 500) >> 'ERROR'
        | default        >> 'UNKNOWN')
```

```python
assert reason(200) == 'OK'
assert reason(500) == 'ERROR'
assert reason(400) == 'UNKNOWN'
```

Which is syntax sugar for:

```python
from switch_case import *
from operator import eq
reason = (
    switch
        | case(_ /eq/ 200) >> 'OK'
        | case(_ /eq/ 500) >> 'ERROR'
        | default        >> 'UNKNOWN')
```

So you can use it like this:

```python
from switch_case import *
get_type = (
    switch
        | case(_ /isinstance/ str)   >> "string"
        | case(_ /isinstance/ int)   >> "integer"
        | case(_ /isinstance/ float) >> "float"
        | case(_ /isinstance/ bool)  >> "bool"
        | default                    >> "other")
```

Or as a function:

```python
from switch_case import *
def get_type(smth):
    return ~(
        switch(smth)
            | case(_ /isinstance/ str)   >> "string"
            | case(_ /isinstance/ int)   >> "integer"
            | case(_ /isinstance/ float) >> "float"
            | case(_ /isinstance/ bool)  >> "bool"
            | default                    >> "other")
```

```python
assert get_type(42) == "integer"
assert get_type("42") == "string"
assert get_type(3.14) == "float"
```
