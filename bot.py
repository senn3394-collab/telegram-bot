import os
from flask import Flask
import threading
import telebot

app = Flask('')

@app.route('/')
def home():
    return "IT Interview Bot is running!"

def run_web():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.start()

TOKEN = '8618381807:AAGEfDmpsdWgJSYRJpzqmPGqyiufQveDQFc'
bot = telebot.TeleBot(TOKEN)

ALLOWED_USERS = [2043946113] 

qa_database = {
    'q1': "🔹 សំណួរ: ណែនាំខ្លួនប្រាប់ពីប្រវត្តិរូប និងបទពិសោធន៍របស់អ្នក?\n\n🔸 ចម្លើយ: និយាយពីឈ្មោះ ជំនាញសិក្សា បទពិសោធន៍ការងារ ឬ Project និងចំណង់ចំណូលចិត្តលើផ្នែកបច្ចេកវិទ្យា។",
    
    'q2': "🔹 សំណួរ: តើអ្វីជាចំណុចខ្លាំង និងចំណុចខ្សោយរបស់អ្នក?\n\n🔸 ចម្លើយ: ចំណុចខ្លាំងគឺងាយចេះដឹងរឿងថ្មីៗ និងចូលចិត្តការងារជាក្រុម។ ចំណុចខ្សោយគឺចង់ឱ្យការងារល្អឥតខ្ចោះពេក ប៉ុន្តែមានវិធីកែលម្អ។",
    
    'q3': "🔹 សំណួរ: ហេតុអ្វីបានជាយើងគួរជ្រើសរើសអ្នកចូលធ្វើការ?\n\n🔸 ចម្លើយ: មានឆន្ទៈរៀនសូត្រ យកជំនាញមកអភិវឌ្ឍក្រុមហ៊ុន និងអាចសម្របខ្លួនធ្វើការជាមួយក្រុមបានល្អ។",
    
    'q4': "🔹 សំណួរ: ពេលជួបបញ្ហា Bug ដែលដោះស្រាយមិនចេញ តើអ្នកធ្វើដូចម្តេច?\n\n🔸 ចម្លើយ: អាន Error Log ឆែក Documentation ស្វែងរកតាម Stack Overflow ឬពិភាក្សាជាមួយក្រុម។",
    
    'q5': "🔹 សំណួរ: តើអ្នកដោះស្រាយបញ្ហាយ៉ាងណាពេលមាន Deadline កៀកថ្ងៃ?\n\n🔸 ចម្លើយ: រៀបចំកិច្ចការតាមលំដាប់លំដោយ ផ្តោតលើចំណុចសំខាន់មុន និងប្រឹក្សាយោបល់ជាមួយ Supervisor។",
    
    'q6': "🔹 សំណួរ: តើអ្នកមើលឃើញខ្លួនឯងនៅឯណាក្នុងរយៈពេល ៣ ដល់ ៥ ឆ្នាំទៀត?\n\n🔸 ចម្លើយ: ក្លាយជា Senior Developer ដែលមានសមត្ថភាពដឹកនាំក្រុម ឬអ្នកជំនាញលើផ្នែក Software Architecture។",
    
    'q7': "🔹 សំណួរ: តើអ្នករំពឹងទទួលបានប្រាក់ខែប៉ុន្មាន?\n\n🔸 ចម្លើយ: បើកចំហរទទួលយកតាមគោលការណ៍ក្រុមហ៊ុន ប៉ុន្តែសមស្របតាមសមត្ថភាព និងទីផ្សារបច្ចុប្បន្ន។",
    
    'q8': "🔹 សំណួរ: តើអ្នកធ្លាប់មានបញ្ហាមិនចុះសម្រុងជាមួយមិត្តរួមការងារដែរឬទេ?\n\n🔸 ចម្លើយ: ធ្លាប់តែយើងដោះស្រាយដោយការយកហេតុផលមកនិយាយគ្នា ស្ដាប់ភាគីម្ខាងទៀត ដើម្បរក្សាទំនាក់ទំនងល្អ។",
    
    'q9': "🔹 សំណួរ: តើអ្នកមានវិធីសាស្ត្រអ្វីខ្លះដើម្បីអាប់ដេតចំណេះដឹងបច្ចេកវិទ្យាថ្មីៗ?\n\n🔸 ចម្លើយ: អានអត្ថបទ Tech មើលវីដេអូបណ្តុះបណ្តាល និងសាកល្បងសរសេរ Code Project ថ្មីៗ។",
    ី
    'q10': "🔹 សំណួរ: តើអ្នកមានសំណួរអ្វីចង់សួរខាងក្រុមហ៊ុនយើងវិញទេ?\n\n🔸 ចម្លើយ: សួរពីបច្ចេកវិទ្យាដែលក្រុមការងារកំពុងប្រើប្រាស់ និងដំណើរការវាយតម្លៃការងាររបស់ក្រុមហ៊ុន។"
}

def check_permission(message):
    if message.from_user.id not in ALLOWED_USERS:
        bot.reply_to(message, "🚫 សុំទោស! អ្នកមិនមានសិទ្ធិប្រើប្រាស់ Bot នេះទេ។")
        return False
    return True

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if check_permission(message):
        bot.reply_to(message, "សូមជ្រើសរើសពាក្យបញ្ជាពី /q1 ដល់ /q10 ដើម្បីមើលសំណួរ និងចម្លើយ។")

@bot.message_handler(func=lambda message: message.text.startswith('/q'))
def handle_q_commands(message):
    if not check_permission(message):
        return

    command = message.text[1:].lower()
    
    if command in qa_database:
        bot.reply_to(message, qa_database[command])
    else:
        bot.reply_to(message, "❌ មិនមានពាក្យបញ្ជានេះទេ។ សូមប្រើ /q1 ដល់ /q10។")

if __name__ == '__main__':
    keep_alive()  
    bot.infinity_polling()
