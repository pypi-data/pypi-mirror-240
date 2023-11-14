# Ipyllogger
[SCHOOL PROJECT - PYTHON BASICS] | Minimum Python package to write logs in a file

## Installation

```bash
pip install ipyllogger
```

## Tests

```bash
make test
```

## Usage

```python
from ipyllogger import log, get_logs
from ipyllogger import level

# Log an error
log("Hello World", level.ERROR)

# Log a warning
log("Hello World", level.WARNING)

# Get all errors logs
print(get_logs(level.ERROR))

# Get all warnings logs
print(get_logs(level.WARNING))

```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributors
- [Makendy ALEXIS](https://github.com/RagnarBob)
- [Louis Midson LAJEANTY](https://github.com/midsonlajeanty)
