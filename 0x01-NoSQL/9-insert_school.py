#!/usr/bin/env python3
"""
A Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    :param mongo_collection: is the pymongo collection object
    :param kwargs: more arguments
    :return:  new _id
    """
    insert_document = mongo_collection.insert(kwargs)
    return insert_document
