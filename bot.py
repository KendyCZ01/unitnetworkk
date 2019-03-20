import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = "u!")

client.remove_command('help')



@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name='bot-log')
    await client.change_presence(game=discord.Game(name= "Napiš u!help"))
    print("The bot is online and connected with Discord!") 
    await client.send_message(channel, "**Reset bota proběhl uspěšně!** :thumbsup:")
    

@client.event
async def on_message(message):
    channel = message.channel
    r = random.choice
    mod = "522048274689949712"
    odp1 = "::incoming_envelope: Nápověda poslána, zkontroluj PM {0}".format(message.author.mention)
    odp2 = "Nejsi moderátorem a nemáš pravomoce!"
    devodp = "Nejsi developer tohoto bota!"
    user = message.author
    embed = discord.Embed(title = "Unit-Network", icon_url="https://cdn.discordapp.com/attachments/514801364526825474/526861094182977540/creepy-icon-25.jpg", color = 0x5AD4A9)
    embed.add_field(name = "Prefix:", value = "u!",inline=False)
    embed.add_field(name = "Main server:", value = "https://discord.gg/U3eeYhz",inline=False)
#----------------------------------------------
    if message.content.upper() == "u!info":
        await client.send_message(channel, embed=embed)
    embed = discord.Embed(title="Důležité info!", color = 0x8AD2A6)
    embed.add_field(name = "Důležité:",value="-- Připravujeme --",inline=False)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/514801364526825474/526861094182977540/creepy-icon-25.jpg")
#----------------------------------------------
    if message.content.upper() == "DULEZITE INFO":
        await client.send_message(user, "<#525371812884906014> pro navraceni se do chatu!", embed=embed)
        await client.send_message(message.channel, ":incoming_envelope: Nápověda poslána, zkontroluj PM {0}".format(message.author.mention))
#----------------------------------------------
    if message.content.upper() == "u!restart":
        if "522048274689949712" in (role.id for role in message.author.roles):
            await client.logout()
            await client.sned_message(message.channel, "Restartuji se. Počkejte chvíli.")
        else:
            await client.send_message(message.channel, "Nemáš dostatečné oprávnění!")
#----------------------------------------------
    if message.content.upper() == "u!next update":
        if "522048274689949712" in (role.id for role in message.author.roles):
            embed = discord.Embed(title = "Pristi update", color = 0x0FF00F)
            embed.add_field(name = "Pristi update bude o:", value = "``ban/kick/fun`` prikazech! a ``rcolor`` rcolor = rolecolor a budete si moct menit barvy role pomocí hex barv (#00FF00 atd...)",inline=False)
            await client.send_message(user, embed=embed)
            await client.send_message(message.channel, ":incoming_envelope: {} Podívej se do DM! :incoming_envelope:".format(message.author.mention))
        else:
            await client.send_message(message.channel, "Nejsi developer tohoto bota!")
#----------------------------------------------
    if message.content.upper() == "u!help":
        embed = discord.Embed(title = "Nápověda:", color = 0x00FF00)
        embed.add_field(name = "Prefix:", value = "u!",inline=True)
        embed.add_field(name = "Zábava: [0]", value = "Příkazy připravujeme",inline = False)
        embed.add_field(name = "Pro moderátory: [0]", value = "Příkazy připravujeme",inline = False)
        embed.add_field(name = "Pro developery: [1]", value = "restart",inline = False)
        embed.add_field(name = "Informace: [0]", value = "Příkazy připravujeme",inline=False)
        embed.set_footer(text = "Prefix: u!, na žádost hráče {}".format(message.author.name))
                                                          
        await client.send_message(user, embed=embed)
        await client.send_message(channel, odp1)
#----------------------------------------------
    if message.content.upper() == "u!wad awd awd awd asd awd asd awd":
        if "525379003079720970" in (role.id for role in message.author.roles):
            embed = discord.Embed(title = "Pomoc pro developery!", color = 0x3D5AFE)
            embed.add_field(name = "S!restart", value = "Restartuje Bota!",inline=True)
            embed.add_field(name = "S!Pristi Update", value = "Ukáže ti další update!",inline=True)
            await client.send_message(user, embed=embed)
            await client.send_message(channel, odp1)
        else:
            await client.send_message(channel, devodp)
#----------------------------------------------
    if message.content.upper() == "u!dw awd asd awd asd wa":
        
        if "525379003079720970" in (role.id for role in message.author.roles):
            
                embed = discord.Embed(title = "Pomoc Pro Moderátory!", color = 0x006400)
                embed.add_field(name = "S!clear", value = "Smaže daný počet zpráv!",inline=False)
                embed.add_field(name = "S!warn", value = "Varuje uživatele! Použití: S!warn @user Důvod",inline=False)
                embed.add_field(name = "S!kick", value = "Vyhodí uživatele!",inline=False)
                embed.add_field(name = "S!ban", value = "Banuje Uživatele!",inline=False)
                embed.set_footer(text = "Použito hráčem: {}".format(message.author.name))
                
                await client.send_message(user, embed=embed)
                await client.sned_message(channel, ":incoming_envelope: {} Podívej se do DM! :smile: :incoming_envelope:".format(message.author.mention))
        else:
            await client.send_message(channel, "Nejsi moderátorem a nemáš pravomoce!")
#----------------------------------------------   
    if message.content.upper() == "u! awd asd awd sad awdsasd awds awdsd awdsad awd as":
        embed = discord.Embed(title = "Fun Příkazy!", color = 0xFFFF00)
        embed.add_field(name = "S!LASKA",value = "Ukáže jak moc danou/daného věc/člověka miluješ",inline=False)
        embed.set_footer(text="Přivolal si mě ty ({})".format(message.author.name))
        await client.send_message(user, embed=embed)
#----------------------------------------------
    
        
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("Použití příkazu ``S!rcolor @(ROLENAME) #(HEX BARVA)``")
        return
    if value is None:
        await client.say("Použití příkazu ``S!rcolor @(ROLENAME) #(HEX BARVA)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await client.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await client.say("Barva role {} byla změněna!.".format(role))


@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)

async def warn(ctx, userName: discord.User, *, message:str):
    
    
    
    embed = discord.Embed(color = 0xB22222, title = "Hráč byl varován!")
    embed.add_field(name = "Člověk varován", value = "{0}".format(userName), inline=False)
    embed.add_field(name = "Moderator", value = "{0}".format(ctx.message.author), inline=False)
    embed.add_field(name = "Důvod", value = "{0}".format(message), inline=False)
 
    await client.send_message(message.channel, embed=embed)
   
    
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.send_message(channel, str(number)+' zpráv vymazáno')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.send_message(message.channel, 'Něco se pokazilo')
        return         
   
 
    await client.delete_messages(mgs)      

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def restart():
    await client.logout()
    
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        embed1 = discord.Embed(title = "Error", color = 0xFFFF00)
        embed1.add_field(name = "Denied!", value = "On/Ona je Mod/Admin a nemám pravomoc ho/ji kicknout!!",inline=False)
        await client.say(embed=embed1)
        return
    
    try:
        embed2 = discord.Embed(title = "Povedli se!", color = 0x2E8B57)
        embed2.add_field(name = "Povoleno!", value = user.name+" byl vyhozen!",inline=False)
        await client.kick(user)
        await client.say(embed=embed2)
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        embed3 = diwcird.Embed(title = "Permissions denied!", color = 0xA52A2A)
        embed3.add_field(name = "Pravomoce Odebrány!", value = "Nemáš dostatečné pravomoce na tento příkaz!",inline=False)
        await client.say(embed=embed3)
        return

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        embed3 = discord.Embed(title = "Denied!", color = 0xFFFF00)
        embed3.add_field(name = "Denied!", value = "On/Ona je mod/Admin a nemam odvahu ho/ji zabanovat",inline=False)
        await client.say(embed=embed3)
        return

    try:
        embed2 = discord.Embed(title = "Povedlo se!", color = 0x2E8B57)
        embed2.add_field(name = "Ban se povedl!", value = user.name+" byl zabanován!",inline=False)
        await client.ban(user)
        await client.say(embed=embed2)

    except discord.Forbidden:
        embed1 = discord.Embed(title = "Permission denied!", color = 0xA52A2A)
        embed1.add_field(name = "Permissions Error", value = "Nejspíše nemám práva na ban!",inline=False)
        await client.say(embed=embed1)
        return
    except discord.HTTPException:
        embed = discord.Embed(title = "Error!", color = 0xFFFF00)
        embed.add_field(name = "Nezdařilo se!", value = "Ban se nepodařil!",inline=False)
        await client.say(embed=embed)
        return		 

@client.command()
async def justnela():

    await client.say(embed=embed)

global counter
counter = 0
@client.command(pass_context=True)
async def pick(ctx):
    
    
    counter += 1
    await client.say(counter, "Lol")

#global counter
#counter = 0
#@client.command(pass_context=True)
#   async def pick(ctx):
#   counter += 1
client.run(os.getenv("BOT_TOKEN"))
                                                                                 
