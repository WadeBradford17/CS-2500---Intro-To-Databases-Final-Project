import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect('event_management.db')
cursor = connection.cursor()
# function to display all records in a table
# prompt user for which table (attendees, events, tickets) to display
def display_table():
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
    print("Which table would you like to add an entry to?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        cursor.execute("SELECT attendee_id FROM attendees ORDER BY cast(attendee_id as int) DESC LIMIT 1")
        last_attendee_id = cursor.fetchone()[0]
        last_attendee_id = int(last_attendee_id)
        if last_attendee_id is None:
            last_attendee_id = 0
        attendee_id = last_attendee_id + 1
        # turn it back into a string in this format 'id'
        attendee_id = str(attendee_id)
        name = input("Enter the full name of the attendee: ")
        email = input("Enter the email of the attendee: ")
        age = input("Enter the age of the attendee: ")
        registration_date = input("Enter the registration date of the attendee (MM/DD/YYYY): ")

        cursor.execute("INSERT INTO attendees (attendee_id, name, email, age, registration_date) VALUES (?, ?, ?, ?, ?)",
                       (attendee_id, name, email, age, registration_date))
        connection.commit()
        print("Record added to attendees table successfully.")

    elif table_choice == "2":
        cursor.execute("SELECT event_id FROM events ORDER by cast(event_id as int) DESC LIMIT 1")
        last_event_id = cursor.fetchone()[0]
        last_event_id = int(last_event_id)
        if last_event_id is None:
            last_event_id = 0
        event_id = last_event_id + 1
        event_name = input("Enter the name of the event: ")
        location = input("Enter the location of the event: ")
        event_date = input("Enter the date of the event (MM/DD/YYYY): ")
        event_type = input("Enter the type of the event: ")
        ticket_price = input("Enter the ticket price of the event: ")

        cursor.execute("INSERT INTO events (event_id, event_name, location, event_date, event_type, ticket_price) "
                       "VALUES (?, ?, ?, ?, ?, ?)",
                       (event_id, event_name, location, event_date, event_type, ticket_price))
        connection.commit()
        print("Record added to events table successfully.")

    elif table_choice == "3":
        cursor.execute("SELECT ticket_id FROM tickets ORDER BY cast(ticket_id as int) DESC LIMIT 1")
        last_ticket_id = cursor.fetchone()[0]
        last_ticket_id = int(last_ticket_id)
        if last_ticket_id is None:
            last_ticket_id = 0
        ticket_id = last_ticket_id + 1
        event_id = input("Enter the event ID: ")
        attendee_id = input("Enter the attendee ID: ")
        purchase_date = input("Enter the purchase date (MM/DD/YYYY): ")
        seat_number = input("Enter the seat number: ")

        cursor.execute("INSERT INTO tickets (ticket_id, event_id, attendee_id, purchase_date, seat_number) "
                       "VALUES (?, ?, ?, ?, ?)",
                       (ticket_id, event_id, attendee_id, purchase_date, seat_number))
        connection.commit()
        print("Record added to tickets table successfully.")

    else:
        print("Invalid table choice. Please try again.")

# function to modify an entry in a table
# prompt user for which table (attendees, events, tickets), which column to modify, and the new value
def modify_record():

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


# function to make basic statistical queries such as- mean, min,
# max, median, standard deviation mean, on numerical columns
def basic_statistical_query():

    print("Which table would you like to make a basic statistical query on?")
    print("1. Attendees")
    print("2. Events")
    print("(Tickets does not have numerical columns for statistical queries.)")

    table_choice = input("Enter the table number: ")

    if table_choice == "1":
        print("Which column would you like to make a basic statistical query on?")
        print("1. Age")
        column_choice = input("Enter the column number: ")

        if column_choice == "1":
            # select which query to do
            print("Which query would you like to make?")
            print("1. Mean")
            print("2. Minimum")
            print("3. Maximum")
            print("4. Median")
            print("5. Standard Deviation")
            query_choice = input("Enter the query number: ")

            if query_choice == "1":
                cursor.execute("SELECT AVG(age) FROM attendees")
                avg_age = cursor.fetchone()[0]
                print("Average age of attendees:", avg_age)
            elif query_choice == "2":
                cursor.execute("SELECT MIN(age) FROM attendees")
                min_age = cursor.fetchone()[0]
                print("Minimum age of attendees:", min_age)
            elif query_choice == "3":
                cursor.execute("SELECT MAX(age) FROM attendees")
                max_age = cursor.fetchone()[0]
                print("Maximum age of attendees:", max_age)
            elif query_choice == "4":
                cursor.execute("SELECT AVG(age) FROM attendees")
                avg_age = cursor.fetchone()[0]
                print("Median age of attendees:", avg_age)
            elif query_choice == "5":
                cursor.execute("SELECT AVG(age) FROM attendees")
                avg_age = cursor.fetchone()[0]
                cursor.execute("SELECT age FROM attendees")
                rows = cursor.fetchall()
                ages = [int(row[0]) for row in rows]  # Convert ages to integers
                sum_squared_diff = sum((age - avg_age) ** 2 for age in ages)
                standard_deviation = (sum_squared_diff / len(ages)) ** 0.5
                print("Standard deviation of ages of attendees:", standard_deviation)
            else:
                print("Invalid query choice. Please try again.")

        else:
            print("Invalid column choice. Please try again.")

    elif table_choice == "2":
        print("Which column would you like to make a basic statistical query on?")
        print("1. Ticket Price")
        column_choice = input("Enter the column number: ")

        if column_choice == "1":
            # select which query to do
            print("Which query would you like to make?")
            print("1. Mean")
            print("2. Minimum")
            print("3. Maximum")
            print("4. Median")
            print("5. Standard Deviation")
            query_choice = input("Enter the query number: ")

            if query_choice == "1":
                cursor.execute("SELECT AVG(ticket_price) FROM events")
                avg_ticket_price = cursor.fetchone()[0]
                print("Average ticket price of events:", avg_ticket_price)
            elif query_choice == "2":
                cursor.execute("SELECT MIN(ticket_price) FROM events")
                min_ticket_price = cursor.fetchone()[0]
                print("Minimum ticket price of events:", min_ticket_price)
            elif query_choice == "3":
                cursor.execute("SELECT MAX(ticket_price) FROM events")
                max_ticket_price = cursor.fetchone()[0]
                print("Maximum ticket price of events:", max_ticket_price)
            elif query_choice == "4":
                cursor.execute("SELECT AVG(ticket_price) FROM events")
                avg_ticket_price = cursor.fetchone()[0]
                print("Median ticket price of events:", avg_ticket_price)
            elif query_choice == "5":
                cursor.execute("SELECT AVG(ticket_price) FROM events")
                avg_ticket_price = cursor.fetchone()[0]
                cursor.execute("SELECT ticket_price FROM events")
                rows = cursor.fetchall()
                ticket_prices = [float(row[0]) for row in rows]  # Convert ticket prices to floats
                sum_squared_diff = sum((price - avg_ticket_price) ** 2 for price in ticket_prices)
                standard_deviation = (sum_squared_diff / len(ticket_prices)) ** 0.5
                print("Standard deviation of ticket prices of events:", standard_deviation)
            else:
                print("Invalid query choice. Please try again.")


#function to let user perform queries using "where"
def where_query():
    print("Which table would you like to perform a query on?")
    print("1. Attendees")
    print("2. Events")
    print("3. Tickets")

    table_choice = input("Enter the table number: ")
    if table_choice =="1":
        cursor.execute("PRAGMA table_info(attendees)")
        columns = [row[1] for row in cursor.fetchall()]
        user_query=input("Please enter one query: ")
        new_query=user_query.split(" ", 2)

        while new_query[0].lower() not in columns or new_query[1] not in ["<", ">", "=", '>=', '<=']:
            print('Please enter valid query: ')
            user_query=input("Please enter one valid query: ")
            new_query=user_query.split(" ")

        column = new_query[0].strip().lower()
        operator = new_query[1]
        value = new_query[2].strip()

        if (column == 'name' or column == 'email' or column == 'registration_date') and operator in ['>', '<']:
            print('No results')
        
        else:
            cursor.execute(f"Select * from attendees where {column} {operator} ?", (value,))
            query1 = cursor.fetchall()
            for row in query1:
                print(row)
    elif table_choice == '2':
        cursor.execute("PRAGMA table_info(events)")
        columns = [row[1] for row in cursor.fetchall()]
        user_query=input("Please enter one query: ")
        new_query=user_query.split(" ", 2)

        while new_query[0].lower() not in columns or new_query[1] not in ["<", ">", "=", '<=', '>=']:
            user_query=input("Please enter one valid query: ")
            new_query=user_query.split(" ")

        column = new_query[0].strip().lower()
        operator = new_query[1]
        value = new_query[2].strip()

        if (column == 'event_name' or column == 'location' or column == 'event_date' or column == 'event_type') and operator in ['>', '<']:
            print('No results')
                
        
        else:
            cursor.execute(f"Select * from events where {column} {operator} ?", (value,))
            query1 = cursor.fetchall()
            for row in query1:
                print(row)
    elif table_choice == '3':
        cursor.execute("PRAGMA table_info(tickets)")
        columns = [row[1] for row in cursor.fetchall()]
        user_query=input("Please enter one query: ")
        new_query=user_query.split(" ", 2)

        while new_query[0].lower() not in columns or new_query[1] not in ['=']:
            user_query=input("Please enter one valid query: ")
            new_query=user_query.split(" ")

        column = new_query[0].strip().lower()
        operator = new_query[1]
        value = new_query[2].strip()

        cursor.execute(f"Select * from tickets where {column} {operator} ?", (value,))
        query1 = cursor.fetchall()
        for row in query1:
            print(row)
    else:
        print('Not a valid table choice\n')


#offers the user some queries to perform to see an example join query
def join_query():
    print('Which query would you like to perform?')
    print("1. A person's age versus how much they spent on an event ticket")
    print("2. Which attendees have purchased tickets for which events ")
    print('3. Which events are attended by people above age 30')
    print('4. A list of events in order of ticket price, and who is attending them')
    col_choice = input('Enter a number: ')
    if col_choice == '1':
        cursor.execute('select age, ticket_price from tickets natural join attendees natural join events')
        result1=cursor.fetchall()
        for row in result1:
            print(row)
    if col_choice == '2':
        cursor.execute('select name, email, event_name from tickets natural join attendees natural join events')
        result2=cursor.fetchall()
        for row in result2:
            print(row)
    if col_choice == '3':
        cursor.execute("select age, event_name from tickets natural join attendees natural join events where age > '30'")
        result3=cursor.fetchall()
        for row in result3:
            print(row)
    if col_choice == '4':
        cursor.execute('select ticket_price, name, email, event_name from tickets natural join attendees natural join events order by cast(ticket_price as float)')
        result4=cursor.fetchall()
        for row in result4:
            print(row)
    else:
        print('Not a valid column choice')


# function to display bar plot of the number of events in each month and pie chart of event type
def generate_visualizations():
    cursor.execute("SELECT event_date FROM events")
    rows = cursor.fetchall()

    # the dates are in M/DD/YYYY format
    months = []
    for row in rows:
        date = row[0]
        month = date.split('/')[0]
        months.append(month)

    # count the number of events in each month
    month_counts = {}
    for month in months:
        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1

    # create a bar plot of the number of events in each month
    plt.bar(month_counts.keys(), month_counts.values())
    plt.xlabel('Month')
    plt.ylabel('Number of Events')
    plt.title('Number of Events in Each Month')
    plt.show()

    # create a pie chart of the event types
    cursor.execute("SELECT event_type FROM events")
    rows = cursor.fetchall()
    event_types = []
    for row in rows:
        event_types.append(row[0])

    event_type_counts = {}
    for event_type in event_types:
        if event_type in event_type_counts:
            event_type_counts[event_type] += 1
        else:
            event_type_counts[event_type] = 1

    plt.pie(event_type_counts.values(), labels=event_type_counts.keys(), autopct='%1.1f%%')
    plt.title('Event Types')
    plt.show()

    print("Visualizations generated successfully, shown one at a time.")
