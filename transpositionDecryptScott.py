# Transpositon - Decrypt
# Scott

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')
    print('Now show me the baby.')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):

    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns  # plaintext is a list of strings for each column

    col = 0
    row = 0     # track where we are in the table

    for symbol in message:
        plaintext[col] += symbol    # build each column into a string one char at a time
        col += 1                    # move over to the next column

        # Are we off the end of a column OR at a shaded box?
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1      # go back to the first column and down one row

    return ''.join(plaintext)


if __name__ == '__main__':
    main()
