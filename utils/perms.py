import discord
from utils import vars

def get_perms(message):
    try:
        perms = message.author.permissions_in(message.channel)
    except AttributeError:
        perms = discord.Permissions(permissions=0)
    return perms

def is_admin(message):
    return get_perms(message).administrator

def is_lmao_admin(message):
    return is_admin(message) or str(message.author.id) in vars.get_lmao_admin_list(message.guild.id) or message.author.id == 210220782012334081
