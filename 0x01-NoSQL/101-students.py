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
