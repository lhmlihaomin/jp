"""
import words from csv files.
"""

import csv
import sqlite3
lesson_name = input("Lesson name: ")
fname = "%s.csv"%(lesson_name)
dbfile = "C:/Users/lhm/Documents/git/jp/db.sqlite3"

with sqlite3.connect(dbfile) as dbconn:
	c = dbconn.cursor()
	sql = "SELECT id FROM notebook_lesson WHERE name='%s'"%(lesson_name,)
	c.execute(sql)
	r = c.fetchone()
	if r == None:
		print("No such lesson.")
		exit()
	else:
		lesson_id = r[0]
		print(lesson_id)
	with open(fname, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			word = ''
			pronunciation = ''
			note = ''
			print(len(row))
			if len(row) <= 0:
				continue
			if len(row) >= 1:
				word = row[0]
			if len(row) >= 2:
				pronunciation = row[1]
			if len(row) >= 3:
				note = row[2]
			
			sql = "INSERT INTO notebook_word (word, pronunciation, note, marked, highlighted, mastered, lesson_id) VALUES ('%s', '%s', '%s', 0, 0, 0, %s)"
			sql = sql%(word, pronunciation, note, lesson_id)
			print(sql)
			c.execute(sql)
	dbconn.commit()
	