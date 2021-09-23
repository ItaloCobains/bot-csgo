import discord
from discord import user
from discord.ext import commands, tasks



bot = commands.Bot('.')

@bot.event
async def on_ready():
    print(f'rodando como {bot.user}')

@bot.event
async def nao_entra_em_loop(message):
    if message.author == bot.user:
         return
    await bot.process_commands(message)

@bot.command(name="scream")
async def cfg(ctx):
    #name = ctx.author.name
    nome_do_jogador = "𝙎𝙘𝙧𝙚𝙖𝙢"
    mouse = "DPI: 400 / Sensitivity: 2.50 / eDPI: 1000 / Raw Input: ON / Hz: 1000 / Zoom Sensitivity: 1.00 / Windows Sensitivity: 6 / Mouse Acceleration: OFF"
    monitor_cfg = "Resolução: 800x600 4:3 Black Bars 360Hz"
    mira = "𝙢𝙞𝙧𝙖: \ncl_crosshairalpha 255; cl_crosshaircolor 4; cl_crosshairdot 1; cl_crosshairgap -999; cl_crosshairsize 3; cl_crosshairstyle 4; cl_crosshairusealpha 1; cl_crosshairthickness 0.5; cl_crosshair_drawoutline 1; cl_crosshair_outlinethickness 1; cl_crosshair_sniper_width 1; cl_crosshairgap_useweaponvalue 0; cl_crosshaircolor_b 250; cl_crosshaircolor_r 250; cl_crosshaircolor_g 250;"
    viewmodel = "𝙫𝙞𝙚𝙬𝙢𝙤𝙙𝙚𝙡: \nviewmodel_fov 68; viewmodel_offset_x 2.5; viewmodel_offset_y 0; viewmodel_offset_z -1.5; viewmodel_presetpos 3; cl_viewmodel_shift_left_amt 0.5; cl_viewmodel_shift_right_amt 0.25; viewmodel_recoil 1; cl_righthand 1;"
    cl_bob = "𝙘𝙡_𝙗𝙤𝙗: \ncl_bob_lower_amt 5; cl_bobamt_lat 0.33; cl_bobamt_vert 0.14; cl_bobcycle 0.98;"
    resposta = nome_do_jogador + "\n" + mouse + "\n" + monitor_cfg + "\n" + mira + "\n" + viewmodel + "\n" + cl_bob
    await ctx.send(resposta)

@bot.command(name="fallen")
async def cfg(ctx):
    #name = ctx.author.name
    nome_do_jogador = "𝙁𝙖𝙡𝙡𝙚𝙣"
    mouse = "DPI: 400 / Sensitivity: 2.20 / eDPI: 880 / Raw Input: ON / Hz: 1000 / Zoom Sensitivity: 1.00 / Windows Sensitivity: 6 / Mouse Acceleration: OFF"
    monitor_cfg = "Resolução: 1680x1050 16x10 Stretched 360Hz"
    mira = "𝙢𝙞𝙧𝙖: \ncl_crosshairalpha 255; cl_crosshaircolor 1; cl_crosshairdot 0; cl_crosshairgap -2; cl_crosshairsize 4; cl_crosshairstyle 4; cl_crosshairusealpha 1; cl_crosshairthickness 1; cl_crosshair_drawoutline 0; cl_crosshair_sniper_width 1;"
    viewmodel = "𝙫𝙞𝙚𝙬𝙢𝙤𝙙𝙚𝙡: \nviewmodel_fov 60; viewmodel_offset_x 1; viewmodel_offset_y 1; viewmodel_offset_z -1; viewmodel_presetpos 1; cl_viewmodel_shift_left_amt 1.5; cl_viewmodel_shift_right_amt 0.75; viewmodel_recoil 1; cl_righthand 0;"
    cl_bob = "𝙘𝙡_𝙗𝙤𝙗: \ncl_bob_lower_amt 21; cl_bobamt_lat 0.4; cl_bobamt_vert 0.25; cl_bobcycle 0.98;"
    resposta = nome_do_jogador + "\n" + mouse + "\n" + monitor_cfg + "\n" + mira + "\n" + viewmodel + "\n" + cl_bob
    await ctx.send(resposta)






bot.run()
