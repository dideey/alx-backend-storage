#!/usr/bin/env python3
"""
returns a list of all documents in a collection
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """lists all documents"""
    return ([documents for documents in mongo_collection.find()])

