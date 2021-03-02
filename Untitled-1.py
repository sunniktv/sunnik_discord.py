from discord.ext import commands

bot = commands.Bot(command_prefix='+')

self.bg_task = self.loop.create_task(self.my_background_task())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id) # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') 

@bot.group()
async def cpp(ctx):
    await ctx.send("1.hello world\n2.입출력\n")

@cpp.command()
async def _helloworld(ctx):
    await ctx.send("```c++\n#include <iostream>\n\nint main()\n{\nstd::cout << "Hello World!";\n}```")

bot.run('ODE2MTI1MjIwMjA0NzA3ODUw.YD2Z1w.KyYJVM36CWV1YEki5PU77g8xSmM')