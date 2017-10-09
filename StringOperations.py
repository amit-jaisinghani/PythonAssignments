def rotate(str, exponent):
    length = len(str)
    for x in range(exponent):
        str = str[length - 1] + str[0:length - 1]
    return str


def shift_character(c, k):
    ascii_value = ord(c)
    for x in range(k):
        ascii_value = ascii_value + 1
        if ascii_value == 91:
            ascii_value = 65
    c = chr(ascii_value)
    return c


def convert(input):
    input = input.upper()
    index_s = input.index('S')
    index = input[index_s + 1:input.index(',')]
    exponent = input[input.index(','):]
    message = 'amit'
    return message, index, exponent


def main():
    print(rotate('amit',2))
    print(shift_character('G', 10))
    print(convert('S10,12'))


if __name__ == '__main__':
    main()
