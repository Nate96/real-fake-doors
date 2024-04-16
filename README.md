**Gool:** Improve Reviewing Test Cases experience.

# User Requirements
1. As a user I want to write and run SQLite queries so that I can utilize its advanced filtering features
2. As a user I want to import data into the SQLite database from a CSV file so that I can add the data to the SQLite database
3. As a user I want to use a text editor to view filtered data so that I can utilize the `ctl-f` to find text.

# Non-Functional Requirements
1. No licenses needed to use the tool
2. All Data must be stored on the local machine (no hosting).

# Functional Requirements
U1F2 - The system shall run and store SQlite scripts when given the scripts' nam \n
2. U2F3 - The system shall add new entries to the database when given a CSV file
3. U2F4 - The system shall remove duplicate entries when adding new data to the database
U3F4 - The system shall export query results to a txt file with the following format
	COLOM-NAME:
	column content
	COLOM-NAME:
	column content
	COLOM-NAME:
	column content
	 ---
U3F5 - The system shall export query results to an MD file with the following format
	# row-number 	
	## COLOM-NAME:
	column content
	## COLOM-NAME:
	column content
	## COLOM-NAME:
	column content
	 ---
