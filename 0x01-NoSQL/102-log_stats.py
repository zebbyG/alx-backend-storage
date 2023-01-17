#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
"""
required module for task
"""
if __name__ == "__main__":
    """
    run script
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

top_ips = collection_nginx.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

print("IPs:")
for top_ip in top_ips:
    ip = top_ip.get("ip")
    count = top_ip.get("count")
    print(f'\t{ip}: {count}')
