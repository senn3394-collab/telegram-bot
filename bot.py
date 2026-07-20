import telebot

# ដាក់ Token ដែលបានពី BotFather នៅទីនេះ
TOKEN = '8618381807:AAEGeZLBDSB1ORCpRhDNEPww05BfluhH2FU'
bot = telebot.TeleBot(TOKEN)

# ចំណុច C: បញ្ជី User ID ដែលត្រូវបានអនុញ្ញាតឱ្យប្រើប្រាស់ Bot នេះ
# (អ្នកអាចយក User ID របស់អ្នកបានដោយចូលទៅកាន់ @userinfobot ក្នុង Telegram)
ALLOWED_USERS = [2043924613] 

# ចំណុច A & B: សំណួរ និងចម្លើយសម្ភាសន៍សម្រាប់តំណែង Developer ទាំង ១០
qa_database = {
    'q1': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្វីទៅជា Object-Oriented Programming (OOP)?\n🔸 ចម្លើយ: OOP គឺជាវិធីសាស្ត្រសរសេរកូដដែលពឹងផ្អែកលើ Objects ដោយមានលក្ខណៈសំខាន់ៗ៤គឺ Encapsulation, Abstraction, Inheritance និង Polymorphism។",
    
    'q2': "តំណែង: Developer\n\n🔹 សំណួរ: តើ Pointer នៅក្នុងភាសា C++ គឺជាអ្វី?\n🔸 ចម្លើយ: Pointer គឺជាអថេរ (Variable) មួយប្រភេទដែលផ្ទុកអាសយដ្ឋានអង្គចងចាំ (Memory Address) របស់អថេរផ្សេងមួយទៀត។",
    
    'q3': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្វីជាភាពខុសគ្នារវាង Array និង Linked List?\n🔸 ចម្លើយ: Array រក្សាទុកទិន្នន័យនៅជាប់ៗគ្នាក្នុង Memory និងមានទំហំកំណត់ ចំណែក Linked List រក្សាទុកទិន្នន័យដោយភ្ជាប់ Pointer ពីមួយទៅមួយ និងអាចប្រែប្រួលទំហំបាន។",
    
    'q4': "តំណែង: Developer\n\n🔹 សំណួរ: តើ Git និង GitHub ខុសគ្នាដូចម្តេច?\n🔸 ចម្លើយ: Git គឺជា Version Control System សម្រាប់គ្រប់គ្រងកូដ ចំណែក GitHub គឺជាសេវាកម្ម Cloud សម្រាប់រក្សាទុក (Host) Git Repositories។",
    
    'q5': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្វីជា Inheritance នៅក្នុង C++?\n🔸 ចម្លើយ: Inheritance អនុញ្ញាតឱ្យ Class ថ្មីមួយអាចទាញយកលក្ខណៈសម្បត្តិ (Properties) និងមុខងារ (Methods) ពី Class ចាស់ដែលមានស្រាប់មកប្រើប្រាស់បន្តបាន។",
    
    'q6': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្វីជាភាពខុសគ្នាចម្បងរវាងភាសា Python និង C++?\n🔸 ចម្លើយ: C++ ជា Compiled Language ដែលមានល្បឿនលឿន និងគ្រប់គ្រង Memory ដោយផ្ទាល់ ចំណែក Python ជា Interpreted Language ដែលងាយស្រួលសរសេរជាង តែដំណើរការយឺតជាងបន្តិច។",
    
    'q7': "តំណែង: Developer\n\n🔹 សំណួរ: តើ API (Application Programming Interface) គឺជាអ្វី?\n🔸 ចម្លើយ: API គឺជាសំណុំនៃវិធានដែលអនុញ្ញាតឱ្យកម្មវិធី Software ពីរអាចធ្វើការទំនាក់ទំនង និងទាញយកទិន្នន័យពីគ្នាទៅវិញទៅមកបាន។",
    
    'q8': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្វីទៅជា MVC Framework?\n🔸 ចម្លើយ: MVC (Model-View-Controller) គឺជា Design Pattern ដែលបំបែកកម្មវិធីជាបីផ្នែក: Model (ទិន្នន័យ), View (ចំណុចប្រទាក់) និង Controller (ដំណើរការតក្កវិជ្ជា)។",
    
    'q9': "តំណែង: Developer\n\n🔹 សំណួរ: តើ SQL និង NoSQL Databases ខុសគ្នាយ៉ាងដូចម្តេច?\n🔸 ចម្លើយ: SQL ជា Relational Database ប្រើប្រាស់តារាងមានរចនាសម្ព័ន្ធច្បាស់លាស់ (ឧ. MySQL) ចំណែក NoSQL ជា Non-relational រក្សាទុកទិន្នន័យបែបបត់បែនជាង (ឧ. MongoDB)។",
    
    'q10': "តំណែង: Developer\n\n🔹 សំណួរ: តើអ្នកមានវិធីសាស្ត្រអ្វីខ្លះក្នុងការ Debug កូដរបស់អ្នកនៅពេលមាន Error?\n🔸 ចម្លើយ: វិធីសាស្ត្ររួមមានការអាន Error Messages, ការប្រើប្រាស់ Print Statements, ការសរសេរ Unit Tests, និងការប្រើប្រាស់ Debugger Tools នៅក្នុង IDE ដូចជា VS Code, Dev-C++ ឬ Code::Blocks ជាដើម។"
}

# ពិនិត្យមើលថាតើអ្នកប្រើប្រាស់មានសិទ្ធិឬអត់
def check_permission(message):
    if message.from_user.id not in ALLOWED_USERS:
        bot.reply_to(message, "🚫 សុំទោស! អ្នកមិនមានសិទ្ធិប្រើប្រាស់ Bot នេះទេ ព្រោះអ្នកមិនមានឈ្មោះក្នុងបញ្ជី។")
        return False
    return True

# ឆ្លើយតបនៅពេលវាយ /start ឬ /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if check_permission(message):
        bot.reply_to(message, "សួស្តី! សូមជ្រើសរើសពាក្យបញ្ជាពី /q1 ដល់ /q10 ដើម្បីមើលសំណួរ និងចម្លើយសម្ភាសន៍ការងារសម្រាប់តំណែង Developer។")

# ចាប់យកពាក្យបញ្ជា q1 ដល់ q10
@bot.message_handler(func=lambda message: message.text.startswith('/q'))
def handle_q_commands(message):
    if not check_permission(message):
        return

    command = message.text[1:].lower() # ដកសញ្ញា '/' ចេញ ហើយប្តូរជាអក្សរតូច
    
    if command in qa_database:
        bot.reply_to(message, qa_database[command])
    else:
        bot.reply_to(message, "❌ មិនមានពាក្យបញ្ជានេះទេ។ សូមវាយពាក្យបញ្ជាត្រឹមត្រូវ (ឧ. /q1, /q2 ... /q10)។")

# ឱ្យ Bot ដំណើរការរហូត
print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()