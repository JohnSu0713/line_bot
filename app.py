from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

import random

app = Flask(__name__)

line_bot_api = LineBotApi('2MMEZj3CbTCP6rt6UYYueBD9MsNnIjFAksct60sVTurfG2zg/Q/3oj9rTDXoldcYw1kpQr1Rit4qaU/qC4z0DUP1ufmUquHJQzDxriissAtciyL1U/rBzEzx5JPHIcbRvuzImGpARrsmLFu+rSFnsQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1989623446333031b8adaceca81bd94d')


@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		print("Invalid signature. Please check your channel access token/channel secret.")
		abort(400)

	return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text

	say_list = ["本貓優點是：我很帥～但是我的缺點是：本貓帥的不明顯...", '我是胖貓，不是病貓。', "雖然你身上噴香水，但我還是能隱約聞到一股胖貓味。", "本貓沒有豬的形象，但是我有豬的氣質!", "本泥餓，沒空聽你說啦～"]

	if "貼圖" in msg:
		message = StickerSendMessage(
		package_id='1',
		sticker_id=str(random.randint(1,18)))
		line_bot_api.reply_message(event.reply_token, message)

	for i in 

	if msg in "食物罐罐頭貓飼料吃飽餵食了沒嗎？":
		r = "泥泥永遠餓著呢...泥泥胖!!"
	elif "嗨" in msg:
		r = "泥泥餓，沒空跟你說『嗨』啦..."
	elif "泥爸" in msg:
		r = "泥爸是個超級大帥哥-A.K.A 『永安金城武』是他！！"
	elif "泥媽" in msg:
		r = "泥媽跟泥泥一樣，好愛好愛吃東西哦"
	elif ["哎","唉","哼","喂","哦","哈","嘿","嘖嘖",'噢','唔','嗯'] in msg:
		r = "本貓只想著吃，你怎麼問題這麼多？"
	else:
		r = say_list[random.randint(0,6)]

	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=r))


if __name__ == "__main__":
	app.run()















