import pyautogui
import time
import asyncio
import discord
import mss
import mss.tools
import threading as t

from discord.utils import get

path = r"C:\Users\Arnav\PycharmProjects\DiscordtoClash\ClanChat.png"
rate = 5
top1 = 150
top2 = 690

left1 = 1010
left2 = 1375
width1 = left2 - left1
height1 = top2 - top1


def take_picture():
    time.sleep(rate - 0.5)

    with mss.mss() as sct:
        top = top1
        left = left1
        width = width1
        height = height1

        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = "ClanChat.png"

        sct_image = sct.grab(monitor)
        mss.tools.to_png(sct_image.rgb, sct_image.size, output=output)

    take_picture()


clantodisc = t.Thread(target=take_picture)

clantodisc.start()

cooldown = True
bot_token = 'OTU1MTEwNTgyMDc0MzUxNjQ3.Yjc6Cw.DzT2-8olOYMEkXIdxtvZVRT0DcM'
client = discord.Client()

xpos = 1353
ypos = 753


@client.event
async def on_ready():
    print(f"Logged in as {client}")


@client.event
async def on_message(message):
    global cooldown
    global rate
    if message.author == client.user:
        return

    if message.content.startswith('/start') and get(message.author.roles, id=955160021409361951):
        while True:
            await message.channel.send(file=discord.File(path))
            await asyncio.sleep(rate)
    if message.content.startswith('/rate') and get(message.author.roles, id=955160021409361951):
        msg = message.content
        msg1 = msg.replace("/rate", "")
        rate = float(msg1.strip())
        await message.channel.send(f" The rate of images is now {msg1} seconds per image!")

    if message.content.startswith('/chat') and cooldown:
        cooldown = False
        await message.channel.send("Message sent!")
        msg = message.content
        

        sender = str(message.author.nick)

        head, sep, tail = sender.partition("#")

        pyautogui.moveTo(xpos, ypos)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.typewrite("DISCORD " + head + ": " + msg.replace('/chat', ''))
        time.sleep(1)
        pyautogui.press("enter")

        time.sleep(3)
        cooldown = True


client.run(bot_token)
