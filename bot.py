import requests
from telethon import events, Button, TelegramClient
import os
import logging


logging.basicConfig(level=logging.INFO)

try:
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
except ValueError:
    print("You forgot to fullfill vars")
    print("Bot is quitting....")
    exit()
except Exception as e:
    print(f"Error - {str(e)}")
    print("Bot is quitting.....")
    exit()
except ApiIdInvalidError:
    print("Your API_ID or API_HASH is Invalid.")
    print("Bot is quitting.")
    exit()

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)

@bin.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    if event.is_group:
        await event.reply("**Bin-Api is Alive**")
        return
    await event.reply(f"**Hola {event.sender.first_name}**\nBin-Api se a Iniciado.\nUse /help para ver el menu de ayuda.\nUse /bin + el número de bin que desea verificar.", buttons=[
    [Button.url("💸 Create Donation", "https://www.paypal.me/srnovus")]
    [Button.url("🗃 Codigo Fuente", "https://github.com/jcystem/bin-api-bot")]
    ])

@bin.on(events.NewMessage(pattern="^[!?/]help$"))
async def help(event):
    text = """
**Bienvenido al Menu de Ayuda:**

- /start - Inicia el Bot :)
- /help - Para ver el Menu de Ayuda
- /bin - Crea y verifica la Disponibilidad de un Bin

- *Nota : *
__Este Bot-Api esta en desarrollo y en constante
actualizaciónes, esto significa que puede presentar
fallas, puedes reportarlas aqui: -> @jcystemchat
"""
    await event.reply(text, buttons=[
    [Button.url("💸 Create Donation", "https://www.paypal.me/srnovus")]
    [Button.url("🗃 Codigo Fuente", "https://github.com/jcystem/bin-api-bot")]
    ])
    
@bin.on(events.NewMessage(pattern="^[!?/]info$"))
async def info(event):
   text = """

**🤖 Bot :** Bin Checker Api
**📥 Versión :** v0.1 
**🧑‍💻 Developer :** [Javier Caceres](https://github.com/jcystem/)
**💻 Channel :** No Disponible
**☎️ Support :** No Disponible
**🗂️ Api :** [BIN API v0.1](https://github.com/jcystem/)
**⚙️ Language :** Python 3
**🛡️ Framework :** Pyrogram

"""

@bin.on(events.NewMessage(pattern="^[!?/]bin"))
async def binc(event):
    xx = await event.reply("`Verificando.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        me = (await event.client.get_me()).username

        valid = f"""
<b>➤ Bin Valido ✔:</b>

<b>Bin -</b> <code>{input}</code>
<b>Estado -</b> <code>Valid Bin</code>
<b>Servicio -</b> <code>{vendor}</code>
<b>Tipo -</b> <code>{type}</code>
<b>Nivel -</b> <code>{level}</code>
<b>Banco -</b> <code>{bank}</code>
<b>Región -</b> <code>{country}</code>

<b>Checked By - @{me}</b>
<b>User-ID - {event.sender_id}</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("Plese provide a bin to check\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**➤ Bin Invalido ✖:**\n\n**Bin -** `{input}`\n**Estado -** `Bin Invalido`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")

print ("Successfully Started")
bin.run_until_disconnected()
