"""
Ingredient Inventory Management Module

This module provides functionality to manage the ingredient inventory
in the Chocolate House Management System.
"""

import sqlite3

def manage_ingredient_inventory(conn):
    """
    Main function to manage ingredient inventory.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    while True:
        print("\nManage Ingredient Inventory")
        print("1. Add new ingredient")
        print("2. View all ingredients")
        print("3. Update ingredient quantity")
        print("4. Delete ingredient")
        print("5. Return to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_ingredient(conn)
        elif choice == '2':
            view_ingredients(conn)
        elif choice == '3':
            update_ingredient_quantity(conn)
        elif choice == '4':
            delete_ingredient(conn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_ingredient(conn):
    """
    Add a new ingredient to the inventory.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    name = input("Enter ingredient name: ")
    quantity = float(input("Enter quantity: "))
    unit = input("Enter unit of measurement: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ingredient_inventory (name, quantity, unit) VALUES (?, ?, ?)",
                   (name, quantity, unit))
    conn.commit()
    print("Ingredient added successfully!")

def view_ingredients(conn):
    """
    View all ingredients in the inventory.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredient_inventory")
    ingredients = cursor.fetchall()
    
    if not ingredients:
        print("No ingredients found.")
    else:
        for ingredient in ingredients:
            print(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]} {ingredient[3]}")

def update_ingredient_quantity(conn):
    """
    Update the quantity of an existing ingredient.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    ingredient_id = input("Enter the ID of the ingredient to update: ")
    new_quantity = float(input("Enter new quantity: "))
    
    cursor = conn.cursor()
    cursor.execute("UPDATE ingredient_inventory SET quantity = ? WHERE id = ?", (new_quantity, ingredient_id))
    conn.commit()
    print("Ingredient quantity updated successfully!")

def delete_ingredient(conn):
    """
    Delete an ingredient from the inventory.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    ingredient_id = input("Enter the ID of the ingredient to delete: ")
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ingredient_inventory WHERE id = ?", (ingredient_id,))
    conn.commit()
    print("Ingredient deleted successfully!")
