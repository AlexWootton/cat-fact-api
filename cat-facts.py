#!/usr/bin/env python3

import click  # intended for CLI argument parsing
import models
import requests
import string

from flask import Flask, jsonify  # intended for providing HTTP server and JSON
from flask_restful import Resource, Api  # intended for serving API endpoint

SOURCE = 'https://cat-fact.herokuapp.com/facts'

def GetFacts():
    """Fetches and stores facts that meet the filter criteria."""
    # create a list with all letters of the alphabet
    fact_filter = list(string.ascii_lowercase)

    # using a slice, reduce this list to just the odd numbered characters
    fact_filter = fact_filter[::2]

    # try to fetch latest facts from the specified source
    try:
        r = requests.get(SOURCE)
        data = r.json()
    except:
        print('Unable to fetch latest facts. Using existing data...')
    else:
        # check each fact's user's name against our filter
        # TODO add check for ids matching blacklisted ids
        for fact in data['all']:
            # this try block is needed to bypass an issue I could not solve
            # where a KeyError for the 'user' key occurs
            try:  
                if fact['user']['name']['first'][0].lower() in fact_filter:
                    # try to store acceptable facts in the database
                    try:
                        models.Fact.create(
                            _id=fact['_id'],
                            text=fact['text']
                        )
                    # skip if fact id already exists in the database
                    # TODO check if id exists before trying to create a new record
                    except models.IntegrityError:
                        continue
            # silently ignoring KeyErrors as could not find root cause
            except KeyError:
                continue
    return


def ListFacts():
    """Returns all stored facts in the specified format.
    Format defaults to pretty print.
    Format options:
        pretty, json, yaml, csv
    """
    query = models.Fact.select()
    for fact in query:
        print('ID: {} | {}'.format(fact._id, fact.text))
    return


def DeleteFact(id):
    """Deletes the specified fact and adds its ID to the blacklist
    to ensure that it is ignored during future fetches.
    """
    return


def ServeAPI():
    """Starts an http server that returns all stored facts as JSON when it recives a GET request at the root path"""
    return

if __name__ == "__main__":
    models.initialise()
    GetFacts()
    ListFacts()