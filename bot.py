import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
# -*- coding: UTF-8 -*-
Client = discord.Client()
client = commands.Bot(command_prefix = "/")
botid="469477762017656842"


@client.event
async def on_message(message):
    if message.content.startswith('/napravigame') and message.author.id != botid:
        Random=random.randint(0,30)
        if Random==0:
            msg=await client.send_message(message.channel, "Mapa: Amazonia\nhttp://aoe3.heavengames.com/pix/randommaps/rms_amazonia.gif")
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==1:
            msg=await client.send_message(message.channel,'Mapa: Andes\nhttp://aoe3.heavengames.com/pix/randommaps/rms_andes.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==2:
            msg=await client.send_message(message.channel,'Mapa: Araucania\nhttp://aoe3.heavengames.com/pix/randommaps/rms_araucania.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==3:
            msg=await client.send_message(message.channel,'Mapa: Bayou\nhttp://aoe3.heavengames.com/pix/randommaps/rms_bayou.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==4:
            msg=await client.send_message(message.channel,'Mapa: Borneo\nhttp://aoe3.heavengames.com/pix/randommaps/Borneo.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==5:
            msg=await client.send_message(message.channel,'Mapa: California\nhttp://aoe3.heavengames.com/pix/randommaps/rms_california.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==6:
            msg=await client.send_message(message.channel,'Mapa: Caribbean\nhttp://aoe3.heavengames.com/pix/randommaps/rms_caribbean.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==7:
            msg=await client.send_message(message.channel,'Mapa: Carolina\nhttp://aoe3.heavengames.com/pix/randommaps/rms_carolina.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==8:
            msg=await client.send_message(message.channel,'Mapa: Ceylon\nhttp://aoe3.heavengames.com/pix/randommaps/Ceylon.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==9:
            msg=await client.send_message(message.channel,'Mapa: Deccan\nhttp://aoe3.heavengames.com/pix/randommaps/Deccan.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==10:
            msg=await client.send_message(message.channel,'Mapa: Great Lakes\nhttp://aoe3.heavengames.com/pix/randommaps/rms_greatlakes.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==11:
            msg=await client.send_message(message.channel,'Mapa: Great Plains\nhttp://aoe3.heavengames.com/pix/randommaps/rms_greatplains.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==12:
            msg=await client.send_message(message.channel,'Mapa: Himalayas\nhttp://aoe3.heavengames.com/pix/randommaps/Himalayas.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==13:
            msg=await client.send_message(message.channel,'Mapa: Himalayas - Upper\nhttp://aoe3.heavengames.com/pix/randommaps/Himalayasupper.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==14:
            msg=await client.send_message(message.channel,'Mapa: New England\nhttp://aoe3.heavengames.com/pix/randommaps/rms_newengland.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==15:
            msg=await client.send_message(message.channel,'Mapa: Northwest Territory\nhttp://aoe3.heavengames.com/pix/randommaps/rms_northwest.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==16:
            msg=await client.send_message(message.channel,'Mapa: Orinoco\nhttp://aoe3.heavengames.com/pix/randommaps/rms_orinoco.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==17:
            msg=await client.send_message(message.channel,'Mapa: Painted Desert\nhttp://aoe3.heavengames.com/pix/randommaps/rms_painteddesert.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==18:
            msg=await client.send_message(message.channel,'Mapa: Pampas\nhttp://aoe3.heavengames.com/pix/randommaps/rms_pampas.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==19:
            msg=await client.send_message(message.channel,'Mapa: Patagonia\nhttp://aoe3.heavengames.com/pix/randommaps/rms_patagonia.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==20:
            msg=await client.send_message(message.channel,'Mapa: Rockies\nhttp://aoe3.heavengames.com/pix/randommaps/rms_rockies.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==21:
            msg=await client.send_message(message.channel,'Mapa: Saguenay\nhttp://aoe3.heavengames.com/pix/randommaps/rms_saguenay.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==22:
            msg=await client.send_message(message.channel,'Mapa: Sonora\nhttp://aoe3.heavengames.com/pix/randommaps/rms_sonora.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==23:
            msg=await client.send_message(message.channel,'Mapa: Texas\nhttp://aoe3.heavengames.com/pix/randommaps/rms_texas.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==24:
            msg=await client.send_message(message.channel,'Mapa: Unknown\nhttp://aoe3.heavengames.com/pix/randommaps/rms_unknown.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==25:
            msg=await client.send_message(message.channel,'Mapa: Yucatan\nhttp://aoe3.heavengames.com/pix/randommaps/rms_yucatan.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==26:
            msg=await client.send_message(message.channel,'Mapa: Yukon\nhttp://aoe3.heavengames.com/pix/randommaps/rms_yukon.gif')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==27:
            msg=await client.send_message(message.channel,'Mapa: Europa (small)\nhttps://cdn.discordapp.com/attachments/469228128024133635/469582325253013524/imageedit_9_4761086992.png')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==28:
            msg=await client.send_message(message.channel,'Mapa: Europa (big)\nhttps://cdn.discordapp.com/attachments/469228128024133635/469579961292816384/imageedit_7_5916529584.png')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==29:
            msg=await client.send_message(message.channel,'Mapa: Sj. Amerika\nhttps://cdn.discordapp.com/attachments/469228128024133635/469551739742453761/imageedit_1_3422115150.png')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
        elif Random==30:
            msg=await client.send_message(message.channel,'Mapa: Azija\nhttps://cdn.discordapp.com/attachments/469228128024133635/469553724403220481/imageedit_5_9576557025.png')
            await client.add_reaction(msg,"👍")
            await client.add_reaction(msg,"👎")
client.run(str(os.environ.get('BOT_TOKEN')))
