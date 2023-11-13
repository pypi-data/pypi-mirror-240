class Files:
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def write(file_name, data):
        with open(file_name, "w") as f:
            f.write(data)

    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return f"File not found: {file_path}"

    @staticmethod
    def append(self, file_name, data):
        with open(file_name, "a") as f:
            f.write(data)
