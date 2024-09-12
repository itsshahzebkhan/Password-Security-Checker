# step 1 - install Pycharm community edition from Google Chrome
# step 2 - before starting the project, you need to install 3 packages from Python library -
# step 3 - open terminal on your Pycharm app and type these 3 things one by one individually and then press enter
# pip3 install requests, pip3 install hashlib,  pip3 install sys
# step 4 - start coding

import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was NOT found. Carry on')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# note - in order to check whether your password is safe or not, open terminal after completing your code on your Pycharm app and type - py checkmypass.py since it is the name of my file, you can type the name of your file and then type your password and press the enter key