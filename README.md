<p align="center">
<a href="https://github.com/jcystem/"><img title="Autor" src="https://img.shields.io/badge/Autor-Javier-blue?style=for-the-badge&logo=github"></a>
</p>
 
</details>
<P align="center">


</p>

## Características del bot 

```

@bin.on(events.NewMessage(pattern="^[!?/]info$"))
async def info(event):
   text = """

**🤖 Bot :** Bin Checker Api
**📥 Versión :** v2.0.0
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

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        me = (await event.client.get_me()).username

        valid = f
        
```

## Requisitos
``` 
API_ID - Your Telegram API ID
API_HASH - Your Telegram API HASH
TOKEN - Your Bot Token
```

# Deploy To Heroku
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/jcystem/bin-bot)

### `—◉ 💰 DONAR 💰`
- AGRADECE CON UNA DONACION VOLUNTARIA [Aqui](https://www.paypal.me/srnovus/)


### `—◉ 📝 NOTAS 📝`
```bash
- ES POSIBLE QUE EL BOT TENGA ALGUNAS FALLAS, SE IRAN SOLUCIONANDO CONFORME SE VAYAN DETECTANDO
- ES RECOMENDABLE LEER TODO EL MENU Y VER EL FUNCIONAMIENTO DE CADA UNO DE LOS COMANDOS
- REPORTA CUALQUIER FALLO
```

## `EDITOR Y PORPIETARIO DEL BOT` 

`BIN APIs - Bot __________ By Javier Caceres`

