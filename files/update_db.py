#!/usr/bin/env python
import pymongo
import sys

def update_runs_count(url):
  client = pymongo.MongoClient("mongodb://localhost:27017/labs_stats_db")
  db = client.labs_stats_db

  runs = db.GlobalStats.find({'name': 'runs'})
  if runs.count() == 0:
    db.GlobalStats.insert({'name': 'runs', 'count': 1})
  else:
    db.GlobalStats.update_one({'name': 'runs'}, {'$inc': {'count': 1}}, upsert=False)

def update_count_per_user(url, username):
  client = pymongo.MongoClient("mongodb://localhost:27017/labs_stats_db")
  db = client.labs_stats_db

  user_runs_count = db.UserRuns.find({'username': username})
  unique_users_count = db.GlobalStats.find({'name': 'unique_users'})

  if unique_users_count.count() == 0:
    db.GlobalStats.insert({'name': 'unique_users', 'count': 1})

  if user_runs_count.count() == 0:
    db.UserRuns.insert({'username': username, 'count': 1})
    db.GlobalStats.update_one({'name': 'unique_users'}, {'$inc': {'count': 1}}, upsert=False)
  else:
    db.UserRuns.update_one({'username': username}, {'$inc': {'count': 1}}, upsert=False)

command = sys.argv[1]
url = sys.argv[2]
username = sys. argv[3]

if command == 'update_runs_count':
  update_runs_count(url)
elif command == 'update_count_per_user':
  update_count_per_user(url, username)
