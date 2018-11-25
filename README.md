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
