from datetime import datetime

# Ask the user how their day was
while True:
  verbalMood = input("How was your day? (Choices: Good, Bad, Meh, Perfect) ").strip()
  if verbalMood.replace(" ", "").isalpha():
    verbalMood = verbalMood.capitalize()
    break
  else:
    print("Invalid input. Please enter a word.")
while True:
 try:
   numericMood = int(input("On a scale of 1-10, how was your day? "))
   if 1 <= numericMood <= 10:
     break
   else:
     print("Invalid input. Please enter a number between 1 and 10. ")
 except ValueError:
    print("Invalid input. Please enter a number. ")

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create long entry
entry = f"{timestamp} - Mood: {verbalMood} ({numericMood}/10)\n"

# Save entry to file
with open("mood_log.txt","a") as file:
  file.write(entry)

print(" Your mood has been saved")