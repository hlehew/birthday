"""
Email notification system using Gmail SMTP
Sends birthday reminder emails
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from database import get_birthdays_today
import config


def send_email(subject, body):
    """Send an email using Gmail SMTP"""

    # Check if email configuration is set
    if not config.GMAIL_ADDRESS or not config.GMAIL_APP_PASSWORD or not config.RECIPIENT_EMAIL:
        print("Email configuration not set. Skipping email send.")
        print("Please set GMAIL_ADDRESS, GMAIL_APP_PASSWORD, and RECIPIENT_EMAIL environment variables.")
        return False

    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = config.GMAIL_ADDRESS
        message['To'] = config.RECIPIENT_EMAIL
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'html'))

        # Create SMTP session
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        server.starttls()  # Enable security
        server.login(config.GMAIL_ADDRESS, config.GMAIL_APP_PASSWORD)

        # Send email
        text = message.as_string()
        server.sendmail(config.GMAIL_ADDRESS, config.RECIPIENT_EMAIL, text)
        server.quit()

        print(f"Email sent successfully to {config.RECIPIENT_EMAIL}")
        return True

    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False


def send_birthday_reminders():
    """Check for today's birthdays and send reminder email"""
    print(f"Checking for birthdays on {datetime.now().strftime('%Y-%m-%d')}...")

    todays_birthdays = get_birthdays_today()

    if not todays_birthdays:
        print("No birthdays today.")
        return

    # Create email content
    subject = f"🎂 Birthday Reminder - {datetime.now().strftime('%B %d, %Y')}"

    body = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 20px;
                }}
                .birthday-item {{
                    background-color: #f9f9f9;
                    border-left: 4px solid #4CAF50;
                    padding: 15px;
                    margin: 10px 0;
                }}
                .footer {{
                    margin-top: 20px;
                    padding-top: 20px;
                    border-top: 1px solid #ddd;
                    font-size: 12px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🎂 Birthday Reminder</h1>
                <p>{datetime.now().strftime('%B %d, %Y')}</p>
            </div>
            <div class="content">
                <h2>Today's Birthdays:</h2>
    """

    for birthday in todays_birthdays:
        birthday_date = datetime.strptime(birthday['birthday'], '%Y-%m-%d')
        age = datetime.now().year - birthday_date.year

        body += f"""
                <div class="birthday-item">
                    <h3>{birthday['name']}</h3>
                    <p><strong>Birthday:</strong> {birthday_date.strftime('%B %d, %Y')}</p>
                    <p><strong>Turning:</strong> {age} years old</p>
                </div>
        """

    body += """
                <div class="footer">
                    <p>This is an automated reminder from your Birthday Reminder App.</p>
                </div>
            </div>
        </body>
    </html>
    """

    # Send the email
    success = send_email(subject, body)

    if success:
        print(f"Birthday reminder sent for {len(todays_birthdays)} person(s).")
    else:
        print("Failed to send birthday reminder email.")
