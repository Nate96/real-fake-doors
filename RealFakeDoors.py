import sqlite3


class RealFakeDoors:
    def run_sql_script(self, script, database):
        connection = self._connect_to_database(database)

        # Read SQL script from a file
        with open(f'sqlite-test/{script}.sql', 'r') as file:
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
        connection.conn.commit()
        connection.cursor.close()
        connection.conn.close()

    def _write_sql_script_reults(self, results):
        with open('sqlite-test/results.txt', 'w') as output_file:
            for row in results:
                output_file.write(str(row) + '\n')
