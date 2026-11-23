# campaign_audit.py

import csv

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
campaigns = load_campaigns("campaigns_C(1)")

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

