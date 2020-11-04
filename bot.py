# bot.py
import os, csv

import shutil
from tempfile import NamedTemporaryFile
printf ("hello")
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = "!" #TODO: Make this not hard-coded.


class CustomClient(discord.Client):
    combinations={}
    #Key: tuple of 2 elements "(element1, element2)"
    #Value: Product
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    
    async def on_connect(self):
        print("on_connect")
        with open("combinations.csv","r") as combinationsFile:
            combinationsreader=csv.reader(combinationsFile)
            for combination in combinationsreader:
                self.combinations[(combination[1],combination[2])]=combination[0]
    async def on_member_join(self,member):
        #pass#For later
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f'Welcome to the server {member.mention}!')
    async def on_message(self,message):
        content=message.content
        channel=message.channel
        if(content.startswith(PREFIX)):
            args=content.split(" ")
            command=args[0][len(PREFIX):]#remove the prefix from the command
            #print(args)
            if(command=="combine"):
                if((args[1],args[2]) in self.combinations):
                    print("user "+str(message.author)+" successfully combined "+args[1]+" with "+args[2]+" to get "+self.combinations[(args[1],args[2])])
                    await channel.send(args[1]+"+"+args[2]+"="+self.combinations[(args[1]),(args[2])])
                    with open("userCombinations.txt", "a+") as userCombFile:
                        userCombFile.seek(0)
                        for element in userCombFile.readlines():
                            if element.strip("\n") == self.combinations[(args[1]),(args[2])]:
                                await channel.send("(You've already made this element.)")
                                break
                        else:
                            userCombFile.write(self.combinations[(args[1]),(args[2])]+"\n")
                else:
                    print("user "+str(message.author)+" made an invalid combination")    
                    await channel.send("Invalid combination")

#check if code works 
# async def ModRemoveItem(self,ctx):
     # if ctx.message.author.server_permissions.administrator:
        # content=message.content
        # if(content.startswith(PREFIX)):
            # args=content.split(" ")
            # command=args[0][len(PREFIX):] #removes prefix
            # if(command == "remove"):
                # filename="combinations.csv"
                # temp_file=NamedTemporaryfile(delete=False)
                # with open(filename,"rb") as csvfile, temp_file:
                    # reader=csv.DictReader(csvfile)
                    # writer=csv.DictWriter(temp_file)
                    # for row in reader:
                        # if(combination[1]==args[1] and combination[2]==args[2]):
                            # next(row) #skip line 
                        # else writer.writerow(row)
                              
                              
            # shutile.move(temp_file.name,filename) #move new file with deleted combination to combinations.csv file
             # return true                 
           # return false    
                                     
      # else:
        # msg = "You're  not a admin and dont have permission {0.author.mention}".format(ctx.message)  
         # await client.send_message(ctx.message.channel, msg)
         # return true
   
      #  async def hint(self, message):
       #   content=message.content
        #channel=message.channel
        #if(content.startswith(PREFIX)):
         #   args=content.split(" ")
          #  command=args[0][len(PREFIX):]
           # if(command=="hint"):
                        

client = CustomClient()
client.run(TOKEN)
