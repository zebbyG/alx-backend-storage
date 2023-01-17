#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
"""
required module for task
"""

client = MongoClient('mongodb://127.0.0.1:27017')
collection_nginx = client.logs.nginx
num_of_logs = collection_nginx.count_documents({})
print(f"{num_of_logs} logs")
print("Methods:")
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for m in method:
    count_per_method = collection_nginx.count_documents({"method": method})
    print(f"\tmethod {m}: {count_per_method}")

status_check = collection_nginx.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")
