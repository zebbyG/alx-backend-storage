<<<<<<< HEAD
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
=======
#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    :param mongo_collection: the pymongo collection object
    :return: list of all documents in this collection
    """
    all_documents = mongo_collection.find({})
    if all_documents == 0:
        return []
    return all_documents
>>>>>>> 88c4115a39dff248b76182fdf4ab4acc04d5fb23
