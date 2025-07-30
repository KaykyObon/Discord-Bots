# Discord Message Cleaner Bot

This bot is designed to clean or delete messages from a specified Discord text channel, or delete the channel itself. It runs via command line and prompts the user to choose the desired action at runtime.

## Features

* Clean messages from:

  * Today
  * The last 7 days
  * The last 30 days
  * All messages
* Option to delete the entire text channel
* Interactive terminal input
* Requires bot token input on startup

---

## Prerequisites

* Python 3.7 or higher
* A Discord bot created in the [Discord Developer Portal](https://discord.com/developers/applications)
* The following bot permissions:

  * View Channels
  * Read Message History
  * Manage Messages
  * Manage Channels
* The following privileged intent must be enabled in the Discord Developer Portal:

  * **Message Content Intent**

---

## Setup

1. Clone the repository or download the script.

2. Navigate to the project directory:

   ```bash
   cd your-project-directory
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. Install the required package:

   ```bash
   pip install discord.py
   ```

---

## Running the Bot

1. Execute the script:

   ```bash
   python bot.py
   ```

2. You will be prompted to enter your bot token:

   ```
   Enter your bot token:
   ```

3. Then, you will be asked for the name of the text channel you want to operate on:

   ```
   Enter the exact name of the text channel you want to clean or delete:
   ```

4. Finally, choose one of the following actions:

   ```
   1 - Clean messages from today
   2 - Clean messages from the last 7 days
   3 - Clean messages from the last 30 days
   4 - Clean all messages
   5 - Delete the entire channel
   ```

5. The bot will execute the action and shut down once complete.

---

## Notes

* This bot must be invited to the server with the appropriate permissions.
* Message deletion uses the `purge()` method, which can only delete messages sent within the last 14 days (Discord limitation).
* The channel name must be typed exactly as it appears in Discord.

---

## License

This project is licensed for personal or educational use. Use responsibly in compliance with Discord's Terms of Service.
