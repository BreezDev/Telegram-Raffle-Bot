import telebot
import random
import pandas as pd
from collections import Counter


# Initialize the bot with your token
bot = telebot.TeleBot("YOUR_BOT_TOKEN")
admin_id = "your_telegram_user_id"


# A list to store user IDs of those who purchased a plan
raffle_participants = []


# add a user to the raffle with entries based on days purchased
def add_to_raffle(user_id, days):
    entries_to_add = days  # Number of entries based on days purchased
    raffle_participants.extend([user_id] * entries_to_add)  # Add the user multiple times based on days
    return f"You have been added to the raffle with {entries_to_add} entries!"


# trigger the raffle drawing (restricted to admin ID)
@bot.message_handler(commands=['draw_raffle'])
def draw_raffle(message):
    if message.from_user.id == admin_id:  # Only allow this command for your ID
        if raffle_participants:
            winner = random.choice(raffle_participants)
            bot.send_message(winner, "Congratulations! You've won the raffle!")
            bot.send_message(message.chat.id, f"The winner is: {winner}")
            # Optionally, clear the participants list after drawing
            raffle_participants.clear()
        else:
            bot.send_message(message.chat.id, "There are no participants in the raffle.")
    else:
        bot.send_message(message.chat.id, "You are not authorized to draw the raffle.")


# generate and send a CSV document with raffle stats
@bot.message_handler(commands=['raffle_stats'])
def raffle_stats(message):
    if not raffle_participants:
        bot.send_message(message.chat.id, "The raffle is currently empty. No entries to display.")
        return
    user_entries = Counter(raffle_participants)
    data = {
        "User ID": list(user_entries.keys()),
        "Entries": list(user_entries.values())
    }
    df = pd.DataFrame(data)
    csv_filename = "/tmp/raffle_stats.csv"
    df.to_csv(csv_filename, index=False)
    with open(csv_filename, 'rb') as file:
        bot.send_document(message.chat.id, file)


## This is where you should add your logic and include the amount of raffle_days that you want to add to a user
@bot.message_handler(commands=['buy_plan'])
def buy_plan(message):
    paid = 'yes'
    if paid == 'yes':
        raffle_days = 1
        response = add_to_raffle(message.from_user.id, raffle_days)
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Payment verification failed. Please try again.")



bot.polling()
