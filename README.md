# 🎂 Birthday Reminder App

A simple, personal birthday reminder web application that sends you email notifications every day at 7 AM (America/New_York timezone) when it's someone's birthday.

## Features

- ✨ Simple web interface to add/delete birthdays
- 📧 Automatic daily email reminders at 7 AM EST
- 🎨 Beautiful, responsive design
- 💾 SQLite database (no complex setup needed)
- 🔒 Secure - uses environment variables for sensitive data
- 🚀 Easy to deploy to free cloud services

## Technology Stack

- **Backend**: Python + Flask
- **Database**: SQLite
- **Scheduler**: APScheduler
- **Email**: Gmail SMTP

---

## 📋 Prerequisites

Before you start, you'll need:

1. **Python 3.11+** installed on your computer
2. **A Gmail account** with an App Password (instructions below)
3. **Git** (for deploying to cloud services)
4. **A GitHub account** (for version control and deployment)

---

## 🔐 Step 1: Create a Gmail App Password

To send emails, you need a Gmail App Password (NOT your regular Gmail password):

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** in the left sidebar
3. Enable **2-Step Verification** if you haven't already (required for App Passwords)
4. After enabling 2-Step Verification, search for "App passwords" or go to: https://myaccount.google.com/apppasswords
5. Click **Select app** → Choose "Mail"
6. Click **Select device** → Choose "Other" and type "Birthday Reminder"
7. Click **Generate**
8. **Copy the 16-character password** (you'll need this later)

---

## 💻 Option A: Running Locally (On Your Computer)

### Step 1: Clone the Repository

```bash
cd ~/Documents
git clone https://github.com/YOUR_USERNAME/birthday.git
cd birthday
```

### Step 2: Create a Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file with your favorite text editor
# For Mac:
open .env
# For Windows:
# notepad .env
```

Fill in your details in the `.env` file:

```env
GMAIL_ADDRESS=your.email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_app_password
RECIPIENT_EMAIL=your.email@gmail.com
SECRET_KEY=any_random_long_string_here
```

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
Starting Birthday Reminder App...
Scheduler set to check birthdays daily at 7:00 AM America/New_York
Access the website at: http://127.0.0.1:5000
```

### Step 6: Open Your Browser

Go to: **http://127.0.0.1:5000**

🎉 You're ready to add birthdays!

### Step 7: Keep It Running

**Important**: For the app to check birthdays daily at 7 AM, your computer needs to be on and the app needs to be running. If you turn off your computer, the app stops working.

**Recommendation**: Deploy to a cloud service (see Option B below) so it runs 24/7 for free!

---

## ☁️ Option B: Deploy to Render (Free, Always-On Cloud Hosting)

Render is a free cloud service that will keep your app running 24/7. Perfect for this use case!

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial birthday reminder app"
git push origin main
```

### Step 2: Sign Up for Render

1. Go to: https://render.com/
2. Click **"Sign Up"** and use your GitHub account

### Step 3: Create a New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub account if prompted
3. Select your **`birthday`** repository
4. Fill in the details:
   - **Name**: `birthday-reminder` (or any name you like)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Select **"Free"**

### Step 4: Add Environment Variables

In the "Environment" section, add these variables:

| Key | Value |
|-----|-------|
| `GMAIL_ADDRESS` | your.email@gmail.com |
| `GMAIL_APP_PASSWORD` | your_16_char_app_password |
| `RECIPIENT_EMAIL` | your.email@gmail.com |
| `SECRET_KEY` | any_random_long_string |

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Wait 2-3 minutes for deployment
3. Once deployed, you'll get a URL like: `https://birthday-reminder.onrender.com`

🎉 Your app is now live and will run 24/7 for free!

**Note**: Render's free tier may "sleep" after 15 minutes of inactivity. The daily 7 AM check will wake it up automatically, so your birthday reminders will always work!

---

## ☁️ Option C: Deploy to Railway (Alternative Free Hosting)

Railway is another excellent free option:

### Step 1: Push to GitHub (if not done already)

```bash
git add .
git commit -m "Initial birthday reminder app"
git push origin main
```

### Step 2: Sign Up for Railway

1. Go to: https://railway.app/
2. Click **"Start a New Project"** and connect GitHub

### Step 3: Deploy from GitHub

1. Select your **`birthday`** repository
2. Railway will auto-detect it's a Python app
3. Click **"Deploy Now"**

### Step 4: Add Environment Variables

1. Go to your project → **"Variables"** tab
2. Add these variables:
   - `GMAIL_ADDRESS`
   - `GMAIL_APP_PASSWORD`
   - `RECIPIENT_EMAIL`
   - `SECRET_KEY`

### Step 5: Generate a Domain

1. Go to **"Settings"** → **"Networking"**
2. Click **"Generate Domain"**
3. You'll get a URL like: `https://birthday-xxx.railway.app`

🎉 Done! Your app is live!

---

## 🎯 How to Use the App

### Adding a Birthday

1. Open your app URL in a browser
2. Fill in the form:
   - **Name**: Person's name
   - **Birthday**: Select the date
3. Click **"Add Birthday"**

### Testing Email Notifications

1. Click the **"Test Email Now"** button at the bottom of the form
2. Check your email inbox
3. If someone has a birthday today, you'll receive an email immediately

### Daily Automatic Reminders

- The app automatically checks every day at **7:00 AM America/New_York time**
- If anyone has a birthday, you'll receive a beautiful HTML email
- No action needed from you!

---

## 📁 Project Structure

```
birthday/
├── app.py                 # Main Flask application
├── config.py              # Configuration (reads environment variables)
├── database.py            # SQLite database functions
├── email_sender.py        # Email notification system
├── templates/
│   └── index.html         # Web interface
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore file
├── Procfile              # For Render/Heroku deployment
├── runtime.txt           # Python version for deployment
└── README.md             # This file!
```

---

## 🔧 Troubleshooting

### Emails Not Sending?

1. **Check your Gmail App Password**: Make sure you copied all 16 characters correctly
2. **2-Step Verification**: Ensure it's enabled on your Google account
3. **Environment Variables**: Verify they're set correctly in `.env` (local) or in your hosting service dashboard (cloud)
4. **Check Spam Folder**: Sometimes birthday emails end up in spam

### App Not Starting?

1. **Python Version**: Make sure you have Python 3.11+ installed
2. **Dependencies**: Run `pip install -r requirements.txt` again
3. **Environment Variables**: Ensure your `.env` file exists and has all required variables

### Database Errors?

1. Delete `birthdays.db` file and restart the app (it will recreate the database)
2. Make sure you have write permissions in the app directory

---

## 🔒 Security Notes

- **NEVER commit your `.env` file** to GitHub (it's in `.gitignore`)
- **NEVER share your Gmail App Password** with anyone
- Use GitHub Secrets or environment variables in your hosting service for sensitive data
- The `.env` file is only for local development

---

## 🎨 Customization

### Change Reminder Time

Edit [config.py:11](config.py#L11):

```python
REMINDER_HOUR = 7  # Change to any hour (0-23)
```

### Change Timezone

Edit [config.py:10](config.py#L10):

```python
TIMEZONE = 'America/New_York'  # Change to your timezone
```

Common timezones:
- `America/Los_Angeles` (Pacific)
- `America/Chicago` (Central)
- `America/New_York` (Eastern)
- `Europe/London` (UK)
- `Asia/Tokyo` (Japan)

Full list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

---

## 📝 License

This project is open source and free to use for personal purposes.

---

## 🤝 Support

If you encounter any issues:

1. Check the **Troubleshooting** section above
2. Make sure all environment variables are set correctly
3. Verify your Gmail App Password is correct

---

## 🎉 Enjoy!

Never forget a birthday again! 🎂

---

**Made with ❤️ for personal use**
