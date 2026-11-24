

# Campaign Audit Quiz

## Project Description

This project is a Python quiz based on advertising campaign data.

The program reads a CSV file, cleans the data, calculates marketing performance indicators and asks the player five questions.

## Features

The program can:

1. Read campaign data from campaigns_C.csv.
2. Remove campaigns with missing impressions.
3. Convert European decimal commas into dots.
4. Calculate CTR, CPA and ROAS.
5. Ask five questions about campaign performance.
6. Check the answers and calculate a score out of 5.
7. Save the player's name, score and date in result.csv.

## Marketing Indicators

- CTR = Clicks / Impressions
- CPA = Cost / Conversions
- ROAS = Revenue / Cost

The program also handles zero conversions to avoid division errors.

## How to Run the Program

Open the terminal in GitHub Codespaces and type:

`python campaign_audit.py`

Enter your name and answer the five questions.

At the end, the program displays your score and saves the result in result.csv.

## Project Files

- campaign_audit.py — Main Python program
- campaigns_C.csv — Advertising campaign dataset
- result.csv — Player scores and dates
- CONVERSATION.md — AI conversations, tests and errors

## Testing

I tested the program using my campaign dataset.

The program successfully loaded 12 campaigns and kept 11 valid campaigns after cleaning.

I tested the quiz twice and obtained scores of 5/5 and 4/5.

The program correctly calculated the scores and saved the results in result.csv.

