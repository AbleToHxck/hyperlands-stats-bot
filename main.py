import discord
from discord.ext import commands
import requests

pogbot = commands.Bot(command_prefix='-')

TOKEN = "TOKEN"

@pogbot.event
async def on_ready():
    print(f'Alive! Logged in as: {pogbot.user}')

@pogbot.command()
async def stats(ctx, user): 
	await ctx.send(f"Getting the stats for {user}.")
	stats = requests.get('https://api.hyperlandsmc.net/stats/{}'.format(user))
	stats = stats.json()
	online = stats['status']['online']
	if online is True:
		last_server = stats['status']['lastServer']
		rank = stats['rankData']['rank']
		level = stats['stats']['general']['level']
		levelprogress = stats['stats']['general']['progress']
		max_level_progress = stats['stats']['general']['maxProgress']
		skywars_wins = stats['stats']['skywars']['wins']
		skywars_kills = stats['stats']['skywars']['kills']
		bedwars_wins = stats['stats']['bedwars']['wins']
		bedwars_kills = stats['stats']['bedwars']['kills']
		bedwars_finalkills = stats['stats']['bedwars']['finalKills']
		bedwars_beds_broken = stats['stats']['bedwars']['bedsBroken']
		bedwars_current_ws = stats['stats']['bedwars']['currentWinstreak']
		bedwars_overall_ws = stats['stats']['bedwars']['bestWinstreak']
		thebridge_wins = stats['stats']['thebridge']['wins']
		thebridge_goals = stats['stats']['thebridge']['goals']
		thebridge_current = stats['stats']['thebridge']['currentWinstreak']
		thebridge_best = stats['stats']['thebridge']['bestWinstreak']
		duels_wins = stats['stats']['duels']['buildUhcWins']
		duels_potwins = stats['stats']['duels']['potWins']
		duels_ironwins = stats['stats']['duels']['ironWins']
		duels_archerwins = stats['stats']['duels']['archerWins']
		duels_sumowis = stats['stats']['duels']['sumoWins']
		duels_ws = stats['stats']['duels']['currentWinstreak']
		duel_best_ws = stats['stats']['duels']['bestWinstreak']
		duel_elo = stats['stats']['duels']['elo']
		UHC_wins = stats['stats']['uhcmeetup']['wins']
		UHC_kills = stats['stats']['uhcmeetup']['kills']

		embed=discord.Embed(title=f"AbleToHxck's HyperLands stats", color=discord.Color.blue())
		embed.set_author(name=f"Requested by {ctx.message.author}", icon_url=ctx.author.avatar_url)
		embed.set_thumbnail(url="https://api.hyperlandsmc.net/head/{}".format (user))
		embed.add_field(name='Rank', value=rank, inline=False)
		embed.add_field(name='Level', value=f'{level}, Progress {levelprogress}/{max_level_progress}', inline=False)
		embed.add_field(name='Skywars Wins', value=skywars_wins, inline=True)
		embed.add_field(name='Skywars Kills', value=skywars_kills, inline=True)
		embed.add_field(name='Bedwars Wins', value=bedwars_wins, inline=True)
		embed.add_field(name='Bedwars Kills', value=bedwars_kills, inline=True)
		embed.add_field(name='Bedwars Final Kills', value=bedwars_finalkills, inline=True)
		embed.add_field(name='Bedwars Beds Broken', value=bedwars_beds_broken, inline=True)
		embed.add_field(name='Bedwars Current Winstreak', value=bedwars_current_ws, inline=True)
		embed.add_field(name='Bedwars Overall Winstreak', value=bedwars_overall_ws, inline=True)
		embed.add_field(name='The Bridge Wins', value=thebridge_wins, inline=True)
		embed.add_field(name='The Bridge Goals', value=thebridge_goals, inline=True)
		embed.add_field(name='The Bridge Current Winstreak', value=thebridge_current, inline=True)
		embed.add_field(name='The Bridge Best Winstreak', value=thebridge_best, inline=True)
		embed.add_field(name='Duels Elo', value=duel_elo, inline=True)
		embed.add_field(name='BuildUHC Wins', value=duels_wins, inline=True)
		embed.add_field(name='PotPvP Wins', value=duels_potwins, inline=True)
		embed.add_field(name='Iron Wins', value=duels_ironwins, inline=True)
		embed.add_field(name='Archer Wins', value=duels_archerwins, inline=True)
		embed.add_field(name='Duels Current Winstreak', value=duels_ws)
		embed.add_field(name='Duels Best Winstreak', value=duel_best_ws, inline=True)
		embed.add_field(name='UHC Wins', value=UHC_wins, inline=True)
		embed.add_field(name='UHC Kills', value=UHC_kills,)
		embed.set_footer(text=f'Online in {last_server}', icon_url='https://as2.ftcdn.net/jpg/04/27/96/91/220_F_427969127_NAdMpfCaKZ58RkeSCzNUIbz1PFVv0x9E.jpg')
		await ctx.send(embed=embed)
	else:
		last_server = stats['status']['lastServer']
		rank = stats['rankData']['rank']
		level = stats['stats']['general']['level']
		levelprogress = stats['stats']['general']['progress']
		max_level_progress = stats['stats']['general']['maxProgress']
		skywars_wins = stats['stats']['skywars']['wins']
		skywars_kills = stats['stats']['skywars']['kills']
		bedwars_wins = stats['stats']['bedwars']['wins']
		bedwars_kills = stats['stats']['bedwars']['kills']
		bedwars_finalkills = stats['stats']['bedwars']['finalKills']
		bedwars_beds_broken = stats['stats']['bedwars']['bedsBroken']
		bedwars_current_ws = stats['stats']['bedwars']['currentWinstreak']
		bedwars_overall_ws = stats['stats']['bedwars']['bestWinstreak']
		thebridge_wins = stats['stats']['thebridge']['wins']
		thebridge_goals = stats['stats']['thebridge']['goals']
		thebridge_current = stats['stats']['thebridge']['currentWinstreak']
		thebridge_best = stats['stats']['thebridge']['bestWinstreak']
		duels_wins = stats['stats']['duels']['buildUhcWins']
		duels_potwins = stats['stats']['duels']['potWins']
		duels_ironwins = stats['stats']['duels']['ironWins']
		duels_archerwins = stats['stats']['duels']['archerWins']
		duels_sumowis = stats['stats']['duels']['sumoWins']
		duels_ws = stats['stats']['duels']['currentWinstreak']
		duel_best_ws = stats['stats']['duels']['bestWinstreak']
		duel_elo = stats['stats']['duels']['elo']
		UHC_wins = stats['stats']['uhcmeetup']['wins']
		UHC_kills = stats['stats']['uhcmeetup']['kills']

		embed=discord.Embed(title=f"AbleToHxck's HyperLands stats", color=discord.Color.blue())
		embed.set_author(name=f"Requested by {ctx.message.author}", icon_url=ctx.author.avatar_url)
		embed.set_thumbnail(url="https://api.hyperlandsmc.net/head/{}".format (user))
		embed.add_field(name='Rank', value=rank, inline=False)
		embed.add_field(name='Level', value=f'{level}, Progress {levelprogress}/{max_level_progress}', inline=False)
		embed.add_field(name='Skywars Wins', value=skywars_wins, inline=True)
		embed.add_field(name='Skywars Kills', value=skywars_kills, inline=True)
		embed.add_field(name='Bedwars Wins', value=bedwars_wins, inline=True)
		embed.add_field(name='Bedwars Kills', value=bedwars_kills, inline=True)
		embed.add_field(name='Bedwars Final Kills', value=bedwars_finalkills, inline=True)
		embed.add_field(name='Bedwars Beds Broken', value=bedwars_beds_broken, inline=True)
		embed.add_field(name='Bedwars Current Winstreak', value=bedwars_current_ws, inline=True)
		embed.add_field(name='Bedwars Overall Winstreak', value=bedwars_overall_ws, inline=True)
		embed.add_field(name='The Bridge Wins', value=thebridge_wins, inline=True)
		embed.add_field(name='The Bridge Goals', value=thebridge_goals, inline=True)
		embed.add_field(name='The Bridge Current Winstreak', value=thebridge_current, inline=True)
		embed.add_field(name='The Bridge Best Winstreak', value=thebridge_best, inline=True)
		embed.add_field(name='Duels Elo', value=duel_elo, inline=True)
		embed.add_field(name='BuildUHC Wins', value=duels_wins, inline=True)
		embed.add_field(name='PotPvP Wins', value=duels_potwins, inline=True)
		embed.add_field(name='Iron Wins', value=duels_ironwins, inline=True)
		embed.add_field(name='Archer Wins', value=duels_archerwins, inline=True)
		embed.add_field(name='Duels Current Winstreak', value=duels_ws)
		embed.add_field(name='Duels Best Winstreak', value=duel_best_ws, inline=True)
		embed.add_field(name='UHC Wins', value=UHC_wins, inline=True)
		embed.add_field(name='UHC Kills', value=UHC_kills,)
		embed.set_footer(text=f'Offline • Last seen in {last_server}', icon_url="https://images-ext-2.discordapp.net/external/joqnTJ2o-HMFWdi31uYfsm_Db8skV2GnFz_i_y_hLA4/https/cdn.nethergames.org/img/red.png")
		await ctx.send(embed=embed)

@pogbot.command() #hyper stats 
async def compare(ctx, player1, *, p2):
	await ctx.send(f"Comparing {player1} and {p2}.", delete_after=2)
	stats = requests.get(f'https://api.hyperlandsmc.net/stats/{player1}')
	stats = stats.json()
	online = stats['status']['online']
	last_server = stats['status']['lastServer']
	rank = stats['rankData']['rank']
	level = stats['stats']['general']['level']
	levelprogress = stats['stats']['general']['progress']
	max_level_progress = stats['stats']['general']['maxProgress']
	skywars_wins = stats['stats']['skywars']['wins']
	skywars_kills = stats['stats']['skywars']['kills']
	bedwars_wins = stats['stats']['bedwars']['wins']
	bedwars_kills = stats['stats']['bedwars']['kills']
	bedwars_finalkills = stats['stats']['bedwars']['finalKills']
	bedwars_beds_broken = stats['stats']['bedwars']['bedsBroken']
	bedwars_current_ws = stats['stats']['bedwars']['currentWinstreak']
	bedwars_overall_ws = stats['stats']['bedwars']['bestWinstreak']
	thebridge_wins = stats['stats']['thebridge']['wins']
	thebridge_goals = stats['stats']['thebridge']['goals']
	thebridge_current = stats['stats']['thebridge']['currentWinstreak']
	thebridge_best = stats['stats']['thebridge']['bestWinstreak']
	duels_wins = stats['stats']['duels']['buildUhcWins']
	duels_potwins = stats['stats']['duels']['potWins']
	duels_ironwins = stats['stats']['duels']['ironWins']
	duels_archerwins = stats['stats']['duels']['archerWins']
	duels_sumowis = stats['stats']['duels']['sumoWins']
	duels_ws = stats['stats']['duels']['currentWinstreak']
	duel_best_ws = stats['stats']['duels']['bestWinstreak']
	duel_elo = stats['stats']['duels']['elo']
	UHC_wins = stats['stats']['uhcmeetup']['wins']
	UHC_kills = stats['stats']['uhcmeetup']['kills']

	stat = requests.get(f'https://api.hyperlandsmc.net/stats/{p2}')
	stat = stat.json()
	online2 = stat['status']['online']
	last_server2 = stat['status']['lastServer']
	rank2 = stat['rankData']['rank']
	level2 = stat['stats']['general']['level']
	levelprogress2 = stat['stats']['general']['progress']
	max_level_progress2 = stat['stats']['general']['maxProgress']
	skywars_wins2 = stat['stats']['skywars']['wins']
	skywars_kills2 = stat['stats']['skywars']['kills']
	bedwars_wins2 = stat['stats']['bedwars']['wins']
	bedwars_kills2 = stat['stats']['bedwars']['kills']
	bedwars_finalkills2 = stat['stats']['bedwars']['finalKills']
	bedwars_beds_broken2 = stat['stats']['bedwars']['bedsBroken']
	bedwars_current_ws2 = stat['stats']['bedwars']['currentWinstreak']
	bedwars_overall_ws2 = stat['stats']['bedwars']['bestWinstreak']
	thebridge_wins2 = stat['stats']['thebridge']['wins']
	thebridge_goals2 = stat['stats']['thebridge']['goals']
	thebridge_current2 = stat['stats']['thebridge']['currentWinstreak']
	thebridge_best2 = stat['stats']['thebridge']['bestWinstreak']
	duels_wins2 = stat['stats']['duels']['buildUhcWins']
	duels_potwins2 = stat['stats']['duels']['potWins']
	duels_ironwins2 = stat['stats']['duels']['ironWins']
	duels_archerwins2 = stat['stats']['duels']['archerWins']
	duels_sumowis = stat['stats']['duels']['sumoWins']
	duels_ws2 = stat['stats']['duels']['currentWinstreak']
	duel_best_ws2 = stat['stats']['duels']['bestWinstreak']
	duel_elo2 = stat['stats']['duels']['elo']
	UHC_wins2 = stat['stats']['uhcmeetup']['wins']
	UHC_kills2 = stat['stats']['uhcmeetup']['kills']
	embed=discord.Embed(title=f"{player1}'s stats vs {p2}'s stats", description=f"Requested by {ctx.message.author}", color=discord.Color.blue())
	e=embed
	embed.set_author(name=f"Requested by {ctx.message.author}")
	embed.add_field(name=f"Rank:", value=f"{player1}: {rank}\n{p2}: {rank2}")
	embed.add_field(name=f"Level:", value=f'{player1}: {level}\n{p2}: {level2}')
	embed.add_field(name=f"Skywars wins:", value=f"{player1}: {skywars_wins}\n{p2}: {skywars_wins2}")
	embed.add_field(name=f"Skywars Kills:", value=f"{player1}: {skywars_kills}\n{p2}: {skywars_kills2}")
	embed.add_field(name=f"Bedwars wins:", value=f"{player1}: {bedwars_wins}\n{p2}: {bedwars_wins2}")
	embed.add_field(name=f"Bedwars finalkills:", value=f"{player1}: {bedwars_finalkills}\n{p2}: {bedwars_finalkills2}")
	embed.add_field(name=f"Bedwars bedsbroken:", value=f"{player1}: {bedwars_beds_broken}\n{p2}: {bedwars_beds_broken2}")
	embed.add_field(name=f"Bedwars C.WS:", value=f"{player1}: {bedwars_current_ws}\n{p2}: {bedwars_current_ws2}")
	embed.add_field(name=f"Bedwars O.WS:", value=f"{player1}: {bedwars_overall_ws}\n{p2}: {bedwars_overall_ws2}")
	embed.add_field(name=f"The Bridge wins:", value=f"{player1}: {thebridge_wins}\n{p2}: {thebridge_wins2}")
	embed.add_field(name=f"The Bridge goals:", value=f"{player1}: {thebridge_goals}\n{p2}: {thebridge_goals2}")
	embed.add_field(name=f"The Bridge C.WS:", value=f"{player1}: {thebridge_current}\n{p2}: {thebridge_current2}")
	embed.add_field(name=f"The Bridge O.WS:", value=f"{player1}: {thebridge_best}\n{p2}: {thebridge_best2}")
	embed.add_field(name=f"Duels ELO:", value=f"{player1}: {duel_elo}\n{p2}: {duel_elo2}")
	embed.add_field(name=f"BuildUHC wins:", value=f"{player1}: {duels_wins}\n{p2}: {duels_wins2}")
	embed.add_field(name=f"PotPvP wins:", value=f"{player1}: {duels_potwins}\n{p2}: {duels_potwins2}")
	embed.add_field(name=f"Iron wins:", value=f"{player1}: {duels_ironwins}\n{p2}: {duels_ironwins2}")
	embed.add_field(name=f"Archer wins:", value=f"{player1}: {duels_archerwins}\n{p2}: {duels_archerwins2}")
	embed.add_field(name=f"Duels C.WS:", value=f"{player1}: {duels_ws}\n{p2}: {duels_ws2}")
	embed.add_field(name=f"UHC wins:", value=f"{player1}: {UHC_wins}\n{p2}: {UHC_wins2}")
	embed.add_field(name=f"UHC kills:", value=f"{player1}: {UHC_kills}\n{p2}: {UHC_kills2}")
	embed.set_image(url="https://discordapp.com/assets/e4923594e694a21542a489471ecffa50.svg")
	await ctx.send(embed=embed)

@pogbot.command()
async def skin(ctx, player):
    embed = discord.Embed(title=f"{player}'s skin", color=discord.Color.blue(), url=f'https://api.hyperlandsmc.net/skin/{player}')
    embed.set_image(url = f"https://api.hyperlandsmc.net/skin/{player}")
    await ctx.send(embed=embed)

pogbot.run(TOKEN)
