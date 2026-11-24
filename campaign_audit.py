# campaign_audit.py

import csv
import os
from datetime import date

# This function reads the CSV file and stores the campaigns.
def load_campaigns(filename):
    campaigns = []

    # Open the file and read each campaign.
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            campaigns.append(row)

    return campaigns


# Test to see the file can be read correctly.
campaigns = load_campaigns("campaigns_C.csv")

print("Number of campaigns:", len(campaigns))
print("First campaign:", campaigns[0]["Campaign"])


# This function cleans the campaign data.
def clean_campaigns(campaigns):
    clean_data = []

    # Check each campaign one by one.
    for campaign in campaigns:

        # Skip campaigns with missing impressions.
        if campaign["Impressions"] == "":
            continue

        try:
            # Convert text values into numbers.
            campaign["Impressions"] = int(campaign["Impressions"])
            campaign["Clicks"] = int(campaign["Clicks"])
            campaign["Conversions"] = int(campaign["Conversions"])

            # Replace European decimal commas with dots.
            campaign["Cost (€)"] = float(
                campaign["Cost (€)"].replace(",", ".")
            )
            campaign["Revenue (€)"] = float(
                campaign["Revenue (€)"].replace(",", ".")
            )

            # Keep the cleaned campaign.
            clean_data.append(campaign)

        except (ValueError, TypeError):
            # Skip rows containing invalid numbers.
            print("Invalid data:", campaign["Campaign"])

    return clean_data

# This function calculates the performance indicators.
def calculate_metrics(campaigns):

    # Calculate the metrics for each campaign.
    for campaign in campaigns:

        impressions = campaign["Impressions"]
        clicks = campaign["Clicks"]
        conversions = campaign["Conversions"]
        cost = campaign["Cost (€)"]
        revenue = campaign["Revenue (€)"]

        # Calculate CTR and avoid division by zero.
        if impressions > 0:
            campaign["CTR"] = clicks / impressions
        else:
            campaign["CTR"] = None

        # Calculate CPA only when conversions are not zero.
        if conversions > 0:
            campaign["CPA"] = cost / conversions
        else:
            campaign["CPA"] = None

        # Calculate ROAS and avoid division by zero.
        if cost > 0:
            campaign["ROAS"] = revenue / cost
        else:
            campaign["ROAS"] = None

    return campaigns


# This function finds the correct answers for the quiz.
def get_correct_answers(campaigns):

    # Find the campaign with the highest CTR.
    valid_ctr = [c for c in campaigns if c["CTR"] is not None]
    best_ctr = max(valid_ctr, key=lambda c: c["CTR"])["Campaign"]

    # Find the campaign with the highest CPA.
    valid_cpa = [c for c in campaigns if c["CPA"] is not None]
    highest_cpa = max(valid_cpa, key=lambda c: c["CPA"])["Campaign"]

    # Count campaigns with ROAS above 3.
    roas_above_3 = sum(
        1 for c in campaigns
        if c["ROAS"] is not None and c["ROAS"] > 3
    )

    # Calculate total conversions for each channel.
    channel_totals = {}

    for campaign in campaigns:
        channel = campaign["Channel"]
        conversions = campaign["Conversions"]

        if channel not in channel_totals:
            channel_totals[channel] = 0

        channel_totals[channel] += conversions

    # Find the channel with the most conversions.
    best_channel = max(channel_totals, key=channel_totals.get)

    # Calculate the average CTR as a percentage.
    average_ctr = round(
        sum(c["CTR"] for c in valid_ctr) / len(valid_ctr) * 100, 2
    )

    return [
        best_ctr,
        highest_cpa,
        roas_above_3,
        best_channel,
        average_ctr
    ]



# This function asks the questions and calculates the score.
def play_quiz(answers):
    score = 0

    # Store the five quiz questions.
    questions = [
        "Which campaign has the best CTR?",
        "Which campaign has the highest CPA?",
        "How many campaigns have a ROAS above 3?",
        "Which channel generated the most conversions?",
        "What is the average CTR (%) rounded to 2 decimals?"
    ]

    # Ask each question and check the answer.
    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        user_answer = input(questions[i] + " ")

        # Compare answers without case sensitivity.
        if i == 4:
            try:
                correct = float(user_answer.replace(",", ".")) == answers[i]
            except ValueError:
                correct = False
        else:
            correct = user_answer.strip().lower() == str(answers[i]).lower()

        if correct:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! Correct answer:", answers[i])

    return score

# This function saves the player's score in a CSV file.
def save_result(player_name, score):

    filename = "result.csv"

    # Check if the result file already exists.
    file_exists = os.path.exists(filename)

    try:
        # Open the file and add a new result.
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the column names if the file is new.
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writerow(["Player", "Score", "Date"])

            # Save the player name, score and today's date.
            writer.writerow([
                player_name,
                score,
                date.today().isoformat()
            ])

        print("Result saved successfully!")

    except OSError as error:
        # Show an error if the file cannot be saved.
        print("Error saving result:", error)



# Load the CSV file.
campaigns = load_campaigns("campaigns_C.csv")

# Clean the campaign data.
clean_data = clean_campaigns(campaigns)

# Check the results.
print("Total campaigns:", len(campaigns))
print("Valid campaigns:", len(clean_data))
print("First campaign:", clean_data[0]["Campaign"])
print("Cost:", clean_data[0]["Cost (€)"])
print("Conversions:", clean_data[0]["Conversions"])


# Calculate the performance indicators.
results = calculate_metrics(clean_data)

# Check the metrics of the first campaign.
print("Campaign:", results[0]["Campaign"])
print("CTR:", results[0]["CTR"])
print("CPA:", results[0]["CPA"])
print("ROAS:", results[0]["ROAS"])



# Find the correct answers.
answers = get_correct_answers(results)

# Display the answers to check the calculations.
print("\nQUIZ ANSWERS")
print("1. Best CTR:", answers[0])
print("2. Highest CPA:", answers[1])
print("3. ROAS above 3:", answers[2])
print("4. Best channel:", answers[3])
print("5. Average CTR (%):", answers[4])



# Start the quiz.
print("\nWELCOME TO THE CAMPAIGN AUDIT QUIZ")

player_name = input("Enter your name: ")

# Ask the questions and calculate the score.
final_score = play_quiz(answers)

# Display the final score.
print("\nPlayer:", player_name)
print("Final score:", final_score, "/ 5")


# Save the final result in result.csv.
save_result(player_name, final_score)
