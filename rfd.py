import click
import RealFakeDoors


@click.command()
@click.option('--run', '-r',
              type=str,
              required=False,
              default='test',
              help='run given script')
@click.option('--database', '-d',
              type=str,
              required=False,
              default='users',
              help='connect to geven database')
@click.option('--cvs',
              type=str,
              required=False,
              default='index',
              help='import data from a given csv')
def rfd(run, database, csv):
    RealFakeDoors.run_sql_script(run, database)


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
