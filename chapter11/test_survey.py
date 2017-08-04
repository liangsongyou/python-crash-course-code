import unittest
from survey import AnonymousSurvey

class SurveyTest(unittest.TestCase):
    """Do some checks on anonymous survey class."""

    def setUp(self):
        """Create instance of a class once for reuse."""
        question = 'Which languages do you know?'
        self.survey = AnonymousSurvey(question)
        self.responses = ['English','Mandarin','Spanish']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.survey.responses)

    def test_store_multiple_responses(self):
        """Test that multiple responses are stored correctly."""
        for response in self.responses:
            self.survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.survey.responses)

unittest.main()