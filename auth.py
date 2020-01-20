import getpass
import pickle
import sys

def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return username, password

def read_pwdb(pwdb_file):
    pwdb = pickle.load(pwdb_file)
    return pwdb

def write_pwdb(pwdb, pwdb_file):
    pickle.dump(pwdb, pwdb_file)

if __name__ == '__main__':
    DEFAULT_PWDB = 'pwdb.pkl'

    try:
        pwdb_file = open(DEFAULT_PWDB, 'rb')
    except FileNotFoundError:
        pwdb_file = open(DEFAULT_PWDB, 'wb')
        pickle.dump({}, pwdb_file)
        pwdb_file.close()
        print('Created empty pw database!')
        sys.exit(0)

    username, password = get_credentials()
    pwdb = read_pwdb(pwdb_file)

    print(username, password)
