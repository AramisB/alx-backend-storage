#!/usr/bin/env python3
"""
a Python function that changes all topics
of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.
    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    name (string): The name of the school to update.
    topics (list of strings): The list of topics approached in the school.
    Returns: The modified document with the new topics.
    """
    return mongo_collection.update_many(
        {
            "name": name
            },
        {"$set":
         {
             "topics": topics
             }
         }
         )
