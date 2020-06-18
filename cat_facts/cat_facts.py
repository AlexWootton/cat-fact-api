#!/usr/bin/env python3

import click
import models
import formatters
import requests
import string

from resources import facts_api
from flask import Flask

SOURCE = "https://cat-fact.herokuapp.com/facts"


# registering the Flask app and API blueprint
app = Flask(__name__)
app.register_blueprint(facts_api, url_prefix="/api/v1")


@click.group()
def cli():
    """A command line interface for viewing and deleting facts about cats."""
    return


def GetFacts():
    """Fetches and stores facts that meet the filter criteria."""
    # create a list with all letters of the alphabet
    fact_filter = list(string.ascii_lowercase)

    # using a slice, reduce this list to just the odd numbered characters
    fact_filter = fact_filter[::2]

    # try to fetch latest data from the specified source
    try:
        r = requests.get(SOURCE)
        data = r.json()
    except:
        print("Unable to fetch form source. Using existing data...")
    else:
        for fact in data["all"]:
            # this try block is needed to bypass an issue I could not solve
            # where a KeyError for the 'user' key occurs
            try:
                # check each fact's user's name against our filter
                if fact["user"]["name"]["first"][0].lower() in fact_filter:
                    # check whether the id is blacklisted
                    if (
                        not models.Blacklist.select()
                        .where(models.Blacklist._id == fact["_id"])
                        .exists()
                    ):
                        # try to store acceptable facts in the database
                        try:
                            models.Fact.create(_id=fact["_id"], text=fact["text"])
                        # skip if fact id already exists in the database
                        except models.IntegrityError:
                            continue
            # silently handling KeyErrors as could not find root cause
            except KeyError:
                continue
    return


@cli.command("list")
@click.option(
    "-F",
    "--format",
    default="pretty",
    show_default=True,
    help="List output format.",
    metavar="FORMAT",
)
def ListFacts(format):
    """Returns all stored facts in the specified format.
    Format defaults to pretty print.
    Format options:
        pretty, json
    """
    # attempt to fetch latest facts data
    GetFacts()

    # select all facts from the database and pass to the relevant formatter
    query = models.Fact.select()
    if format == "pretty":
        print(formatters.ConvertToPretty(query))
    elif format == "json":
        print(formatters.ConvertToJson(query))
    else:
        print("Unrecognised output format specified.")
    return


@cli.command("delete")
@click.option(
    "--id", prompt="ID", help="The ID of the fact to be deleted.", metavar="ID"
)
def DeleteFact(id):
    """Deletes the specified fact and adds its ID to the blacklist.
    Ensures that facts are not restored on subsequent fetches.
    """
    # check the result of an attempted deletion
    # returns the number of rows deleted which we interpret as true or false
    if models.Fact.delete().where(models.Fact._id == id).execute():
        print("Fact ID: {} has been deleted.".format(id))
        # try to create a Blacklist entry with the specified id
        try:
            models.Blacklist.create(_id=id)
        # an IntergrityError can be assumed to mean that the id already exists
        # as we enforce uniqueness on this field in the database model
        except models.IntegrityError:
            print("Fact ID: {} is already blacklisted".format(id))
    else:
        print("Fact ID: {} does not exist".format(id))
    return


@cli.command("server")
@click.option(
    "-h",
    "--host",
    default="0.0.0.0",
    show_default=True,
    help="The host address to listen on.",
    metavar="IP",
)
@click.option(
    "-p",
    "--port",
    default=8080,
    show_default=True,
    help="The port to listen on.",
    metavar="PORT",
)
@click.option(
    "--debug",
    is_flag=True,
    default=False,
    help="Enables DEBUG mode on the HTTP server.",
    metavar="DEBUG",
)
def ServeAPI(host, port, debug):
    """Starts an http server that returns all stored facts as JSON.

    Provides two endpoints: `/api/v1/facts` and `/api/v1/facts/<id>`.

    `/api/v1/facts` returns all stored facts as JSON.

    `/api/v1/facts/<id>` can be passed a fact ID and will return the matching
    fact as JSON if it exists in the database.

    Optional parameters for host address, port number and to enable debug mode.
    Defaults to listening on `0.0.0.0` and `8080` with debug mode off.
    """
    app.run(debug=debug, host=host, port=port)
    return


if __name__ == "__main__":
    models.initialise()
    cli()
