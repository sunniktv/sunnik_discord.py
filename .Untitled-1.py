from discord.ext import commands

bot = commands.Bot(command_prefix='+')

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

@cpp.group()
async def _helloworld(ctx):
    await ctx.send("```c++\n#include <iostream>\n\nint main()\n{\n    std::cout << 'Hello World!'<<std::endl;\n}```")

@cpp command()
async def _입출력(ctx):
    await ctx.send("1.hello world\n2.입출력\n 2-1.입력\n 2-2.출력")

@cpp command()
async def _입출력_입력(ctx):
    await ctx.send("```C++\n#include <iostream>\n\nint main(void)\n{\n    int tlqkf;\n    std::cout<<'뭐';\n    std::cin>>tlqkf;\n\n    std::cout<<''<<tlqkf<<''<<std::endl;\n}")

@cpp command()
async def _입출력_출력(ctx):
    await ctx.send("```#include <stdio.h>\n\nint main(void)\n{\nprint('aaa');\n}```\n```#include <iostream>\n\nint main(void)\n{\n    std::cout<<'d'<<std::endl;")

@bot group()
async def 도움말(ctx):
    await ctx.send(">>>도움말\n-주의\n-명령어")

@도움말 command()
async def _명령어(ctx):
    await ctx.send(">>>도움말 명령어\n-cpp\n-py(미개방)\n-js(계획)\n-java(계획)\n-lua(미개방)")

bot.run('')
