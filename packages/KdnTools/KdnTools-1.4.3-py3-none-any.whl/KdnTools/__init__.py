from prettytable import PrettyTable
from colorama import init, Fore
import sqlite3 as sq
import logging
import random
import os

class Tools:
    class User:
        def __init__(self):
            init()
            self.clear = "\033c"
            self.red = Fore.RED
            self.blue = Fore.BLUE
            self.green = Fore.GREEN
            self.reset = Fore.RESET

        def Ctext(self, colour, text):
            print(f"{colour}{text}{self.reset}\n")

        def Choice(self, text, options):
            check = [i for i in range(1, len(options) + 1)]

            while True:
                self.Ctext(self.blue, f"{text}")
                for i, option in enumerate(options):
                    print(f"({i + 1}) {option}")
                choice = input("\nInput: ")
                if choice.isnumeric():
                    if int(choice) in check:
                        return int(choice)
                    else:
                        self.Ctext(self.red, f"{self.clear}Input must be one of the options (e.g. 1).")
                        continue
                else:
                    self.Ctext(self.red, f"{self.clear}Input must be an integer.")
                    continue

    class DatabaseManager:
        def __init__(self, db_location):
            self.db_name = db_location
            self.conn = self.connect_db()

        def connect_db(self):
            try:
                conn = sq.connect(self.db_name)
                logging.info("Database opened successfully")
                return conn
            except sq.Error as e:
                logging.error(f"Error connecting to the database: {e}")
                return None

        def close_db(self):
            if self.conn is not None:
                self.conn.close()
                logging.info("Database closed")

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
                    logging.error(f"Error executing query: {e}")
                    return None

        def create_table(self, table_name, columns):
            column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
            self.execute_query(query)
            logging.info(f"Table '{table_name}' created")

        def insert_data(self, table_name, data):
            placeholders = ', '.join(['?'] * len(data))
            columns = ', '.join(data.keys())
            values = list(data.values())

            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.execute_query(query, values)
            logging.info("Data inserted into the table")

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
                logging.error(f"Error viewing data: {e}")

        def remove_data(self, table_name, condition):
            query = f"DELETE FROM {table_name} WHERE {condition}"
            cursor = self.execute_query(query)
            if cursor.rowcount == 0:
                print("No data found for the given condition.")
            else:
                logging.info(f"{cursor.rowcount} row(s) deleted from the {table_name}.")

        def search_data(self, table_name, condition):
            query = f"SELECT * FROM {table_name} WHERE {condition}"
            cursor = self.execute_query(query)

            column_names = [description[0] for description in cursor.description]

            table = PrettyTable()
            table.field_names = column_names

            for row in cursor:
                table.add_row(row)

            print(table)

    class DriveLetter:
        def __init__(self):
            self.script_directory = os.path.dirname(os.path.abspath(__file__))
            self.drive_letter = self.get_drive_letter()

        def get_drive_letter(self):
            return self.script_directory[0] if self.script_directory else None

        def __str__(self):
            return str(self.drive_letter)

    class WordCount:
        def __init__(self, input_string):
            self.input_string = input_string

        @classmethod
        def count_words(cls, input_string):
            word_count = len(input_string.split())
            return word_count

        def __str__(self):
            return str(self.count_words(self.input_string))

    class Data:
        def __init__(self, db_location, tools_instance):
            self.tools_instance = tools_instance
            self.db_manager = tools_instance.DatabaseManager(db_location, tools_instance.User())

        def search_and_format(self, text, search_keywords):
            try:
                words = text.split()
                matching_words_with_context = []

                for keyword in search_keywords:
                    keyword = keyword.strip()
                    context = self.extract_context(words, keyword)
                    if context:
                        matching_words_with_context.append((keyword, context))

                results = []

                if not matching_words_with_context:
                    return "No matches found."

                for keyword, context in matching_words_with_context:
                    result = f"Keyword: {keyword}\nContext:\n\n{' '.join(context)}"
                    results.append(result)

                return "\n\n".join(results)
            except Exception as e:
                return f"An error occurred: {str(e)}"

        @staticmethod
        def extract_context(words, keyword, window_size=5):
            matching_indices = [i for i, word in enumerate(words) if keyword in word]
            context_words = []
            for index in matching_indices:
                start_index = max(0, index - window_size)
                end_index = min(len(words), index + window_size + 1)
                context_words.extend(words[start_index:end_index])
            return context_words

        def search_and_display_results(self):
            text_input = input("Enter text: ")
            search_queries = input("Enter search keywords (space-separated): ").split()

            formatted_results = self.search_and_format(text_input, search_queries)
            print(formatted_results)

    class RandNumber:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        @classmethod
        def rand_number(cls, num1, num2):
            try:
                return random.randint(num1, num2)
            except ValueError as e:
                logging.error(f"Error generating random number: {e}")
                return None

        def __str__(self):
            rand_num = self.rand_number(self.num1, self.num2)
            return str(rand_num) if rand_num is not None else "Error"

    def __init__(self, db_location):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
