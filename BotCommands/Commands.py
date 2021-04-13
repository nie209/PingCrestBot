import discord
from os import listdir
import random
import time
async def PingCrest(message):
    # ping the author as well but not right away  whenever they use the command
    crest_id = None
    msg_list = message.content.split(" ")
    time_interval = int(msg_list[1])
    often = int(msg_list[2])
    if (time_interval == 1 and often > 2):
        await message.channel.send("chill the fuck out god")
    elif (often > 100 ):
        await message.channel.send("get a life loser")
    else:
        m = message.guild.members
        for x in m:
            if x.name == "Crest":
                crest_id = x.id
        for i in range(often):
            await message.channel.send("<@{}>".format(crest_id))
            time.sleep(time_interval)

async def ShitOnTofu(message):
    tofu_id = None
    random_int = random.randint(1,10)
    if random_int > 8:
        if message.author.id != None:
            members_list =  message.guild.members
            for x in members_list:
                if x.name == "OG Tofu":
                    tofu_id = x.id
            if  message.author.id == tofu_id:
                await message.channel.send("your mom gotem lmao")

async def TofuInternet(message):
    tofu_id = None
    copy_pasta = "I Spectrum sexually identify as an Internet Service Provider. Ever since I was a boy I dreamed of disappointing customers all around the nation and charging them an unnecessary high fee. People say to me that a person being an ISP is impossible and I'm fucking retarded, but I don't care, I'm 300GBps fast. I'm having a technician installing Ethernet cables, Optic Fiber cables and a Wi-Fi antenna on my body. From now on, I want you guys to call me \"Disgusting Greedy Company\" and respect my right to give Internet to everybody and not to fix the problems they have with my connection. If you can't accept me you are an ISP-phobe and need to check your sysadmin privileges. Thank you for being so understanding."
    members_list =  message.guild.members
    for x in members_list:
        if x.name == "OG Tofu":
            tofu_id = x.id
    await message.channel.send("Hello <@{}> ".format(tofu_id) + copy_pasta)


async def TagAlmondWithRandomFeetPic(member, channel):
    # there are total of total of 5 feet pic in the folder
    almond_id  = member.id
    random_int = random.randint(0,4)
    image_list = []
    path = 'C:\\Users\wilson\\Desktop\\PingCrestBot\\BotCommands\\feet\\'
    for f in listdir(path):
        image_list.append(f)
    image = discord.File(path+image_list[random_int])
    await channel.send("<@{}> where is my feet pic".format(almond_id),file=image)
    return True
# async def StoreIsCloseLmao():
#     pass

async def DeeNutsJokes(message):
    chance  =  random.randint(1,10)
    if chance > 8:
        if message.content[-1] == '?':
            msg_list = message.content.split(' ')
            last_word = None
            if msg_list[-1] != '?':
                ## check the last character is a ? if so removed it otherwise keep the whole word
                last_word = msg_list[-1]
                if last_word[-1] == '?':
                    last_word = last_word[:-1]

            else:
                last_word = msg_list[-2]
            await message.channel.send(last_word + " dee nuts lmao gotem")


async def RandomCopyPastaRespone(reddit_client, message):
    text = []
    copypasta_posts = reddit_client.subreddit('copypasta').top(limit=100)
    for post in copypasta_posts:
        if len(post.selftext.encode("utf-8")) < 1000 and len(post.selftext.encode("utf-8")) != 0 :
            text.append(post.selftext.encode("utf-8"))
    await message.channel.send(text[1])


async def SarcasticResponse(message):
    chance  =  random.randint(1,10)
    random_int = random.randint(0,4)
    msg_string  = message.content
    respone = ""
    if chance > 8:
        for i in range(len(msg_string)):
            c  = None
            random_int = random.randint(1,10)
            if random_int <= 5:
                c = msg_string[i].lower()
            else:
                c  = msg_string[i]
            respone = respone + c
        await message.channel.send(respone)

async def Pyramid(message):
    msg_list = message.content.split(" ")
    num = int(msg_list[1])
    if num < 20:
        for i in range(num, 0, -1):
            msg = ""
            for j in range(i, 0, -1):
                msg = msg + "?"
            await message.channel.send(msg)
    else:
        await message.channel.send("fuck u")
