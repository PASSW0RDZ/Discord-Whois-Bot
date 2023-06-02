#Made by; PASSW0RDZ




import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.guilds)} servers!'))
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!whois'):
        if len(message.mentions) == 1:
            user = message.mentions[0]
            username = user.name + '#' + user.discriminator
            user_id = user.id
            badges = ', '.join(str(badge).split('.')[1].replace('_', ' ').title() for badge in user.public_flags.all())
            joined_at = user.joined_at.strftime('%Y-%m-%d %H:%M:%S')
            created_at = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
            embed = discord.Embed(title=f'{username}', description=f'({user_id})', color=discord.Color.dark_theme())
            embed.set_thumbnail(url=user.avatar.url)
            embed.add_field(name='Badges', value=badges)
            embed.add_field(name='Joined Server', value=joined_at)
            embed.add_field(name='Account Created', value=created_at)
            embed.set_author(name='Whois Lookup', icon_url=client.user.avatar.url)
            await message.channel.send(embed=embed)
    elif message.content.startswith('!ping'):
        embed = discord.Embed(title='Pong!', color=discord.Color.dark_theme())
        await message.channel.send(embed=embed)
    elif message.content.startswith('!credits'):
        embed = discord.Embed(title='Credits', description='https://github.com/PASSW0RDZ', color=discord.Color.dark_theme()) #leave my github here skid
        await message.channel.send(embed=embed)
    elif message.content.startswith('!help'):
        embed = discord.Embed(title='Help', description='Here are the available commands:', color=discord.Color.dark_theme())
        embed.add_field(name='!whois [user mention]', value='Shows information about the mentioned user.', inline=False)
        embed.add_field(name='!ping', value='Pings the bot and returns "Pong!".', inline=False)
        embed.add_field(name='!credits', value='Shows credits for the bot.', inline=False)
        embed.set_footer(text='PASSW0RDZ', icon_url=client.user.avatar.url)
        await message.channel.send(embed=embed)

    
client.run('TOKEN HERE') #add your bot token here which you will find in the dev portal on discord.com

###import http.server
###import socketserver

###PORT = 3000

###Handler = http.server.SimpleHTTPRequestHandler

###with socketserver.TCPServer(("", PORT), Handler) as httpd:
###    print("serving at port", PORT)
###    httpd.serve_forever()  

#24/7 Replit System ^
