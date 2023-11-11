## Background

Reporting tools and datafeeds for Tellor oracles.

The package `telliot-feeds` version `0.1.14` forked from:<br />
https://github.com/tellor-io/telliot-feeds

## Initial Setup

### Prerequisites
The following tools are expected to be installed on your system to run this project:

- Python 3.9.x
- Pip 23.3.x
- Git

### Setup

```bash
python3.9 -m venv tenv
source tenv/bin/activate
pip3.9 install .
```

### Test

Install development requirements:
```bash
pip3.9 install -r requirements-dev.txt
```

Run automated testing in all environments:
```bash
tox
```

Run `py39` testing:
```bash
tox -e py39
```

Run `style` testing:
```bash
tox -e style
```

Run `typing` typing:
```bash
tox -e typing
```

## Usage

TBD

## Contributing

Bug reports and pull requests are welcome on GitHub at:<br />
https://github.com/SELISEdigitalplatforms/l3-solidity-bcts-tellor
