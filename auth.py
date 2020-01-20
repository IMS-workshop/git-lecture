import getpass
import pickle
import sys

def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return username, password

def authenticate(username, password, pwdb):
    if username in pwdb:
        if password == pwdb[username]:
            return True
    return False

def read_pwdb(pwdb_file):
    pwdb_file.seek(0)
    pwdb = pickle.load(pwdb_file)
    return pwdb

def write_pwdb(pwdb, pwdb_file):
    pwdb_file.seek(0)
    pickle.dump(pwdb, pwdb_file)

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

if __name__ == '__main__':
    DEFAULT_PWDB = 'pwdb.pkl'

    try:
        pwdb_file = open(DEFAULT_PWDB, 'rb+')
    except FileNotFoundError:
        pwdb_file = open(DEFAULT_PWDB, 'wb')
        pickle.dump({}, pwdb_file)
        pwdb_file.close()
        print('Created empty pw database!')
        sys.exit(0)

    username, password = get_credentials()
    pwdb = read_pwdb(pwdb_file)

    if authenticate(username, password, pwdb):
        print('Successfull authentication', username, password)
    else:
        ans = input('User not known or password is wrong. Do you want to add the '
                    'user to the password database? [y/n]')

        if ans == 'y':
            add_user(username, password, pwdb)
            write_pwdb(pwdb, pwdb_file)

