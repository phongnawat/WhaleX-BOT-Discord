# OTgwOTA2MjUwOTY1NTA4MTA2.GqNgLI.fSE6taWqsDPeX9rrHfVHU9h79EBXUrGW3azAdw token

from email.mime import image
import imghdr
from tkinter import Image, PhotoImage, image_names
from turtle import color
import discord

from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL


bot = commands.Bot(command_prefix='!wx ', help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command
async def test(ctx):
    await ctx.channel.send("hello")

@bot.command()
async def team(ctx):
    emBed = discord.Embed(title="WhaleX Player", description="WhaleX Valorant", color=0x42f5a7)
    emBed.add_field(name="Player", value="1.WX Phongnawat\n2.WX Ríkkäッ\n3.WX Ruz1o\n4.WX CuraCao\n5.WX cChaos")
    emBed.add_field(name="Manager", value="Sphikultunyong")
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="help", value="!wx player1-5 (sample: !wx player1)", inline=False)
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def player1(ctx):
    emBed = discord.Embed(title="WX Phongnawat", description="WhaleX Player", color=0x42f5a7)
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="Player", value="WX Phongnawat")
    emBed.add_field(name="Sensitivity", value="400 dpi | 0.785 in game")
    emBed.add_field(name="Role", value="Duelists")
    emBed.add_field(name="Youtube", value="https://www.youtube.com/channel/UC9PYkqk8JoqZogsVzlhtDlw", inline=False)
    emBed.add_field(name="Twitch", value="https://www.twitch.tv/phongnawatboon")
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def player2(ctx):
    emBed = discord.Embed(title="WX Ríkkäッ", description="WhaleX Player", color=0x42f5a7)
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="Player", value="WX Ríkkäッ")
    emBed.add_field(name="Sensitivity", value="800 dpi | 0.2-0.7 in game")
    emBed.add_field(name="Role", value="Initiators")
    emBed.add_field(name="Youtube", value="https://www.youtube.com/channel/UC4Fl4-A870Ob2OsUUXhB9KA", inline=False)
    emBed.add_field(name="Twitch", value="https://www.twitch.tv/wx_rikka")
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def player3(ctx):
    emBed = discord.Embed(title="WX Ruz1o", description="WhaleX Player", color=0x42f5a7)
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="Player", value="WX Ruz1o")
    emBed.add_field(name="Sensitivity", value="- dpi | - in game")
    emBed.add_field(name="Role", value="free kill")
    emBed.add_field(name="Youtube", value="https://www.youtube.com/channel/UCFqgW7CmXq7Clhdh8M_Tm-w", inline=False)
    emBed.add_field(name="Twitch", value="https://www.twitch.tv/ruz1o")
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def player4(ctx):
    emBed = discord.Embed(title="WX CuraCao", description="WhaleX Player", color=0x42f5a7)
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="Player", value="WX CuraCao")
    emBed.add_field(name="Sensitivity", value="- dpi | - in game")
    emBed.add_field(name="Role", value="Flex")
    emBed.add_field(name="Youtube", value="-", inline=False)
    emBed.add_field(name="Twitch", value="-")
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def player5(ctx):
    emBed = discord.Embed(title="WX cChaos", description="WhaleX Player", color=0x42f5a7)
    emBed.set_thumbnail(url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    emBed.add_field(name="Player", value="WX cChaos")
    emBed.add_field(name="Sensitivity", value="800 dpi | 0.3 in game")
    emBed.add_field(name="Role", value="Flex")
    emBed.add_field(name="Youtube", value="https://www.youtube.com/channel/UCKsoIAAV2Dn44N1vKrQGNgg", inline=False)
    emBed.add_field(name="Twitch", value="https://twitch.tv/domewst")
    emBed.set_footer(text='WhaleX LOGO', icon_url='https://media.discordapp.net/attachments/917030228705038457/981206456793698314/WhaleX_BG.png?width=489&height=489')
    await ctx.channel.send(embed=emBed)

@bot.event
async def on_message(message):
    if message.content == 'สวัสดี':
        await message.channel.send("สวัสดี ผมชื่อปลาวาฬ")
    elif message.content == 'WhaleX':
        await message.channel.send("WhaleX สู้ๆ") 
    elif message.content == 'หวัดดี':
        await message.channel.send("หวัดดี "+ str(message.author.name))
    elif message.content == 'กินไรยัง':
        await message.channel.send("ยัง")
    elif message.content == 'กินไร':
        await message.channel.send("กินปลาค้าบ")
    elif message.content == 'ทำไร':
        await message.channel.send("ยุ่งควยไรอ่าาา "+ str(message.author.name)) 
    elif message.content == 'ควย':
        await message.channel.send("ควยไรไอ้ควาย "+ str(message.author.name))
    elif message.content == 'ปลาโง่':
        await message.channel.send("โง่พ่อมึงดิ "+ str(message.author.name))
    elif message.content == 'ควาย':
        await message.channel.send("ควายพ่อมึงอ่ะสัด "+ str(message.author.name))  
    elif message.content == 'บอทควายๆ':
        await message.channel.send("มึงอ่ะควาย ยุ่งเหี้ยไรด้วย"+ str(message.author.name))
    elif message.content == 'เหี้ยไร':
        await message.channel.send("ป่าว")
    elif message.content == 'มาดิ':
        await message.channel.send("มาดิค้าบบบบบ รู้จักป่าวปลาวาฬรับจบบบ")
    elif message.content == 'วาโร':
        await message.channel.send("วาฬเล่นด้วยยยยย")
    elif message.content == 'วาโล':
        await message.channel.send("วาฬเล่นด้วยยยยย") 
    elif message.content == 'โง่':
        await message.channel.send("โง่เหมือนคนแถวนี้เลยอ่ะ")
    elif message.content == 'กาก':
        await message.channel.send("เก่งกว่าพ่อมึงอีก") 
    elif message.content == 'วาฬ':
        await message.channel.send("ผมเองงงงง")
    elif message.content == 'ทำอะไรได้บ้าง':
        await message.channel.send("!wx team : ดูรายละเอียดทีม WhaleX\n!wx play (linkyoutube) : ปลาวาฬเปิดเพลง")
    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client == None:
        ctx.channel.send("ปลาวาฬมาแล้วค้าบบบบบ")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)

    YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
    voice_client.play(discord.FFmpegPCMAudio(URL))
    voice_client.is_playing()
    return

@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("ปลาวาฬไม่อยู่ครับ ฮื่ออออ")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("อย่ามั่วได้มั้ย ปลาวาฬทำตัวไม่ถูก")
        return

    voice_client.stop()

@bot.command()
async def pause(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("ปลาวาฬไม่อยู่ครับ ฮื่ออออ")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("อย่ามั่วได้มั้ย ปลาวาฬทำตัวไม่ถูก")
        return

    voice_client.pause()

@bot.command()
async def resume(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("ปลาวาฬไม่อยู่ครับ ฮื่ออออ")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("อย่ามั่วได้มั้ย ปลาวาฬทำตัวไม่ถูก")
        return

    voice_client.resume()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run('OTgwOTA2MjUwOTY1NTA4MTA2.GqNgLI.fSE6taWqsDPeX9rrHfVHU9h79EBXUrGW3azAdw')