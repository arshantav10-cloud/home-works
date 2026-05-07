while True:
    print()
    print("1) search")
    print("2) add")
    print("3) exit")
    print("4) show all irregulars")
    try:
        user_respond = int(input("Enter your choice[1, 2, 3, 4]: "))
    except ValueError:
        print("!!Please enter a valid option(not an alphabetic word)!!")
        continue

    if user_respond == 1:
        word_base_form = input("Enter base form of word: ").lower()

        f = open("irregulars.txt", 'r')
        lines = f.readlines()

        # preparation
        clean_words = []
        for line in lines:
            clean_words.append(line.strip().split(","))

        # search
        found = False
        for item in clean_words:
            if item[0] == word_base_form:
                print(f'Base form: {item[0]}')
                print(f'Past simple: {item[1]}')
                print(f'Participle: {item[2]}\n')
                found = True
                break

        if not found:
            print(f'{word_base_form} not found!!!')

        f.close()

    elif user_respond == 2:
        base_form = input("Please enter the base form of the word: ")
        past_simple = input("Please enter the past simple form of the word: ")
        participle = input("Please enter the participle form of the word: ")
        new_item = f'{base_form},{past_simple},{participle}'

        # check line exists
        exists = False
        f = open("irregulars.txt", 'r')
        lines = f.readlines()
        for line in lines:
            if line.strip() == new_item:
                exists = True
                print("This verb already exists in the irregulars list")
                break
        f.close()
        # end of check line exists

        if not exists:
            f = open('irregulars.txt', 'a')
            f.write(new_item + '\n')
            print(f"your word has been added to the irregulars list\n")
            f.close()

    elif user_respond == 3:
        break

    elif user_respond == 4:
        f = open("irregulars.txt", 'r')
        lines = f.readlines()
        for line in lines:
            print(line.strip().replace(',', '-'))
    else:
        print("Please enter a valid option")

print("See you next time!")
