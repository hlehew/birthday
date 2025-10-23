"""
Birthday Reminder Web Application
A simple Flask app to manage birthdays and send daily email reminders
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from email_sender import send_birthday_reminders
from database import init_db, add_birthday, get_all_birthdays, delete_birthday
import config

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize database on startup
init_db()

# Set up the scheduler for daily birthday checks
scheduler = BackgroundScheduler()
scheduler.add_job(
    func=send_birthday_reminders,
    trigger='cron',
    hour=7,  # 7 AM
    minute=0,
    timezone='America/New_York'
)
scheduler.start()


@app.route('/')
def index():
    """Display the main page with all birthdays"""
    birthdays = get_all_birthdays()
    # Sort birthdays by month and day
    birthdays.sort(key=lambda x: (datetime.strptime(x['birthday'], '%Y-%m-%d').month,
                                   datetime.strptime(x['birthday'], '%Y-%m-%d').day))
    return render_template('index.html', birthdays=birthdays)


@app.route('/add', methods=['POST'])
def add():
    """Add a new birthday to the database"""
    name = request.form.get('name')
    birthday = request.form.get('birthday')

    if not name or not birthday:
        flash('Please provide both name and birthday!', 'error')
        return redirect(url_for('index'))

    try:
        add_birthday(name, birthday)
        flash(f'Birthday added for {name}!', 'success')
    except Exception as e:
        flash(f'Error adding birthday: {str(e)}', 'error')

    return redirect(url_for('index'))


@app.route('/delete/<int:birthday_id>', methods=['POST'])
def delete(birthday_id):
    """Delete a birthday from the database"""
    try:
        delete_birthday(birthday_id)
        flash('Birthday deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting birthday: {str(e)}', 'error')

    return redirect(url_for('index'))


@app.route('/test-email')
def test_email():
    """Test endpoint to manually trigger birthday check (for testing)"""
    try:
        send_birthday_reminders()
        flash('Test email check completed! Check your email if anyone has a birthday today.', 'success')
    except Exception as e:
        flash(f'Error sending test email: {str(e)}', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    print(f"Starting Birthday Reminder App...")
    print(f"Scheduler set to check birthdays daily at 7:00 AM America/New_York")
    print(f"Access the website at: http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), use_reloader=False)
