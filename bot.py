# bot.py
import os, csv

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = "!" #TODO: Make this not hard-coded.


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    async def on_member_join(self,member):
        pass#For later
    async def on_message(self,message):
        content=message.content
        channel=message.channel
        if(content.startswith(PREFIX)):
            args=content.split(" ")
            command=args[0][len(PREFIX):]#remove the prefix from the command
            #print(args)
            if(command=="combine"):
                with open("combinations.csv","r") as cominationsFile:
                    combinationsreader=csv.reader(cominationsFile)
                    for combination in combinationsreader:
                        #print(combination)
                        if(combination[1]==args[1] and combination[2]==args[2]):
                            print("user "+str(message.author)+" successfully combined "+combination[1]+" with "+combination[2]+" to get "+combination[0])
                            await channel.send(combination[1]+"+"+combination[2]+"="+combination[0])
                            break
                    else:
                        print("user "+str(message.author)+" made an invalid combination")    
                        await channel.send("Invalid combination")
                with open("userCombinations.txt", "a") as userCombFile:
                    userCombFile.write("{}\n".format(combination[0]))

                #with open("userCombinations.txt", "w") as userCombFile:
                    #userCombFile.write(combination[0])
                #else:               
                 #   with open("userCombinations.txt", "r+") as userCombFile:
                  #      for line in userCombFile:
                   #         if combination[0] in line:
                    #            await channel.send("Element already created.")
                     #           break
                      #  userCombFile.seek(0, 2)
                       # userCombFile.write("{}\n".format(combination[0]))
                            
                    



client = CustomClient()
client.run(TOKEN)