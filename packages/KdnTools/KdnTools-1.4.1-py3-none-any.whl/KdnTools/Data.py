class Data:
    def __init__(self, db_location, tools_instance):
        self.tools_instance = tools_instance
        self.db_manager = tools_instance.DBManage(db_location, tools_instance.User())

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
