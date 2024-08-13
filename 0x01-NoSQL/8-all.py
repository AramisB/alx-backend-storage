#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    Returns:
    List[Dict]: A list of documents in the collection.
                An empty list if no documents are found.
    """
    count = mongo_collection.count_documents({})
    if count == 0:
        return []

    return list(mongo_collection.find())
