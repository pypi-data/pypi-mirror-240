import sqlite3 as sq
from LoggingConfig import logging


class DatabaseManager:
    def __init__(self, db_location):
        self.db_name = db_location
        self.conn = self.connect_db()
        self.table_name = "your_table"  # Replace with your actual table name
        self.logger = logging.getLogger(__name__)

    def connect_db(self):
        try:
            connection = sq.connect(self.db_name)
            self.logger.info("Connected to the database successfully.")
            return connection
        except sq.Error as e:
            self.logger.error(f"Error connecting to the database: {e}")
            return None

    def close_db(self):
        if self.conn is not None:
            self.conn.close()
            self.logger.info("Database connection closed.")

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            self.logger.debug(f"Executed query: {query} with params: {params}")
            return cursor
        except sq.Error as e:
            self.logger.error(f"Error executing query: {e}")
            return None

    def create_table(self, columns_definition):
        column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns_definition.items()])
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({column_definitions})"
        self.execute_query(query)
        self.logger.info(f"Table '{self.table_name}' created successfully.")

    def insert_data(self, data):
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())

        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, list(data.values()))
        self.logger.info("Data inserted into the table successfully.")

    def view_data(self, page_size=50):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
            total_rows = cursor.fetchone()[0]
            total_pages = (total_rows + page_size - 1) // page_size

            for page in range(1, total_pages + 1):
                offset = (page - 1) * page_size
                cursor.execute(f"SELECT * FROM {self.table_name} LIMIT ? OFFSET ?", (page_size, offset))
                data = cursor.fetchall()

                if len(data) == 0:
                    self.logger.info(f"No data found in the '{self.table_name}'.")
                else:
                    table = PrettyTable()
                    table.field_names = list(data[0].keys())

                    for row in data:
                        table.add_row(row.values())

                    print(table)

                    if total_pages > 1:
                        print(f"Page {page} of {total_pages}")
                        input("Press Enter to continue...")

        except sq.Error as e:
            self.logger.error(f"Error viewing data: {e}")

    def remove_data(self, condition):
        query = f"DELETE FROM {self.table_name} WHERE {condition}"
        cursor = self.execute_query(query)
        if cursor.rowcount == 0:
            self.logger.info("No data found for the given condition.")
        else:
            self.logger.info(f"{cursor.rowcount} row(s) deleted from the '{self.table_name}'.")

    def search_data(self, condition):
        query = f"SELECT * FROM {self.table_name} WHERE {condition}"
        cursor = self.execute_query(query)

        column_names = [description[0] for description in cursor.description]

        table = PrettyTable()
        table.field_names = column_names

        for row in cursor:
            table.add_row(row)

        print(table)