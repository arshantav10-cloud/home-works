f = open('pattern-1.txt', 'w')

for i in range(1, 11):
    for j in range(i, 0, -1):
        f.write(f'{j}\t')
    f.write('\n')

print('you\'re file is ready')
f.close()
