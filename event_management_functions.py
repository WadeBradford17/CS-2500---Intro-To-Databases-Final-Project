import sqlite3

# function to display all records in a table
# prompt user for which table (attendees, events, tickets) to display
def display_table():
    connection = sqlite3.connect('event_management.db')
    cursor = connection.cursor()

    print("Which table would you like to display?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        cursor.execute("SELECT * FROM attendees")
        rows = cursor.fetchall()
        print("attendee_id, name, email, age, registration_date")
        for row in rows:
            print(row)

    elif table_choice == "2":
        cursor.execute("SELECT * FROM events")
        rows = cursor.fetchall()
        print("event_id, event_name, location, event_date, event_type, ticket_price")
        for row in rows:
            print(row)

    elif table_choice == "3":
        cursor.execute("SELECT * FROM tickets")
        rows = cursor.fetchall()
        print("ticket_id, event_id, attendee_id, purchase_date, seat_number")
        for row in rows:
            print(row)

    else:
        print("Invalid table choice. Please try again.")


# function to add an entry to a table
# prompt user for which table (attendees, events, tickets) and values for the type of table
def add_record():
    connection = sqlite3.connect('event_management.db')
    cursor = connection.cursor()

    print("Which table would you like to add an entry to?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        cursor.execute("SELECT MAX(attendee_id) FROM attendees")
        last_attendee_id = cursor.fetchone()[0]
        # turn last_attendee_id into an integer
        last_attendee_id = int(last_attendee_id)
        if last_attendee_id is None:
            last_attendee_id = 0
        attendee_id = last_attendee_id + 1
        name = input("Enter the full name of the attendee: ")
        email = input("Enter the email of the attendee: ")
        age = input("Enter the age of the attendee: ")
        registration_date = input("Enter the registration date of the attendee (YYYY-MM-DD): ")

        cursor.execute("INSERT INTO attendees (attendee_id, name, email, age, registration_date) VALUES (?, ?, ?, ?)",
                       (attendee_id, name, email, age, registration_date))
        connection.commit()
        print("Record added to attendees table successfully.")

    elif table_choice == "2":
        cursor.execute("SELECT MAX(event_id) FROM events")
        last_event_id = cursor.fetchone()[0]
        last_event_id = int(last_event_id)
        if last_event_id is None:
            last_event_id = 0
        event_id = last_event_id + 1
        event_name = input("Enter the name of the event: ")
        location = input("Enter the location of the event: ")
        event_date = input("Enter the date of the event (YYYY-MM-DD): ")
        event_type = input("Enter the type of the event: ")
        ticket_price = input("Enter the ticket price of the event: ")

        cursor.execute("INSERT INTO events (event_id, event_name, location, event_date, event_type, ticket_price) "
                       "VALUES (?, ?, ?, ?, ?)",
                       (event_id, event_name, location, event_date, event_type, ticket_price))
        connection.commit()
        print("Record added to events table successfully.")

    elif table_choice == "3":
        cursor.execute("SELECT MAX(ticket_id) FROM tickets")
        last_ticket_id = cursor.fetchone()[0]
        last_ticket_id = int(last_ticket_id)
        if last_ticket_id is None:
            last_ticket_id = 0
        ticket_id = last_ticket_id + 1
        event_id = input("Enter the event ID: ")
        attendee_id = input("Enter the attendee ID: ")
        purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
        seat_number = input("Enter the seat number: ")

        cursor.execute("INSERT INTO tickets (ticket_id, event_id, attendee_id, purchase_date, seat_number) "
                       "VALUES (?, ?, ?, ?)",
                       (ticket_id, event_id, attendee_id, purchase_date, seat_number))
        connection.commit()
        print("Record added to tickets table successfully.")

    else:
        print("Invalid table choice. Please try again.")

# function to modify an entry in a table
# prompt user for which table (attendees, events, tickets), which column to modify, and the new value
def modify_record():
    connection = sqlite3.connect('event_management.db')
    cursor = connection.cursor()

    print("Which table would you like to modify an entry in?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        print("Which column would you like to modify?")
        print("1. Full Name")
        print("2. Email")
        print("3. Age")
        print("4. Registration Date")
        column_choice = input("Enter the column number: ")

        if column_choice == "1":
            new_value = input("Enter the new full name: ")
            attendee_id = input("Enter the attendee ID: ")
            cursor.execute("UPDATE attendees SET name = ? WHERE attendee_id = ?", (new_value, attendee_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "2":
            new_value = input("Enter the new email: ")
            attendee_id = input("Enter the attendee ID: ")
            cursor.execute("UPDATE attendees SET email = ? WHERE attendee_id = ?", (new_value, attendee_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "3":
            new_value = input("Enter the new age: ")
            attendee_id = input("Enter the attendee ID: ")
            cursor.execute("UPDATE attendees SET age = ? WHERE attendee_id = ?", (new_value, attendee_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "4":
            new_value = input("Enter the new registration date (YYYY-MM-DD): ")
            attendee_id = input("Enter the attendee ID: ")
            cursor.execute("UPDATE attendees SET registration_date = ? WHERE attendee_id = ?", (new_value, attendee_id))
            connection.commit()
            print("Record modified successfully.")

        else:
            print("Invalid column choice. Please try again.")

    elif table_choice == "2":
        print("Which column would you like to modify?")
        print("1. Event Name")
        print("2. Location")
        print("3. Event Date")
        print("4. Event Type")
        print("5. Ticket Price")
        column_choice = input("Enter the column number: ")

        if column_choice == "1":
            new_value = input("Enter the new event name: ")
            event_id = input("Enter the event ID: ")
            cursor.execute("UPDATE events SET event_name = ? WHERE event_id = ?", (new_value, event_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "2":
            new_value = input("Enter the new location: ")
            event_id = input("Enter the event ID: ")
            cursor.execute("UPDATE events SET location = ? WHERE event_id = ?", (new_value, event_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "3":
            new_value = input("Enter the new event date (YYYY-MM-DD): ")
            event_id = input("Enter the event ID: ")
            cursor.execute("UPDATE events SET event_date = ? WHERE event_id = ?", (new_value, event_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "4":
            new_value = input("Enter the new event type: ")
            event_id = input("Enter the event ID: ")
            cursor.execute("UPDATE events SET event_type = ? WHERE event_id = ?", (new_value, event_id))
            connection.commit()
            print("Record modified successfully.")

        elif column_choice == "5":
            new_value = input("Enter the new ticket price: ")
            event_id = input("Enter the event ID: ")
            cursor.execute("UPDATE events SET ticket_price = ? WHERE event_id = ?", (new_value, event_id))
            connection.commit()
            print("Record modified successfully.")

        else:
            print("Invalid column choice. Please try again.")

# function to remove a record from the table
# prompt user for which table (attendees, events, tickets) and the ID of the record to remove
def remove_record():
    connection = sqlite3.connect('event_management.db')
    cursor = connection.cursor()

    print("Which table would you like to remove an entry from?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        attendee_id = input("Enter the attendee ID to remove: ")
        cursor.execute("DELETE FROM attendees WHERE attendee_id = ?", (attendee_id,))
        connection.commit()
        print("Record removed from attendees table successfully.")

    elif table_choice == "2":
        event_id = input("Enter the event ID to remove: ")
        cursor.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
        connection.commit()
        print("Record removed from events table successfully.")

    elif table_choice == "3":
        ticket_id = input("Enter the ticket ID to remove: ")
        cursor.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
        connection.commit()
        print("Record removed from tickets table successfully.")

    else:
        print("Invalid table choice. Please try again.")
