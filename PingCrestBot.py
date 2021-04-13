import discord
import time
from RedditClientInfo import Login
from BotCommands import Commands
import random
almond_message = False
TOKEN = "Nzk1NzgyMjYyOTM4Nzk2MTEy.X_OX_A.ONxDJa0APN4zTT1Jrk6L7NosFnQ"
reddit_client  = Login.LoginReddit()
copypasta_posts = reddit_client.subreddit('copypasta').hot(limit=20)
# for post in copypasta_posts:
#     print(post.selftext.encode("utf-8"))

intents = discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_voice_state_update(member, before, after):
    for guild in client.guilds:
        if almond_message == False:
            channel = discord.utils.get(guild.channels, name="general")
            channel_id  = channel.id
            channel = client.get_channel(channel_id)
            if member.name == "Rena":
                almond_message =  await Commands.TagAlmondWithRandomFeetPic(member, channel)


@client.event
async def on_message(message):
    if message.author.id != None:
        await Commands.ShitOnTofu(message)
    if message.content[-1] == '?':
        #await Commands.DeeNutsJokes(message)
        #await Commands.RandomCopyPastaRespone(reddit_client, message).
        pass
    if message.content.startswith('!a_bit'):
        await Commands.PingCrest(message)
    if message.content.startswith("!lmao_tofu_internet"):
        await Commands.TofuInternet(message)
    if message.content.isupper():
        await Commands.SarcasticResponse(message)
    if message.content.startswith("!pyramid"):
        await Commands.Pyramid(message)

@client.event
async def on_ready():
    channel_id = None
    channel = None
    for guild in client.guilds:

        if discord.utils.get(guild.channels, name="general") != None:
            channel = discord.utils.get(guild.channels, name="general")
        else:
            channel = discord.utils.get(guild.channels, name="bot")
        channel_id = channel.id
        x = client.get_channel(channel_id)
        #await x.send("Hello i am PingCrestBot!\nUse the following command to ping crest bap\n!a_bit  [number_of_second] [number_of_time_you_want_to_ping_crest]\n got a problem with tofu's internt? no worrie use the following command !lmao_tofu_internet")
client.run(TOKEN)
