"""
Seasonal Flavors Management Module

This module provides functionality to manage seasonal chocolate flavors
in the Chocolate House Management System.
"""

def manage_seasonal_flavors(conn):
    """
    Main function to manage seasonal flavors.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    while True:
        print("\nManage Seasonal Flavors")
        print("1. Add new flavor")
        print("2. View all flavors")
        print("3. Update flavor")
        print("4. Delete flavor")
        print("5. Return to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_flavor(conn)
        elif choice == '2':
            view_flavors(conn)
        elif choice == '3':
            update_flavor(conn)
        elif choice == '4':
            delete_flavor(conn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_flavor(conn):
    """
    Add a new seasonal flavor to the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    name = input("Enter flavor name: ")
    season = input("Enter season (Spring/Summer/Fall/Winter): ")
    description = input("Enter flavor description: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (name, season, description) VALUES (?, ?, ?)",
                   (name, season, description))
    conn.commit()
    print("Flavor added successfully!")

def view_flavors(conn):
    """
    View all seasonal flavors in the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    
    if not flavors:
        print("No flavors found.")
    else:
        for flavor in flavors:
            print(f"ID: {flavor[0]}, Name: {flavor[1]}, Season: {flavor[2]}, Description: {flavor[3]}")

def update_flavor(conn):
    """
    Update an existing seasonal flavor in the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    flavor_id = input("Enter the ID of the flavor to update: ")
    name = input("Enter new name (press enter to skip): ")
    season = input("Enter new season (press enter to skip): ")
    description = input("Enter new description (press enter to skip): ")
    
    cursor = conn.cursor()
    update_query = "UPDATE seasonal_flavors SET "
    update_params = []
    
    if name:
        update_query += "name = ?, "
        update_params.append(name)
    if season:
        update_query += "season = ?, "
        update_params.append(season)
    if description:
        update_query += "description = ?, "
        update_params.append(description)
    
    update_query = update_query.rstrip(", ") + " WHERE id = ?"
    update_params.append(flavor_id)
    
    cursor.execute(update_query, tuple(update_params))
    conn.commit()
    print("Flavor updated successfully!")

def delete_flavor(conn):
    """
    Delete a seasonal flavor from the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    flavor_id = input("Enter the ID of the flavor to delete: ")
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM seasonal_flavors WHERE id = ?", (flavor_id,))
    conn.commit()
    print("Flavor deleted successfully!")
