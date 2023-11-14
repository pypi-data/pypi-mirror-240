from prettytable import PrettyTable
import sqlite3 as sq
from logging import info, error
from .User import User


class DbManage:
    def __init__(self, db_location):
        self.db_name = db_location
        self.conn = self.connect_db()
        self.conn.row_factory = sq.Row
        self.Ctext = User.Ctext
        self.Choice = User.Choice

    def connect_db(self):
        try:
            conn = sq.connect(self.db_name)
            info("Database opened successfully")
            return conn
        except sq.Error as e:
            error(f"Error connecting to the database: {e}")
            return None

    def close_db(self):
        if self.conn is not None:
            self.conn.close()
            info("Database closed")

    def execute_query(self, query, params=None):
        with self.conn:
            cursor = self.conn.cursor()
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()
                return cursor
            except sq.Error as e:
                error(f"Error executing query: {e}")
                return None

    def create_table(self, table_name, columns):
        column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.execute_query(query)
        info(f"Table '{table_name}' created")

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())
        values = list(data.values())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, values)
        info("Data inserted into the table")

    def view_data(self, table_name, page_size=50):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            total_rows = cursor.fetchone()[0]
            total_pages = (total_rows + page_size - 1) // page_size

            for page in range(1, total_pages + 1):
                offset = (page - 1) * page_size
                cursor.execute(f"SELECT * FROM {table_name} LIMIT ? OFFSET ?", (page_size, offset))
                data = cursor.fetchall()

                if len(data) == 0:
                    print(f"No data found in the {table_name}.")
                else:
                    table = PrettyTable()
                    table.field_names = list(data[0].keys())

                    for row in data:
                        table.add_row(row.values())

                    print(table)

                    if total_pages > 1:
                        print(f"Page {page} of {total_pages}")
                        print("Press Escape to exit, or any other key to continue...")

        except sq.Error as e:
            error(f"Error viewing data: {e}")

    def remove_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor = self.execute_query(query)
        if cursor.rowcount == 0:
            print("No data found for the given condition.")
        else:
            info(f"{cursor.rowcount} row(s) deleted from the {table_name}.")

    def search_data(self, table_name, condition):
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        cursor = self.execute_query(query)

        column_names = [description[0] for description in cursor.description]

        table = PrettyTable()
        table.field_names = column_names

        for row in cursor:
            table.add_row(row)

        return table

    def DbUse(self, subject_name: str, table, columns: dict):
        self.create_table(table, columns)
        self.Ctext(User().green, f"Welcome to the {subject_name} database.")

        while True:
            choice = self.Choice("Do you want to:", ["Input Data", "See Data", "Delete data", "Quit"])

            if choice == 1:
                self.insert_data(subject_name, table)

            elif choice == 2:
                self.view_data(subject_name, table)

            elif choice == 3:

                while True:
                    choice = self.Choice("Do you want to:", ["Delete all data", "Delete specific data", "Return"])

                    if choice == 1:
                        self.remove_data(subject_name, "all")
                        break

                    elif choice == 2:
                        self.remove_data(subject_name, "specific")
                        break

                    elif choice == 3:
                        break

            elif choice == 4:
                print("Exiting the program")
                break