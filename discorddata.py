# This example requires the 'message_content' intent.
import json
import re

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

data = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(761059144253177866)
    messages = channel.history(limit=10000000000000000000)
    async for message in messages:
        print(message.content)
        emojis = re.findall(r'<:(\w*):\d*>', message.content)
        reactions = message.reactions
        data[message.author.name] = data.get(message.author.name, {})
        for reaction in reactions:
            try:
                emoji_id = str(reaction.emoji.name)
                async for user in reaction.users():
                    data[user.name] = data.get(user.name, {})
                    data[user.name][emoji_id] = data[user.name].get(emoji_id, {"reaction": 0, "message": 0})
                    data[user.name][emoji_id]["reaction"] += 1
            except:
                pass
        for emoji in emojis:
            emoji_id = str(emoji)
            data[message.author.name][emoji_id] = data[message.author.name].get(emoji_id, {"reaction": 0, "message": 0})
            data[message.author.name][emoji_id]["message"] += 1
    print(json.dumps(data))



client.run("ODgyMzI0MTM5NjE5Mjc4ODg4.G1Ln9i.mzpsT0RASr4sSH2V_A_rdLK-sgnQ37Nn1IVcfY")