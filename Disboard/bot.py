from wsgiref import headers
import discord
import discord.client
import random
import pandas as pd
from tabulate import tabulate

TOKEN = 'MTAzNTQxODAzNDcyODM1MzgxMg.GOdvwQ.j4pk8cGOz7h2jANrFx3ZGHrNzUZhcELK8gyNQo'

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

def givedarkjoke():
    darklist =[]

    darkFile = open("Disboard\darkJokes.txt", encoding="utf8")
    darks = darkFile.readlines()

    for line in darks:
        darklist.append(line)
        darkFile.close()
    
    randomdarkJoke = random.randint(0, 33)
    qq = darklist[randomdarkJoke]
    givedarkjoke.sendTheJoke = qq

def giveratherjoke():
    ratherlist =[]

    ratherFile = open("Disboard\Jrather.txt", encoding="utf8")
    darks = ratherFile.readlines()

    for line in darks:
        ratherlist.append(line)
        ratherFile.close()
    
    randomratherJoke = random.randint(0, 147)
    r = ratherlist[randomratherJoke]
    giveratherjoke.sendTheJoke = r

def getThumbnail():
    thumbnaillist =[]

    thumbnailFile = open("Disboard\Thumbnails.txt", encoding="utf8")
    darks = thumbnailFile.readlines()

    for line in darks:
        thumbnaillist.append(line)
        thumbnailFile.close()
    
    randomthumbnail = random.randint(0, 2)
    r = thumbnaillist[randomthumbnail]
    getThumbnail.sendTheJoke = r

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

        if message.content.startswith("/darkjoke"):
            givedarkjoke()
            print(givedarkjoke.sendTheJoke)
            await message.channel.send(givedarkjoke.sendTheJoke)

        thatsWhatSheSaid = ['long', 'big', 'put it in', 'in my mouth', '69', 'facial', 'blow', 'one night', 'so hard', 'long enough', 'cant get enough']

        for x in range(len(thatsWhatSheSaid)):
            if thatsWhatSheSaid[x] in message.content:
                await message.channel.send("That's what she said")
        
        if message.content.startswith("/knock knock"):
            giveknockjoke()
            await message.channel.send(giveknockjoke.sendTheJoke)
            print(giveknockjoke.sendTheJoke)

        if message.content.startswith("/fifa23player"):

            FifaPlayersDB = pd.read_csv('Disboard\players_fifa23.csv', usecols=["Name", "FullName", "Age", "Nationality", "Overall"])

            playertosearch = message.content[13:len(message.content)]
            print(type(playertosearch), playertosearch)

            data = FifaPlayersDB[(FifaPlayersDB["Name"] == playertosearch.strip())]
            await message.channel.send(tabulate(FifaPlayersDB[(FifaPlayersDB["Name"] == playertosearch.strip())], headers=["Name", "FullName", "Age", "Nationality", "Overall"], tablefmt="pretty", showindex=False))
            
        if message.content.startswith("/rather"):
            giveratherjoke()
            getThumbnail();

            thumbna = "https://i.imgur.com/4mj7bDz.gif"
            embed=discord.Embed(title="Would you rather statement", description=giveratherjoke.sendTheJoke, color=0xFF5733)
            embed.set_author(name="Disboard", icon_url="https://i.imgur.com/3ltbVie.jpeg")
            embed.set_thumbnail(url=getThumbnail.sendTheJoke)
            print(embed)
            
            await message.channel.send(embed=embed)

client.run(TOKEN)