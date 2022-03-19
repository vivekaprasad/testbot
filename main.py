from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, input_message_content, user_and_chats
from pyrogram.types import ChatPermissions
from pyrogram.errors import MessageNotModified

bot = Client(
    'all subject bot',
    api_id=7009965,
    api_hash="06651b174c4f0591deb0ed1e5663c996",
    bot_token="5212184338:AAEkdTH6o0ljH_FU8rYu_z6f7B_MrIaWQpA"
)

START_MESSAGE='group menu'
A001_TEXT='subject menu'
A002_TEXT='menu closed'
A003_TEXT='secound menu'
A004_TEXT='ICT MENU'
A005_TEXT='MATHS MENU'
A006_TEXT='BIOLOGY'
A007_TEXT='TEC MENU'
A008_TEXT='COMMERCE'
A009_TEXT='ART MENU'
CLOSE_TEXT='Menu closed!'

START_BUTTONS=[
    [InlineKeyboardButton('ENTER SUBJECT MENU',callback_data='A001')],
    [InlineKeyboardButton('MORE',callback_data='A003')],
    [InlineKeyboardButton('HELP',url='https://t.me/ictstudenthelper/140')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
# subject menu
A001_BUTTONS=[
    [InlineKeyboardButton('ICT',callback_data='A004')],
    [InlineKeyboardButton('MATHS',callback_data='A005')],
    [InlineKeyboardButton('BIOLOGY',callback_data='A006')],
    [InlineKeyboardButton('TECHNOLGY',callback_data='A007')],
    [InlineKeyboardButton('COMMERCE',callback_data='A008')],
    [InlineKeyboardButton('ART',callback_data='A009')],
    [InlineKeyboardButton('🔙BACK',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
#more
A003_BUTTONS=[
    [InlineKeyboardButton('HOW TO USE',url='https://t.me/ictstudenthelper/140')],
    [InlineKeyboardButton('Useful groups and channels',callback_data='A010')],
    [InlineKeyboardButton('➕ADD TO GROUP➕',url='http://t.me/grpmenubot?startgroup=botstart')],
    [InlineKeyboardButton('🔙BACK',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
#ict
A004_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A010'),InlineKeyboardButton('NOTES',callback_data='A011')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
#maths
A005_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A011'),InlineKeyboardButton('NOTES',callback_data='A012')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
A006_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A013'),InlineKeyboardButton('NOTES',callback_data='A014')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
A007_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A015'),InlineKeyboardButton('NOTES',callback_data='A016')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
A008_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A016'),InlineKeyboardButton('NOTES',callback_data='A017')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
A009_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A018'),InlineKeyboardButton('NOTES',callback_data='A019')],
    [InlineKeyboardButton('MAIN MENU',callback_data='MAIN'),InlineKeyboardButton('BACK',callback_data='A001')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]

@bot.on_message(filters.command('start')) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="A001":
        reply_markup = InlineKeyboardMarkup(A001_BUTTONS)
        try:
            await query.edit_message_text(
                A001_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="A003":
        reply_markup=InlineKeyboardMarkup(A003_BUTTONS)
        try:
            await query.edit_message_text(
                A003_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A004":
        reply_markup=InlineKeyboardMarkup(A004_BUTTONS)
        try:
            await query.edit_message_text(
                A004_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A005":
        reply_markup=InlineKeyboardMarkup(A005_BUTTONS)
        try:
            await query.edit_message_text(
                A005_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        

    elif query.data=="A006":
        reply_markup=InlineKeyboardMarkup(A006_BUTTONS)
        try:
            await query.edit_message_text(
                A006_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A007":
        reply_markup=InlineKeyboardMarkup(A007_BUTTONS)
        try:
            await query.edit_message_text(
                A007_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A008":
        reply_markup=InlineKeyboardMarkup(A008_BUTTONS)
        try:
            await query.edit_message_text(
                A008_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A009":
        reply_markup=InlineKeyboardMarkup(A009_BUTTONS)
        try:
            await query.edit_message_text(
                A009_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="MAIN":
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
        try:
            await query.edit_message_text(
                START_MESSAGE,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="CLOSE":
        reply_markup=InlineKeyboardButton(CLOSE_BUTTONS)
        try:
            await query.edit_message_text(
                CLOSE_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
        
print("bot alive")
bot.run()
