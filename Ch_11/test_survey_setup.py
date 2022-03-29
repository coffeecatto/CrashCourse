# Chapter 11

# File for testing the survey class from survey.py 
# NOTE: setUp() version
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey."""
    
    def setUp(self):
        """Create a survey and a set of responses to be used in tests."""
        question = "What language did you first learn to speak?"
        self.test_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Polish', 'Spanish']
    
    def test_store_single_response(self):
        """Tests that a single response got stored correctly."""
        self.test_survey.store_response(self.responses[0])
        self.assertIn('English', self.test_survey.responses)
    
    def test_store_three_responses(self):
        """Tests if storing three responses works correctly."""
        for response in self.responses:
            self.test_survey.store_response(response)        
        for response in self.responses:
            self.assertIn(response, self.test_survey.responses)

if __name__ == '__main__':
    unittest.main()