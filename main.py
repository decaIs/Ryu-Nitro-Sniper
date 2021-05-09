import re
import requests
import keep_alive
from colorama import Fore, init
from discord.ext import commands
init()

Ryu = commands.Bot(command_prefix="|", help_command=None, self_bot=False)


worker = ""
claimer = ""


@Ryu.event
async def on_message(message):
    try:
        if 'discord.gift/' in message.content:
            epic = re.search("discord.gift/(.*)", message.content).group(1)
            headers = {
                'Authorization': claimer,
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36 "
            }
            x = f"{Fore.GREEN} Ryu {Fore.RESET}| Code: {epic} {Fore.GREEN} {Fore.RESET}| "
            r = requests.post(
            f'https://discordapp.com/api/v8/entitlements/gift-codes/{epic}/redeem', headers=headers)

            if '{"message": "Unknown Gift Code", "code": 10038}' in r.text:
                print(x + Fore.RED + f'| This code is fake! | {message.guild} | {message.author}'
            elif '{"message": "This gift has already been Reddemed.", "code": 50050}' in r.text:
                print(x + Fore.YELLOW + f'| The code was already Redeemed by someone. | {message.guild} | {message.author}')
            elif 'Rate Limited' in r.text:
                print(x + Fore.RED + f'| Stop spamming Codes! | {message.guild} | {message.author}')
            elif 'Access denied' in r.text:
                print(x + Fore.YELLOW + f'| Failed to Claim the Code | {message.guild} | {message.author}')
            elif len(x) != 16 or x.isnumeric() == True:
            	print(x + Fore.RED + f'| The code is fake! | {message.guild} | {message.author}')
            elif 'subscription_plan' in r.text:
                print(x + Fore.GREEN + f'| Nitro Sniped! | {message.guild} | {message.author}')
    except AttributeError:
        pass

#THIS WAS ORIGINALLY WROTE BY Topia
Ryu.run(worker, bot=False)
