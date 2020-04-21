# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.



while True:
    phrase = input('Please enter a word or phrase: ').lower()
    if phrase == "quit":
        break
    else: 
        print (f"That word is {len(phrase)} characters long.")
