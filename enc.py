import random
import string

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*'
char = random.choice(alphabet)

matrix = ['A5', 'B13', 'B40', 'A31', 'B8', 'B33', 'B5', 'B59', 'B37', 'C35', 'C53', 'C60', 'C1', 'A16', '', 'D5', 'B36',
          'D30', 'C28', 'A34', 'D4', 'C49', 'A56', 'B22', 'A57', 'D13', 'C48', 'C20', 'A40', 'D29', 'A45', 'B29', 'D50',
          'D45', 'C44', 'B42', 'B31', 'D6', 'D8', 'D31', 'C23', 'C8', 'B45', 'B21', 'D20', 'B46', 'C55', 'D35', 'A14',
          'D22', 'C59', '', 'B32', 'A21', 'B15', 'D52', 'C45', 'B51', '', 'D58', 'C10', 'A22', 'A11', 'A49', 'A52',
          'C47', 'D3', '', 'D23', '', 'B3', 'A54', 'C29', 'B6', 'D47', 'C4', 'B25', 'A2', 'A10', 'D46', 'C52', 'B14',
          'A18', 'A58', 'A26', 'B10', 'D41', 'D14', 'D42', 'B52', 'C24', 'C26', 'C46', '', 'B9', 'A30', 'D33', '',
          'D25', 'C12', 'D55', 'B47', 'A51', 'C50', 'A50', 'D21', 'D9', 'B30', 'B54', 'D32', 'B35', 'C14', 'A32', 'C31',
          'A12', 'A17', 'C27', '', 'A1', 'C15', 'D11', 'C36', 'D16', 'A35', 'B2', 'A44', 'C32', 'C13', 'D49', 'D57',
          'A46', 'A41', 'A28', 'A7', 'D37', 'A33', 'A29', 'B12', 'C34', 'A55', 'A42', 'D26', '', 'A13', 'C5', '', 'C22',
          'D60', 'A43', 'C9', 'B23', 'C11', 'C57', 'A60', '', 'C42', 'C25', 'C17', 'C33', '', 'B49', 'B55', 'C7', 'B50',
          'C41', 'A19', 'D19', 'A59', 'C43', '', 'D39', 'A47', 'D53', 'B53', 'A20', 'A9', 'D24', 'B39', 'C19', 'C58',
          'A4', 'D7', 'C56', 'A15', 'B4', 'C37', 'A38', 'A27', 'B56', 'A8', 'D54', 'A24', 'C40', 'A37', 'A6', 'B48', '',
          'B58', 'B16', 'B26', 'B27', 'B60', 'B41', 'B43', 'D38', 'C51', 'D56', 'D40', 'A23', 'D18', 'B57', 'D34',
          'D15', '', 'C54', 'D44', 'B17', 'B28', 'C39', 'C38', 'D28', 'B44', 'C2', 'D48', 'C21', 'D43', 'C3', 'D10',
          'B34', 'D1', '', 'A53', 'B1', 'C18', 'D17', 'B18', 'D59', 'D12', 'C6', 'D51', 'A36', 'B38', 'C16', 'D36',
          'D27', 'C30', 'A39', 'A48', 'B7', 'A25', 'D2', 'B24', 'B20', 'B11', 'A3', 'B19']
cipher = ['' for _ in range(256)]
print("----------------------------------------------------------------")
plaintext = "i want to play star rail day and night"
print("明文长度为：", len(plaintext))
key = [(5, 8),(11, 5),(3, 17),(9, 4)]
num_offsets = [4, 3, 9, 6]

for i in range(4):
    for j in range(len(plaintext)):
        index = matrix.index(chr(ord('A') + i) + str(j + 1))
        if plaintext[j] == " ":
            cipher[index] = '*'
        else:
            if plaintext[j] in string.ascii_lowercase:
                cipher[index] = chr(((ord(plaintext[j])-ord('a')) * key[i][0] + key[i][1]) % 26 + ord('a'))
            elif plaintext[j] in string.ascii_uppercase:
                cipher[index] = chr(((ord(plaintext[j])-ord('A')) * key[i][0] + key[i][1]) % 26 + ord('A'))
            else:
                cipher[index] = str((int(plaintext[j]) + num_offsets[i]) % 10)

for i in range(len(cipher)):
    if cipher[i] == '':
        cipher[i] = "+"

print(cipher)
txt = ''

with open("real.txt", "w") as file:
    for i in range(256):
        file.write(cipher[i])
        if (i + 1) % 16 == 0:
            file.write("\n")

with open("code.txt", "w") as file:
    for j in range(18):
        file.write(random.choice(alphabet))

    file.write("\n")
    file.write(random.choice(alphabet))
    for i in range(256):
        file.write(cipher[i])
        if i % 16 == 15:
            file.write(random.choice(alphabet))
            file.write("\n")
            file.write(random.choice(alphabet))

    for j in range(17):
        file.write(random.choice(alphabet))


