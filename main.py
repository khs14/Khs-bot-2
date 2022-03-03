import os
import wikipedia

my_secret = os.environ['token2']

from bot_forever import bot_forever

import datetime

from datetime import datetime

import discord
import random
from discord.ext import commands
import time
import sys
import requests

client = commands.Bot(command_prefix='^')


def get_name(full_list):
    name = ''
    for m in range(len(full_list)):
        if m == 0:
            pass
        else:
            name += full_list[m] + ' '
    return name

def get_google_search(term):
  term_list=term.split()
  x = len(term_list)
  for m in range(x):
    if m == (x - 1):
      pass
    else:
      term_list[m] = term_list[m] + '%20'
      search_term = ''
  for k in term_list:
    search_term = search_term + k
  return search_term  


def get_search(term_p):
  term_list=term_p.split()
  x = len(term_list)
  for m in range(x):
    if m == (x - 1):
      pass
    else:
      term_list[m] = term_list[m] + '_'
      search_term = ''
  for k in term_list:
    search_term = search_term + k
  return search_term  


@client.event
async def on_ready():
    print("Bot is online")


@client.event
async def on_message(message):

    #message.channel=client.get_channel(858592938400153600) # change message.channel for diff channels
    s = message.content
    if s.lower() == '^bye':
        await message.channel.send("BYE TTYL")
    f = s.lower()
    l = f.split()
    h = ['hello boi', 'bro get a life', 'Hey man', 'Hey boi', 'hi',
        "What's up?"]
    if f in ['^hi', '^hello', '^hey']:
        await message.channel.send(str(random.choice(h)))
    if f[:5:] == '^wish':
        wish_gif = [
            'https://media.giphy.com/media/12hdeiFVeNm0Ug/giphy.gif',
            'https://media.giphy.com/media/xT0BKqk8FSsAgRQ0SY/giphy.gif',
            'https://media.giphy.com/media/lNByEO1uTbVAikv8oT/giphy.gif',
            'https://media.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif',
            'https://media.giphy.com/media/mcJohbfGPATW8/giphy.gif',
            'https://media.giphy.com/media/28PObmWAiyWRO/giphy.gif',
            'https://media.giphy.com/media/0JFf11Sa7OuoBpYxsC/giphy.gif',
            'https://media.giphy.com/media/5ZMwfuSNy8idGArxQ6/giphy.gif'
        ]

        w = [
            'Happy birthday, bud. Enjoy your Facebook wall filled with messages from people you dont talk to.',
            'Let go of the past; it cant be changed. Let go of the future; no one can predict it. Also, forget about the present. I dmessage.channel not get you one. Happy birthday.',
            ' You are older than you were yesterday, but dont worry; you are younger than you will be tomorrow. Happy birthday.',
            'Finally, you are now one step closer to your big boy pants.',
            'Happy birthday to the only person whose birthday I remember without the help of a Facebook notification.',
            'Happy birthday. You dont look that old, but then neither do you look that young.',
            'Happy birthday to you. You are smart, funny, and fabulous, just like me!',
            'Dont get weirded out about growing older. Our age is actually the number of years the earth has been enjoying us.',
            'As one gets older, three things happen. One, your memory goes, and I cant remember the other two. Happy Birthday.',
            'You are young only once in life, but immaturity is forever. Happy birthday.',
            ' I thought I would bring a celebrity along with me to your party, but then I thought of a better option, M.E.',
            'Happy birthday to my evergreen, forever young partner in crime.',
            'Is one year older? Another opportunity to dress up like you are ten years younger. Happy Birthday!',
            'It is my superiority complex that has made me wish you for your birthday so early. Now I can strut about and tell all your other well-wishers that I was the first!',
            'Another you older, another year wiser. Happy birthday.'
        ]
        await message.channel.send(random.choice(wish_gif))
        await message.channel.send(str(random.choice(w)))

    if f[:8:] == '^gayrate':
        gif_gay = [
            'https://media.giphy.com/media/cyQXvx6OoSDTjukfLJ/giphy.gif',
            'https://media.giphy.com/media/mIwRwDz23fxAc/giphy.gif',
            'https://media.giphy.com/media/l0NwMvJsKiJW1OPQs/giphy.gif',
            'https://media.giphy.com/media/jGZtt36D85tcI/giphy.gif'
        ]

        if len(l) == 1:
            x = random.randint(0, 100)
            g = str(x)
            if x > 50:
                await message.channel.send(random.choice(gif_gay))
            await message.channel.send(
                str(message.author) + ' is ' + g + '%' + 'gay')

        else:
            p = get_name(l)
            x = random.randint(0, 100)
            if x > 50:
                await message.channel.send(random.choice(gif_gay))
                g = str(x)
                await message.channel.send(p + ' is  ' + g + '% gay')
    if f == '^bored':
        site_url = [ "https://www.reddit.com/",
            "https://skribbl.io/", "https://lichess.org/",
            "http://www.higherlowergame.com/", "https://garticphone.com/",
            "https://www.geoguessr.com/", 'http://radio.garden/',
            'https://www.nvidia.com/en-us/research/ai-playground/',
            'http://stuffin.space/', 'https://vole.wtf/','http://slither.io/','https://hackertyper.com/','https://krunker.io/','https://krunker.io/?play=Firefly_Royale','https://krunker.io/?play=KrunCar','https://krunker.io/?play=AIM_Room','https://krunker.io/?play=LaserWar','https://krunker.io/social.html?q=CS1.6_dust2&p=map','https://open.spotify.com/','https://www.miniclip.com/games/en/','https://totaljerkface.com/happy_wheels.tjf','https://tankionline.com/play/','https://pizz.uno/','https://jklm.fun/','https://connect-4.org/en'
        ]
        url_to_be_sent = random.choice(site_url)
        await message.channel.send(url_to_be_sent)
    if f[:11:] == '^gamer_rate':
        gif_gamer = [
            'https://media.giphy.com/media/1n3HCzfkJgEp01nVF8/giphy.gif',
            'https://media.giphy.com/media/S9oOiPA3AlyO3FHc8D/giphy.gif',
            'https://media.giphy.com/media/S9oOiPA3AlyO3FHc8D/giphy.gif',
            'https://media.giphy.com/media/cgCMnZr84zE40/giphy.gif',
            'https://media.giphy.com/media/xTiTnwgQ8Wjs1sUB4k/giphy.gif',
            'https://media.giphy.com/media/y0NFayaBeiWEU/giphy.gif','https://hackertyper.com/','https://en.akinator.com/theme-selection',''
        ]
        if len(l) == 1:
            x = random.randint(0, 100)
            if x > 50:
                await message.channel.send(random.choice(gif_gamer))
            g = str(x)
            a = str(message.author)
            await message.channel.send(a + ' is ' + g + '%' + ' gamer')

        else:
            x = random.randint(0, 100)
            if x > 50:
                await message.channel.send(random.choice(gif_gamer))
            g = str(x)

            await message.channel.send(get_name(l) + ' is  ' + g + '% gamer')

    if f[:10:] == '^simp_rate':

        if len(l) == 1:
            x = random.randint(0, 100)
            if x > 50:
                await message.channel.send("https://gph.is/g/4LDWpL3")
            g = str(x)
            a = str(message.author)

            await message.channel.send(a + ' is ' + g + '%' + ' simp')
        else:
            x = random.randint(0, 100)
            if x > 50:
                await message.channel.send("https://gph.is/g/4LDWpL3")
            g = str(x)

            await message.channel.send(get_name(l) + ' is  ' + g + '% simp')
    if f[:6:] == '^8ball':

        ball_gif = [
            'https://media.giphy.com/media/fkeLNBr7pdr0c/giphy.gif',
            'https://media.giphy.com/media/26tk0engIMdzHKfQc/giphy.gif',
            'https://media.giphy.com/media/QrwRyhHjq8EFO/giphy.gif',
            'https://media.giphy.com/media/vvJmQRgLwtLxBVSYhK/giphy.gif',
            'https://media.giphy.com/media/LRezgP0lV8ZPeV3Inl/giphy.gif',
            'https://media.giphy.com/media/kBkd95U7W0pLI6Vax5/giphy.gif',
            'https://media.giphy.com/media/141iprzbEPjCiQ/giphy.gif',
            'https://media.giphy.com/media/xULW8vm4QWDd4BXDMc/giphy.gif'
        ]
        if len(l) > 1:
            await message.channel.send(random.choice(ball_gif))
            ans = [
                "It is certain", "It is possible", "Without a doubt",
                "Yes, definitely", "You may rely on it", "As I see it, yes",
                "Most likely", "Outlook good", "Yes", "Signs point to yes",
                "Reply hazy try again", "Ask again later",
                "Better not tell you now", "Cannot predict now",
                "Concentrate and ask again", "Do not count on it",
                "My reply is no", "My sources say no", "Outlook not so good",
                "Very doubtful"
            ]
            answer = random.choice(ans)
            await message.channel.send(answer)
        else:
            await message.channel.send("Give a question boi!")
    if f[:2:] == '^q':
        l = f.split(':')
        if len(l) > 1:
            options = l[1].split(',')
            await message.channel.send(random.choice(options))
        else:
            await message.channel.send(
                "Give the question and options correctly boi!")

    if f[:5:] == '^help':
        await message.channel.send(
            'https://kaustubhsethi14.wixsite.com/khs-bot')
    if f[:5:] == '^slap':

        slap_gif = [
            'https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif',
            'https://media.giphy.com/media/uG3lKkAuh53wc/giphy.gif',
            'https://media.giphy.com/media/l2SpSQLpViJk9vhmg/giphy.gif',
            'https://media.giphy.com/media/4Nphcg0CCOfba/giphy.gif',
            'https://media.giphy.com/media/3o84skA6NkEvJg4LlK/giphy.gif'
        ]
        await message.channel.send(random.choice(slap_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to slap ' + get_name(l))

    if f[:5:] == '^kill':

        kill_gif = [
            'https://media.giphy.com/media/lnakxcfG2MFy/giphy.gif',
            'https://media.giphy.com/media/yNFjQR6zKOGmk/giphy.gif',
            'https://media.giphy.com/media/CiZB6WIjaoXYc/giphy.gif',
            'https://media.giphy.com/media/3oz8xy1gPFHsB6NMDm/giphy.gif',
            'https://media.giphy.com/media/Mkrv6hMDj7kcM/giphy.gif'
        ]
        await message.channel.send(random.choice(kill_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to kill ' + get_name(l))

    if f[:6:] == '^snipe':

        snipe_gif = [
            'https://media.giphy.com/media/VwGFJ4NHMBWpDw22ko/giphy.gif',
            'https://media.giphy.com/media/xT0xeHi1rHNKi8j4Ck/giphy.gif',
            'https://media.giphy.com/media/3o6nUXeKldJ2dYMSeA/giphy.gif',
            'https://media.giphy.com/media/3o6nUXeKldJ2dYMSeA/giphy.gif'
        ]
        await message.channel.send(random.choice(snipe_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to snipe ' + get_name(l))

    if f[:5:] == '^stab':

        stab_gif = [
            'https://media.giphy.com/media/IepJKLLnVc17nPRkTh/giphy.gif',
            'https://media.giphy.com/media/xUySTCy0JHxUxw4fao/giphy.gif',
            'https://media.giphy.com/media/T6erVmXL956DK/giphy.gif',
            'https://media.giphy.com/media/kpDKiZGR6wB7pT7IVT/giphy.gif',
            'https://media.giphy.com/media/EVSRCoCP8mlh5GE8ru/giphy.gif'
        ]
        await message.channel.send(random.choice(stab_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to stab ' + get_name(l))

    if f[:5:] == '^kick':

        kick_gif = [
            'https://media.giphy.com/media/10M6fIkFbwqaEo/giphy.gif',
            'https://media.giphy.com/media/PipD5GTXYySWhF3V4j/giphy.gif',
            'https://media.giphy.com/media/l1J3AS8RShMebsmgU/giphy.gif',
            'https://media.giphy.com/media/3o7TKwVQMoQh2At9qU/giphy.gif'
        ]
        await message.channel.send(random.choice(kick_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to kick ' + get_name(l))

    if f[:4:] == '^hug':

        hug_gif = [
            'https://media.giphy.com/media/l8ooOxhcItowwLPuZn/giphy.gif',
            'https://media.giphy.com/media/KL7xA3fLx7bna/giphy.gif',
            'https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif',
            'https://media.giphy.com/media/U4LhzzpfTP7NZ4UlmH/giphy.gif',
            'https://media.giphy.com/media/VbawWIGNtKYwOFXF7U/giphy.gif',
            'https://media.giphy.com/media/e4PybfEfkhLiVDsuT4/giphy.gif'
        ]
        await message.channel.send(random.choice(hug_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to hug ' + get_name(l))

    if f[:12:] == '^play_phrase':

        if len(l) == 2:
            await message.channel.send(
                "https://playphrase.me/#/search?q={}".format(l[1]))
        else:

            term = f[12::]
            search_send = get_google_search(term)
            await message.channel.send(
                "https://playphrase.me/#/search?q={}".format(search_send))

    if f[:6:] == '^roast':

        roast_list = [
            'I made a roast video just for you! : https://tinyurl.com/4ydmv5er',
            'If I had a dollar for every time you said something smart,I would be broke.',
            'Someday you will go far.I hope you stay there.',
            'I will never forget the first time we met.But I will keep trying.',
            'If you are going to be two-faced, at least make one of them pretty.',
            'You are my favorite person... besides every other person I have ever met.',
            'Keep rolling your eyes. Maybe you’ll find your brain back there.',
            'I am not ignoring you. I am simply giving you time to reflect on what an idiot you are being.',
            'No, no. I am listening. It just takes me a moment to process so much stupid information all at once.',
            'Everyone brings happiness to a room. I do when I enter, you do when you leave.',
            'I’m visualizing duck tape over your mouth.'
        ]

        roast_gif = [
            'https://media.giphy.com/media/RdKjAkFTNZkWUGyRXF/giphy.gif',
            'https://media.giphy.com/media/8lT5KZ9zd3w0odjJsN/giphy.gif',
            'hhttps://media.giphy.com/media/4cjgnb2VUb04/giphy.gif',
            'https://media.giphy.com/media/ekwdb5QbKTn3IbZGas/giphy.gif',
            'https://media.giphy.com/media/wKTy5uTiXiYik/giphy.gif',
            'https://media.giphy.com/media/l378uryY4KwoqtVqo/giphy.gif',
            'https://media.giphy.com/media/QUFSSkeKMU1kuI7dHo/giphy.gif',
            'https://media.giphy.com/media/xUOrwaHqU0yIy2TvTa/giphy.gif',
            'https://media.giphy.com/media/Ke2KBmPiwWmH0ZKgHl/giphy.gif',
            'https://media.giphy.com/media/Pn0GNRHkEJuDxRGLef/giphy.gif',
            'https://media.giphy.com/media/MB0xT7Izw5GtZVPPMm/giphy.gif'
        ]
        await message.channel.send(random.choice(roast_gif))
        if len(l) == 1:
            await message.channel.send(
                str(message.author) + ' , ' + random.choice(roast_list))
        if len(l) > 1:

            await message.channel.send(
                get_name(l) + ' , ' + random.choice(roast_list))

    if f[:5:] == '^wiki':

        if len(l) == 1:
            await message.channel.send("Bro enter a term too!")
        if len(l) == 2:
            await message.channel.send(wikipedia.summary(l[1], sentences=2))
            await message.channel.send('https://en.wikipedia.org/wiki/' + l[1])
        else:
            term = get_name(l)
            await message.channel.send(wikipedia.summary(term, sentences=2))
            search_send = get_search(term)
            await message.channel.send('https://en.wikipedia.org/wiki/' +
                                       search_send)

    if f[:5:] == '^time':

        time_current = datetime.now().time()
        await message.channel.send("Time : " + str(time_current))

    if f[:5:] == '^date':
        from datetime import date
        today = date.today()
        date_current = today.strftime("%B %d, %Y")
        await message.channel.send("Date : " + str(date_current))

    if f[:6:] == '^punch':

        punch_gif = [
            'https://media.giphy.com/media/arbHBoiUWUgmc/giphy.gif',
            'https://media.giphy.com/media/nq0qLlrcdahiw/giphy.gif',
            'https://media.giphy.com/media/xT0BKiwgIPGShJNi0g/giphy.gif',
            'https://media.giphy.com/media/GV53c1VNt0x4k/giphy.gif',
            'https://media.giphy.com/media/GRM7Z2s6AougoR3rvv/giphy.gif',
            'https://giphy.com/gifs/old-punch-karma-D6FoVWHnl3Hy0',
            'https://media.giphy.com/media/eiw5mph3qBvdiiHxMa/giphy.gif',
            'https://media.giphy.com/media/l0HlLFVBqUVwxSOzu/giphy.gif',
            'https://media.giphy.com/media/Z5zuypybI5dYc/giphy.gif',
            'https://media.giphy.com/media/AdrRtrWyItfWw/giphy.gif'
        ]
        await message.channel.send(random.choice(punch_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to punch ' + get_name(l))

    if f[:4:] == '^pat':

        pat_gif = [
            'https://media.giphy.com/media/N0CIxcyPLputW/giphy.gif',
            'https://media.giphy.com/media/xUA7bahIfcCqC7S4qA/giphy.gif',
            'https://media.giphy.com/media/6Uhw9V8w8TEBy/giphy.gif',
            'https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif',
            'https://media.giphy.com/media/1eAv6ZRemX1iRJ19oD/giphy.gif',
            'https://media.giphy.com/media/82YkzGpzlJglTVqbDq/giphy.gif',
            'https://media.giphy.com/media/3oFzmm13V0h44D61bi/giphy.gif',
            'https://media.giphy.com/media/3o6Zt2qh8vSNFH30SQ/giphy.gif',
            'https://media.giphy.com/media/uw3fTCTNMbXAk/giphy.gif',
            'https://media.giphy.com/media/3o6gbdUCgjRauJ3vLG/giphy.gif'
        ]
        await message.channel.send(random.choice(pat_gif))
        if len(l) > 1:
            await message.channel.send(
                str(message.author) + ' wants to pat ' + get_name(l))

    if f[:8:] == '^weather':
        if len(l) == 1:
            await message.channel.send("Bro Enter a City")
        else:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=41b3c4002669dd2d593949b0f360142e&units=metric'.format(
                get_name(l))
            request = requests.get(url)
            weather_data = request.json()
            temp = weather_data['main']['temp']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            humidity = weather_data['main']['humidity']
            decrp = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']
            weather_gif = [
                'https://media.giphy.com/media/yNCdgVjhko3cfFYNIi/giphy.gif',
                'https://media.giphy.com/media/jsm7XMcyeTFJE4vHzO/giphy.gif',
                'https://media.giphy.com/media/RMlLEDOPl89mj38GsU/giphy.gif',
                'https://media.giphy.com/media/rVbMAD4irXSkU/giphy.gif',
                'https://media.giphy.com/media/OngAe4RMc0d3i/giphy.gif',
                'https://media.giphy.com/media/QA1OGJyH6NdJ1if3xU/giphy.gif',
                'https://media.giphy.com/media/33Fab84abwCKWPSmaK/giphy.gif',
                'https://media.giphy.com/media/za5xikuRr0OzK/giphy.gif'
            ]
            await message.channel.send(random.choice(weather_gif))
            await message.channel.send('City : {}'.format(get_name(l)))
            await message.channel.send('Description : {}'.format(decrp))
            await message.channel.send(
                "Temperature : {} ° celsius".format(temp))
            await message.channel.send(
                "Temperature minimum : {} ° celsius".format(temp_min))
            await message.channel.send(
                "Temperature maximum : {} ° celsius".format(temp_max))
            await message.channel.send("Humidity : {} %".format(humidity))
            await message.channel.send(
                "Wind Speed : {} km/hr".format(wind_speed))
      
    if f[:7:]=='^google':
      search_google=get_google_search(get_name(l))
      await message.channel.send('http://www.google.com/search?q=' + search_google)
    



    if f[:5:] == '^nuke':
      nuke_gif = ['https://media.giphy.com/media/3oKIPwoeGErMmaI43S/giphy.gif', 'https://media.giphy.com/media/YA6dmVW0gfIw8/giphy.gif', 'https://media.giphy.com/media/RLc1PRYkr4Kju/giphy.gif', 'https://media.giphy.com/media/5tseTlneKSzQVX3WQu/giphy.gif', 'https://media.giphy.com/media/bZvCs7CK4rDG3CFcd2/giphy.gif', 'https://media.giphy.com/media/8ZkdxlG3LGhAlzaqVI/giphy.gif','https://media.giphy.com/media/KzKXmxsMue4CSxzYBK/giphy.gif', 'https://media.giphy.com/media/FnatKdwxRxpVC/giphy.gif', 'https://media.giphy.com/media/l3vR1tookIhM8nZJu/giphy.gif']
      await message.channel.send(random.choice(nuke_gif))
      if len(l) > 1:
        await message.channel.send(
                str(message.author) + ' wants to nuke ' + get_name(l))
  

    if f[:6:] == '^shoot':
      shoot_gif = ['https://media.giphy.com/media/7ZwQ1SEqj7SQr1tkq3/giphy.gif', 'https://media.giphy.com/media/3ohze3pdoPu1xXSmmQ/giphy.gif', 'https://media.giphy.com/media/XD30R2uSWMsaot8CwT/giphy.gif','https://media.giphy.com/media/Tfv8FvB22qD8SUzPDp/giphy.gif','https://media.giphy.com/media/VEzspneHDuo4PQzKc3/giphy.gif','https://media.giphy.com/media/1dSh339toYJr2/giphy.gif','https://media.giphy.com/media/3o6ozBHlv63ZvZWD28/giphy.gif', 'https://media.giphy.com/media/IOzEKEu0R5lwrDnEJC/giphy.gif', 'https://media.giphy.com/media/darPDA1632Aemf7gJq/giphy.gif','https://media.giphy.com/media/l3q2A93zxqHnFDkuQ/giphy.gif', 
      'https://media.giphy.com/media/pHZbBj2w1XdppVFDwA/giphy.gif', 
      'https://media.giphy.com/media/3o6wrmUCx5jyih8gtG/giphy.gif',
      'https://media.giphy.com/media/ik8lXkVRZAbSVDtDsQ/giphy.gif',
      'https://media.giphy.com/media/xIytx7kHpq74c/giphy.gif',
      'https://media.giphy.com/media/DIQo6ECmedYbK/giphy.gif','https://media.giphy.com/media/gCzPZyR0ayIak/giphy.gif','https://media.giphy.com/media/pi0A1X7MG5TTq/giphy.gif']
      await message.channel.send(random.choice(shoot_gif))
      if len(l) > 1:
        await message.channel.send(str(message.author) + ' wants to shoot ' + get_name(l))
    

    if f[:7:] == '^attack' or f[:7:] == '^ambush' :
      attack_gif = ['https://media.giphy.com/media/rVYbN0uxznAaI/giphy.gif',
      'https://media.giphy.com/media/okV4QVqrnlnoeQ7lAl/giphy.gif',
      'https://media.giphy.com/media/SmwsaXanCdOxy/giphy.gif',
      'https://media.giphy.com/media/YN7DcBA6rgI9opx0aj/giphy.gif','https://media.giphy.com/media/xUA7b4LNqswUGX2REs/giphy.gif','https://media.giphy.com/media/dyjrpqaUVqCELGuQVr/giphy.gif','https://media.giphy.com/media/X7Z4lDnPqcF0dyY2dX/giphy.gif','https://media.giphy.com/media/1Nclw5CJ3N77G/giphy.gif','https://media.giphy.com/media/YO5e7gmuBuwFygt3g9/giphy.gif','https://media.giphy.com/media/RKYKrH7WJh7oPzzix0/giphy.gif',
      'https://media.giphy.com/media/AEldvF2yu5Wthpxoih/giphy.gif','https://media.giphy.com/media/137qIhWsIf9bDW/giphy.gif','https://media.giphy.com/media/eR7OEDQDyA7Cg/giphy.gif','https://media.giphy.com/media/8L0T4WZWActpZhAS2h/giphy.gif','https://media.giphy.com/media/26hirKDWxy7WcdU5i/giphy.gif','https://media.giphy.com/media/hIacKgI8mIqdhRBoa2/giphy.gif','https://media.giphy.com/media/jQ651dzYNOPmwmtrrG/giphy.gif'
      ]
      await message.channel.send(random.choice(attack_gif))
      if len(l) > 1:
        await message.channel.send(
                str(message.author) + ' wants to attack ' + get_name(l))

bot_forever()

client.run(my_secret)
