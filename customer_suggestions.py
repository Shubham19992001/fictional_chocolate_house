"""
Customer Suggestions Management Module

This module provides functionality to manage customer suggestions
in the Chocolate House Management System.
"""

from datetime import datetime

def manage_customer_suggestions(conn):
    """
    Main function to manage customer suggestions.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    while True:
        print("\nManage Customer Suggestions")
        print("1. Add new suggestion")
        print("2. View all suggestions")
        print("3. Delete suggestion")
        print("4. Return to main menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_suggestion(conn)
        elif choice == '2':
            view_suggestions(conn)
        elif choice == '3':
            delete_suggestion(conn)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_suggestion(conn):
    """
    Add a new customer suggestion to the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    flavor_name = input("Enter suggested flavor name: ")
    description = input("Enter flavor description: ")
    allergy_concerns = input("Enter any allergy concerns (comma-separated): ")
    submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customer_suggestions (flavor_name, description, allergy_concerns, submission_date) VALUES (?, ?, ?, ?)",
                   (flavor_name, description, allergy_concerns, submission_date))
    conn.commit()
    print("Suggestion added successfully!")

def view_suggestions(conn):
    """
    View all customer suggestions in the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_suggestions")
    suggestions = cursor.fetchall()
    
    if not suggestions:
        print("No suggestions found.")
    else:
        for suggestion in suggestions:
            print(f"ID: {suggestion[0]}, Flavor: {suggestion[1]}, Description: {suggestion[2]}")
            print(f"Allergy Concerns: {suggestion[3]}, Submitted: {suggestion[4]}")
            print("-" * 50)

def delete_suggestion(conn):
    """
    Delete a customer suggestion from the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    suggestion_id = input("Enter the ID of the suggestion to delete: ")
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customer_suggestions WHERE id = ?", (suggestion_id,))
    conn.commit()
    print("Suggestion deleted successfully!")
