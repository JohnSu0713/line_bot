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
    r = "泥泥餓，聽不懂～"

    if msg in "食物罐罐頭貓飼料吃飽餵食了沒嗎？":
        r = "泥泥永遠餓著呢...泥泥胖!!"
    elif "嗨" in msg:
        r = "泥泥餓，沒空跟你說『嗨』啦..."
    elif "泥爸" in msg:
        r = "泥爸是個超級大帥哥-A.K.A 『永安金城武』是他！！"
    elif "泥媽" in msg:
        r = "泥媽跟泥泥一樣，好愛好愛吃東西哦～"



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()















