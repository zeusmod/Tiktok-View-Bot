import sys
import requests
AngivLink = input('Video ID Fx 6971527305076231430 -> ')
url = "https://homedecoratione.com/v4.php"
hat = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length': '52',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'PHPSESSID=c1a15a17a74a3c4fa17d859ce3e3cc90; n=1',
'origin': 'https://homedecoratione.com',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'sec-gpc': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.366',
'x-requested-with': 'XMLHttpRequest',
}
date =  {
'0429a': 'tok_free',
'af49f': 'hearts',
'9a898': '{AngivLink}'}
while True:
    tiktoker = requests.post(url, data=date, headers=hat)
    print("Succesfully Booted the Video Response -> ", tiktoker)
