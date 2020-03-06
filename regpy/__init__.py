#!/usr/bin/python3
from re import findall

# text function to grab all alphabetic data.
def text(data):
	pattern = r'[a-zA-Z]'
	expression = findall(pattern,data)
	if expression:
		print(','.join(expression))
	else:
		return False

# emails function to grab all valid mails id's & join them. 
def emails(data):
	pattern = r'[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{1,3}'
	expression = findall(pattern,data)
	if expression:
		print('-'.join(expression))
	else:
		return False
		
# everything function will match everything except alphanumeric data.
def everything(data):
	pattern = r'[^a-zA-Z0-9]'
	expression = findall(pattern,data)
	if expression:
		return expression
	else:
		return False

# postal_code function to grab all valid postal code in list.
def postal_code(data):
	pattern = r'^[1-9]\d{5}$'
	expression = findall(pattern,data)
	if expression:
		return expression
	else:
		return False


# url function to grab all urls in list.
def url(data):
	pattern = r'https://[a-zA-Z0-9]+\.[a-z]{1,3}'
	expression = findall(pattern,data)
	if expression:
		return expression
	else:
		return False

# ip function to grab all ip's in list.
def ip(data):
	pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
	expression = findall(pattern,data)
	if expression:
		return expression
	else:
		return False
