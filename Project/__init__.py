from flask import Flask

app = Flask(__name__,static_folder='templates/static')

from Project import Chatbot
from Project import routes






