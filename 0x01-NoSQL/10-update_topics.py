#!/usr/bin/env python3
"""
changes all topics of a document
"""

def update_topics(mongo_collection, name, topics):
    """update the topics"""
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )

