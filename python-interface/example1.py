# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# accessing a PostgreSQL database using psycopg2
# 
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

import psycopg2

# load the psycopg extras module
import psycopg2.extras

# try to connect to the given database
try:
	# enable connection
	database = "publications"
	user = "frank"
	host = "localhost"
	password = "password"
	conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (database, user, host, password))

	# print connector
	print (conn)

	# define cursor
	# - simple cursor
	# cur = conn.cursor()
	#
	# - a column-based cursor
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	# send an SQL query
	cur.execute("""SELECT * from publications""")

	# fetch data
	rows = cur.fetchall()

	print "Show me the content of %s:" % (database)
	for row in rows:
		keys = row.keys()
		for key in keys:
			print "%s: %s" % (key, row[key])

except:
	# puh ... we failed
    print "I am unable to connect to the database"

