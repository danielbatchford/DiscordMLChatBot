from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

import discord


class ChatHandler():

    bot = None

    def __init__(self):
        self.bot = ChatBot(
            "Bot",
        preprocessors = [
            "chatterbot.preprocessors.clean_whitespace",
            "chatterbot.preprocessors.convert_to_ascii",
        ],
            logic_adapters = [
                "chatterbot.logic.BestMatch",
                "chatterbot.logic.TimeLogicAdapter",
                "chatterbot.logic.MathematicalEvaluation",

            ]
        )
        print("Initialised Bot")

    def get_response(self, message):
        return self.bot.get_response(message)

    def train(self, file_name):
        with open(file_name) as file:

            print("Reading data from file {}".format(file_name))
            data = file.read()
            print("Successfully Read Data from file {}".format(file_name))

        if len(data) % 2 == 1:
            raise Exception("Data was of odd length")

        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )
        print("Trained client on English corpus")

        trainer = ListTrainer(self.bot)
        trainer.train(data)
        print("Trained client on custom data source")




