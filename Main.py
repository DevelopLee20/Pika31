import Pika31 as pika
import My_token as token

# event loop off in jupyter notebook
import nest_asyncio
nest_asyncio.apply()

bot = pika.getting_started()
bot.run(token.get_token())