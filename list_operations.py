participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements



# First, display all the current participants with their scores. Use zip()



# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.




# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.




# Display every participant's name, score, and whether they are qualified or not. 







# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).


# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.




# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list




# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score





# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified




# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above



if len(participants) != len(scores):
    print("Error: Participants and scores lists have different lengths!")
else:
    print(f"Lists are synchronized. Total participants: {len(participants)}")

print("\n" + "=" * 50)
print("Current Participants and Their Scores:")
print("=" * 50)
for name, score in zip(participants, scores):
    print(f"{name}: {score}")


def add_participant():
    print("\n" + "=" * 50)
    print("Add New Participant")
    print("=" * 50)

    name = input("Enter participant's name: ").strip()

    if name == "":
        print("ERROR: Name cannot be empty!")
        return False

    if name in participants:
        print(f"ERROR: {name} is already registered!")
        return False

    score_input = input("Enter participant's score: ").strip()

    try:
        score = float(score_input)
    except ValueError:
        print("ERROR: Score must be a number!")
        return False

    if score < 0 or score > 100:
        print("ERROR: Score must be between 0 and 100!")
        return False

    participants.append(name)
    scores.append(score)
    print(f"SUCCESS: {name} has been successfully registered with a score of {score}!")
    return True


def search_participant():
    print("\n" + "=" * 50)
    print("Search Participant")
    print("=" * 50)

    name = input("Enter participant's name to search: ").strip()

    if name == "":
        print("ERROR: Name cannot be empty!")
        return

    if name in participants:
        index = participants.index(name)
        score = scores[index]
        print(f"\nParticipant Found!")
        print(f"Name: {name}")
        print(f"Score: {score}")

        if score >= distinction_score:
            print("Status: DISTINCTION")
        elif score >= qualification_score:
            print("Status: QUALIFIED")
        else:
            print("Status: NOT QUALIFIED")
    else:
        print(f"ERROR: {name} not found!")


def display_all_participants():
    print("\n" + "=" * 50)
    print("All Participants - Qualification Status")
    print("=" * 50)
    print(f"{'Name':<20} {'Score':<10} {'Status'}")
    print("-" * 50)

    for name, score in zip(participants, scores):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"{name:<20} {score:<10} {status}")


def check_distinction_and_pass():
    print("\n" + "=" * 50)
    print("Distinction and Pass Check")
    print("=" * 50)

    has_distinction = any(score >= distinction_score for score in scores)
    all_passed = all(score >= 50 for score in scores)

    if has_distinction:
        print("There is at least one participant with a DISTINCTION!")
    else:
        print("No participant has a DISTINCTION.")

    if all_passed:
        print("All participants have PASSED (scored 50 or more)!")
    else:
        failed_count = sum(1 for score in scores if score < 50)
        print(f"Not all participants have passed. {failed_count} participant(s) scored below 50.")


def update_score():
    print("\n" + "=" * 50)
    print("Update Participant Score")
    print("=" * 50)

    name = input("Enter participant's name to update: ").strip()

    if name == "":
        print("ERROR: Name cannot be empty!")
        return

    if name not in participants:
        print(f"ERROR: {name} not found!")
        return

    score_input = input("Enter new score: ").strip()

    try:
        new_score = float(score_input)
    except ValueError:
        print("ERROR: Score must be a number!")
        return

    if new_score < 0 or new_score > 100:
        print("ERROR: Score must be between 0 and 100!")
        return

    index = participants.index(name)
    old_score = scores[index]
    scores[index] = new_score
    print(f"SUCCESS: {name}'s score has been updated from {old_score} to {new_score}!")


def remove_participant():
    print("\n" + "=" * 50)
    print("Remove Participant")
    print("=" * 50)

    name = input("Enter participant's name to remove: ").strip()

    if name == "":
        print("ERROR: Name cannot be empty!")
        return

    if name not in participants:
        print(f"ERROR: {name} not found!")
        return

    index = participants.index(name)
    removed_name = participants.pop(index)
    removed_score = scores.pop(index)
    print(f"SUCCESS: {removed_name} (score: {removed_score}) has been removed!")


def display_scoreboard():
    print("\n" + "=" * 50)
    print("SCOREBOARD - Ranked by Score")
    print("=" * 50)

    scoreboard = sorted(zip(scores, participants), reverse=True)

    print(f"{'Rank':<6} {'Name':<20} {'Score':<10}")
    print("-" * 50)

    for rank, (score, name) in enumerate(scoreboard, 1):
        if rank == 1:
            medal = "1st"
        elif rank == 2:
            medal = "2nd"
        elif rank == 3:
            medal = "3rd"
        else:
            medal = f"{rank}th"
        print(f"{medal:<6} {name:<20} {score:<10}")


def calculate_statistics():
    print("\n" + "=" * 50)
    print("STATISTICS")
    print("=" * 50)

    if len(scores) == 0:
        print("No participants to calculate statistics.")
        return

    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    highest_count = scores.count(highest_score)
    lowest_count = scores.count(lowest_score)

    distinction_count = sum(1 for score in scores if score >= distinction_score)
    qualified_count = sum(1 for score in scores if distinction_score > score >= qualification_score)
    not_qualified_count = sum(1 for score in scores if score < qualification_score)

    print(f"Highest Score: {highest_score} (achieved by {highest_count} participant(s))")
    print(f"Lowest Score: {lowest_score} (achieved by {lowest_count} participant(s))")
    print(f"Average Score: {average_score:.2f}")
    print(f"Distinctions (greater than or equal to {distinction_score}): {distinction_count}")
    print(f"Qualified (greater than or equal to {qualification_score}): {qualified_count}")
    print(f"Not Qualified (less than {qualification_score}): {not_qualified_count}")


def generate_final_report():
    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)

    scoreboard = sorted(zip(scores, participants), reverse=True)

    print("\nPARTICIPANT DETAILS:")
    print(f"{'Rank':<6} {'Name':<20} {'Score':<10} {'Status'}")
    print("-" * 60)

    for rank, (score, name) in enumerate(scoreboard, 1):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"{rank:<6} {name:<20} {score:<10} {status}")

    print("\nSTATISTICS:")
    print("-" * 60)

    if len(scores) > 0:
        highest_score = max(scores)
        lowest_score = min(scores)
        average_score = sum(scores) / len(scores)
        highest_count = scores.count(highest_score)
        lowest_count = scores.count(lowest_score)
        distinction_count = sum(1 for score in scores if score >= distinction_score)
        qualified_count = sum(1 for score in scores if distinction_score > score >= qualification_score)
        not_qualified_count = sum(1 for score in scores if score < qualification_score)

        print(f"  Total Participants: {len(participants)}")
        print(f"  Highest Score: {highest_score} (achieved by {highest_count} participant(s))")
        print(f"  Lowest Score: {lowest_score} (achieved by {lowest_count} participant(s))")
        print(f"  Average Score: {average_score:.2f}")
        print(f"  Distinctions: {distinction_count}")
        print(f"  Qualified: {qualified_count}")
        print(f"  Not Qualified: {not_qualified_count}")
    else:
        print("  No participants to display statistics.")

    print("\n" + "=" * 50)
    print("END OF REPORT")
    print("=" * 50)


def main():
    while True:
        print("\n" + "=" * 50)
        print("PARTICIPANT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Participant")
        print("2. Search Participant")
        print("3. Display All Participants")
        print("4. Check Distinction & Pass")
        print("5. Update Score")
        print("6. Remove Participant")
        print("7. Display Scoreboard")
        print("8. Calculate Statistics")
        print("9. Generate Final Report")
        print("0. Exit")
        print("-" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_participant()
        elif choice == "2":
            search_participant()
        elif choice == "3":
            display_all_participants()
        elif choice == "4":
            check_distinction_and_pass()
        elif choice == "5":
            update_score()
        elif choice == "6":
            remove_participant()
        elif choice == "7":
            display_scoreboard()
        elif choice == "8":
            calculate_statistics()
        elif choice == "9":
            generate_final_report()
        elif choice == "0":
            print("\nThank you for using the Participant Management System. Goodbye!")
            break
        else:
            print("ERROR: Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
