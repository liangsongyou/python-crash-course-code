class AnonymousSurvey():
    """Collect anonymous answers to the survey questions."""

    def __init__(self, question):
        """Store a question and prepare to store answers."""

        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey questions."""
        print(self.question)

    def store_response(self, response):
        """Store a single response to the survey."""
        self.responses.append(response)

    def show_result(self):
        """Show the overall survey result."""
        print("Survey Result: ")
        for response in self.responses:
            print('- {}'.format(response))