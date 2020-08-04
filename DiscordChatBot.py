from chatterbot import ChatBot
import discord

class DiscordChatBot():

    BOT_NAME = "BOT"
    bot = ChatBot(BOT_NAME)
    chat_data = []
    ctx = None

    def __init__(self, ctx):
        self.ctx = ctx


    def get_discord_chats(self):
        chat_data = None


    def train(self):
        trainer = ListTrainer(bot)
        trainer.train(chat_data)


    def get_response(self, message):
        return self.bot.get_response(message)
