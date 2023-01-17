<<<<<<< HEAD
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
=======
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

    top_ips = nginx_collection.aggregate([
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
>>>>>>> 88c4115a39dff248b76182fdf4ab4acc04d5fb23
