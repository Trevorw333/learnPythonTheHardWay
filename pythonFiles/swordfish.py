while True:
    print("what is your name?")
    name = input()
    if name != "Joe":
        continue
    print('What is your password?')
    password = input()
    if password == 'password':
        break
print('Authenticated')
