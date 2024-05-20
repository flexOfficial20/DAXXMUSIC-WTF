from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✧ ᴡᴀʟᴄᴏᴍᴇ ᴛᴏ ғʟᴇx ʙᴏᴛs ✧

➲ 𝗘𝗠𝗫𝗘𝗦 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬  [https://t.me/EMXES_COMMUNITY]

➲ 𝗙𝗟𝗘𝗫 𝗕𝗢𝗧𝗦 𝗨𝗣𝗗𝗔𝗧𝗘 [https://t.me/FleX_Bots_News]

➲ 𝗙𝗟𝗘𝗫 𝗕𝗢𝗧 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 [https://t.me/Flex_Support_Chat]

➲ 𝗘𝗠𝗫𝗘𝗦 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 [https://t.me/EMXES_NETWORK]

➲ 𝗞𝗔𝗠𝗨𝗜 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 [https://t.me/KAMUI_NETWORK]

➲ 𝗪/𝗛 𝗧𝗥𝗔𝗗𝗘 𝗔𝗥𝗘𝗔 [https://t.me/The_Trader_Zone]
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Flex_Support_Chat"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/FlexDub_Official"),
          ],
               [
                InlineKeyboardButton("𝗨𝗽𝗱𝗮𝘁𝗲𝘀", url="https://t.me/FleX_Bots_News"),

],
[
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎ 𝗕𝗢𝗧", url=f"https://t.me/Ayanokoji_Kiyotaka_Robot"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧", url=f"https://t.me/FLEX_X_MUSIC_BOT"),
              ],
              [
              InlineKeyboardButton("𝗛𝗨𝗦𝗕𝗔𝗡𝗗𝗢 𝗕𝗢𝗧", url=f"https://t.me/GRABBING_YOUR_HUSBANDO_BOT"),
InlineKeyboardButton("𝗪𝗔𝗜𝗙𝗨 𝗕𝗢𝗧", url=f"https://t.me/GRABBING_YOUR_WAIFU_BOT"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗕𝗢𝗧", url=f"https://t.me/String_Season_robot"),
InlineKeyboardButton("𝗙𝗜𝗟𝗘 𝗦𝗧𝗢𝗥𝗘 𝗕𝗢𝗧", url=f"https://t.me/File_Store_ProxBot"),
],
[
              InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
              InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
              ],
              [
              InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
],
[
InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),
],
[
InlineKeyboardButton("𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡", url=f"https://t.me/FleX_Bots_News"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="img",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/FleX_Bots_News) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/The_Trader_Zone)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


