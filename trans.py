from papago import Translator
from config import *

if __name__ == "__main__":
	#print('hello')
	translator = Translator(PAPAGO_ID, PAPAGO_SECRET)
	response = translator.translate('예시')
	print(response.code)