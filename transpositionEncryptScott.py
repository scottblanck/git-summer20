import pyperclip

def main():
    myMessage = 'Show me the baby.'
    myKey = 13

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)   # copy to the clipboard

def encryptMessage(key, message):
    ciphertext = [''] * key      # each string represents a column of text

    #Loop through each column
    for col in range(key):
        pointer = col

        while pointer < len(message):   # Repeat until past end of message
            ciphertext[col] += message[pointer]  # Grab a single char

            pointer += key   # jump the pointer to the next char

    return ''.join(ciphertext)  # return a single string joined together


# if run directly then call the main() function
if __name__ == '__main__':
    main()
    
