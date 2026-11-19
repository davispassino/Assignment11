#load the video game catalog:

import pandas as pd

games = pd.read_csv("video_games_raw (3).csv")

print("\nVIDEO GAME CATALOG MANAGER\n")

#validate the row number:

row_options = range(1,len(games)+1)

while True:
    try:
        row_number = int(input("Enter a row number to inspect: "))

        if row_number in row_options:
            break
        else:
            print("Please enter a valid row number.")

    except ValueError:
        print("Please enter a valid row number.")

selected_game = games.iloc[row_number-1]

#displat the game information:

print("Selected Game:\n")

print(f"Title: {selected_game['Title']}")
print(f"Platform: {selected_game['Platform']}")
print(f"Genre: {selected_game['Genre']}")
print(f"Rating: {selected_game['Rating']}")
print(f"Current Status: {selected_game['Status']}")

#Ask for new status/validate:

print("\nPlease enter a new status")
print("Status Options: Completed, Playing, Backlog, Dropped")

new_status = (input("Enter a new status here: ")).capitalize()

status_options = ["Completed", "Playing", "Backlog", "Dropped"]

while new_status not in status_options:
    new_status = input("Sorry, Enter a valid status: ").capitalize()

#Update status:

games.at[games.index[row_number - 1], "Status"] = new_status

#Create new column to identify recommended games:

games["Recommended"] = "No"

#Find?filter recommended games

games.loc[(games["Rating"] >= 8) & (games["Price"] <= 40), "Recommended"] = "Yes"

recommended_games = games.query("Recommended == 'Yes'")

print("\nRecommended Games:\n")
print(recommended_games[["Title", "Platform", "Price", "Rating"]])

#Save the updated catalog:

games.to_csv("video_games_cleaned.csv", index=False)

print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.\n")