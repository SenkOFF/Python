def user(defname):
    print(f'Hello {defname}')


def wiek(age):
    print(f'Your age -> {age}')

if __name__ == '__main__':
    name = input('Pls input your Name:')
    user(name)
    wiek(30)
    print(f"my name -> {__name__} and I working by my self")
else:
    print(f'my name -> {__name__} and I working from {__name__} files like a slave')