#!/usr/bin/python
#encoding: UTF-8

import pdb

hostname = 'localhost'
username = 'ambev'
password = 'ambev'
database = 'pedida_development'

def doQuery( conn ) :
	cur = conn.cursor()

	cur.execute( "SELECT name FROM users LIMIT 10" )

	for user_name in cur.fetchall() :
		print user_name

print "Using psycopg2..."
import psycopg2

myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

doQuery( myConnection )
myConnection.close()

print "Using PyGreSQL…"
import pgdb
myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
doQuery( myConnection )
myConnection.close()