# Telegram Raffle Bot

A Telegram bot for running raffles with multiple entry options. This bot allows users to be added to a raffle based on the number of days purchased and supports admin-only commands for drawing a winner and viewing raffle statistics.

## Features
- **Add Users to Raffle**: Users can buy a plan with entries based on days purchased.
- **Draw a Raffle Winner**: Admin-only command to randomly select a winner from participants.
- **View Raffle Stats**: Admin-only command to generate and send a CSV of participants and their entries.

## Setup

1. Clone this repository.
2. Install required packages:
   
   ```bash
   pip install pytelegrambotapi pandas
3. Replace the placeholder values in bot = telebot.TeleBot("YOUR_BOT_TOKEN") and admin_id = "your_telegram_user_id" with your Telegram bot token and your admin user ID.
4. Run the bot:
      
   ```bash
   pip install pytelegrambotapi pandas

## Commands

### `/buy_plan`
Simulate a purchase to add a user to the raffle.

- **Admin**: Not required
- **Usage**: User sends the command `/buy_plan`
- **Description**: When a user purchases a plan (simulated here), they’re added to the raffle with a set number of entries (`raffle_days`).

### `/draw_raffle`
Draw a random winner from the list of raffle participants. Restricted to the admin ID.

- **Admin**: Required
- **Usage**: Admin sends the command `/draw_raffle`
- **Description**: Randomly selects a winner and sends them a congratulatory message.

### `/raffle_stats`
Generate a CSV file showing all participants and their number of entries, and send it to the admin.

- **Admin**: Required
- **Usage**: Admin sends the command `/raffle_stats`
- **Description**: Creates a CSV file listing each user and the number of raffle entries they have, then sends it to the admin.
