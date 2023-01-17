#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    :param mongo_collection: the pymongo collection object
    :return: list of all documents in this collection
    """
    all_documents = mongo_collection.find()
    if all_documents == 0:
        return []
    return all_documents
