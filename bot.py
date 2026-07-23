import os
from flask import Flask
import threading
import telebot

# --- ផ្នែកបោកបញ្ឆោត Render ឱ្យស្គាល់ Port (កុំកែប្រែ) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.start()
# --------------------------------------------------------

# ប្រើ Token របស់អ្នកពីកូដដើម
TOKEN = '8618381807:AAEGeZLBDSB1ORCpRhDNEPww05BfluhH2FU'
bot = telebot.TeleBot(TOKEN)

# បន្ថើមកូដកន្លែង Bot របស់អ្នក (រក្សាកូដ qa_database របស់អ្នកទុកដដែលក៏បាន)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្ដី! Bot កំពុងដំណើរការលើ Render ជោគជ័យហើយ!")

if __name__ == '__main__':
    keep_alive()  # បើក Web Server ឱ្យ Render ស្គាល់ Port
    bot.infinity_polling()  # រត់ Bot
