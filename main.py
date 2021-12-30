import discord
from discord.ext import commands
import requests
import json
import datetime
import asyncio

bot = commands.Bot(command_prefix='-' or '/')

TOKEN = "Your Token Here"
offlineicon = "https://images-ext-2.discordapp.net/external/joqnTJ2o-HMFWdi31uYfsm_Db8skV2GnFz_i_y_hLA4/https/cdn.nethergames.org/img/red.png"
onlineicon = "https://as2.ftcdn.net/jpg/04/27/96/91/220_F_427969127_NAdMpfCaKZ58RkeSCzNUIbz1PFVv0x9E.jpg"

@bot.event
async def on_ready():
    print(f"Currently logged in as: {bot.user}!")

@bot.command()
async def stats(ctx, player):
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_author(name=f"Getting the stats for {player}.", icon_url=f'https://api.hyperlandsmc.net/head/{player}')
    await ctx.send(embed=embed)
    req = requests.get(f"https://api.hyperlandsmc.net/stats/{player}")
    stat = req.json()
    online = stat["status"]["online"]
    lastLogout = stat["status"]["lastLogout"]
    lastserver = stat["status"]["lastServer"]
    rank = stat["rankData"]["rank"]
    tag = stat["rankData"]["tag"]
    pluscolor = stat["rankData"]["pluscolor"]
    expiry = stat["rankData"]["expiry"]
    level = stat["stats"]["general"]["level"]
    levelprogress = stat["stats"]["general"]["progress"]
    levelmaxprogress = stat["stats"]["general"]["maxProgress"]
    skywars_wins = stat["stats"]["skywars"]["wins"]
    skywars_kills = stat["stats"]["skywars"]["kills"]
    bedwars_wins = stat["stats"]["bedwars"]["wins"]
    bedwars_kills = stat["stats"]["bedwars"]["kills"]
    bedwars_finalkills = stat["stats"]["bedwars"]["finalKills"]
    bedwars_bedbroken = stat["stats"]["bedwars"]["bedsBroken"]
    bedwars_c_ws = stat["stats"]["bedwars"]["currentWinstreak"]
    bedwars_o_ws = stat["stats"]["bedwars"]["bestWinstreak"]
    tb_wins = stat["stats"]["thebridge"]["wins"]
    tb_goals = stat["stats"]["thebridge"]["goals"]
    tb_c_ws = stat["stats"]["thebridge"]["currentWinstreak"]
    tb_o_ws = stat["stats"]["thebridge"]["bestWinstreak"]
    builduhc_wins = stat["stats"]["duels"]["buildUhcWins"]
    potpvp_wins = stat["stats"]["duels"]["potWins"]
    iron_wins = stat["stats"]["duels"]["ironWins"]
    archer_wins = stat["stats"]["duels"]["archerWins"]
    sumo_wins = stat["stats"]["duels"]["sumoWins"]
    duels_elo = stat["stats"]["duels"]["elo"]
    duels_c_ws = stat["stats"]["duels"]["currentWinstreak"]
    duels_o_ws = stat["stats"]["duels"]["bestWinstreak"]
    uhc_wins = stat["stats"]["uhcmeetup"]["wins"]
    uhc_kills = stat["stats"]["uhcmeetup"]["kills"]
    duels_wins = builduhc_wins, potpvp_wins, archer_wins, sumo_wins, iron_wins
    if online is False:
        embed = discord.Embed(title=f"{player}'s HyperLands stats", color=discord.Color.blue())
        embed.set_author(name=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar.url)
        embed.set_thumbnail(url=f"https://api.hyperlandsmc.net/head/{player}")
        embed.add_field(name=f"Name:", value=f"{player}", inline=False)
        embed.add_field(name=f"Rank:", value=rank, inline=False)
        embed.add_field(name=f"Tag:", value=f"{tag}", inline=False)
        embed.add_field(name=f"Level:", value=f"{level}, {levelprogress}/{levelmaxprogress}", inline=True)
        embed.add_field(name=f"Skywars wins:", value=f"{skywars_wins}", inline=True)
        embed.add_field(name=f"Skywars kills:", value=f"{skywars_kills}", inline=True)
        embed.add_field(name=f"Bedwars wins:", value=f"{bedwars_wins}", inline=True)
        embed.add_field(name=f"Bedwars kills:", value=f"{bedwars_kills}", inline=True)
        embed.add_field(name=f"Bedwars FinalKills:", value=f"{bedwars_finalkills}", inline=True)
        embed.add_field(name=f"Bedwars Beds Broken:", value=f"{bedwars_bedbroken}", inline=True)
        embed.add_field(name=f"Bedwars Current Winstreak:", value=f"{bedwars_c_ws}", inline=True)
        embed.add_field(name=f"Bedwars Best Winstreak:", value=f"{bedwars_o_ws}", inline=True)
        embed.add_field(name=f"The Bridge Wins:", value=f"{tb_wins}", inline=True)
        embed.add_field(name=f"The Bridhe Goals:", value=f"{tb_goals}", inline=True)
        embed.add_field(name=f"The Bridge Current Winstreak:", value=f"{tb_c_ws}", inline=True)
        embed.add_field(name=f"The Bridge Best Winstreak:", value=f"{tb_o_ws}", inline=True)
        embed.add_field(name=f"Duels Total Wins:", value=sum(duels_wins), inline=True)
        embed.add_field(name=f"Duels ELO:", value=f"{duels_elo}", inline=True)
        embed.add_field(name=f"BuildUHC Wins:", value=f"{builduhc_wins}", inline=True)
        embed.add_field(name=f"PotPvP Wins:", value=f"{potpvp_wins}", inline=True)
        embed.add_field(name=f"Iron Wins:", value=f"{iron_wins}", inline=True)
        embed.add_field(name=f"Archer Wins:", value=f"{archer_wins}", inline=True)
        embed.add_field(name=f"Duels Current Winstreak:", value=f"{duels_c_ws}", inline=True)
        embed.add_field(name=f"Duels Best Winstreak:", value=f"{duels_o_ws}", inline=True)
        embed.add_field(name=f"UHC Meetup Wins:", value=f"{uhc_wins}", inline=True)
        embed.add_field(name=f"UHC Meetup Kills:", value=f"{uhc_kills}", inline=True)
        date_time = datetime.datetime.fromtimestamp(lastLogout)  
        embed.set_footer(text=f"Currently offline, last seen in {lastserver}, at {date_time}", icon_url=offlineicon)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"{player}'s HyperLands stats", color=discord.Color.blue())
        embed.set_author(name=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar.url)
        embed.set_thumbnail(url=f"https://api.hyperlandsmc.net/head/{player}")
        embed.add_field(name=f"Name:", value=f"{player}", inline=False)
        embed.add_field(name=f"Rank:", value=rank, inline=False)
        embed.add_field(name=f"Tag:", value=f"{tag}", inline=False)
        embed.add_field(name=f"Level:", value=f"{level}, {levelprogress}/{levelmaxprogress}", inline=True)
        embed.add_field(name=f"Skywars wins:", value=f"{skywars_wins}", inline=True)
        embed.add_field(name=f"Skywars kills:", value=f"{skywars_kills}", inline=True)
        embed.add_field(name=f"Bedwars wins:", value=f"{bedwars_wins}", inline=True)
        embed.add_field(name=f"Bedwars kills:", value=f"{bedwars_kills}", inline=True)
        embed.add_field(name=f"Bedwars FinalKills:", value=f"{bedwars_finalkills}", inline=True)
        embed.add_field(name=f"Bedwars Beds Broken:", value=f"{bedwars_bedbroken}", inline=True)
        embed.add_field(name=f"Bedwars Current Winstreak:", value=f"{bedwars_c_ws}", inline=True)
        embed.add_field(name=f"Bedwars Best Winstreak:", value=f"{bedwars_o_ws}", inline=True)
        embed.add_field(name=f"The Bridge Wins:", value=f"{tb_wins}", inline=True)
        embed.add_field(name=f"The Bridhe Goals:", value=f"{tb_goals}", inline=True)
        embed.add_field(name=f"The Bridge Current Winstreak:", value=f"{tb_c_ws}", inline=True)
        embed.add_field(name=f"The Bridge Best Winstreak:", value=f"{tb_o_ws}", inline=True)
        embed.add_field(name=f"Duels Total Wins:", value=sum(duels_wins), inline=True)
        embed.add_field(name=f"Duels ELO:", value=f"{duels_elo}", inline=True)
        embed.add_field(name=f"BuildUHC Wins:", value=f"{builduhc_wins}", inline=True)
        embed.add_field(name=f"PotPvP Wins:", value=f"{potpvp_wins}", inline=True)
        embed.add_field(name=f"Iron Wins:", value=f"{iron_wins}", inline=True)
        embed.add_field(name=f"Archer Wins:", value=f"{archer_wins}", inline=True)
        embed.add_field(name=f"Duels Current Winstreak:", value=f"{duels_c_ws}", inline=True)
        embed.add_field(name=f"Duels Best Winstreak:", value=f"{duels_o_ws}", inline=True)
        embed.add_field(name=f"UHC Meetup Wins:", value=f"{uhc_wins}", inline=True)
        embed.add_field(name=f"UHC Meetup Kills:", value=f"{uhc_kills}", inline=True)
        embed.set_footer(text=f"Currently online in {lastserver}", icon_url=onlineicon)
        await ctx.send(embed=embed)

@bot.command()
async def compare(ctx, player1, p2):
	if player1 == p2:
		embed = discord.Embed(title=f"Error!", description=f"You can' compare yourself!", color=discord.Color.red())
		await ctx.send(embed=embed)
	else:
		testbed = discord.Embed(color=discord.Color.blue())
		testbed.set_author(name=f"Comparing {player1} and {p2}.")
		await ctx.send(embed=testbed, delete_after=1)
		stats = requests.get(f'https://api.hyperlandsmc.net/stats/{player1}')
		stats = stats.json()
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
		potstr = duels_potwins
		builduhcwinsstr = duels_wins
		archerWinsstr = duels_archerwins
		sumowinsstr = duels_sumowis
		ironwinsstr = duels_ironwins
		duelwinreal1 = builduhcwinsstr + potstr + ironwinsstr + archerWinsstr + sumowinsstr
		duelwinreal = str(duelwinreal1)
		UHC_wins = stats['stats']['uhcmeetup']['wins']
		UHC_kills = stats['stats']['uhcmeetup']['kills']

		stat = requests.get(f'https://api.hyperlandsmc.net/stats/{p2}')
		stat = stat.json()
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
		duels_sumowis2 = stat['stats']['duels']['sumoWins']
		duels_ws2 = stat['stats']['duels']['currentWinstreak']
		duel_best_ws2 = stat['stats']['duels']['bestWinstreak']
		duel_elo2 = stat['stats']['duels']['elo']
		potstr2 = duels_potwins2
		builduhcwinsstr2 = duels_wins2
		archerWinsstr2 = duels_archerwins2
		sumowinsstr2 = duels_sumowis2
		ironwinsstr2 = duels_ironwins2
		duelwinreal22 = builduhcwinsstr2 + potstr2 + ironwinsstr2 + archerWinsstr2 + sumowinsstr2
		duelwinreal2 = str(duelwinreal22)
		UHC_wins2 = stat['stats']['uhcmeetup']['wins']
		UHC_kills2 = stat['stats']['uhcmeetup']['kills']

		comparebed = discord.Embed(title=f"{player1} vs {p2}", color=discord.Color.green())
		comparebed.set_author(name=f"Requested by: {ctx.message.author}", icon_url=ctx.message.author.avatar.url)
		if level > level2:
			comparebed.add_field(name=f"Levels:", value=f'⬆️{player1}: {level}\n⬇️{p2}: {level2}')
		elif level2 > level:
			comparebed.add_field(name=f"Levels:", value=f'⬇️{player1}: {level}\n⬆️{p2}: {level2}')
		elif level == level2:
			comparebed.add_field(name=f"Levels:", value=f"↕️{player1}: {level}\n↕️{p2}: {level2}")
		if skywars_wins > skywars_wins2:	
			comparebed.add_field(name='Skywars Wins:', value=f"⬆️{player1}: {skywars_wins}\n⬇️{p2}: {skywars_wins2} wins")
		elif skywars_wins2 > skywars_wins:
			comparebed.add_field(name=f"Skywars Wins:", value=f"⬇️{player1}: {skywars_wins}\n⬆️{p2}: {skywars_wins2} wins")
		elif skywars_wins == skywars_wins:
			comparebed.add_field(name=f"Skywars Wins:", value=f"↕️{player1}: {skywars_wins}\n↕️{p2}: {skywars_wins2} wins")
		if skywars_kills > skywars_kills2:
			comparebed.add_field(name=f"Skywars Kills:", value=F"⬆️{player1}: {skywars_kills}\n⬇️{p2}: {skywars_kills2} kills")
		elif skywars_kills2 > skywars_wins: 
			comparebed.add_field(name=f"Skywars Kills:", value=f"⬇️{player1}: {skywars_kills} kills\n⬆️{p2}: {skywars_kills2} kills")
		elif skywars_kills == skywars_kills2:
			comparebed.add_field(name=f"Skywars Kills:", value=f"↕️{player1}: {skywars_kills} kills\n↕️{p2}: {skywars_kills2} kills")
		if bedwars_wins > bedwars_wins2:
			comparebed.add_field(name=f"Bedwars Wins:", value=f"⬆️{player1}: {bedwars_wins}\n⬇️{p2}: {bedwars_wins2}")
		elif bedwars_wins2 > bedwars_wins:
			comparebed.add_field(name=f"Bedwars Wins:", value=f"⬇️{player1}: {bedwars_wins}\n⬆️{p2}: {bedwars_wins2}")
		elif bedwars_wins == bedwars_wins2:
			comparebed.add_field(name=f"↕️{player1}: {bedwars_wins}\n↕️{p2}: {bedwars_wins2}") 
		if bedwars_kills > bedwars_kills2:
			comparebed.add_field(name=f"Bedwars Kills:", value=f"⬆️{player1}: {bedwars_kills}\n⬇️{p2}: {bedwars_kills2}")
		elif bedwars_kills2 > bedwars_kills:
			comparebed.add_field(name=f"Bedwars Kills:", value=f"⬇️{player1}: {bedwars_kills}\n⬆️{p2}: {bedwars_kills2}")
		elif bedwars_kills == bedwars_kills2:
			comparebed.add_field(name=f"Bedwars Kills:", value=f"↕️{player1}: {bedwars_kills}\n↕️{p2}: {bedwars_kills2}")
		if bedwars_beds_broken > bedwars_beds_broken2:
			comparebed.add_field(name=f"Bedwars Beds Broken:", value=f"⬆️{player1}: {bedwars_beds_broken}\n⬇️{p2}: {bedwars_beds_broken2}")
		elif bedwars_beds_broken2 > bedwars_beds_broken:
			comparebed.add_field(name=f"Bedwars Beds Broken", value=f"⬇️{player1}: {bedwars_beds_broken}\n⬆️{p2}: {bedwars_beds_broken2}")
		elif bedwars_beds_broken == bedwars_beds_broken2:
			comparebed.add_field(name=f"Bedwars Beds Broken:", value=f"↕️{player1}: {bedwars_beds_broken}\m↕️{p2}: {bedwars_beds_broken2}")
		if thebridge_wins > thebridge_wins2:
			comparebed.add_field(name=f"The Bridge Wins:", value=f"⬆️{player1}: {thebridge_wins}\n⬇️{p2}: {thebridge_wins2}")
		elif thebridge_wins2 < thebridge_wins:
			comparebed.add_field(name=f"The Bridge Wins:", value=f"⬇️{player1}: {thebridge_wins}\n⬆️{p2}: {thebridge_wins2}")
		elif thebridge_wins == thebridge_wins2:
			comparebed.add_field(name=f"The Bridge Wins:", value=f"↕️{player1}: {thebridge_wins}\n↕️{p2}: {thebridge_wins2}")
		if thebridge_goals > thebridge_goals2:
			comparebed.add_field(name=f"The Bridge Goals:", value=f"⬆️{player1}: {thebridge_goals}\n⬇️{p2}: {thebridge_goals2}")
		elif thebridge_goals2 > thebridge_goals:
			comparebed.add_field(name=f"The Bridge Goals:", value=f"⬇️{player1}: {thebridge_goals}\n⬆️{p2}: {thebridge_goals2}")
		elif thebridge_goals == thebridge_goals2:
			comparebed.add_field(name=f"The Bridge Goals:", value=f"↕️{player1}: {thebridge_goals}\n↕️{p2}: {thebridge_goals2}")
		if duelwinreal > duelwinreal2:
			comparebed.add_field(name=f"Duels Wins:", value=f"⬆️{player1}: {duelwinreal}\n⬇️{p2}: {duelwinreal2}")
		elif duelwinreal2 > duelwinreal:
			comparebed.add_field(name=f"Duels Wins:", value=f"⬇️{player1}: {duelwinreal}\n⬆️{p2}: {duelwinreal2}")
		elif duelwinreal == duelwinreal2:
			comparebed.add_field(name=f"Duels Wins:", value=f"↕️{player1}: {duelwinreal}\n↕️{p2}: {duelwinreal2}")
		if duel_elo > duel_elo2:
			comparebed.add_field(name=f"Duels ELO:", value=f"⬆️{player1}: {duel_elo}\n⬇️{p2}: {duel_elo2}")
		elif duel_elo2 > duel_elo:
			comparebed.add_field(name=f"Duels ELO:", value=f"⬇️{player1}: {duel_elo}\n⬆️{p2}: {duel_elo2}")
		elif duel_elo == duel_elo2:
			comparebed.add_field(name=f"Duels ELO:", value=f"↕️{player1}: {duel_elo}\n↕️{p2}: {duel_elo2}")
		if UHC_wins > UHC_wins2:
			comparebed.add_field(name=f"UHC Wins:", value=f"⬆️{player1}: {UHC_wins}\n⬇️{p2}: {UHC_wins2}")
		elif UHC_wins2 > UHC_wins: 
			comparebed.add_field(name=f"UHC Wins:", value=f"⬇️{player1}: {UHC_wins}\n⬆️{p2}: {UHC_wins2}")
		elif UHC_wins == UHC_wins2:
			comparebed.add_field(name=f"UHC Wins:", value=f"↕️{player1}: {UHC_wins}\n↕️{p2}: {UHC_wins2}")
		if UHC_kills > UHC_kills2:
			comparebed.add_field(name=f"UHC Kills:", value=f"⬆️{player1}: {UHC_kills}\n⬇️{p2}: {UHC_kills2}")
		elif UHC_kills2 > UHC_kills:
			comparebed.add_field(name=f"UHC Kills:", value=f"⬇️{player1}: {UHC_kills}\n⬆️{p2}: {UHC_kills2}")
		elif UHC_kills == UHC_kills2:
			comparebed.add_field(name=f"UHC Kills:", value=f"↕️{player1}: {UHC_kills}\n↕️{p2}: {UHC_kills2}")
		await ctx.send(embed=comparebed)
@bot.command()
async def lb(ctx, *, leaderboard):
	req = requests.get("https://api.hyperlandsmc.net/leaderboards")
	req = req.json()
	leaderboards = req[f"{leaderboard}"]

	leaderboard1str = " - ".join([str(elem) for elem in leaderboards[0]])
	leaderboard2str = " - ".join([str(elem) for elem in leaderboards[1]])
	leaderboard3str = " - ".join([str(elem) for elem in leaderboards[2]])
	leaderboard4str = " - ".join([str(elem) for elem in leaderboards[3]])
	leaderboard5str = " - ".join([str(elem) for elem in leaderboards[4]])
	leaderboard6str = " - ".join([str(elem) for elem in leaderboards[5]])
	leaderboard7str = " - ".join([str(elem) for elem in leaderboards[6]])
	leaderboard8str = " - ".join([str(elem) for elem in leaderboards[7]])
	leaderboard9str = " - ".join([str(elem) for elem in leaderboards[8]])
	leaderboard10str = " - ".join([str(elem) for elem in leaderboards[9]])
	leaderboard11str = " - ".join([str(elem) for elem in leaderboards[10]])
	leaderboard12str = " - ".join([str(elem) for elem in leaderboards[11]])
	leaderboard13str = " - ".join([str(elem) for elem in leaderboards[12]])
	leaderboard14str = " - ".join([str(elem) for elem in leaderboards[13]])
	leaderboard15str = " - ".join([str(elem) for elem in leaderboards[14]])
	leaderboard16str = " - ".join([str(elem) for elem in leaderboards[15]])
	leaderboard17str = " - ".join([str(elem) for elem in leaderboards[16]])
	leaderboard18str = " - ".join([str(elem) for elem in leaderboards[17]])
	leaderboard19str = " - ".join([str(elem) for elem in leaderboards[18]])
	leaderboard20str = " - ".join([str(elem) for elem in leaderboards[19]])
	leaderboard21str = " - ".join([str(elem) for elem in leaderboards[20]])
	############################################################################################################
	embed1 = discord.Embed(title=f"{leaderboard} Leaderboards 1/2", description=f"""`
1. {leaderboard1str}
2. {leaderboard2str}
3. {leaderboard3str}
4. {leaderboard4str}
5. {leaderboard5str}
6. {leaderboard6str}
7. {leaderboard7str}
8. {leaderboard8str}
9. {leaderboard9str}
10. {leaderboard10str}`""", color=discord.Color.blue())
	embed1.set_author(name=f"Requested by {ctx.message.author}", icon_url=f"{ctx.message.author.avatar.url}")
	############################################################################################################
	embed2 = discord.Embed(title=f"{leaderboard} Leaderboards, Page 2/2", description=f"""`
11. {leaderboard11str}
12. {leaderboard12str}
13. {leaderboard13str}
14. {leaderboard14str}
15. {leaderboard15str}
16. {leaderboard16str}
17. {leaderboard17str}
18. {leaderboard18str}
19. {leaderboard19str}
20. {leaderboard20str}`""",color=discord.Color.blue())
	embed2.set_author(name=f"Requested by: {ctx.message.author}", icon_url=ctx.message.author.avatar.url)
	############################################################################################################
	message = await ctx.send(embed=embed1)
	pages = 2
	cur_page = 1
	await message.add_reaction("◀️")
	await message.add_reaction("▶️")
	def check(reaction, user):
		return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

	while True:
		try:
			reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            
			if str(reaction.emoji) == "▶️" and cur_page == 1:
				cur_page += 1
				await message.edit(embed=embed2)
				await message.remove_reaction(reaction, user)

			elif str(reaction.emoji) == "◀️" and cur_page == 2:
				cur_page -= 1
				await message.edit(embed=embed1)
				await message.remove_reaction(reaction, user)

			elif str(reaction.emoji) == "▶️" and cur_page == 2:
				await message.remove_reaction(reaction, user)
				await message.edit(embed=embed1)
			elif str(reaction.emoji) == "◀️" and cur_page == 2:
				await message.edit(embed=embed1)
				await message.remove_reaction(reaction, user)
		except asyncio.TimeoutError:
			await message.remove_reaction("▶️")
			await message.remove_reaction("◀️")
			break
@stats.error
async def stats_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        error = error.original
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"Invalid syntax!", description=f"Usage: -stats <player>", color=discord.Color.red())
        embed.set_footer(text="Arguments in <> are required, and arguments in [] are not required.")
        await ctx.send(embed=embed)
    if isinstance(error, KeyError):
        embed = discord.Embed(title=f"Invalid player detected!", description="Please check the capitalization and spelling for the player, and retry",color=discord.Color.red())
        await ctx.send(embed=embed)
@compare.error
async def compare_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        error = error.original
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title=f"Invalid syntax!", description=f"Usage: -compare <player1> <player2>", color=discord.Color.red())
        embed.set_footer(text="Arguments in <> are required and arguments in [] are not required.")
        await ctx.send(embed=embed)
    if isinstance(error, KeyError):
        embed = discord.Embed(title=f"Invalid player(s) detected!", description=f"Please check the capitalization and spelling for the player(s) and retry.", color=discord.Color.red())
        await ctx.send(embed=embed)
@lb.error
async def lb_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        error = error.original
        pass
    elif isinstance(error, KeyError):
        embed=discord.Embed(title=f"Invalid leaderboard detected!", color=discord.Color.red())
        await ctx.send(embed=embed)
bot.run(TOKEN)
