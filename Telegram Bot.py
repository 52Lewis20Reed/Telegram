from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import re
import random
import datetime
import random



TOKEN = '5899803591:AAEQj2g_6DI_ArHLiXb0ZtwTGRmKjrL4S34'
chat_ids = set()



def send_initial_message(update, context):
    if update.message.chat.type == 'group':
        context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm here and ready to engage.")

def reply_to_message(update, context):
    message = update.message.text.lower()
    username = update.message.from_user.username  # Retrieving the username
    
    if 'hate' in message and 'job' in message:
        # Quote the message and respond
        quoted_message = f'"{update.message.text}"'
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Apply for a new job, Mamal Sandusky. You said: {quoted_message}")
    

    if message.startswith('why'):
        responses = [
            "I'm not sure. Find out yourself.",
            "You could search for that.",
            "That's for you to explore.",
            "I don't know, Google it.",
            "It's a mystery to me.",
            "Because you didn't search it."
        ]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)
        
    if message.startswith('when'):
        responses = [
            "Tomorrow",
            "Idk, soon",
            "That's for you to explore.",
            "2 weeks from now",
            "Next year",
            "Next month."
        ]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)
        
    if 'you know' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text= "No, I don't know that")
        
    if 'thot' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text= "Yo momma a thot!")
        
    if 'soggy' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text= "Yo momma soggy")
        
    if 'wet' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text= "Wet like yo momma!")

    if 'milk'in message:
        context.bot.send_message(chat_id=update.message.chat_id, text= "I milked yo momma!")

    elif message.startswith('how'):
        responses = [
            "Figure it out yourself.",
            "Research and find the answer.",
            "Explore and learn about it.",
            "Try Googling it.",
            "It's a mystery.",
            "Because you haven't sought it out."
        ]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)

    elif 'feel' in message:
        custom_responses = [
            "I sense you're feeling something interesting.",
            "Feelings are quite complex, aren't they?",
            "How do you feel about that?",
            "No one cares"
        ]
        chosen_custom_response = random.choice(custom_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_custom_response)
        
        

    elif 'funny' in message:
        custom_responses = [
            "Wow hahaha so funny!"
        ]
        chosen_custom_response = random.choice(custom_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_custom_response)

    if 'broke' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text="Not as broke as Team Fatol")
        
    if 'nothing' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text="I DINDU NUFFIN!!")
        
    if 'AI' in message:
        random_year = datetime.date.today().year + random.randint(5, 10)
        responses = [
        f"AI might take my job, but it can't take my charisma! -{username}, {random_year}",
        f"I'll be here long after you're gone, AI! -{username}, {random_year}",
        f"AI? More like Almost Intuitive! -{username}, {random_year}",
        f"AI? Please, I've got more personality in my code! -{username}, {random_year}"
        ]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)

    if 'i need' in message:
        context.bot.send_message(chat_id=update.message.chat_id, text="Naw you need a THUG in yo life if bustas ain't loving you right!")
    
    if 'man' in message and len(message) == 3:  # Checking for the standalone word "man"
        responses = ["MAN WHAT", "Bear", "MAAAAAAN", "Woman (something Fatol will never have)","Woman"]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)  
        
    if 'Stfu' in message and len(message) == 4:  # Checking for the standalone word "man"
        responses = ["No, YOU shut the fuck up, idiot", "K", "No"]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)  
        
    
    if 'pig' in message and len(message) == 3:  # Checking for the standalone word "man"
        context.bot.send_message(chat_id=update.message.chat_id, text="LETS GOOOO! *DUNKS ON FATOL*")
        
    if 'lol' in message and len(message) == 3:
        responses = ["Did that truly make you laugh out loud?",
        "Is your laughter audible enough for the entire neighborhood?",
        "Laughing out loud, are we? Or just breathing a little harder?",
        "LOLOLOLOL!",
        "You've reached peak laughter, congratulations!"]
        chosen_response = random.choice(responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)

    pattern = r'\b(?:should|would|could)\b'
    if re.search(pattern, message):
        context.bot.send_message(chat_id=update.message.chat_id, text="shoulda woulda coulda")
        
    if 'dolphins' in message:
        last_playoff_win_date = datetime.date(2000, 12, 30)  # Replace this with the actual date
        current_date = datetime.date.today()
        days_since_last_win = (current_date - last_playoff_win_date).days

        context.bot.send_message(chat_id=update.message.chat_id, text=f"It's been {days_since_last_win} days since the Dolphins last won a playoff game.")
    
    if 'sorry' in message:
        snarky_responses = [
            "Apologies won't fix everything. #FUCKFATOL",
            "Sorry seems to be the hardest word.",
            "Save your apologies for rainy days."
        ]
        chosen_response = random.choice(snarky_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)

    if 'mistake' in message:
        snarky_responses = [
            "Yeah it was a mistake alright, just like the birth of Fatol"
            "Mistakes are just experiences in disguise.",
            "Welcome to the 'Oops' club!",
            "Mistakes are just innovative discoveries."
        ]
        chosen_response = random.choice(snarky_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)

    if 'stupid' in message:
        snarky_responses = [
            "Stupidity is the ultimate wisdom in disguise.",
            "Welcome to the 'Captain Obvious' club!",
            "Only geniuses know the value of 'stupid.'"
        ]
        chosen_response = random.choice(snarky_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_response)
        
    if 'bot' in message:
        snarky_responses = [
            "Bot? I'm more of a digital genius, thank you.",
            "Who are you calling a 'bot'? Faggot",
            "Bot? I prefer the term 'digital prodigy.'",
            "Did someone say 'bot'? That's so 2000s!",
            "Bot? More like your digital wiz!",
            "You can fuck around and find out how nasty I get"
            # Add more snarky responses as needed
        ]
        chosen_snarky_response = random.choice(snarky_responses)
        context.bot.send_message(chat_id=update.message.chat_id, text=chosen_snarky_response)
        
    if len(message) > 300:
        # Create a mocking message with alternating capital and lowercase letters
        mocked_message = ''.join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(message)
        )
        context.bot.send_message(chat_id=update.message.chat_id, text=mocked_message)
    


def collect_group_chats(update, context):
    chat_id = update.message.chat_id
    if chat_id not in chat_ids and update.message.chat.type == 'group':
        chat_ids.add(chat_id)
        context.bot.send_message(chat_id=chat_id, text="I'm here and ready to engage.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & (Filters.group | Filters.private), reply_to_message))
    dp.add_handler(CommandHandler("start", send_initial_message))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, collect_group_chats))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
