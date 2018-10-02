# coding=utf-8
import requests, json, time, random, datetime, threading, pickle, os, string
from termcolor import colored

sitekey = "6LfYhz0UAAAAAJFKp28Sg0NnAEIPMfKI1RJSGsdB"

firstnames = ["King ","Allen ","Jev ","Chef ","Moe ","Juelz "]
fn = random.choice(firstnames)

lastnames = ["Mayweather ","Dick ","Muff ","Money ","Santana "]
ln = random.choice(lastnames)

sizes = ['38 ½','39','40','40 ½','41','42','42 ½','43','44','44 ½','45','45 ½','46','47'] #check sizes on site first
size = random.choice(sizes)

url = "https://slamjamsocialism-drops.com/graphql"

shoe_id = "132" #update
shoe_name = "Nike Air Blazer X Off White"
raffle_id = "67" # update 
country_id = "840" #US country code
city = " " #enter city

def emailz():
	string.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	username = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
	e = " " #enter Domain
	
	return username + (str(e))

email = emailz()

def gen_phone():
    first = str(random.randint(100,999))
    second = str(random.randint(1,888)).zfill(3)

    last = (str(random.randint(1,9998)).zfill(4))
    while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
        last = (str(random.randint(1,9998)).zfill(4))

    return '{}-{}-{}'.format(first,second, last)

phone = gen_phone()

def log(event):
	d = datetime.datetime.now().strftime("%H:%M:%S")
	print("Raffle SJS by @Moneymitchell :: " + str(d) + " :: " + event)

class Raffle(object):
	def __init__(self):
		self.s = requests.session()
		self.shoes = [
		{"shoe_id":"132","shoe_name":"Nike Air Blazer X Off White","raffle_id":"67"},
		]
		self.url = "https://slamjamsocialism-drops.com/graphql"
		return Raffle()
url="http://2captcha.com/in.php?key=*2captchakey*&method=userrecaptcha&googlekey=6LfYhz0UAAAAAJFKp28Sg0NnAEIPMfKI1RJSGsdB&pageurl=https://slamjamsocialism-drops.com/graphql"

def solvecaptcha():
	resp = requests.get(url) 
	if resp.text[0:2] != 'OK':
	    quit('Error. Captcha is not received')
	captcha_id = resp.text[3:]
	# return captcha_id

	# fetch ready 'g-recaptcha-response' token for captcha_id  
	fetch_url = "http://2captcha.com/res.php?key=*2captchakey*&action=get&id=" + captcha_id
	for i in range(1, 20):	
		sleep(2) # wait 5 sec.
		r = requests.get(fetch_url)
		if resp.text[0:2] == 'OK':
			break
	soup = bs(resp.text,'html.parser')
	# return soup

	url2 = "http://2captcha.com/res.php"
	for i in range(1,20):
		sleep(15)
		res = requests.get(url2, action)
	soups = bs(res.text,'html.parser')
	return soups

token = solvecaptcha()

print token

def register():
	d = datetime.datetime.now().strftime('%H:%M')
	
	headers = {
	    'authorization': "null",
	    'origin': "https://slamjamsocialism-drops.com",
	    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
	    'dnt': "1",
	    'content-type': "application/json",
	    'accept': "*/*",
	    'referer': "https://slamjamsocialism-drops.com/drops/167",
	    'accept-encoding': "gzip, deflate, br",
	    'accept-language': "en-US,en;q=0.9",
	    'cache-control': "no-cache"
	    }

	date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+01:00")

	payload = {
		"query":"mutation RequestOrdertMutation($data: OrderRequestInput!) {\n  requestOrder(data: $data)\n}\n",
		"operationName":"RequestOrdertMutation",
		"variables":{
			"data":{
				"firstName":fn,
				"lastName":ln,
				"email":email,
				"phone":phone,
				"country":country_id,
				"city":city,
				"order":[{'product':shoe_id,'size':size}],"raffle":raffle_id,
				"captcha":token,
				"date":date
			}
		}
		}

	response = requests.request("POST", url, data=payload, headers=headers)
	return response.text
register()