import typing
from discord.ext import commands
import discord
import json
from discord.ext.commands.errors import MessageNotFound

__all__ = (
    "DiscDB"
)


class DiscDB:
    """The main class of the module, which is used for storing data in a discord.Message object. It searches for the message in the cache of the bot, and if not found, would abort the operation
    """

    def __init__(self, bot: typing.Union[discord.Client, discord.AutoShardedClient, commands.Bot, commands.AutoShardedBot]) -> None:
        """The init method takes in only one positional argument, which is bot.

        Args:
            bot (discord.Client | discord.AutoShardedClient | commands.Bot | commands.AutoShardedBot): The commands.Bot or the discord.Client instance.
        """
        self.bot = bot
        self.msg = None

    def get_json(self, message_id: int) -> typing.Union[dict, None]:
        """The method to get the JSON data of the discord.Message contents

        Args:
            message_id (int): The ID of the message, in which the data is stored

        Raises:
            MessageNotFound: 
                -> If the message ID is not valid
                -> If the message is not found in the internal cache of the bot

        Returns:
            dict | None: 
                -> The method would return a dict if the message is found, with the JSON contents of the Message
                -> The method would return None if the message is not found 
        """
        self.msg = self.bot._connection._get_message(message_id)
        if self.msg is None:
            raise MessageNotFound(
                "The message ID is either wrong, or the message is not found in the bot's internal cache. Cannot proceed further, sorry")
        if isinstance(self.msg, discord.Message) or self.msg is not None:
            msg: dict = json.loads(self.msg.content)
            return msg

    async def save_json(self, new_dict: dict) -> None:
        """THe method to save the JSON data to the discord.Message contents. Beware, it makes an API call.

        Args:
            new_dict (dict): The new dict, which will be saved to the message contents

        Raises:
            MessageNotFound:
                -> If the message ID is not valid
                -> If the message is not found in the internal cache of the bot
        """
        if self.msg is None:
            raise MessageNotFound(
                "The message ID is either wrong, or the message is not found in the bot's internal cache. Cannot proceed further, sorry")
        if isinstance(self.msg, discord.Message) or self.msg is not None:
            new_json = json.dumps(content=new_dict, indent=4)
            await self.msg.edit(content=new_json)
