import click
import sqlite3


@click.command()
@click.option('--run', '-r',
              type=str,
              required=False,
              default='test',
              help='run given script')
@click.option('--database', '-d',
              type=str,
              required=False,
              default='index',
              help='connect to geven database')
@click.option('--inport', '-i',
              type=str,
              required=False,
              default='index',
              help='import data from a given csv')
def rfd(run, database):
    conn = sqlite3.connect(f'Database/{database}.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Read SQL script from a file
    with open(f'sqlite-test/{run}.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    results = cursor.execute(sql_script).fetchall()

    # Write the results to a text file
    with open('sqlite-test/results.txt', 'w') as output_file:
        for row in results:
            output_file.write(str(row) + '\n')

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    rfd()

"""
import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table in the database to store the CSV data
cursor.execute('''CREATE TABLE IF NOT EXISTS your_table (
                    column1 TEXT,
                    column2 TEXT,
                    column3 INTEGER
                  )''')

# Path to the CSV file
csv_file = 'data.csv'

# Open the CSV file and read its contents
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Insert the row into the database
        cursor.execute('INSERT INTO your_table VALUES (?, ?, ?)', row)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
"""
