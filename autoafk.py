import discord, time, os, random
from time import sleep
from colorama import Fore
from discord.ext import commands
from random import randint


def clear():
    os.system('cls')

clear()

client = discord.Client()
prefix = "!"
client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

token = input(f'{Fore.MAGENTA}Enter {Fore.LIGHTMAGENTA_EX}Token:{Fore.WHITE} ')



def start():
    print(f'''
{Fore.CYAN}                    Dev: {Fore.MAGENTA}@9n8
{Fore.CYAN}                    Login:{Fore.MAGENTA}[{Fore.WHITE}{client.user.name}{Fore.MAGENTA}#{Fore.WHITE}{client.user.discriminator}{Fore.MAGENTA}]
''')




@client.event
async def on_ready():
    os.system(f'title [Anti AFK]')
    os.system(f'mode 60,20')
    clear()
    start()

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
      time.sleep(randint(1,10)) #msg delay
      await message.channel.send(random.choice(['focus', 'z','nice try', '??', 'pressure', 'You wanna leave?', 'Kid stop', 'L', 'beg', "🤓", "lzz and im sleeping", "my son u suck", "ur ass", "lame ass boy", "troll,", "shutup u lame loser", "u suck ma son", "ur horrible", "awwwww", "u already wanna go", "ahahahahha ur tried", "my son soo tired", "LOOOOOOOL", "LOL", "UR MUM IS UGLY SHUTUP UP KID", "blahblah"])) #msg to send   
    if client.user.mentioned_in(message):
      time.sleep(randint(1,8)) #reaction delay
      await message.add_reaction(random.choice(["💤","👍", "🤓","🛏️", "🧋", "😴"])) #reaction emojis

while True:
    client.run(token, bot=False)
