#!/usr/bin/env python3
"""
A Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    :param mongo_collection: the pymongo collection object
    :param name: (string) will be the school name to update
    :param topics: (list of strings) will be the list of topics approached in the school
    """
    based_name = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(based_name, new_topics)
