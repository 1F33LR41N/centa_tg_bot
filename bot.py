#!/usr/bin/python
import config 
import telegram
import os
import subprocess
import sys
import shlex
import datetime
from subprocess import Popen, PIPE
from telegram.ext import CommandHandler
from imp import reload 

#bot = telegram.Bot(token = config.token)
#Проверка бота
#print(bot.getMe())
from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Приветики, меня зовут Centa, я твой покорный бот, жду команды")


def help(bot, update):
    reload(config)
    bot.sendMessage(chat_id=update.message.chat_id, text='''список доступных команд:
    /id - узнать свой Telegram id
    /ts3status- состояние сервера TS3
    /ts3restart - перезапуск сервера TS3
    /ts3start - запуск сервера TS3
    /ts3stop - остановка сервера TS3
    /ts3update - обновление сервера TS3
    /ts3backup - резервная копия сервера TS3
    /df - информация о наличии места на жетском диске

    ''')

#функция команады id
def myid(bot, update):
    userid = update.message.from_user.id
    bot.sendMessage(chat_id=update.message.chat_id, text=userid)

#функция команады df
def df(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("df -h")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады ts3status
def ts3status(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3status_command = config.ts3dir + "ts3server.sh status"
        run_command(ts3status_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3restart
def ts3restart(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3restart_command = config.ts3dir + "ts3server.sh restart"
        run_command(ts3restart_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3update
def ts3update(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3update_command = config.ts3dir + "ts3server.sh update"
        run_command(ts3update_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3backup
def ts3backup(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3backup_command = config.ts3dir + "ts3server.sh backup"
        run_command(ts3backup_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3stop
def ts3stop(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3stop_command = config.ts3dir + "ts3server.sh stop"
        run_command(ts3stop_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3start
def ts3start(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3start_command = config.ts3dir + "ts3server.sh start"
        run_command(ts3start_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)        
        
        
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

df_handler = CommandHandler('df', df)
dispatcher.add_handler(df_handler)

ts3status_handler = CommandHandler('ts3status', ts3status)
dispatcher.add_handler(ts3status_handler)

ts3restart_handler = CommandHandler('ts3restart', ts3restart)
dispatcher.add_handler(ts3restart_handler)

ts3update_handler = CommandHandler('ts3update', ts3update)
dispatcher.add_handler(ts3update_handler)

ts3backup_handler = CommandHandler('ts3backup', ts3backup)
dispatcher.add_handler(ts3backup_handler)

ts3stop_handler = CommandHandler('ts3stop', ts3stop)
dispatcher.add_handler(ts3stop_handler)

ts3start_handler = CommandHandler('ts3start', ts3start)
dispatcher.add_handler(ts3start_handler)

updater.start_polling()
