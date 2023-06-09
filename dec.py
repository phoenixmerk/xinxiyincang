import string
from gmpy2 import invert

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
# cipher = ['v', 'f', '+', 'v', '0', '*', 's', '+', 'e', 'p', '+', '+', 'p', '9', '+', 'r', 't', 'e', 'l', 'v', '0', '+', '+', 'f', '+', 'e', '+', '*', '+', '*', '+', '*', '+', '+', '+', '+', 's', 't', '3', 'r', 'p', '6', '+', 'k', '*', '+', '+', 'y', 'y', 'e', '+', '+', 'm', 'p', '*', '+', '+', '+', '+', '+', '*', 'i', 'f', '+', '+', '+', 'u', '+', 'y', '+', 'n', '+', '*', 'g', '+', '3', '*', '*', '*', '+', '+', 'j', 'i', '+', 'x', '*', '+', 'm', '+', '+', 'y', 'a', '+', '+', 'd', 'i', '*', '+', '*', '0', '+', '+', '+', '+', '+', 'b', 'a', 'f', '+', 'f', 'p', 'l', 'x', 'e', '5', 'z', 'r', '+', 'w', '*', 'j', 'j', '1', 'w', '*', '+', 'a', 'r', '+', '+', '+', '+', 'y', '*', 'p', '*', '*', '4', 'e', '+', '+', 'f', '+', 'i', 'e', '+', 'r', '+', '+', 'h', 'p', 'k', '+', '+', '+', '+', '*', 'w', '*', '+', '+', '+', '*', '+', '+', 'p', 'b', '+', '+', '+', '+', '+', '+', '+', '*', 'a', 'z', '+', 'q', '+', '8', '*', '+', '*', '7', 'm', 'z', 'i', '+', '1', '+', 'l', '+', 'r', 'z', '+', '+', '+', '8', 'm', 'f', '+', '+', '+', 't', '+', '+', '+', 'w', 'e', '+', 'r', '*', '+', '+', '+', 'g', 'j', '+', 'w', 'm', '+', '*', '+', 'q', '+', 'f', '*', 's', 'y', '+', '+', 'p', 'r', 't', 'f', '+', '7', 'w', '+', 'm', 'g', '4', 'g', 'e', 'r', '+', '+', '*', '*', '*', 'w', '*', 'o', 'o', 'k']
plaintext = ['' for _ in range(4)]
key = [(5, 8), (11, 5), (3, 17), (9, 4)]
num_offsets = [4, 3, 9, 6]
# cipher = []
#
# with open("real.txt", "r") as file:
#     for i in range(16):
#         txt = file.readline().strip()
#         for j in range(16):
#             cipher.append(txt[j])
#             # print(cipher)
#
# print(len(cipher))
#
# for i in range(4):
#     for j in range(60):
#         index = matrix.index(chr(ord('A') + i) + str(j + 1))
#         if cipher[index] == "*":
#             plaintext[i] += " "
#         elif cipher[index] != "+":
#             if cipher[index] in string.ascii_lowercase:
#                 plaintext[i] += chr(
#                     ((ord(cipher[index]) - ord('a') - key[i][1]) * invert(key[i][0], 26)) % 26 + ord('a'))
#             elif cipher[index] in string.ascii_uppercase:
#                 plaintext[i] += chr(
#                     ((ord(cipher[index]) - ord('A') - key[i][1]) * invert(key[i][0], 26)) % 26 + ord('A'))
#             else:
#                 plaintext[i] += str((int(cipher[index]) - num_offsets[i]) % 10)
#         else:
#             plaintext[i] += "*"
# print("解密后的明文:")
# for i in plaintext:
#     print(i)

# tmp = []
#
# with open("code.txt", "r") as file:
#     for i in range(18):
#         txt = file.readline().strip()
#         for j in range(18):
#             tmp.append(txt[j])
#
# import random
# import string
#
#
# def replace_characters(lst):
#     # 选择随机的两个索引
#     indices = random.sample(range(len(lst)), 130)
#     # 生成替换的随机字母
#     replacements = random.choices(string.ascii_letters, k=130)
#     # 替换列表中的字符
#     for i, idx in enumerate(indices):
#         lst[idx] = replacements[i]
#     return lst
#
#
# # 示例用法
# tmp = replace_characters(tmp)
# print(tmp)
#
# def write_to_file(lst, filename):
#     with open(filename, "w") as file:
#         for i in range(0, len(lst), 18):
#             line = lst[i:i + 18]
#             line_str = "".join(line)
#             file.write(line_str + "\n")
#
#
# write_to_file(tmp, "code.txt")

cipher1 = []

with open("code.txt", "r") as file:
    next(file)  # 跳过第一行
    prev_line = ""  # 用于记录上一行的内容
    for line in file:
        line = line.strip()  # 去除行尾的换行符
        if prev_line:  # 检查是否为最后一行
            chars = prev_line[1:17]  # 提取第2到17个字符
            cipher1.extend(chars)
        prev_line = line  # 记录当前行的内容

# print(cipher)
print(cipher1)

# count = 0
# for i in range(0, 256):
#     if (cipher[i] == cipher1[i]):
#         count += 1
# print(count)

plaintext1 = ['' for _ in range(4)]
for i in range(4):
    for j in range(60):
        index = matrix.index(chr(ord('A') + i) + str(j + 1))
        if cipher1[index] == "*":
            plaintext1[i] += " "
        elif cipher1[index] != "+":
            if cipher1[index] in string.ascii_lowercase:
                plaintext1[i] += chr(
                    ((ord(cipher1[index]) - ord('a') - key[i][1]) * invert(key[i][0], 26)) % 26 + ord('a'))
            elif cipher1[index] in string.ascii_uppercase:
                plaintext1[i] += chr(
                    ((ord(cipher1[index]) - ord('A') - key[i][1]) * invert(key[i][0], 26)) % 26 + ord('A'))
            else:
                plaintext1[i] += str((int(cipher1[index]) - num_offsets[i]) % 10)
        else:
            plaintext1[i] += "*"
print("解密后的明文:")
for i in plaintext1:
    print(i)
