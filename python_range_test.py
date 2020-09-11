# string = 'abcdcba'
# L = len(string)
# print('len:', L)
# print('len//2:', L // 2)
# print(string[0:4])
# print(string[:-5:-1])
#
# print(string[:L // 2 + 1])
# print(string[:-L // 2 - 1:-1])
#
# string = 'abcddcba'
# L = len(string)
# print('len:', L)
# print('len//2:', L // 2)
#
# print(string[:4])
# print(string[:-5:-1])
#
# print(string[:L // 2])
# print(string[:-L // 2 - 1:-1])

string = 'abcdcba'
L = len(string)
# odd string pattern
print(string[:L // 2 + 1])
print(string[:-L // 2 - 1:-1])
string = 'abcddcba'
L = len(string)
# even string pattern
print(string[:L // 2])
print(string[:-L // 2 - 1:-1])

string = 'hello'
print(string)
print(string[::-1])

print(ord('a'))
print(chr(ord('a') + 7))
print(ord('z'))
print(ord('z') - ord('a'))


def caesarCipherEncryptor(string, key):
    L = list(string)
    for i in range(len(L)):
        L[i] = chr((ord(L[i]) - ord('a') + key) % 26 + ord('a'))
    return ''.join(L)


print(caesarCipherEncryptor('xyz', 2))


print(-2 % 26)


new_list = [8,2,-6]
new_list.sort()
s = set(new_list)
print(new_list)
print(s)
# new_list = new_list.sort()


my_list = [1,2,3,2,7,4,2,5,2]

for elem in my_list:
    if elem == 7:
        my_list.remove(elem)
print(my_list)
my_list.remove(2)
print(my_list)
