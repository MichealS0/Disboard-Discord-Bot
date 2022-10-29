import discord
import discord.client
import random

TOKEN = 'MTAzNTQxODAzNDcyODM1MzgxMg.GpkF37.ah77qMMsw9le8oIsKXX5OHWSwplrlBnz5iBRvs'

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

def roast( memberToRoast):
    them =[]

    wantedFile = open("Disboard\Roasts.txt", encoding="utf8")
    lines = wantedFile.readlines()

    for line in lines:
        them.append(line)
        wantedFile.close()
    
    randomLine = random.randint(0, 58)
    wantedRoast = them[randomLine]

    roast.roasted = memberToRoast  + ", " + wantedRoast

def giveDadJoke():
    jokelist =[]

    jokeFile = open("Disboard\dadJokes.txt", encoding="utf8")
    lines = jokeFile.readlines()

    for line in lines:
        jokelist.append(line)
        jokeFile.close()
    
    randomJoke = random.randint(0, 144)
    x = jokelist[randomJoke]
    giveDadJoke.sendTheJoke = x

def giveknockjoke():
    knocklist =[]

    knockFile = open("Disboard\KnockKnockJokes.txt", encoding="utf8")
    knocks = knockFile.readlines()

    for line in knocks:
        knocklist.append(line)
        knockFile.close()
    
    randomknockJoke = random.randint(0, 47)
    q = knocklist[randomknockJoke]
    giveknockjoke.sendTheJoke = q

@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.author != client.user:
        if message.content.startswith("hello"):
            await message.channel.send(f'Hello, {message.author.display_name}!')
            return

        if message.content.startswith("/roast"):
            Command, memberToR = message.content.split()
            roast(memberToR)
            print(roast.roasted)
            await message.channel.send(roast.roasted)
        
        if message.content.startswith("/dadjoke"):
            giveDadJoke()
            print(giveDadJoke.sendTheJoke)
            await message.channel.send(giveDadJoke.sendTheJoke)

        thatsWhatSheSaid = ['long', 'big', 'put it in', 'in my mouth', '69', 'facial', 'blow', 'one night', 'so hard', 'long enough', 'cant get enough']

        for x in range(len(thatsWhatSheSaid)):
            if thatsWhatSheSaid[x] in message.content:
                await message.channel.send("That's what she said")
        
        if message.content.startswith("/knock knock"):
            giveknockjoke()
            await message.channel.send(giveknockjoke.sendTheJoke)
            print(giveknockjoke.sendTheJoke)
        
client.run(TOKEN)