import getpass
import pickle

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
    username, password = get_credentials()
    print(username, password)
