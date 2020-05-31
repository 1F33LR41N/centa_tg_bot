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
    /db_backup - резервная копия базы данных сервера TS3
    /freemem - информация о памяти
    /df - информация о наличии места на жетском диске
    /dirspace - объем папки''' + config.dir1 + '''
    /bkpspace - размер файла бэкапа за текущий день в папке ''' + config.dir_backup + '''

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

#функция команады freemem
def freemem(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("free -m")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады dir1
def dir1(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        dir1_command = "du -sh "+ config.dir1
        run_command(dir1_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады dirbackup - проверяет наличие файла по дате
def dirbackup(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        now_date = datetime.date.today() # Текущая дата
        cur_year = str(now_date.year) # Год текущий
        cur_month = now_date.month # Месяц текущий
        if cur_month < 10:
            cur_month = str(now_date.month)
            cur_month = '0'+ cur_month
        else:
            cur_month = str(now_date.month)
        cur_day = str(now_date.day) # День текущий
        filebackup = config.dir_backup + cur_year + '-' + cur_month + '-' + cur_day + '.03.00.co.7z'  #формируем имя файла для поиска
        print (filebackup)
        filebackup_command = "ls -lh "+ filebackup
        run_command(filebackup_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

#функция команады ts3status
def ts3status(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3status_command = config.dir1+"ts3server status"
        run_command(ts3status_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3restart
def ts3restart(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3restart_command = config.dir1+"ts3server restart"
        run_command(ts3restart_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3update
def ts3update(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3update_command = config.dir1+"ts3server update"
        run_command(ts3update_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3backup
def ts3backup(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3backup_command = config.dir1+"ts3server backup"
        run_command(ts3backup_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3stop
def ts3stop(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3stop_command = config.dir1+"ts3server stop"
        run_command(ts3stop_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)
        
#функция команады ts3start
def ts3start(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        ts3start_command = config.dir1+"ts3server start"
        run_command(ts3start_command)
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)        
        
        
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

df_handler = CommandHandler('df', df)
dispatcher.add_handler(df_handler)

freemem_handler = CommandHandler('freemem', freemem)
dispatcher.add_handler(freemem_handler)

dir1_handler = CommandHandler('dir1', dir1)
dispatcher.add_handler(dir1_handler)

dirbackup_handler = CommandHandler('dirbackup', dirbackup)
dispatcher.add_handler(dirbackup_handler)

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

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
