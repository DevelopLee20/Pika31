import Pika31 as pika
import My_token as token

# event loop off in jupyter notebook
import nest_asyncio
nest_asyncio.apply()

bot = pika.getting_started()

@bot.command(aliases=['안녕'])
async def hi(ctx):
    await ctx.send(f'안녕하세요 {ctx.author.mention} 님')
    print(f'{ctx.author} used hi.')

bot.run(token.get_token())