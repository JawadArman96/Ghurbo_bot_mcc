# encoding=utf-8
import random
import re
import sys
import BotArchitecture
import FlightConversationTemplate
reload(sys)
sys.setdefaultencoding('utf-8')

# url = 'https://mccltd.info/projects/ghurbo/messenger-bot/form.php'
#
# # Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url + 'doc/')
#
# # Open URL in new window, raising the window if possible.
# webbrowser.open_new(url)

while True:
     user_input=raw_input();
     bot_reply_type=FlightConversationTemplate.detect_place(user_input)
     print(bot_reply_type)