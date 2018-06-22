print('Mode 1 >>> text to cipher\nMode 2 >>> cipher to text')
mode = int(input('choose your mode :'))
if mode == 1 :
    text = input('Your text :').lower()
    key = input('Your key :').lower()
    result = ''
    if len(text) < len(key):
        key = key[:len(text)]
    if len(text) > len(key):
        key *= len(text) // len(key)
        key += key[:len(text) - len(key)]

    for i in range(len(text)):
       cipher = ((ord(text[i])-97) + (ord(key[i])-97)) % 26
       cipher = cipher + 97
       cipher = chr(cipher)
       result += cipher
    print('You cipher is >>>', result)
elif mode == 2 :
    cipher = input('You cipher :').lower()
    key = input('You key :').lower()
    result = ''
    if len(cipher) < len(key):
        key = key[:len(cipher)]
    if len(cipher) > len(key):
        key *= len(cipher) // len(key)
        key += key[:len(cipher) - len(key)]
    for i in range(len(cipher)):
        text = ((ord(cipher[i])-97) - (ord(key[i])-97)) % 26
        text = text + 97
        text = chr(text)
        result += text
    print('You text >>>', result)

