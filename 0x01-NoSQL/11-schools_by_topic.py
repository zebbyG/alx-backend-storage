#!/usr/bin/env python3
"""
A Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    :param mongo_collection: the pymongo collection object
    :param topic: (string) will be topic searched
    :return: the list of school having a specific topic
    """
    list_of_school = mongo_collection.find(topic)
    return list(list_of_school)
