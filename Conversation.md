# AI Conversation — Campaign Audit

## Step 1 — Reading the CSV File

**My question:**
How can I read my campaigns_C.csv file using Python?

**AI answer:**
Use the csv module and csv.DictReader to read the file and store the campaigns in a list.

**What I did:**
I created a function called load_campaigns() to read my CSV file.

**What I learned:**
I learned how to open a CSV file and use a function to read data.

## Step 2 — Cleaning the Data

**My question:**
How can I clean my CSV file and handle missing values and decimal commas?

**AI answer:**
Use continue to skip campaigns with missing impressions. Use replace(",", ".") to convert European decimal commas into dots. Use try and except to handle invalid numbers.

**What I did:**
I created a function called clean_campaigns() to clean the data.

**What I learned:**
I learned how to convert strings into numbers using int() and float(). I also learned how to handle errors using try and except.

## Tests and Errors

**Step 1 test:**
[Write the actual result of your test.]

**Step 2 test:**
[Write the actual result of your test.]

**Errors encountered:**
[Write any errors you encountered and how you fixed them. If there were no errors, write "No errors encountered."]
