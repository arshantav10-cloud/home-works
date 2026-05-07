name = input('ENTER YOUR FILE NAME: ')

try:
    f1 = open(name, 'r')

    file_name = name.split('.')[0]
    extension = name.split('.')[1]

    lines = f1.readlines()

    f2 = open(f'{file_name}-copy.{extension}', 'w')
    for line in lines:
        f2.write(line)

    print("Copied!")
    f1.close()
    f2.close()
except FileNotFoundError:
    print("File not found.")
