# import unittest
import pytest
import os

from pymongo import MongoClient
from mongo.mongo import search_item, search_item_by_id

URI = os.getenv("MONGODB_CONNSTRING")

@pytest.fixture
def mongo_client():
    return MongoClient(URI)

def test_search_item(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection
    collection.insert_one({"docname": "testdoc1", "testattr": "test1"})
    collection.insert_one({"docname": "testdoc2", "testattr": "test2"})

    result = search_item(URI, "test_database", "test_collection", {"docname": "testdoc1"})

    assert result[0]["docname"] == "testdoc1"
    assert result[0]["testattr"] == "test1"

    collection.drop()

def test_search_item_not_found(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection
    collection.insert_one({"docname": "testdoc1", "testattr": "test1"})
    collection.insert_one({"docname": "testdoc2", "testattr": "test2"})

    result = search_item(URI, "test_database", "test_collection", {"docname": "testdoc3"})

    assert result == []

    collection.drop()

def test_search_item_get_all(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection
    collection.insert_one({"docname": "testdoc1", "testattr": "test1"})
    collection.insert_one({"docname": "testdoc2", "testattr": "test2"})

    result = search_item(URI, "test_database", "test_collection", {})

    assert len(result) == 2
    assert result[0]["docname"] == "testdoc1"
    assert result[0]["testattr"] == "test1"
    assert result[1]["docname"] == "testdoc2"
    assert result[1]["testattr"] == "test2"

    collection.drop()

def test_search_item_by_id(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection
    collection.insert_one({"docname": "testdoc1", "testattr": "test1"})
    item = search_item(URI, "test_database", "test_collection", {"docname": "testdoc1"})

    result = search_item_by_id(URI, "test_database", "test_collection", {"_id": item[0]["_id"]})

    assert result[0]["docname"] == "testdoc1"
    assert result[0]["testattr"] == "test1"

    collection.drop()

def test_search_item_by_id_not_found(mongo_client):
    db = mongo_client.test_database
    collection = db.test_collection
    collection.insert_one({"docname": "testdoc1", "testattr": "test1"})
    item = search_item(URI, "test_database", "test_collection", {"docname": "testdoc1"})

    result = search_item_by_id(URI, "test_database", "test_collection", {"_id": "aaaaaaaaaaaaaaaaaaaaaaaa"})

    assert result == []

    collection.drop()