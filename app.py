"""
Birthday Reminder Web Application
A simple website that displays today's birthdays
"""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# HARD-CODED BIRTHDAYS LIST
# Format: (Name, Month, Day)
BIRTHDAYS = [
    ("David", 10, 23),   # October 23
    ("Suzie", 10, 24),   # October 24
    ("Kevin", 10, 25),   # October 25
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
    return render_template('index.html', birthdays=todays_birthdays)


if __name__ == '__main__':
    print("Starting Birthday Reminder App...")
    print("Access the website at: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, port=5000)
