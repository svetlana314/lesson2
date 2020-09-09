def ask_user():
    answer = ''

    while answer != 'Good':
        try:
            answer = input('How are you? \n')
        except KeyboardInterrupt:
            print('Bye')
            break

if __name__ == "__main__":
    ask_user()