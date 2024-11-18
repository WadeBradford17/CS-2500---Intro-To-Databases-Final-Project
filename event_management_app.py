import sqlite3

# a.) App should allow user to add, remove, and modify
# records from all tables.
# b) Allow user to make basic statistical queries such as- Mean, min,
# max, median, standard deviation mean, on numerical columns.
# c) Allow user to query against any column using WHERE and list sample data.
# d) Allow for 2 queries that require a JOIN.
# e) Allow visualizations for key metrics of your choice with at least two different types
# of plots.

# our three SQL database tables are events, attendees, tickets
# events table has columns event_id, event_name, location, event_date, event_type, ticket_price
# attendees table has columns attendee_id, full_name, email, age, registration_date
# tickets table has columns ticket_id, event_id, attendee_id, purchase_date, seat_number


