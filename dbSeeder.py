import json
import os
import random
from random import randint
import requests
import string


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


random.seed = (os.urandom(1024))

protocol = 'https' # http or https
host = 'www.example.localhost'
actionPath = 'someDirectory/submitForm.php'

url = f'{protocol}//{host}/{actionPath}'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "da, en-GB;q=0.9, en;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.example.localhost",
    "Origin": "https://www.example.localhost",
    "Referer": "https://www.example.localhost/",
    "Upgrade-Insecure-Requests": "1",
    "X-Requested-With": "XMLHttpRequest",
    }

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'
]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

titlelist = ['Mr', 'Mrs', 'Miss']
title = random.choice(titlelist)

if title == 'Mr':
	firstnameslist = json.loads(open('male_firstnames.json').read())
else:
	firstnameslist = json.loads(open('female_firstnames.json').read())

firstname = random.choice(firstnameslist)
lastnameslist = json.loads(open('lastnames.json').read())
lastname = random.choice(lastnameslist)

emaildomainlist = ['@gmail.com', '@yahoo.com', '@outlook.com', '@hotmail.com', '@aol.com', '@aim.com', '@mail.com', '@icloud.com']
emaildomain = random.choice(emaildomainlist)
email_extra = str(random_with_N_digits(random.randint(1,3)))
n = random.randint(0,5)
if n == 0:
	email = firstname.lower() + email_extra + emaildomain
if n == 1:
	email = firstname.lower() + '.' + lastname.lower() + email_extra + emaildomain
if n == 2:
	email = firstname.lower() + '_' + lastname.lower() + email_extra + emaildomain
if n == 3:
	email = firstname[0].lower() + lastname.lower() + email_extra + emaildomain
if n == 4:
	email = firstname[0].lower() + '.' + lastname.lower() + email_extra + emaildomain
if n == 5:
	email = firstname[0].lower() + '_' + lastname.lower() + email_extra + emaildomain


contactnumber = '07' + str(random_with_N_digits(9))

# Replace form input field names in the dictionary below

data = {
	'titleFormInputFieldNameHere': title,
	'firstnameFormInputFieldNameHere': firstname,
	'lastnameFormInputFieldNameHere': lastname,
	'emailFormInputFieldNameHere': email,
	'contactnumberFormInputFieldNameHere': contactnumber,
}

print('Posting form: \n Title: %s \n First-name: %s \n Last-name: %s \n Email: %s \n Contact-number: %s \n' % (title, firstname, lastname, email, contactnumber))

response = requests.post(url, headers=headers, allow_redirects=False, data=data)

print(response.request.headers)
print(response.request.body)
print(response.content)
print(response.json)