# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaTwitchBot.data.message_flags import MessageFlags
from AthenaTwitchBot.models.twitch_bot.outputs.output import Output
from AthenaTwitchBot.models.twitch_bot.message_context import MessageContext

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputConsole(Output):
    # noinspection PyMethodOverriding
    async def output(self, context:MessageContext,**_):
        if context.flag == MessageFlags.no_output:
            return
        elif context.raw_input_decoded is not None:
            print(context.raw_input_decoded)