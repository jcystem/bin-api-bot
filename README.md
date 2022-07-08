<P align="center">
Bin Api Telegram
 <P align="center">
<img src="https://github.com/jcystem/bin-api-bot/blob/072fea26efc57182176d698284cd19bb5d662666/20220707_183713.jpg" width="230" height="230"/>
</p>
<br>

<p align="center">
<a href="https://github.com/jcystem/"><img title="Autor" src="https://img.shields.io/badge/Autor-JCystem-orange?style=for-the-badge&logo=github"></a>
</p>
 
</details>
<P align="center">
Codigo Abierto bajo

Licencia GNU

</p>

## Características del bot 

```

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
```

<h1 align="center"><b>Bin Api Bot</b></h1>
<h4 align="center">Bot de codigo abierto que se ejecuta en Telegram, costruido en Python.</h4>

## Información Adicional
![Python Version](https://img.shields.io/badge/python-3.9.1-green?style=for-the-badge&logo=appveyor)
![Telethon Version](https://img.shields.io/badge/telethon-1.21.1-blue?style=for-the-badge&logo=appveyor)


## Api Publico

```

@bin.on(events.NewMessage(pattern="^[!?/]bin"))
async def binc(event):
    xx = await event.reply("`Verificando.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://api-bin-v1.herokuapp.com/api/{bin")
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
```

## Requisitos
``` 
API_ID - Your Telegram API ID
API_HASH - Your Telegram API HASH
TOKEN - Your Bot Token
```

## Our Telegram Support Chat
[![Telegram](https://img.shields.io/badge/telegram-1b77FF.svg?style=for-the-badge&logo=telegram)](https://t.me/jcystemproject)
[![Bin Api Bot](https://img.shields.io/badge/telegram-1b77FF.svg?style=for-the-badge&logo=telegram)](https://t.me/bin_api_bot)

# Deploy To Heroku
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/jcystem/bin-api-bot)
