age = int(input('Enter your age: '))

def occupation(age):
    if age < 0:
        return 'Age must be a positive number!'
    elif 0 <= age <1:
        return 'You are infant, you stay home.'
    elif 1 <= age <7:
        return 'You go to kindergarden.'
    elif 7 <= age < 18:
        return 'You go to school.'
    elif 18 <= age < 22:
        return 'You go to university.'
    elif 22 <= age < 60:
        return 'You work.'
    else:
        return 'You are retired.'

if __name__ == "__main__":
    a = occupation(age)
    print(a)