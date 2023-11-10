from typing import List
from textbase import bot, Message
from textbase.models import OpenAI

# Load your OpenAI API key (if using OpenAI, else feel free to experiment with whatever you need)
OpenAI.api_key = ""

SYSTEM_PROMPT = """Put prompt to configure the behaviour of your GPT-4 or anyother kind of bot.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate responses from the bot (refer to examples in documentation)
    # Use any other kind of logic/integration you want.
    bot_response = ""

    return {
        "messages": [bot_response],
        "state": state
    }