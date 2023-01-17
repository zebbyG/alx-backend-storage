<<<<<<< HEAD
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
=======
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
    insert_document = mongo_collection.insert_one(kwargs)
    return insert_document.inserted_id
>>>>>>> 88c4115a39dff248b76182fdf4ab4acc04d5fb23
