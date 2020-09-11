def main():
    line = input('Enter line: ')
    for word in line:
        for letter in word:
            print(letter)

if __name__ == "__main__":
    main()