import typing
from discord.ext import commands
import discord
import json
from discord.ext.commands.errors import MessageNotFound, ChannelNotFound

__all__ = (  # type: ignore
    "DiscDB"
)


class DiscDB:
    """The main class of the module, which is used for storing data in a discord.Message object. It searches for the message in the cache of the bot, and if not found, would abort the operation
    """

    def __init__(
        self,
        bot: typing.Union[
            discord.Client,
            discord.AutoShardedClient,
            commands.Bot,
            commands.AutoShardedBot
            ]
    ) -> None:
        """The init method takes in only one positional argument, which is bot.

        Args:
            bot (discord.Client | discord.AutoShardedClient | commands.Bot | commands.AutoShardedBot): The commands.Bot or the discord.Client instance.
        """
        self.bot = bot
        self._msg: typing.Union[discord.Message, None] = None

    async def get_json(
        self,
        message_id: int,
        /,
        channel_id: int = None,
        fetch_msg: bool = False
    ) -> typing.Union[dict, None]:
        """The method to get the JSON data of the discord.Message contents

        Args:
            message_id (int): The ID of the message, in which the data is stored
            channel_id (int): The ID of the channel, in case the message is not found in the cache
            fetch_msg (bool): Wether to fetch the message in case it is not found in the cache

        Raises:
            MessageNotFound:
                -> The message ID is not valid
                -> The message is not found in the internal cache of the bot
            
            TypeError:
                -> The channel ID was not supplied

        Returns:
            dict | None:
                -> The method would return a dict if the message is found, with the JSON contents of the Message
                -> The method would return None if the message is not found
        """
        self._msg = self.bot._connection._get_message(message_id)
        if self._msg is None:
            if not fetch_msg:
                self._msg = None
            else:
                if not channel_id:
                    raise TypeError("You did not specify a channel id.")
                else:
                    channel: typing.Union[discord.DMChannel, discord.TextChannel, None] = self.bot.get_channel(channel_id)  # type: ignore
                    if not channel:
                        raise ChannelNotFound("The channel ID is either wrong, or the channel is not found in the bot's internal cache.")
                    else:
                        self._msg = await channel.fetch_message(message_id)
                    
        if isinstance(self._msg, discord.Message) or self._msg is not None:
            msg: dict = json.loads(self._msg.content)
            return msg
        elif not self._msg:
            raise MessageNotFound(
                    "The Message ID is either wrong, or the message is not found in the bot's internal cache.")

    async def save_json(
        self,
        new_dict: dict
    ) -> None:
        """THe method to save the JSON data to the discord.Message contents. Beware, it makes an API call.

        Args:
            new_dict (dict): The new dict, which will be saved to the message contents

        Raises:
            MessageNotFound:
                -> If the message ID is not valid
                -> If the message is not found in the internal cache of the bot
        """
        if self._msg is None:
            raise MessageNotFound(
                "The message ID is either wrong, or the message is not found in the bot's internal cache. Cannot proceed further, sorry")
        if isinstance(self._msg, discord.Message):
            new_json = json.dumps(new_dict, indent=4)
            await self._msg.edit(content=new_json)
