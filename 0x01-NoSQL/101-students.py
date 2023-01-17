<<<<<<< HEAD
#!/usr/bin/env python3
"""
A Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    :param mongo_collection: the pymongo collection object
    :return: all students sorted by average score
    """
    # Use the aggregate method to calculate the average score for each student
    students = [
            {"$group": {"_id": "$student_id", "averageScore": {"$avg": "$score"}}},
            {"$sort": {"averageScore": -1}}
        ]
    result = mongo_collection.aggregate(students)
    return list(sorted(result))
=======
#!/usr/bin/env python3
""" Write a Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ mongo_collection will be the pymongo collection object
        - The top must be ordered
        - The average score must be part of each item
          returns with key = averageScore
    """
    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
>>>>>>> 88c4115a39dff248b76182fdf4ab4acc04d5fb23
