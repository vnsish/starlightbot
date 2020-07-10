from time import time
from config import PAPAGO_ID, PAPAGO_SECRET
import requests
import json

AVAILABLE = ['ko', 'en']

def elapsed(now):
	if time()-now > 15:
		return True
	return False

def detect_language(text):
	payload = {'query': text }
	headers = {'X-Naver-Client-Id': PAPAGO_ID, 'X-Naver-Client-Secret': PAPAGO_SECRET, 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
	body = requests.post('https://openapi.naver.com/v1/papago/detectLangs', headers=headers, data=payload)
	if body.status_code != 200:
		raise Exception('HTTP Response not OK: [{}]'.format(body.status_code))
	
	return json.loads(body.text)['langCode']

def translate(text, source, target):
	if source not in AVAILABLE or target not in AVAILABLE:
		raise Exception('Invalid language')
	payload = {'text': text, 'source':source, 'target':target }
	headers = {'X-Naver-Client-Id': PAPAGO_ID, 'X-Naver-Client-Secret': PAPAGO_SECRET, 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
	body = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=payload)
	if body.status_code != 200:
		raise Exception('HTTP Response not OK: {}'.format(body.status_code))

	return json.loads(body.text)['message']['result']['translatedText']
	

if __name__ == "__main__":
	#print(translate('이것은 한국어로 된 약간의 텍스트 입니다.', 'ko', 'en'))
	print(translate('Text', 'en', 'ko'))