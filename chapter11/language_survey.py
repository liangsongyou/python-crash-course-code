from survey import AnonymousSurvey

# define a question
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the questions and store responses to the question
print('Enter "q" at any time to quit')
my_survey.show_question()
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print('Thank you to everyone who participated in the survey.')
my_survey.show_result()