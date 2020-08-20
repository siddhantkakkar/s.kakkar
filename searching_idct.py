n1 = input()

n = int(n1)

phonebook = {}

for i in range(0, n):

    key_val = input()

    list1 = key_val.split(' ')

    key = list1[0]

    value = list1[1]

    phonebook[key] = value



while True:

    test_key = input()

    if test_key == '':

        break

    if test_key in phonebook:

        ans = phonebook[test_key]

        print(test_key, ': ', ans)

    else:

        print('not found')
