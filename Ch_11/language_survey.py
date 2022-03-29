# Chapter 11

# Using survey class from survey.py 
from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the survey and store respones to the question
my_survey.show_question()
print("Enter 'q' at any time to exit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Print survey results
my_survey.show_results()