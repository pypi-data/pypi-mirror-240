import sqlite3 as sq
from LoggingConfig import logging


class DBManage:
    def __init__(self, db_location, user_instance):
        self.db_manager_logger = logging.getLogger(__name__ + ".DBManager")
        self.db_name = db_location
        self.conn = self.connect_db()
        self.user_instance = user_instance
        self.table_name = "your_table"  # Replace with your actual table name

    def connect_db(self):
        try:
            connection = sq.connect(self.db_name)
            self.db_manager_logger.info("Connected to the database successfully.")
            return connection
        except sq.Error as e:
            self.db_manager_logger.error(f"Error connecting to the database: {e}")
            return None

    # ... (rest of the methods in DBManage class)
