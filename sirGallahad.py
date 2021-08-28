import discord
import asyncio
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

########
# Knights
########
knightServerRolesID = [
    801188644932288553, # new comer 0
    776862867919208478, # main tank 1
    776863053534855238, # flex tank 2
    776863668171964417, # projectile dps 3
    776863489301938237, # hitscan dps 4
    776872636059746335, # main support 5
    776872509961797642, # flex support 6
    798775020364103710, # head coach 7
    798775235289284628, # assistant coach 8
    798775467863703592, # analyst 9
    794996146178097162, # assistant manager 0
    799028318954848286, # lobby manager 1
    798774735273459762, # vod recorder 2
    798776537389596672, # legal assistant 3
    798774288214655002, # content creator and editor 4
    799029075113017364, # programmer 5
    798775481293340682, # developer 6
    799029391794896916, # graphic designer and developer 7
    798775728811671602, # video editing and content creator 8
    797514615252189225, # streamer 9
    798992996728176739, # journalist 0
    797514408384266271, # social media manager 1
    798776882039881769, # school tutoring 2
    799029843513049109, # twitch channel production lead 3
    794980063930089502, # NA 4
    794979984350511104, # EU 5
    784853059376775189, # players to interview 6
    794845156339613747, # staff to interview 7
    794845618874351646  # coaches to interview 8
    ]
    
knightsChanID = 799399499864211537

knightsStaffPositionsStr = [ 
    "Assistant Manager",
    "Lobby Manager",
    "VOD recorder",
    "Legal Assistant",
    "Content creator/Editor",
    "Programmer",
    "Developer",
    "Graphic Designer/developer",
    "Video editing/content creator",
    "streamer",
    "Journalist",
    "Social Media Manager",
    "School Tutoring",
    "Twitch channel production lead"
    ]
    
knightsCoachPositionsStr = [
    "Coach",
    "Assistant Coach",
    "Analyst"
    ]
    
knightsTeamPositionsStr = [
    "Main Tank",
    "Off Tank",
    "Projectile DPS",
    "Hitscan DPS",
    "Main Support",
    "Flex support"
    ]

merlinPlayerPositionsXtraStr = [
    "Main Tank",
    "Off Tank",
    "Flex Tank",
    "Flex DPS",
    "Hitscan DPS",
    "Main support",
    "Flex Support",
    "OTP player please specifiy your specialty when posting your ad."
    ]

merlinPlayerPositionsRegStr = [
    "Main Tank",
    "Off Tank",
    "Hitscan DPS",
    "Flex DPS",
    "Main Support",
    "Flex Support"
    ]

merlinRoleLookingForStr = [
    "Player",
    "Manager",
    "Assistant Manager",
    "Coach",
    "Assistant Coach",
    "Social Media Manager",
    "Editor",
    "Developer",
    "Programmer"
    ]

merlinCurrentRoleStr = [
    "Org owner",
    "Manager",
    "Assistant Manager",
    "Coach",
    "Assistant Coach",
    "Player"
    ]

merlinContentCreators = [
    "Caster",
    "streamer",
    "VOD recorder",
    "camera men",
    "montages",
    "GFX",
    "Musician"
    ]

#######
# test server
#######
testServerRolesID = [
        801223240819277824, # new comer 0
        798660624905142273, # main tank 1
        798660832305086475, # flex tank 2
        797893508077715509, # projectile dps 3
        797233209536151552, # hitscan dps 4
        801956112248995869, # main support 5
        801956128685817927, # flex support 6
        798971361279344681, # head coach 7
        798971374088618054, # assistant coach 8
        798971622844399616, # analyst 9
        801956135426588682, # assistant manager0
        801956138568384582, # lobby manager 1
        801956142346403860, # vod recorder 2
        801956144246816788, # legal assistant 3
        801956145627398154, # content creator and editor 4
        800175616967311381, # programmer 5
        801956148033880065, # developer 6
        801956149715795986, # graphic designer and developer 7
        801956152001953822, # video editing and content creator 8
        801956153416089610, # streamer 9
        801956155017658368, # journalist 0
        801956156489859104, # social media manager 1
        801956158410588191, # school tutoring 2
        801956160026443776, # twitch channel production lead 3
        793360510271488050, # NA 4
        796965297189945395, # EU 5
        798662135693574155, # players to interview 6
        798662169528238152, # staff to interview 7
        801956164131749898  # coaches to interview 8
    ]
    
testServerChanID = 793351956210384910

###########
# Merlin Server
###########
merlinServerRolesID = [
    852331423552634880, # newcomers 0
	828084249042092063, # staff to interview 1
	851301334304686090, # LFT 2
	851301497954500608, # LFP 3
	851302490439811092, # NA 4
	851313938812370954, # EU 5
	828086417460166666, # players 6
	828086520039604284, # managers 7
	828087041987969055, # coaches 8
	828087374834565120, # assistant coach 9
	851314517887418419, # social media manager 0
	851314980456366081, # editor 1
	851316591567175680, # main tank 2
	851316707782950943, # off tank 3
	851316791938121760, # flex tank 4
	851316859848622080, # flex dps 5
	851317006032306177, # hitscan dps 6
	851317113175146588, # main support 7
	851317491757350916, # flex support 8
	851317193647325224, # OTP 9
    851315077172691015, # Programmer 0
    828088024913936384, # Casters 1
    828088074792599582, # Streamers 2
    828087819616124939, # Vod recorders 3
    851317798574620702, # Camera Men 4
    851317958893764639, # Montages 5
    828088165310398514, # GFX 6
    851318159063777301, # Musician 7
    851301645991673887, # LF-Staff 8
    851313759360253962, # LFC 9
    828086820805017650, # Org owners 0
    852712868180393985, # Assistant managers 1
    851315182894317588  # Developer 2
   ]
merlinServerChanID = 851312448408649739

@client.event
async def on_ready():
    print("I'm ready")

welcomeMessage = [":fire: Welcome to the Excalibur Knights server! :fire: \nHere's the steps you need to know in order to set yourself up to tryout for the team\n",
                  "(If you're a ringer the following does not partain to you, thank you for taking the time to ring for us we appreciate it)\n\n",
                  ":one:Go ahead and fill out the appropriate form for your region after which you'll be given your starter roles\n",
                  ":two:These roles will give you access to the interview channel where you'll post your region/sr/role along with the day and time your available for a no more than 20 min interview\n",
                  ":three:This interview will give you all the information you need to know along with scheduling/rules/coaching/tournaments as well as answering any questions you may have\n\n",
                  "For any questions or concerns plz feel free to dm Sparrow the server owner or your recruitment contact to help sort everything out\nThank you and we look forward to you trialing for the team!\n"
                  ]
welcomeMessageFinal = welcomeMessage[0] + welcomeMessage[1] + welcomeMessage[2] + welcomeMessage[3] + welcomeMessage[4] + welcomeMessage[5]

warning = "You have 45 min to submit the appropriate form before you are kicked from the server"

guilder = client.get_guild(695831785900081212)

def testServerRoleObjCreation():


@client.event
async def on_member_join(member):
    joiner = await member.create_dm()
    await joiner.send(welcomeMessageFinal)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f'{dt_string}')
    print(f'{member} joined the server')

    ## This works for excalibur knights specifically cuz the other server has another bot giving newcomers role
    guild = client.get_guild(695831785900081212)
    newComer = member.guild.get_role(801188644932288553)
    await member.add_roles(newComer)
    await asyncio.sleep(10800)
    
    channel = await member.create_dm()
    if newComer in member.roles:
        await channel.send(warning)
    await asyncio.sleep(2700)

    member_renewed = guild.get_member(member.id)
    if newComer in member_renewed.roles:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'{dt_string}')
        print(f'{member} did not submit the form and was kicked')
        await member.kick()

@client.event
async def on_message(message):
    if message.channel.id == testServerChanID:
        newComers = message.guild.get_role(testServerRolesID[0])
        mainTank = message.guild.get_role(testServerRolesID[1])
        flexTank = message.guild.get_role(testServerRolesID[2])
        projectile = message.guild.get_role(testServerRolesID[3])
        hitscan = message.guild.get_role(testServerRolesID[4])
        mainSupport = message.guild.get_role(testServerRolesID[5])
        flexSupport = message.guild.get_role(testServerRolesID[6])
        headCoach = message.guild.get_role(testServerRolesID[7])
        assistantCoach = message.guild.get_role(testServerRolesID[8])
        analyst = message.guild.get_role(testServerRolesID[9])
        assistantManager = message.guild.get_role(testServerRolesID[10])
        lobbyManager = message.guild.get_role(testServerRolesID[11])
        vodRecorder = message.guild.get_role(testServerRolesID[12])
        legalAssistant = message.guild.get_role(testServerRolesID[13])
        contentCreatorEditor = message.guild.get_role(testServerRolesID[14])
        programmer = message.guild.get_role(testServerRolesID[15])
        developer = message.guild.get_role(testServerRolesID[16])
        graphicDesignerDev = message.guild.get_role(testServerRolesID[17])
        vidEditingContentCreator = message.guild.get_role(testServerRolesID[18])
        streamer = message.guild.get_role(testServerRolesID[19])
        journalist = message.guild.get_role(testServerRolesID[20])
        socialMediaManager = message.guild.get_role(testServerRolesID[21])
        schoolTutoring = message.guild.get_role(testServerRolesID[22])
        twitchChannelProduction = message.guild.get_role(testServerRolesID[23])
        na = message.guild.get_role(testServerRolesID[24])
        eu = message.guild.get_role(testServerRolesID[25])
        playersToInterview = message.guild.get_role(testServerRolesID[26])
        staffToInterview = message.guild.get_role(testServerRolesID[27])
        coachesToInterview = message.guild.get_role(testServerRolesID[28])

        knightServerRolesObj = [
            newComers, mainTank, flexTank, projectile, hitscan,
            mainSupport, flexSupport, headCoach, assistantCoach,
            analyst, assistantManager, lobbyManager, vodRecorder,
            legalAssistant, contentCreatorEditor, programmer,
            developer, graphicDesignerDev, vidEditingContentCreator,
            streamer, journalist, socialMediaManager, schoolTutoring,
            twitchChannelProduction, na, eu, playersToInterview,
            staffToInterview, coachesToInterview
        ]
   
    elif message.channel.id == knightsChanID:
        newComers = message.guild.get_role(knightServerRolesID[0])
        mainTank = message.guild.get_role(knightServerRolesID[1])
        flexTank = message.guild.get_role(knightServerRolesID[2])
        projectile = message.guild.get_role(knightServerRolesID[3])
        hitscan = message.guild.get_role(knightServerRolesID[4])
        mainSupport = message.guild.get_role(knightServerRolesID[5])
        flexSupport = message.guild.get_role(knightServerRolesID[6])
        headCoach = message.guild.get_role(knightServerRolesID[7])
        assistantCoach = message.guild.get_role(knightServerRolesID[8])
        analyst = message.guild.get_role(knightServerRolesID[9])
        assistantManager = message.guild.get_role(knightServerRolesID[10])
        lobbyManager = message.guild.get_role(knightServerRolesID[11])
        vodRecorder = message.guild.get_role(knightServerRolesID[12])
        legalAssistant = message.guild.get_role(knightServerRolesID[13])
        contentCreatorEditor = message.guild.get_role(knightServerRolesID[14])
        programmer = message.guild.get_role(knightServerRolesID[15])
        developer = message.guild.get_role(knightServerRolesID[16])
        graphicDesignerDev = message.guild.get_role(knightServerRolesID[17])
        vidEditingContentCreator = message.guild.get_role(knightServerRolesID[18])
        streamer = message.guild.get_role(knightServerRolesID[19])
        journalist = message.guild.get_role(knightServerRolesID[20])
        socialMediaManager = message.guild.get_role(knightServerRolesID[21])
        schoolTutoring = message.guild.get_role(knightServerRolesID[22])
        twitchChannelProduction = message.guild.get_role(knightServerRolesID[23])
        na = message.guild.get_role(knightServerRolesID[24])
        eu = message.guild.get_role(knightServerRolesID[25])
        playersToInterview = message.guild.get_role(knightServerRolesID[26])
        staffToInterview = message.guild.get_role(knightServerRolesID[27])
        coachesToInterview = message.guild.get_role(knightServerRolesID[28])

        knightServerRolesObj = [
            newComers, mainTank, flexTank, projectile, hitscan,
            mainSupport, flexSupport, headCoach, assistantCoach,
            analyst, assistantManager, lobbyManager, vodRecorder,
            legalAssistant, contentCreatorEditor, programmer,
            developer, graphicDesignerDev, vidEditingContentCreator,
            streamer, journalist, socialMediaManager, schoolTutoring,
            twitchChannelProduction, na, eu, playersToInterview,
            staffToInterview, coachesToInterview
        ]

    elif message.channel.id == merlinServerChanID:
        newcomers = message.guild.get_role(merlinServerRolesID[0])
        stafftointerview = message.guild.get_role(merlinServerRolesID[1])
        LFT = message.guild.get_role(merlinServerRolesID[2])
        LFP = message.guild.get_role(merlinServerRolesID[3])
        NA = message.guild.get_role(merlinServerRolesID[4])
        EU = message.guild.get_role(merlinServerRolesID[5])
        players = message.guild.get_role(merlinServerRolesID[6])
        managers = message.guild.get_role(merlinServerRolesID[7])
        coaches = message.guild.get_role(merlinServerRolesID[8])
        assistantCoach = message.guild.get_role(merlinServerRolesID[9])
        socialMediaManager = message.guild.get_role(merlinServerRolesID[10])
        editor = message.guild.get_role(merlinServerRolesID[11])
        mainTank = message.guild.get_role(merlinServerRolesID[12])
        offTank = message.guild.get_role(merlinServerRolesID[13])
        flexTank = message.guild.get_role(merlinServerRolesID[14])
        flexDPS = message.guild.get_role(merlinServerRolesID[15])
        hitscanDPS = message.guild.get_role(merlinServerRolesID[16])
        mainSupport = message.guild.get_role(merlinServerRolesID[17])
        flexSupport = message.guild.get_role(merlinServerRolesID[18])
        OTP = message.guild.get_role(merlinServerRolesID[19])
        programmer = message.guild.get_role(merlinServerRolesID[20])
        caster = message.guild.get_role(merlinServerRolesID[21])
        streamer = message.guild.get_role(merlinServerRolesID[22])
        vodRecorder = message.guild.get_role(merlinServerRolesID[23])
        cameraMen = message.guild.get_role(merlinServerRolesID[24])
        montages = message.guild.get_role(merlinServerRolesID[25])
        gfx = message.guild.get_role(merlinServerRolesID[26])
        musician = message.guild.get_role(merlinServerRolesID[27])
        LFS = message.guild.get_role(merlinServerRolesID[28])
        LFC = message.guild.get_role(merlinServerRolesID[29])
        orgOwner = message.guild.get_role(merlinServerRolesID[30])
        assistantManagers = message.guild.get_role(merlinServerRolesID[31])
        developer = message.guild.get_role(merlinServerRolesID[32])


        knightServerRolesObj = [
            newcomers, NA, EU, LFT, players, managers, assistantManagers, coaches, assistantCoach,
            socialMediaManager, editor, developer, programmer, mainTank, offTank, flexTank, flexDPS,
            hitscanDPS, mainSupport, flexSupport, OTP, LFP, LFS, LFC, orgOwner, managers, assistantManagers,
            coaches, assistantCoach, players, mainTank, offTank, hitscanDPS, flexDPS, mainSupport,
            flexSupport, caster, streamer, vodRecorder, cameraMen, montages, gfx, musician
        ]

    coachingRole = ""
    staffingRole = ""
    teamRoleApp = ""
    playRegion = ""
    EUapp = ""
    NAapp = ""
    regionApp = ""
    discordUsername = ""

    NAplayer = ""
    EUplayer = ""
    staff = False
    NA = False
    EU = False
    staffRolesSTR = []
    coachingRolesSTR = []
    playerRolesSTR = []
    myself = message.guild.get_member(464936463830876160)
        
    if len(message.embeds) > 0 and message.channel.id != merlinServerChanID:
        numFields = len(message.embeds[0].fields)
        embedFields = message.embeds[0].fields
        for fields in embedFields:
            if fields.name == "Please Enter Your Discord tag" or fields.name == "Please Enter Your Discord" or fields.name == "Discord tag" or fields.name == "Please enter your exact discord id?":
                discordUsername = fields.value
                break 
        if discordUsername != "":
            user = message.guild.get_member_named(discordUsername)
            if user != None:
                await user.remove_roles(knightServerRolesObj[0][0])
                for field in embedFields:
                    if field.name == "Which region are you applying for?":
                        regionApp = field.value
                        if regionApp == "NA":
                            await user.add_roles(knightServerRolesObj[24][0])
                            NA = True
                        elif regionApp == "EU":
                            await user.add_roles(knightServerRolesObj[25][0])
                            EU = True
                    elif field.name == "Which role?" or field.name == "Which role are you applying for?" or field.name == "Which role are you applying for? (cont.)":
                        if field.value:
                            index = 1
                            await user.add_roles(knightServerRolesObj[26][0])
                            for poz in knightsTeamPositionsStr:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index][0])
                                    playerRolesSTR.append(poz)
                                index += 1
                    elif field.name == "Which coaching position are you applying for?":
                        if field.value:
                            index = 7
                            await user.add_roles(knightServerRolesObj[28]) # coach to apply role
                            for pos in knightsCoachPositionsStr:
                                if field.value == pos:
                                    await user.add_roles(knightServerRolesObj[index][0])
                                    coachingRolesSTR.append(pos)
                                index += 1
                    elif field.name == "Which Staff Position are you applying for?" or field.name == "Which Staff Position are you applying for? (cont.)":
                        if field.value:
                            index = 10
                            staff = True
                            await user.add_roles(knightServerRolesObj[27][0]) # staff to apply role
                            for positions in knightsStaffPositionsStr:
                                if field.value == positions:
                                    await user.add_roles(knightServerRolesObj[index][0])
                                    staffRolesSTR.append(positions)
                                index += 1

                desc = ""
                if NAplayer != "":
                    desc = NAplayer
                elif EUplayer != "":
                    desc = EUplayer
                elif staff:
                    desc = "Staff Application"

                #### What I want to know ####
                # username, staff vs player vs coach, sr, roles

                #### Create the initial embed object ####
                embed=discord.Embed(title=f"{user} submitted the form", description=desc, color=0x109319)
                if playerRolesSTR:
                    embed.add_field(name="Player Role", value=playerRolesSTR[0], inline=False)

                chan = await myself.create_dm()
                await chan.send(embed=embed)

            else:
                print("ERROR 101: user is null")

        else:
            print("ERROR 100: user not found")

    #### MERLIN ONLY ####

    elif len(message.embeds) > 0 and message.channel.id == merlinServerChanID:
        numFields = len(message.embeds[0].fields)
        embedFields = message.embeds[0].fields
        for fields in embedFields:
            if fields.name == "Please enter your exact discord id?":
                discordUsername = fields.value
                break 
        if discordUsername != "":
            user = message.guild.get_member_named(discordUsername)
            if user != None:
                for field in embedFields:
                    if field.name == "Which region are you applying for?" or field.name == "Which region are you applying for? (cont.)": 
                        regionApp = field.value
                        if regionApp == "NA":
                            await user.add_roles(knightServerRolesObj[1])
                            NA = True
                        elif regionApp == "EU":
                            await user.add_roles(knightServerRolesObj[2])
                            EU = True
                    elif field.name == "Are you looking for a team? LFT":
                        if field.value == "Yes":
                            index = 1
                            ## LFT ##
                            await user.add_roles(knightServerRolesObj[3])
                    elif field.name == "Which role are you looking for?" or field.name == "Which role are you looking for? (cont.)":
                        if field.value:
                            index = 4
                            ## PLAYER, MANAGER, ASSIST MANAGER, COACH, ASSISTANT COACH, SOCIAL MEDIA MANAGER, EDITOR, DEVELOPER, PROGRAMMER ##
                            for poz in merlinRoleLookingForStr:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index])
                                    playerRolesSTR.append(poz)
                                index += 1
                    elif field.name == "For players looking for a team which role are you looking for?" or field.name == "For players looking for a team which role are you looking for? (cont.)":
                        if field.value:
                            index = 13
                            ## MAINTANK, OFFTANK, FLEXTANK, FLEXDPS, HITSCANDPS, MAINSUPPORT, FLEXSUPPORT, OTP LAYER PLEASE SPECIFY YOUR SPECIALTY WHEN POSTING YOUR AD ##
                            for poz in merlinPlayerPositionsXtraStr:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index])
                                    playerRolesSTR.append(poz)
                                index += 1
                    elif field.name == "Are you looking for Players? LFP":
                        if field.value == "Yes":
                            ## LFP ##
                            await user.add_roles(knightServerRolesObj[21])
                    elif field.name == "Are you looking for Staff? LF-Staff":
                        if field.value == "Yes":
                            ## LFS ##
                            await user.add_roles(knightServerRolesObj[22])
                    elif field.name == "Are you looking for a Coach? LFC":
                        if field.value == "Yes":
                            ## LFC ##
                            await user.add_roles(knightServerRolesObj[23])
                    elif field.name == "Which is your current role?" or field.name == "Which is your current role? (cont.)":
                        if field.value:
                            index = 24
                            ## ORGOWNER, MANAGER, ASSISTANT MANAGER, COACH, ASSISTANT COACH, PLAYER ##
                            for poz in merlinCurrentRoleStr:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index])
                                    playerRolesSTR.append(poz)
                                index += 1
                    elif field.name == "Which role or roles can you ring?" or field.name == "Which role or roles can you ring? (cont.)":
                        if field.value:
                            index = 30
                            ## MAIN TANK, OFF TANK, HITSCAN DPS, FLEX DPS, MAIN SUPPORT, FLEX SUPPORT ##
                            for poz in merlinPlayerPositionsRegStr:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index])
                                    playerRolesSTR.append(poz)
                                index += 1
                    elif field.name == "For content creators only" or field.name == "For content creators only (cont.)":
                        if field.value:
                            index = 36
                            ## CASTER, STREAMER, VOD RECORDER, CAMERA MEN, MONTAGES, GFX, MUSICIAN ##
                            for poz in merlinContentCreators:
                                if field.value == poz:
                                    await user.add_roles(knightServerRolesObj[index])
                                    playerRolesSTR.append(poz)
                                index += 1
                else:
                    print("ERROR 101: User is null")

            else:
                print("ERROR 100: User not found")

client.run('ODAyNjY4ODUxNDM0NDg3ODMw.YAylnw.6liyEc11GCMnCYFulkjsLRYACDc')