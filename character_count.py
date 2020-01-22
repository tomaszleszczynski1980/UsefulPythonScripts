def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


CHAR_PATTERN = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzżź1234567890 "


filename = input("Enter a filename: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print ("{0} not found".format(filename))

for char in CHAR_PATTERN:
    count = count_char(text, char)
    perc = 100 * count / len(text)
    print("{0} - {1}: {2}%".format(char, count, round(perc, 2)))
