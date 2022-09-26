#!/usr/bin/env python

import logging
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import psycopg2


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

conn = psycopg2.connect(
	dbname=os.environ['TRACKER_DB'],
	user=os.environ['TRACKER_USERNAME'],
	password=os.environ['TRACKER_PASSWORD'],
	host=os.environ['TRACKER_HOST'])

with conn.cursor() as cursor:
	res = cursor.execute("""
	CREATE TABLE IF NOT EXISTS votes (
            "item" VARCHAR(100),
            "time" TIMESTAMP,
            "userId" VARCHAR(20),
            PRIMARY KEY ("userId", "item")
	);""")
	conn.commit()

app = FastAPI()

class Vote(BaseModel):
	userId: str
	item: str

@app.post('/vote')
def vote(vote: Vote):
	logging.info(f"Vote: ${vote}")
	with conn.cursor() as cursor:
		cursor.execute("""
		INSERT INTO votes(item, "userId", time) VALUES ('%s', '%s', now())
		""" % (vote.item, vote.userId))
		conn.commit()
	

@app.get('/')
def index():
	return FileResponse("index.html")


	
	
