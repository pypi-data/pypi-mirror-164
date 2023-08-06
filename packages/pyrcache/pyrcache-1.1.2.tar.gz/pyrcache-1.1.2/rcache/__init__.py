#!/usr/bin/env python3

from __future__ import annotations
import requests
import json

# GET one object
def rget(key: str, host: str = "localhost", port: int = 8080, db: int = 0) -> any:
    """
    Gets a value by key

    Parameters 
    -------------

        key: str

        host: str = "localhost"

        port: int = 8080

        db: int = 0

    Returns an object
    
    Raises JSONDecodeError if string couldn't be parsed
    """
    try:
        result = rsend("get", key, {}, host=host, port=port, db=db)
    except JSONDecodeError as err:
        raise JSONDecodeError(f"rget() -> {err}")
    else:
        return result

# POST one object
def rset(key: str, value: str | any, host: str = "localhost", port: int = 8080, db: int = 0):
    """
    Sets a value using key

    Parameters 
    -------------

        key: str

        value: str | any

        host: str = "localhost"

        port: int = 8080

        db: int = 0
    """
    rsend("set", key, value, host=host, port=port, db=db)

# GET all keys
def rkeys(host: str = "localhost", port: int = 8080, db: int = 0) -> list[str]:
    """
    Gets all keys

    Parameters 
    -------------

        host: str = "localhost"

        port: int = 8080

        db: int = 0

    Returns a list of keys
    """
    return rsend("get", "", {}, host=host, port=port, db=db)

# Send a request
def rsend(method: str, key: str, value: str | any, host: str = "localhost", port: int = 8080, db: int = 0) -> any:
    """
    Sends a request to Redis Server

    Parameters 
    -------------

        key: str

        value: str | any

        host: str = "localhost"

        port: int = 8080

        db: int = 0

    Returns an object

    Raises JSONDecodeError if result couldn't be parsed
    """
    params = {}
    if key != "":
        params.update({"key": key})
    if value != "" and value != {}:
        params.update({"value": json.dumps(value, ensure_ascii=True)})
    resp = requests.get(f"http://{host}:{port}/{db}/{method}", params=params)
    try:
        if len(resp.content) and method != "set":
            result = resp.json()
        else:
            result = {}
    except requests.JSONDecodeError as err:
        raise JSONDecodeError(f"send() - invalid result: {err}")
    else:
        return result

class JSONDecodeError(Exception):
    def __init__(self, message):
        self.message = message