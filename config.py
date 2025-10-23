"""
Configuration file - reads from environment variables
This keeps sensitive information secure using GitHub secrets or .env file
"""

import os

# Email Configuration
GMAIL_ADDRESS = os.environ.get('GMAIL_ADDRESS')  # Your Gmail address
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')  # Gmail App Password
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')  # Where to send birthday reminders

# Timezone and Schedule
TIMEZONE = 'America/New_York'
REMINDER_HOUR = 7  # 7 AM

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
