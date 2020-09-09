answers = {
    "How are you?": "Good!",
    "What are you doing?": "I am programming",
    "How is the weather today?": "It is cold",
    "Where do you live?": "In Moscow",
    "Do you like to eat?": "Oh, yeah"
}

def ask_user(): 
    question = ''

    while question != 'Bye':
        question = input('Ask me a question or say "Bye".\n')
        print(answers.get(question, ''))
       
if __name__ == "__main__":
    ask_user()