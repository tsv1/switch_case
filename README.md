# switch_case

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
