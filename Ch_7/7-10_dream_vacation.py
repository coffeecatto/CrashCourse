# 7-10 Dream Vacation
# Poll users about their dream vacation. 
# Then print the results.
poll_active = True
poll_results = {}

while poll_active == True:
    participant_name = input("What is your name?: ")
    participant_response = input("What's your dream place to visit?: ")

    poll_results[participant_name] = participant_response

    repeat_poll = input("Ask another person? (YES/NO): ")

    if repeat_poll == 'no' or repeat_poll == 'n':
        poll_active = False
        
        # Now to print the results in a tidy way
        print("\nThanks for participating in the poll! The results:")
        for name, response in poll_results.items():
            print(f"\t{name.title()}'s dream vacation spot is "
            f"{response.title()}!")
