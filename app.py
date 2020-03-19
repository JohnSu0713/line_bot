from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
    reply = "公啥毀？泥泥還小，聽不懂啦！～"

    if msg in ["食物吃飼料罐罐貓食物吃飽肚子餓"]
        reply = "泥泥永遠餓著呢..."
        

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))

@app.route("/StickerSendMessage/")
def location_send_message():
    reply_s = random.int(1, 430)
    sticker_message = StickerSendMessage(
        package_id = '1',
        sticker_id = reply_s
    )
    line_bot_api.push_message(user_id, sticker_message)
    return 'StickerSendMessage Done!'


if __name__ == "__main__":
    app.run()















