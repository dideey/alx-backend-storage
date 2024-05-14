#!/usr/bin/env python3

"""
returns a list of schools based on specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """returns list"""
    schools = mongo_collection.find({"topic": topic})
    return (topics for topics in schools)

