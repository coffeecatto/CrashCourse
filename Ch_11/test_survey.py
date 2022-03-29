# Chapter 11

# File for testing the survey class from survey.py 
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey."""
    
    def test_store_single_response(self):
        """Tests that a single response got stored correctly."""
        question = "What language did you first learn to speak?"
        test_survey = AnonymousSurvey(question)
        test_survey.store_response('English')
        self.assertIn('English', test_survey.responses)
    
    def test_store_three_responses(self):
        """Tests if storing three responses works correctly."""
        question = "What language did you first learn to speak?"
        test_survey = AnonymousSurvey(question)
        responses = ['English', 'Polish', 'Spanish']
        for response in responses:
            test_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, test_survey.responses)

if __name__ == '__main__':
    unittest.main()