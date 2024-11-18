import sqlite3
import csv
conn = sqlite3.connect('event_management.db', isolation_level = None)
cur = conn.cursor()

#drop tables first
cur.execute("DROP TABLE IF EXISTS attendees;")
cur.execute("DROP TABLE IF EXISTS events;")
cur.execute("DROP TABLE IF EXISTS tickets;")

create_table = '''CREATE TABLE attendees('attendee_id','name','email','age','registration_date')'''
cur.execute(create_table)

create_table1 = '''CREATE TABLE events('event_id','event_name','location','event_date','event_type','ticket_price')'''
cur.execute(create_table1)

create_table2 = '''CREATE TABLE tickets('ticket_id','event_id','attendee_id','purchase_date','seat_number')'''
cur.execute(create_table2)


file1=open('csv/attendees.csv')
contents1 = csv.reader(file1)
#throw away header
header1 = next(contents1)
insert_records1 = "INSERT INTO attendees('attendee_id','name','email','age','registration_date') VALUES(?, ?,?,?,?)"
cur.executemany(insert_records1, contents1)

delete_blank_lines1 = "DELETE FROM attendees where attendee_id = ''"
cur.execute(delete_blank_lines1)


file2=open('csv/events.csv')
contents2 = csv.reader(file2)
#throw away header
header2 = next(contents2)
insert_records2 = "INSERT INTO events('event_id','event_name','location','event_date','event_type','ticket_price') VALUES(?, ?, ?,?,?,?)"
cur.executemany(insert_records2, contents2)

delete_blank_lines2 = "DELETE FROM events where event_id = ''"
cur.execute(delete_blank_lines2)


file3=open('csv/tickets.csv')
contents3 = csv.reader(file3)
#throw away header
header3 = next(contents3)
insert_records3 = "INSERT INTO tickets('ticket_id','event_id','attendee_id','purchase_date','seat_number') VALUES(?, ?, ?, ?, ?)"
cur.executemany(insert_records3, contents3)

delete_blank_lines3 = "DELETE FROM tickets where ticket_id = ''"
cur.execute(delete_blank_lines3)


conn.commit()
conn.close()