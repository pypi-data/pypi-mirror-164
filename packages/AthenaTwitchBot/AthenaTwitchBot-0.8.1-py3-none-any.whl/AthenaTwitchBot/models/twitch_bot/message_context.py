# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaTwitchBot.data.message_flags import MessageFlags
from AthenaTwitchBot.models.twitch_bot.message_tags import MessageTags
from AthenaTwitchBot.models.twitch_channel import TwitchChannel
from AthenaTwitchBot.models.twitch_user import TwitchUser

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class MessageContext:
    raw_input:bytearray=None
    raw_input_decoded:str=None
    raw_input_decoded_split:list[str]=None
    chat_message:tuple[str]=None
    flag:MessageFlags=MessageFlags.undefined
    output:str=None
    _tags:MessageTags=None
    _channel:TwitchChannel=None
    _user:TwitchUser=None
    rate_limited:bool=False

    def __post_init__(self):
        if self.raw_input is not None:
            self.raw_input_decoded = self.raw_input.decode("utf_8")
            self.raw_input_decoded_split = self.raw_input_decoded.split(" ")

    # ------------------------------------------------------------------------------------------------------------------
    # - Properties -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, value:str):
        if value is not None:
            self._tags = MessageTags.new_from_tags_str(value)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def channel(self):
        return self._channel
    @channel.setter
    def channel(self, value:str):
        self._channel = TwitchChannel(value)
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value:str):
        self._user = TwitchUser(value)

    # ------------------------------------------------------------------------------------------------------------------
    # - Special methods -
    # ------------------------------------------------------------------------------------------------------------------
    def write(self,output: str):
        self.output = output
        self.flag = MessageFlags.write

    def reply(self, output: str):
        if self.raw_input is None: # which means the context was probably created in a task or something like it
            raise ValueError(
                "This context was not created as a reponse to a chat message and therefor can't reply to anything"
            )

        self.output = output
        self.flag= MessageFlags.reply