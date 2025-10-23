"""
Database helper functions for SQLite
Handles all database operations for birthday storage
"""

import sqlite3
from datetime import datetime
import os

DATABASE_NAME = 'birthdays.db'


def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn


def init_db():
    """Initialize the database with the birthdays table"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS birthdays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")


def add_birthday(name, birthday):
    """Add a new birthday to the database"""
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO birthdays (name, birthday) VALUES (?, ?)',
        (name, birthday)
    )
    conn.commit()
    conn.close()


def get_all_birthdays():
    """Get all birthdays from the database"""
    conn = get_db_connection()
    birthdays = conn.execute('SELECT * FROM birthdays ORDER BY birthday').fetchall()
    conn.close()
    # Convert to list of dictionaries for easier template rendering
    return [dict(row) for row in birthdays]


def delete_birthday(birthday_id):
    """Delete a birthday by ID"""
    conn = get_db_connection()
    conn.execute('DELETE FROM birthdays WHERE id = ?', (birthday_id,))
    conn.commit()
    conn.close()


def get_birthdays_today():
    """Get all birthdays that match today's month and day"""
    today = datetime.now()
    today_month = today.month
    today_day = today.day

    conn = get_db_connection()
    all_birthdays = conn.execute('SELECT * FROM birthdays').fetchall()
    conn.close()

    # Filter birthdays that match today's month and day
    todays_birthdays = []
    for birthday in all_birthdays:
        birthday_date = datetime.strptime(birthday['birthday'], '%Y-%m-%d')
        if birthday_date.month == today_month and birthday_date.day == today_day:
            todays_birthdays.append(dict(birthday))

    return todays_birthdays
