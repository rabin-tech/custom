from userge import userge, Message
from random import choice
import asyncio
from pyrogram import enums

INSULT_STRINGS = (
    'Chup mug',
    'disturb vo mug',
    'christian vanda tallo barga ko kata bata aayo yeha',
    'https://media.tenor.com/images/ee616b63bab2fa326e867f452235894a/tenor.gif',
    'guu kha mug 💩',
    'https://i.imgur.com/M3OhyYn.jpg',
    'lyang lyang na han na lado',
    'https://media.tenor.com/images/8e834a7c1807ac17265c11071b1c5748/tenor.gif',
    'jurukka uthera jhyamma mukh padkau!',
    'Sutna dyao, chuppa lara!',
    'marna nasakya randi muji',
    'https://media.tenor.com/images/4da49d51af9f989e520080b7557e050c/tenor.gif',
    'lado chus machikne',
    'muji sarki',
    'lado kha',
    'tero bauko kalo condo',
    'tero bau',
    'machikne randi kina bolais',
    'uttano khana paryo radi talai?',
    'bhutro khojeko ho muji?',
    'thukka machikne randiko xoroharu',
    'तेरो बाउको झिलझिले कट्टु',
    'Chimma abu',
    'Mampakha Naku na',
    'Randi ko chak beshya chikauti',
    'tero bajeko naito',
    'thukka, sala masti ko natija',
    'English ma Ear\nNepali ma kaan\nChuplag khate muji randikoban',
    'yo muji pakhe feri aayo',
    'tero baje ko turi',
    'vaisi ko lado kha machikne',
    'खसि बलात्कारी माचिक्ने',
    'bahun machikne',
    'Mathyasni randi ko baan',
    'Naak katdim ta mug newarko?',
    'Muji rautey',
    'Badi nabol muji',
    'Machikney chup lag',
    'Maa sala khatey ko ban',
    'randi bhalu',
    'halla nagar chikney!',
    'Geda khana karaira?',
    'lado chus muji randi',
    'radi puti mukhe',
    'hijada radi',
    'terima dharti ko bojh machikne',
    'condom futera janmeko randi kina badi bolira',
    'moran chyase chikne furti lagauxas mug',
    'mero fushi kha machikne',
    'gula kha randi ko ban',
    'chuplag radi ko puti',
    'turi tauke sala',
    'khatey ko ban',
    'Ranmati',
    'ahile rando ko kando phutaidinxu ani tha hunxa',
    'aija muji single single',
    'hasais machikney',
    'Turi tandim tero?',
    'kasto muji gula jasto raixa chikne',
    'https://media.tenor.com/images/fa8ceb000dad3a6b5d34fdc002530715/tenor.gif',
    'class ma jaa chikne. tero mom lai vandim?',
    'k vo mug?',
    'jaa mug tiktok bana. k telegram chalauxas ta',
    'khate bahun',
    'https://media.tenor.com/images/473f1d3b5df4ce28d7ce53ffd8bfd9bd/tenor.gif',
    'lati ko poi',
    'terima dhoti',
    'yo Chinese kata bata aayo',
    'talai bihari'
    )

@userge.on_cmd("oa$", about={'header': "You want gali in Nepali style?"})
async def gali_(message: Message):
    """gali"""
    await check_and_send(message, choice(INSULT_STRINGS), parse_mode=enums.ParseMode.HTML)


async def check_and_send(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(
            message.delete(),
            replied.reply(*args, **kwargs)
        )
    else:
        await message.edit(*args, **kwargs)
   
