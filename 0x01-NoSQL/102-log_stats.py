#!/usr/bin/env python3
"""
log_stats
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB.

    Parameters:
    mongo_collection (Collection): The pymongo collection object.

    Outputs:
    - Number of documents in the collection.
    - Count of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE).
    - Count of documents where method is GET and path is /status.
    - Top 10 IP addresses sorted by frequency.
    """
    # Count the total number of logs
    num_logs = mongo_collection.count_documents({})
    print(f'{num_logs} logs')

    # List of HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count documents with method GET and path /status
    status_check = mongo_collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        }
    )
    print(f'{status_check} status check')

    # Aggregation to get top 10 IP addresses by frequency
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)

    print('IPs:')
    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
