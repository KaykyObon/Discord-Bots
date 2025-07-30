import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

    channel_name = input("Enter the exact name of the text channel you want to clean or delete: ")

    print("\nSelect an action:")
    print("1 - Clean messages from today")
    print("2 - Clean messages from the last 7 days")
    print("3 - Clean messages from the last 30 days")
    print("4 - Clean all messages")
    print("5 - Delete the entire channel")
    action = input("> ")

    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if channel:
            if action == "5":
                confirm = input(f"Are you sure you want to DELETE the channel '{channel.name}'? (y/n): ")
                if confirm.lower() == "y":
                    await channel.delete()
                    print(f"Channel '{channel.name}' has been deleted.")
                else:
                    print("Operation canceled.")
                await bot.close()
                return
            else:
                print(f"Cleaning channel: {channel.name}")
                await clean_messages(channel, action)
                break
    else:
        print("Channel not found.")

    await bot.close()

async def clean_messages(channel, option):
    from datetime import timezone
    now = datetime.now(timezone.utc)

    if option == "1":
        cutoff = now - timedelta(days=1)
    elif option == "2":
        cutoff = now - timedelta(days=7)
    elif option == "3":
        cutoff = now - timedelta(days=30)
    elif option == "4":
        cutoff = None
    else:
        print("Invalid option.")
        return

    def check(m):
        return True if cutoff is None else m.created_at >= cutoff

    deleted = await channel.purge(limit=1000, check=check)
    print(f"{len(deleted)} messages deleted.")

if __name__ == "__main__":
    token = input("Enter your bot token: ")
    try:
        bot.run(token)
    except Exception as e:
        print(f"Failed to start the bot: {e}")

