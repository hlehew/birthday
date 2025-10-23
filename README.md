# 🎂 Birthday Reminder Website

A simple, clean website that displays today's birthdays. Just open it in your browser each day to check if anyone has a birthday!

## What It Does

- Shows a **celebratory message** if someone has a birthday today
- Shows **"No birthdays today"** if nobody has a birthday
- Birthdays are **hard-coded** in the source code (no database needed)
- **No email notifications** - just visit the website when you want to check

## Your Birthdays

Currently tracking:
- **David** - October 23
- **Suzie** - October 24
- **Kevin** - October 25

---

## 🚀 How to Set Up and Run (Beginner-Friendly)

### Step 1: Install Python

First, check if you have Python installed:

1. Open **Terminal** (on Mac) or **Command Prompt** (on Windows)
2. Type this and press Enter:
   ```bash
   python3 --version
   ```
3. If you see something like `Python 3.11.x`, you're good! Skip to Step 2.
4. If not, download Python from: https://www.python.org/downloads/
   - Download the latest version (3.11 or newer)
   - Run the installer
   - **Important on Windows**: Check the box that says "Add Python to PATH"

### Step 2: Open Terminal in the Project Folder

1. Open **Terminal** (Mac) or **Command Prompt** (Windows)
2. Navigate to the birthday folder:
   ```bash
   cd "/Users/dkl2865/Documents/Vibe Coding/birthday"
   ```

   Or simply:
   - On **Mac**: Drag the `birthday` folder onto Terminal
   - On **Windows**: Hold Shift, right-click the `birthday` folder, and select "Open PowerShell window here"

### Step 3: Install Flask (First Time Only)

Flask is the web framework we use. Install it with:

```bash
pip3 install -r requirements.txt
```

This might take 30 seconds. You only need to do this once!

### Step 4: Start the Website

Run this command:

```bash
python3 app.py
```

You should see:
```
Starting Birthday Reminder App...
Access the website at: http://127.0.0.1:5000
Press Ctrl+C to stop the server
```

### Step 5: Open in Your Browser

Open your web browser and go to:

```
http://127.0.0.1:5000
```

🎉 **You should see your birthday reminder page!**

### Step 6: Stop the Website

When you're done, go back to Terminal and press:
- **Ctrl+C** (Mac or Windows)

The website will stop running.

---

## 🎨 How It Looks

**If someone has a birthday today:**
- Big cake emoji 🎂
- "Today is [Name]'s Birthday!"
- Celebration emojis 🎉

**If nobody has a birthday:**
- Calendar emoji 📅
- "No Birthdays Today"
- "Enjoy your day! 😊"

---

## ✏️ How to Add or Change Birthdays

Open the file [app.py](app.py) in any text editor and find this section (around line 13):

```python
# HARD-CODED BIRTHDAYS LIST
# Format: (Name, Month, Day)
BIRTHDAYS = [
    ("David", 10, 23),   # October 23
    ("Suzie", 10, 24),   # October 24
    ("Kevin", 10, 25),   # October 25
]
```

### To Add a Birthday:

Add a new line with the format: `("Name", Month, Day),`

Example - adding Maria's birthday on December 15:
```python
BIRTHDAYS = [
    ("David", 10, 23),
    ("Suzie", 10, 24),
    ("Kevin", 10, 25),
    ("Maria", 12, 15),   # December 15
]
```

### To Remove a Birthday:

Just delete that person's line.

### To Change a Birthday:

Edit the numbers. Remember:
- Months are numbers: January=1, February=2, ... December=12
- Days are just the day number (1-31)

**After making changes**, save the file and restart the website (Ctrl+C then `python3 app.py` again).

---

## 📂 Project Structure

```
birthday/
├── app.py                 # Main Python code (birthdays are here!)
├── templates/
│   └── index.html         # Website design and layout
├── requirements.txt       # Lists what Python packages we need
├── .gitignore            # Tells Git what not to track
└── README.md             # This file!
```

---

## 🐙 Using with GitHub

### First Time Setup

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial birthday reminder website"

# Connect to GitHub (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/birthday.git

# Push to GitHub
git push -u origin main
```

### After Making Changes

```bash
git add .
git commit -m "Updated birthdays"
git push
```

---

## 🔧 Troubleshooting

### "python3: command not found"

- Try `python` instead of `python3`
- Make sure Python is installed (see Step 1)

### "pip3: command not found"

- Try `pip` instead of `pip3`
- Or try: `python3 -m pip install -r requirements.txt`

### "Address already in use"

- Another program is using port 5000
- Try stopping other web servers, or change the port in [app.py:50](app.py#L50):
  ```python
  app.run(debug=True, port=5001)  # Changed from 5000 to 5001
  ```

### The website shows the wrong date or birthdays

- Make sure your computer's date and time are set correctly
- The website uses your computer's date to check birthdays

---

## 💡 Tips

1. **Bookmark the URL** in your browser: `http://127.0.0.1:5000`
2. **Create a daily routine**: Open the website each morning
3. **Keep the app running** in Terminal throughout the day, or start/stop it as needed
4. **Test it**: Temporarily change a birthday to today's date to see the celebration screen!

---

## 🎉 That's It!

You now have a simple birthday reminder website running on your computer. No databases, no email setup, no cloud services - just open it whenever you want to check!

**Questions or issues?** Check the Troubleshooting section above.

---

**Made with ❤️ for personal use**
