"""
Birthday Reminder Web Application
A simple website that displays today's birthdays
"""

from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

# HARD-CODED BIRTHDAYS LIST
# Format: (Name, Month, Day)
BIRTHDAYS = [
    ("David", 10, 23),   # October 23
    ("Suzie", 10, 24),   # October 24
    ("Kevin", 10, 25),   # October 25
]

# BIRTHDAY MESSAGE SUGGESTIONS
BIRTHDAY_MESSAGES = [
    "Happy Birthday! I hope your special day is filled with laughter, love, and lots of wonderful memories. You deserve all the best today and always!",
    "Wishing you the happiest of birthdays! I'm so grateful to have you in my life, and I hope the year ahead brings you everything you're dreaming of.",
    "Happy Birthday to someone who makes life brighter just by being in it. May your day be as amazing as you are!",
    "Sending you all my love on your birthday! I hope your day is filled with all your favorite people and things.",
    "Another year older and even more fabulous! Hope you have a fantastic birthday surrounded by friends, family, and lots of cake.",
    "Happy Birthday! Thank you for always being there for me—I'm so lucky to have you as my friend/family. Hope your day is extra special!",
    "Wishing the happiest birthday to someone who means so much to me. May today bring you joy and the year ahead bring you endless blessings.",
    "Cheers to you on your birthday! I hope this year brings you new adventures, great memories, and plenty of reasons to smile.",
    "Happy Birthday! May your day be filled with laughter, love, and everything you enjoy most. Here's to making more amazing memories together!",
    "On your birthday, I just want you to know how much you're appreciated. Wishing you a year ahead that's as wonderful and inspiring as you are!"
]


def get_todays_birthdays():
    """Check if anyone has a birthday today"""
    today = datetime.now()
    today_month = today.month
    today_day = today.day

    todays_birthdays = []
    for name, month, day in BIRTHDAYS:
        if month == today_month and day == today_day:
            todays_birthdays.append({
                'name': name,
                'month': month,
                'day': day,
                'date_string': datetime(2000, month, day).strftime('%B %d')
            })

    return todays_birthdays


@app.route('/')
def index():
    """Display the main page"""
    todays_birthdays = get_todays_birthdays()
    today_date = datetime.now().strftime('%B %d, %Y')

    # Get 3 random birthday message suggestions
    message_suggestions = random.sample(BIRTHDAY_MESSAGES, 3) if todays_birthdays else []

    return render_template('index.html',
                         birthdays=todays_birthdays,
                         today_date=today_date,
                         message_suggestions=message_suggestions)


if __name__ == '__main__':
    print("Starting Birthday Reminder App...")
    print("Access the website at: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, port=5000)
