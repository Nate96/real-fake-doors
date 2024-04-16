**Gool:** Improve Reviewing Test Cases experience.

# User Requirements
1. As a user I want to write and run sqlite queries so that I can utilize it's advance filtering features
2. As a user I want to import data into the sqlite database from a csv file so that I can add the data to the sqlite database
3. As a user I want to use a text editor to view filtered data so that I can utilize the `ctl-f` to find text.

# Non-Functional Requirements
1. No licenses needed to use tool
2. All Data mush be store on the local machine (no hosting).

# Functional Requirements
U1F2 - The system shall run and stored sqlite scripts when given the scripts' name
U2F3 - The system shall add to new entries to the database when given a csv file
U2F4 - The system shall removed duplicate entries when adding new data to the database
U3F4 - The system shall export query results to a txt file with the following format
	COLOM-NAME:
	column content
	COLOM-NAME:
	column content
	COLOM-NAME:
	column content
	 ---
U3F5 - The system shall export query results to a md file with the following format
	# row-number 	
	## COLOM-NAME:
	column content
	## COLOM-NAME:
	column content
	## COLOM-NAME:
	column content
	 ---
