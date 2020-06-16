# Cat Facts API

Our new overlords demand it. Here cometh the facts!

## Pre-requisites

- Python 3.5 and above
- All Python package dependancies (see installation guide below)
- Sqlite 3 and above

## Installation

- Install all package dependancies using the included `requirements.txt` file. The specific command may vary depending on your setup but for most the following should work:

```bash
pip install -r requirements.txt
```

**Note:** If you are using Pipenv you can install dependancies using the included Pipfile.lock.

From the root of the app directory run:

```bash
pipenv install
```

## Usage

There are two main functions to this application:

### API

To start serving the API run:

```bash
cat-facts.py server [--host] [--port]
```

There is a single endpoint at the root path `/` providing a filtered list of cat facts ([source](https://cat-fact.herokuapp.com/facts)) in JSON format.

### CLI

Running the application without any arguments will return a filtered, pretty printed list of cat facts:

```bash
cat-facts.py [--format]
```

As indicated, the output format can be set to JSON, YAML or CSV instead.
