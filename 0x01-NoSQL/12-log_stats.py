#!/usr/bin/env python3
""" Write a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Database: logs
        Collection: nginx
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

<<<<<<< HEAD
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
=======
client = MongoClient('mongodb://127.0.0.1:27017')
collection_nginx = client.logs.nginx
num_of_logs = collection_nginx.count_documents({})
print(f"{num_of_logs} logs")
print("Methods:")
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for m in method:
    count_per_method = collection_nginx.count_documents({"method": m})
    print(f"\tmethod {m}: {count_per_method}")
>>>>>>> b286e179e22926fce799ee6af8bd3b2bd7f0f6e8

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f'{status_check} status check')
