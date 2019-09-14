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
    MessageEvent, TextMessage, TextSendMessage, FollowEvent , PostbackEvent
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
from .FlexTemplate import *
@handler.add(FollowEvent)
def line_register(event):

    uid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=uid).display_name

    user = User('RegisUncle_01',disname,uid,session = 'none')
    user.update()

    replytoken = event.reply_token
    data = SetMenuMessage_Object(flexdata_regis)
    send_flex(replytoken,data,channel_access_token)

    line_bot_api.link_rich_menu_to_user(uid,'richmenu-4cbfaa427a4db188081ae974b1ca5f2f')


@handler.add(PostbackEvent)
def Postback(event):
    # print(event.postback.as_json_dict()['data'])
    if str(event.postback.as_json_dict()['data']) == '10hrvideo':
        replytoken = event.reply_token
        data = SetMenuMessage_Object(flexdata)
        send_flex(replytoken,data,channel_access_token)

        print(data)


@handler.add(MessageEvent , message = TextMessage)
def GetUserData(event):
    if 'ยืนยันการลงทะเบียน' in event.message.text:
        data = event.message.text

        uid = event.source.user_id
        disname = line_bot_api.get_profile(user_id=uid).display_name

        text_01 = TextSendMessage(text='User_id : {} ท่านได้ทำการลงทะเบียนสำเร็จ'.format(uid))
        text_02 = TextSendMessage(text='ขอบคุณ คุณ {} ที่ใช้บริการ UncleEngineer'.format(disname))
        line_bot_api.reply_message(reply_token = event.reply_token,messages=[text_01,text_02])

        user = User('RegisUncle_01',disname,uid,session = data)
        user.update()

        return 'OK'