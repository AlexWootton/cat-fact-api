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

Provides a formatted output displaying the fact ID and fact body text when run.

Example:

```shell
> ./cat-facts.py
ID: 5cd86b0e1dc6d50015ec2f08 | Norwegian Forest Cats are usually very people friendly.
ID: 5d38b2510f1c57001592f12e | Courgars are the largest wild cats that can purr.
ID: 5ebbf5dd8046d00017776020 | Cats are fat, sometimes.
```

## Planned improvements

- Addition of an API endpoint to serve the currently stored facts as JSON over HTTP.
- Additional formatting options for command line output. Including:
  - JSON
  - YAML
  - CSV

### Proposed API usage

Start serving the API by running:

```bash
cat-facts.py server [-h host] [-p port]
```

Results in a single endpoint at the root path `/` providing a filtered list of cat facts ([source](https://cat-fact.herokuapp.com/facts)) in JSON format.

### Proposed output formatting usage

Running the application without any arguments will return a filtered, pretty printed list of cat facts:

```bash
cat-facts.py [-F format]
```

Valid options for output format would be `json`, `yaml`, `csv` or the default `pretty`.

## Known issues

- `KeyError` occurs whilst looping over the dictionary of facts. I have used a try/except block to bypass the issue as I was unable to get to the root of it in time.
- Some unused imports and empty functions from initial boilerpolating. These have been left in place to demostrate what would have been developed given more time.
