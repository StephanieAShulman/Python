### PyPoll Homework Challenge ###

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create a list of candidate options and a dictionary of resulting votes.
candidate_options = []
candidate_votes = {}

# CHALLENGE (#1-8): From each county – voter turnout, % county vote/total, highest county turnout
# Challenge 1: Create a county list and county votes dictionary.
county_list= []
county_votes ={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge 2: Track the largest county and county voter turnout.
largest_county = ""
cntytrnout_votes = 0
cntytrnout_percentage = 0

# Open the election results and read the file with the reader fxn
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header row
    header = next(reader) #file_reader???

    # Print each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Challange 3: Extract the county name from each row.
        county = row[1]

        # If candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Challenge 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in county_list:
            # 4b: Add the existing county to the list of counties.
           county_list.append(county)
            # 4c: Begin tracking the county's vote count.
           county_votes[county] = 0

        # Challenege 5: Add a vote to that county's vote count (has to be outside if).
        county_votes[county] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results)

    txt_file.write(election_results)

    # Challenege 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > cntytrnout_votes) and (vote_percentage > cntytrnout_percentage):
            cntytrnout_votes = votes
            largest_county = county
            cntytrnout_percentage = vote_percentage

    # Challenege 7: Print the county with the largest turnout to the terminal.
    largest_turnout_summary = (
        f"-----------------------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-----------------------------------------------\n"
        f"Candidate Results:\n")
    print(largest_turnout_summary)

    # Challenege 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)