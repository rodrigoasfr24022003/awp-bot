# This example requires the 'message_content' intent.

import os
import random as r
import pygame
import numpy as np
import discord
import asyncio
import colorsys as csys
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

one='1\u20e3'
two='2\u20e3'
three='3\u20e3'

@client.event
async def on_message(message):
    if message.author.id == 1210515998332035092 and message.channel.id==795123441497145364 and 'AWP' in message.content and 'of the Week' not in message.content:
        await asyncio.sleep(1)
        await message.add_reaction(one)
        await asyncio.sleep(1)
        await message.add_reaction(two)
        await asyncio.sleep(1)
        await message.add_reaction(three)
    elif message.author.id == 1210515998332035092 and message.channel.id==1259185944825958540 and 'BWP' in message.content and 'of the Week' not in message.content:
        await asyncio.sleep(1)
        await message.add_reaction(one)
        await asyncio.sleep(1)
        await message.add_reaction(two)
        await asyncio.sleep(1)
        await message.add_reaction(three)

@tree.command(name="rng", description="RobTop's RNG, partially ported to this bot.", guild=discord.Object(id=715141595153956904))
async def rng(interaction):
    coinlist=['Heads','Tails']
    coin=r.choice(coinlist)
    rpslist=['Rock','Paper','Scissors']
    rps=r.choice(rpslist)
    dicelist=[1,2,3,4,5,6]
    dice=r.choice(dicelist)
    cardnumberlist=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    carddecklist=['Clubs','Spades','Diamonds','Hearts']
    jokerlist=[True,False]
    isjoker=r.choices(jokerlist, weights=[4,52],k=1)[0]
    if isjoker==False:
        cardnumber=r.choice(cardnumberlist)
        carddeck=r.choice(carddecklist)
        cardstring='Card: '+str(cardnumber)+ ' of '+str(carddeck)
    else:
        cardstring='Card: Joker'
    red=r.randint(0,255)
    green=r.randint(0,255)
    blue=r.randint(0,255)
    if red<16:
        red_h='0'+hex(red).replace('0x','')
    else:
        red_h = hex(red).replace('0x', '')
    if green<16:
        green_h='0'+hex(green).replace('0x','')
    else:
        green_h = hex(green).replace('0x', '')
    if blue<16:
        blue_h='0'+hex(blue).replace('0x','')
    else:
        blue_h=hex(blue).replace('0x','')
    char_amount=r.randint(4,8)
    letterString='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters=r.sample(letterString,char_amount)
    lettersOut=''
    for i in letters:
        lettersOut=lettersOut+i
    piglinList=['8-16 Blackstone', '8-16 Gravel', '6-12 Spectral Arrows', '2-8 Nether Brick', '2-8 Soul Sand', '2-4 Leather', '1 Fire Charge', '1-3 Crying Obsidian', '1 Obsidian', '5-12 Nether Quartz', '3-9 String', '2-4 Ender Pearls', '10-36 Iron Nuggets', '1 Water Bottle', '1 Fire Resistance Potion', '1 Splash Fire Resistance Potion', '1 Set of Soul Speed Iron Boots', '1 Soul Speed Enchanted Book']
    piglinBarter=r.choices(piglinList, weights=[40/459,40/459,40/459,40/459,40/459,40/459,40/459,40/459,40/459,20/459,20/459,10/459,10/459,10/459,8/459,8/459,8/459,5/459],k=1)[0]
    embed=discord.Embed(colour=discord.Colour.from_str('#'+red_h+green_h+blue_h))
    embed.add_field(name='Output', value='Coin: '+str(coin)+'\n'+'RPS: '+str(rps)+'\n'+'Dice: '+str(dice)+'\n'+cardstring+'\n'+'Color: #'+red_h+green_h+blue_h+'\n'+'Letters: '+lettersOut+'\n'+'Piglin: '+piglinBarter+'\n'+str(r.randint(1,10))+'/10'+' | '+str(r.randint(1,100))+'/100'+' | '+str(r.randint(1,1000))+'/1000'+' | '+str(r.randint(1,1000000))+'/1000000',inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name="hexgrid", description="Generates a n x n grid of hex codes with their respecitve colors as BG", guild=discord.Object(id=715141595153956904))
@app_commands.describe(size_x="Width of the grid, integer 1-11")
@app_commands.describe(size_y="Height of the grid, integer 1-11")
async def hexgrid(interaction, size_x:int, size_y:int):
    white=(255,255,255)
    black=(0,0,0)
    colors_x=size_x
    colors_y=size_y
    endpoints_x=np.linspace(0,720,colors_x+1)
    endpoints_y=np.linspace(0,720,colors_y+1)
    pygame.init()
    screen=pygame.display.set_mode((720,720))
    screen.fill(white)
    font=pygame.font.Font('C:/Users/rodri/AWP-Bot/Ubuntu-R.ttf',int(120/max(colors_x,colors_y)))
    for x in range(colors_x):
        for y in range(colors_y):
            color=(r.randint(0,255),r.randint(0,255),r.randint(0,255))
            pygame.draw.rect(screen, color, (endpoints_x[x],endpoints_y[y],endpoints_x[x+1],endpoints_y[y+1]), 0)
            midpoint_x=(endpoints_x[x]+endpoints_x[x+1])/2
            text_y=endpoints_y[y+1]-int(120/max(colors_x,colors_y))
            if color[0]<16:
                red_h='0'+hex(color[0]).replace('0x','')
            else:
                red_h = hex(color[0]).replace('0x', '')
            if color[1]<16:
                green_h='0'+hex(color[1]).replace('0x','')
            else:
                green_h = hex(color[1]).replace('0x', '')
            if color[2]<16:
                blue_h='0'+hex(color[2]).replace('0x','')
            else:
                blue_h=hex(color[2]).replace('0x','')
            if csys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)[1]>=0.5:
                text=font.render("#"+red_h+green_h+blue_h,True,black)
                textRect=text.get_rect()
                textRect.center=(midpoint_x,text_y)
                screen.blit(text,textRect)
            else:
                text=font.render("#"+red_h+green_h+blue_h,True,white)
                textRect=text.get_rect()
                textRect.center=(midpoint_x,text_y)
                screen.blit(text,textRect)
    pygame.image.save(screen,'C:/Users/rodri/AWP-Bot/grid.png')
    pygame.display.flip()
    pygame.quit()
    # running  = True
    # while running:
    #     for event in pygame.event.get():  
    #         if event.type == pygame.QUIT:  
    #             running = False
    await interaction.response.send_message(file=discord.File('C:/Users/rodri/AWP-Bot/grid.png'))

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=715141595153956904))
    print("Command Ready!")

client.run(os.getenv('BOT_TOKEN'))
