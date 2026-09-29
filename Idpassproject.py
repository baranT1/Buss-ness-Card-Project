#Id Pass project
ıd = 'Baran'
pas = '21'
print('Please login in')
gıd = input('Id     :')
gpas = input('Password:')
x = 100
if gıd == ıd and gpas == pas :
    
    print('Balance :', x )
elif gıd == ıd and gpas != pas :
    print('Wrong Password')

elif gıd != ıd and gpas == pas :
        print('Wrong ID')

else :
    print('Wrong Id or Password')
