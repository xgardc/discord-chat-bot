import discord
import time
from variables import TOKEN

import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys

browser = uc.Chrome()
browser.get("https://www.cleverbot.com")
browser.find_element_by_id("noteb").click()


def get_response(message):
    browser.find_element_by_xpath(
        "//*[@id='avatarform']/input[1]").send_keys(message + Keys.RETURN)
    while True:
        try:
            browser.find_element_by_xpath("//*[@id='snipTextIcon']")
            break
        except:
            continue
    response = browser.find_element_by_xpath("//*[@id='line1']/span[1]").text
    return response


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"I logged in as {self.user}")
        activity = discord.Game(name="+info")
        await self.change_presence(status=discord.Status.idle, activity=activity)

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id == 889285128331857950:
            await message.channel.send(get_response(message=message.content))


client = MyClient()

client.run(TOKEN)
