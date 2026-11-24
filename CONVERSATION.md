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
Number of campaigns: 12
First campaign: Winter Sale

**Step 2 test:**
Number of campaigns: 12
First campaign: Winter Sale
Total campaigns: 12
Valid campaigns: 11
First campaign: Winter Sale
Cost: 50917.23
Conversions: 1066

**Errors encountered:**
## Step 2 — Testing and Debugging

**Problem encountered:**
When I first ran my program, I received a FileNotFoundError because the CSV filename in my Python code did not match the actual file.

**How I fixed it:**
I corrected the filename to campaigns_C.csv and ran the program again.

**Test results:**
- Total campaigns: 12
- Valid campaigns: 11
- First campaign: Winter Sale
- Cost: 50917.23
- Conversions: 1066

**What I learned:**
I learned that Python needs the exact filename to open a CSV file. I also learned how to clean data, convert decimal commas into dots, and skip campaigns with missing impressions.

## Step 3 — Calculating CTR, CPA and ROAS

**My question:**
How can I calculate CTR, CPA and ROAS for each campaign using Python?

**AI answer:**
Create a function called calculate_metrics() that uses the following formulas:
- CTR = Clicks / Impressions
- CPA = Cost / Conversions
- ROAS = Revenue / Cost

Use if statements to avoid division by zero.

**What I did:**
I created the calculate_metrics() function and tested it using the Winter Sale campaign.

**Test results:**
- CTR: 0.03795827900912647
- CPA: 47.764756097560976
- ROAS: 1.5842051894810458

**What I learned:**
I learned how to calculate advertising performance indicators and how to avoid division by zero using if statements.

## Step 4 — Finding the Quiz Answers

**My question:**
How can I automatically calculate the correct answers to the five quiz questions?

**AI answer:**
Create a function called get_correct_answers() using max(), sum(), loops and conditions to calculate the answers from the campaign data.

**What I did:**
I created the function and tested it with my CSV file.

**Test results:**
1. Best CTR: Cart Retargeting
2. Highest CPA: Black Friday
3. ROAS above 3: 5
4. Best channel: LinkedIn Ads
5. Average CTR: 3.12%

**What I learned:**
I learned how to find maximum values, count campaigns that meet a condition, and calculate averages using Python.

**Errors:**
No errors occurred during this test.

## Step 5 — Interactive Quiz

**My question:**
How can I create an interactive quiz that asks five questions, checks the answers and calculates the final score?

**AI answer:**
Create a function called play_quiz(). Use input() to ask the questions, a for loop to repeat the process and if statements to check if the answers are correct.

**What I did:**
I created the play_quiz() function and tested the five questions using the correct answers calculated from my CSV file.

**Test result:**
Player: Tommaso
Final score: 5 / 5

**What I learned:**
I learned how to use input(), for loops and if statements to create an interactive quiz and calculate a score.

## Step 6 — Saving Results

**My question:**
How can I save the player's name, final score and date in a CSV file?

**AI answer:**
Create a function called save_result() using csv.writer() to save the information and date.today() to get the current date. Use append mode to keep previous results.

**What I did:**
I created the save_result() function and connected it to the quiz.

**Test result:**
Player: Tommaso
Final score: 4 / 5
Result saved successfully!

**What I learned:**
I learned how to create a CSV file, save data using Python and automatically add the current date.

**Errors and testing:**
During the second test, I answered one question incorrectly. The program correctly calculated a score of 4/5 instead of 5/5. I also checked that result.csv was created and contained the correct information.

**Final result:**
The program reads the CSV file, cleans the data, calculates CTR, CPA and ROAS, asks five questions, checks the answers and saves the player's score.