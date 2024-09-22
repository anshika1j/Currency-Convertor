import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1="INR"
currency_2="USD"
amount="1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "04c00e6393msh7428b3c2dde9276p1afe03jsn02c90dfbac3b",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted= "{:,.2f}".format(converted_amount)

print(converted_amount,formatted)