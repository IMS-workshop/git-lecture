import getpass

def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return username, password

if __name__ == '__main__':
    username, password = get_credentials()
    print(username, password)
