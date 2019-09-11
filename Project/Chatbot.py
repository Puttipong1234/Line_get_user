import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent
)




from Project import app

# get channel_secret and channel_access_token from your environment variable
channel_secret = '59e4fa061014bb487744e6c556e2bdfa'
channel_access_token = 'zudm75JEIPI7BDa+YGlWVtvVOTZe/MLQxoYB0kSrbjFoXO1AjGFyxypY8Pf5o7bj+wd3cC5gteHLE7woZAwN6UoCE5jv/e2/+V7soeamiZVLUVmlaeKlWY2kI5iWVvrDejUehtG4ySNcN2zDJHwsVQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


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
        abort(400)

    return 'OK'

from .FireStore import User

@handler.add(FollowEvent)
def GetUserData(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Thank for Registration account')
    )

    uid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=uid).display_name

    user = User(disname,uid)
    user.sendData()

