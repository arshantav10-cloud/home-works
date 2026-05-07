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
        print(f'Participle: {item[2]}')
        found = True
        break

if not found:
    print(f'{word_base_form} not found!!!')

f.close()
