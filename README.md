# Python Web Development Techdegree
### Project 2 - Basketball Team Stats Tool
Author - Hans Steffens

## Project Overview
The Basketball Team Stats Tool is a console-based application designed to help organize and display information about a basketball league. The tool takes a list of players, organizes them into balanced teams, and provides statistics on team composition, including the number of experienced players, average height, and guardian contact information. This application is built as part of the Python Web Development Techdegree program, using fundamental programming concepts such as lists, dictionaries, and control flow structures.

## Features
**Data Cleaning:** Converts player data for easy processing, including standardizing heights and transforming experience status to boolean values.
**Team Balancing:** Distributes players evenly across teams, ensuring each team has a balanced number of experienced and inexperienced players.
**Interactive Console Menu:** Allows users to display team statistics or quit the program.
**Detailed Team Stats:** For each team, the tool displays:
- Total players
- Total experienced and inexperienced players
- Average height of players
- List of player names
- List of guardian names for each player

## Requirements
This project requires `Python 3` to run. No additional packages are needed, as it is built using Python’s standard library.

## 🛠 Installation & Set Up

1. Clone the Repository:
   ```sh
   git clone https://github.com/hanscode/basketball-team-stats_v1.git
   cd basketball-team-stats_v1
   ```
2. Run the Application
   ```sh
   python3 app.py
   ```
## Usage
1. **Launch the Program:** Run `app.py` from your terminal.
2. **Main Menu:**
- Choose `1` to display team stats.
- Choose `2` to quit the program.
3. **Selecting a Team:**
- After selecting 1, you’ll see a list of available teams. Enter the corresponding number to view statistics for that team.
4. **Viewing Team Stats:**
- The program displays detailed information about the team, including player and guardian lists, experience levels, and average height.
5. **Continue or Exit:** After viewing stats, you can continue to explore other teams or return to the main menu.

## Acknowledgments
This project is part of the Python Web Development Techdegree program by Treehouse. Special thanks to the instructors and community for their guidance and support throughout the course.