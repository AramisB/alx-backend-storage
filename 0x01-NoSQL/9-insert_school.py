#!/usr/bin/env python3
"""
a Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    kwargs (Dict): The new document to be inserted.
    Returns: The new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
