import sqlite3
import os


class RealFakeDoors:
    def __init__(self):
        """
        creates all directories and files needed for the application
        """
        files = [
                ['database', 'index.db'],
                ['scirpts', 'index.sql'],
                ['results', 'index.txt']
        ]

        for file in files:
            try:
                os.mkdir(file[0])
                open(file[0] + '/' + file[1], "w").close()
            except FileExistsError:
                print(f"Dectory '{file[0]}' already exisits.")

    def run_sql_script(self, script='index', database='index'):
        """run sql script
        Runs the given sql script in Scripts/ directory.

        Parameters:
            script (str): name of sql file
            databse (str): name of the .db file in the Database/ directory
        """
        connection = self._connect_to_database(database)

        # Read SQL script from a file
        with open(f'Scripts/{script}.sql', 'r') as file:
            sql_script = file.read()

        # Execute the SQL script
        results = connection.cursor.execute(sql_script).fetchall()

        self._write_sql_script_reults(results)
        self._close_connection(connection)

    def _connect_to_database(self, database):
        """Connect to the given database

        Parameters:
            database (str): name of .db file
        """
        conn = sqlite3.connect(f'Database/{database}.db')
        cursor = conn.cursor()

        return (conn, cursor)

    def _close_connection(self, connection):
        """close the given connection to the database"""
        connection.conn.commit()
        connection.cursor.close()
        connection.conn.close()

    def _write_sql_script_reults(self, results='index'):
        """Write Sql results
        Writes the results of the given sql script to a .txt file

        Parameters:
            results (str): name of the result files
        """
        with open(f'Results/{results}.txt', 'w') as output_file:
            for row in results:
                output_file.write(str(row) + '\n')
