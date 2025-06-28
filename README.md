# mood-tracker
# 🧠 Mood Tracker (CLI App)

A simple Python script that helps you log your daily mood with both a written description and a numeric rating. This project is part of my self-taught AI/dev learning journey.

## 📋 What It Does

- Prompts you to describe your mood (e.g., Good, Bad, Meh)
- Asks you to rate your day on a scale of 1–10
- Validates both inputs to avoid invalid entries
- Logs the mood + timestamp in a local text file: `mood_log.txt`

### Example Log Entry:
2025-06-27 22:45:19 - Mood: Good (8/10)
---

## ⚙️ Features

- ✅ Input validation with `while` loops and `try-except`
- ✅ Automatic timestamp logging
- ✅ Persistent mood tracking via local file storage
- ✅ Clean CLI experience with clear error messages

---

## 🧪 How to Run

1. Clone the repo or copy the script into [Replit](https://replit.com) or any Python environment.
2. Run the script:
   ```bash
   python main.py
3. Enter your mood + rating when prompted.
4. Check mood_log.txt for your saved logs.

🧠 Why I Built This
This is my first hands-on project in a self-taught bootcamp I'm creating with the help of ChatGPT (Geppers). The goal is to learn by building — not just consuming tutorials. This script helped me practice:

Input handling

Data validation

Working with files

Writing clean, user-friendly Python
