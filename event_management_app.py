from event_management_functions import (display_table, add_record, modify_record, remove_record,
                                        generate_visualizations, basic_statistical_query , where_query, join_query)

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
# attendees table has columns attendee_id, name, email, age, registration_date
# tickets table has columns ticket_id, event_id, attendee_id, purchase_date, seat_number

# welcome message function
def welcome_message():
    print("Welcome to the Event Management App!")
    print("This app allows you to manage events, attendees, and tickets.")
    print("You can add, remove, and modify records from all tables.")
    print("You can also make basic statistical queries and query against any column using WHERE.")
    print("Let's get started!")

# main function to run the app
def main():
    welcome_message()

    # while loop to keep the app running as the user enters commands
    while True:
        print("Enter a command:")
        print("1. Display a table")
        print("2. Add a table entry")
        print("3. Remove a table entry")
        print("4. Modify a table entry")
        print("5. Make a basic statistical query (min, max, mean, median, standard deviation)")
        print("6. Enter a query against any column using WHERE")
        print("7. Perform a query with JOIN")
        print("8. Generate Visualizations")
        print("9. Exit")
        command = input("Enter the command number: ")

        if command == "1":
            display_table()
        elif command == "2":
            add_record()
        elif command == "3":
            remove_record()
        elif command == "4":
            modify_record()
        elif command == "5":
            basic_statistical_query()
        elif command == "6":
            where_query()
        elif command == "7":
            join_query()
        elif command == "8":
            generate_visualizations()
        elif command == "9":
            print("Exiting the Event Management App. Thank you!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

