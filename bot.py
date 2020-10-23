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
                            with open("userCombinations.txt", "a+") as userCombFile:
                                userCombFile.seek(0)
                                for element in userCombFile.readlines():
                                    if element.strip("\n") == combination[0]:
                                        await channel.send("Element already created.")
                                        break
                                else:
                                    await channel.send(combination[1]+"+"+combination[2]+"="+combination[0])
                                    userCombFile.write("{}\n".format(combination[0]))
                            break
                    else:
                        print("user "+str(message.author)+" made an invalid combination")    
                        await channel.send("Invalid combination")
  
#async def ModRemoveItem(self,member):
  #  if self.message.author.server_permissions.administrator:
           # content=message.content
        #if(content.startswith(PREFIX)):
         #   args=content.split(" ")
              #command=args[0][len(PREFIX):]
                  #if(command == "remove"):
                     # with open("combinations.csv","w") as cominationsFile:
                    #combinationWriter=csv.writer(cominationsFile)
                    #for combination in combinationWriter
                       #if(combination[1]==args[1] and combination[2]==args[2]):      
      #  else:
       # msg = "You're  not a admin and dont have permission {0.author.mention}".format(self.message)  #ctx 
        # await client.send_message(self.message.channel, msg)
    
                        

client = CustomClient()
client.run(TOKEN)
