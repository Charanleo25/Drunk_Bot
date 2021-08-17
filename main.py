import discord
import os
import requests
import json
import random
import keep_alive
import time
import urllib
import environ
import sys
#import main4.py
from discord.ext import commands
import aiohttp
import asyncio

#token = os.environ.get('TOKEN')

intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

'''
    member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)
'''


#client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry","miserable","die","kill","crying","waste","not working"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

drunk_list = ['Yes','No','Maybe','Nah','Yea','Are you serious','I dont want to hear this','What! LoL','Am i dumb','bluh bluh','Are you mad','God!','Am i drunk','Are you drunk','I doubt','Smells nothing','Who cares','Its mean','Cool but no','Is it true','Its hard','Going to sereach','Felt dumb','Oh! no','blah blah','let my soul on rest']
t_t_h=['.tth','.txt-hand','.ttoh']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_joke():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  #data=json_data
  return(json_data)
  
def get_answer():
   rando_var = random.choice(drunk_list)
   return(rando_var)

def t_to_h(string: str, save_to: str = "pywhatkit.png", rgb: list = (0, 0, 138)) -> None:
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()
    return(data)


    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    while 1:
        urllib.request.urlopen("https://NiftyLightcyanRegister.charanleo.repl.co")
        await asyncio.sleep(500)

        # await client.change_presence(activity=discord.Game(name="|Drunken HOT,bot..."))
    # asyncio.gather(send_count())

@client.event
async def on_message(message):

    if message.content.startswith('.du'):
        # if not member: # if member is no mentioned
        #     member = ctx.message.author # set member as the author
        
        userAvatar = client.avatar_url
        await message.channel.send(userAvatar)


    if message.author == client.user:
        #await message.channel.send('hi boss')
        return
    msg = message.content
    
    if message.content.startswith('.hey'):
      #await message.channel.send(file=discord.File("cb.jpg"))
      print(type(message.author))
      user_is=str(message.author)
      print(user_is)
      print(type(user_is))
      await message.channel.send('hi...')
      #await message.channel.send(message.author)
      if user_is == 'charanleo25#1070':
        await message.channel.send('Yes Boss!')
         
    if message.content.startswith('.sleep'):
        user_is=str(message.author)

        await message.channel.send('Are you my boss?')
        if user_is == 'charanleo25#1070':
          await message.channel.send('its sad.. bye..')
          sys.exit()

    if message.content.startswith('.qt'):
        quote = get_quote()
        embed = discord.Embed(title="Wonder thoughts", color=discord.Color.red())
        #embed.set_image(url=imgdat)
        embed.add_field(name="Tada! ", value=quote, inline=False)
        #footie='try once more, there is lot!'
        #embed.set_footer(footie)
        await message.channel.send(embed=embed)

        #await message.channel.send(quote)

    if message.content.startswith('.ask'):
        reply = get_answer()
        await message.channel.send(reply)
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('.joke'):
        joke = get_joke()
        print(joke['nsfw'])
        print(joke['url'])
        imgdat=joke['url']
        #await message.channel.send("```")
        #await message.channel.send(joke['url'])
        embed = discord.Embed(title="MeMe!", color=discord.Color.purple())
        embed.set_image(url=imgdat)
        embed.set_footer(text="Hello amigos its A Meme!")
        await message.channel.send(embed=embed)

      
        #await message.channel.send("```")

    

    if any(word in msg for word in t_t_h):
        word=msg[5:]
        t_to_h(word,"png/pywhatkit.png")
        await message.channel.send(file=discord.File('png/pywhatkit.png'))
        os.remove('png/pywhatkit.png')

    if message.content.startswith('.reptxt'):
        word=msg
        dlist = word.split()
        x = word[7:-2]
        y = int(dlist[-1])
        await message.channel.send(x*y) 

#     # if message.content == '.ping':
# User.avatar_url
# User.avatar_url_as
# ClientUser.avatar_url
# ClientUser.avatar_url_as
# User.default_avatar_url
# ClientUser.default_avatar_url

    #         await message.channel.send(f'Client Latency: {round(self.bot.latency * 1000)}')   
    

    if message.content.startswith('.rip'):
       #cP = client.get_user(message.author)
       #avatar = cP.avatar_url
       # print(avatar)
      #  member = ctx.message.author 
      #  set member as the author
      #  userAvatar = member.avatar_url
      #  await ctx.send(userAvatar)
       await message.reply('Hi', mention_author=True)


    if message.content.startswith('.rep'):
        channel = message.channel
        await channel.send('Say "what" ')

        def check(m):
            return m.content == 'what' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await message.reply('Go Home kid {.author}!'.format(msg),mention_author=False)
    
    if message.content.startswith('.guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))


    if message.content.startswith('.thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

newUserDMMessage = "Welcome DM"


@client.event
async def on_member_join(member):

  await member.guild.system_channel.send(f"""Hello {member.mention.avatar_url} and Thanks for joining!""")
    # await member.create_dm()
    # # await member.dm_channel.send(
    # #     f'Hi {member.name}, welcome to my Discord server!'
    # # )
    
    # embed = discord.Embed(title=member.name,color=discord.Color.purple())
    # embed.set_image(url="https://st.depositphotos.com/1358237/3469/v/950/depositphotos_34691767-stock-illustration-happy.jpg")
    # embed.set_footer(text="thanks for joining!")
    # await member.dm_channel.send(embed=embed)


        
    # async with aiohttp.ClientSession() as wastedSession:
    #     async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') 

keep_alive.keep_alive()

Token = "--------------------------------------------------" #token id of the bot

client.run(Token) 
