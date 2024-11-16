"""
Chocolate House Management System

This module serves as the main entry point for the Chocolate House Management System.
It provides a command-line interface for managing seasonal flavors, ingredient inventory,
and customer suggestions for a chocolate house business.
"""

import sqlite3
from datetime import datetime
import os

from seasonal_flavors import manage_seasonal_flavors
from ingredient_inventory import manage_ingredient_inventory
from customer_suggestions import manage_customer_suggestions

DB_NAME = 'chocolate_house.db'

def establish_db_connection():
    """
    Create and return a database connection.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)

def initialize_database(connection):
    """
    Set up the necessary tables in the database if they don't already exist.

    Args:
        connection (sqlite3.Connection): The database connection object.
    """
    with connection:
        db_cursor = connection.cursor()  # Changed from db_vs() to cursor()
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            season TEXT NOT NULL,
            description TEXT
        )
        ''')
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity REAL NOT NULL,
            unit TEXT NOT NULL
        )
        ''')
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY,
            flavor_name TEXT NOT NULL,
            description TEXT,
            allergy_concerns TEXT,
            submission_date TEXT NOT NULL
        )
        ''')

def display_main_menu():
    """Display the main menu options to the user."""
    print("\nChocolate House Management System")
    print("1. Manage Seasonal Flavors")
    print("2. Manage Ingredient Inventory")
    print("3. Manage Customer Suggestions")
    print("4. Exit")

def process_user_choice(choice, connection):
    """
    Process the user's menu choice and call the appropriate function.

    Args:
        choice (str): The user's input choice.
        connection (sqlite3.Connection): The database connection object.

    Returns:
        bool: False if the user chooses to exit, True otherwise.
    """
    if choice == '1':
        manage_seasonal_flavors(connection)
    elif choice == '2':
        manage_ingredient_inventory(connection)
    elif choice == '3':
        manage_customer_suggestions(connection)
    elif choice == '4':
        print("Thank you for using the Chocolate House Management System. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def run_application():
    """
    Main application loop.
    
    This function establishes a database connection, initializes the database,
    and runs the main menu loop until the user chooses to exit.
    """
    connection = establish_db_connection()
    initialize_database(connection)
    
    application_running = True
    while application_running:
        display_main_menu()
        user_choice = input("Enter your choice (1-4): ")
        application_running = process_user_choice(user_choice, connection)
    
    connection.close()

if __name__ == "__main__":
    run_application()
