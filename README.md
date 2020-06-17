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

### List

Prints a list of all stored cat facts to the command line. Can be set to output as either JSON or pretty printed using the `-F` or `--format` flags. Defaults to pretty printed (as below).

Example:

```shell
> ./cat-facts.py list
ID: 5cd86b0e1dc6d50015ec2f08 | Norwegian Forest Cats are usually very people friendly.
ID: 5d38b2510f1c57001592f12e | Courgars are the largest wild cats that can purr.
ID: 5ebbf5dd8046d00017776020 | Cats are fat, sometimes.
```

### Delete

Allows for the deletion of specific facts by ID.

Example:

```shell
> ./cat-facts.py delete --id 5ebbf5dd8046d00017776020
Fact ID: 5ea7496761cd4d0017498a94 has been deleted.
```

**Note:** You will be prompted for an ID if one is not provided when the command is run.

### Server

Starts an HTTP server that provides two REST API endpoints (detailed below).

Usage example:

```bash
cat-facts.py server [-h --host] [-p --port] [--debug]
```

`--host` specifies host address to listen on

`--port` specifies the port to listen on

`--debug` enables debug mode on the HTTP server

### API

If the server is running two API endpoints will be available at the configured host address and port.

`/api/v1/facts` - produces all stored facts in JSON format.

`/api/v1/facts/<id>` - takes a fact ID and returns the matching fact in JSON format if it exists.

## Planned improvements

- Additional formatting options for command line output. Including:
  - YAML
  - CSV

## Known issues

- `KeyError` occurs whilst looping over the dictionary of facts. I have used a try/except block to bypass the issue as I was unable to get to the root of it in time.
- Some unused imports and empty functions from initial boilerpolating. These have been left in place to demostrate what would have been developed given more time.
