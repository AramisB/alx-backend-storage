#!/usr/bin
"""
schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    topic (string): The topic searched.
    Returns: List[Dict]: A list of documents in the collection.
    """
    return mongo_collection.find({"topics": topic})
