f = 'Fawwaz'
r = input('Enter Your Password : ')

for x in range(2):
    if r==f:
        print('login success')
        break
    elif r!=f:
        print('Sorry, Incorrect Password')
        r=input('Enter Your Password : ')
    else:
        print('You have entered wrong password 3 times, Access Denied')
            