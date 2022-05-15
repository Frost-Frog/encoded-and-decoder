import base64


def encode():
    print('Input what you want encoded:')
    word = input()
    bytes = word.encode('ascii')
    bytes64 = base64.b64encode(bytes)
    encoded = base64.b64decode(bytes64)
    print(bytes64)

def decode():
    print('Input what you want decoded:')
    word = input()
    bytes = word.encode('ascii')
    decoded = base64.b64decode(bytes)
    print(decoded)

print('Would you like to encode or decode?')
decision = input()
if decision == 'encode':
    encode()
elif decision == 'decode':
    decode()
else:
    print('That is not an option')



   