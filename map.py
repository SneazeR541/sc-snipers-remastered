#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a template to make a copy of.


# This must go at the top.
import sys
sys.path.insert(0, 'F:\\PythonPrograms\\TriGen.beta.0.0.5\\TriGen')
from config import *

#Your code goes in here:
# https://stackoverflow.com/a/5655803
from itertools import chain, izip, repeat, islice

def intersperse(delimiter, seq):
    return islice(chain.from_iterable(izip(repeat(delimiter), seq)), 1, None)

deathStates = {
    "ALIVE": 0,
    "DISPLAYING_MESSAGE": 1,
    "WAITING_FOR_TIMER": 2,
    "RESPAWNING": 3
}

leaderboardStates = {
    "MVP": 0,
    "KILLS": 1,
    "DEATHS": 2,
    "BONUSES": 3,
    "FLAGS": 4
}

loc = {
    "topCliff": {
        "entryLow": Location("001"),
        "entryHigh": Location("002"),
        "exitHigh": Location("003"),
        "exitLow": Location("004")
    },
    "bottomCliff": {
        "exitLow": Location("005"),
        "exitHigh": Location("006"),
        "entryLow": Location("007"),
        "entryHigh": Location("008")
    },
    "topBase": {
        "base": Location("009"),
        "leftRs": Location("010"),
        "rightRs": Location("011"),
        "midRs": Location("012"),
        "leftTurret": Location("013"),
        "rightTurret": Location("014"),
        "flag": Location("015"),
        "antiCamp": Location("049"),
        "antiCampBuffer": Location("053"),
    },
    "bottomBase": {
        "base": Location("023"),
        "leftRs": Location("024"),
        "rightRs": Location("025"),
        "midRs": Location("026"),
        "leftTurret": Location("028"),
        "rightTurret": Location("029"),
        "flag": Location("027"),
        "antiCamp": Location("050"),
        "antiCampBuffer": Location("055"),
    },
    "hotTeam": {
        "base": Location("016"),
        "leftTurret": Location("017"),
        "rightTurret": Location("018"),
        "leftRs": Location("019"),
        "rightRs": Location("021"),
        "midRs": Location("020"),
        "flag": Location("022"),
        "antiCamp": Location("051"),
        "antiCampBuffer": Location("054"),
    },
    "coldTeam": {
        "base": Location("030"),
        "leftTurret": Location("033"),
        "rightTurret": Location("034"),
        "leftRs": Location("031"),
        "rightRs": Location("032"),
        "midRs": Location("035"),
        "flag": Location("036"),
        "antiCamp": Location("052"),
        "antiCampBuffer": Location("056"),
    },
    "ss": {
        4: Location("038"),
        5: Location("037"),
        6: Location("039"),
        7: Location("043"),
        0: Location("041"),
        1: Location("040"),
        2: Location("042"),
        3: Location("044"),
        "p3-2": Location("046")
    },
    "bottomLeftBaseVisUnit": Location("047"),
    "bottomLeftOtherUnits": Location("048"),
    "moveOverSniper": Location("057"),
    "unreachable": Location("058"),
    "rightSide": Location("000"),
    "everywhere": Location("045")
}

custom_sound_names = [
    # UT sounds
    "capture",
    "cd1min",
    "dominating",
    "godlike",
    "killingspree",
    "lostlead",
    "lostmatch",
    "monsterkill",
    "multikill",
    "rampage",
    "takenlead",
    "triplekill",
    "ultrakill",
    "unstoppable",
    "winner",
    # Halo sounds
    "killfrenzy",
    "flag_returned",
    "flag_captured",
    
]

custom_sounds = {name: "staredit\\\\wav\\\\" + name + ".wav" for name in custom_sound_names}

sounds = {
    # Built-in sounds go here
    "gameStart": "sound\\\\Bullet\\\\Tfrhit.wav",
    "flagCaptureEffect": "sound\\\\Bullet\\\\tscFir00.wav",
    "flagReturnEffect": "sound\\\\Misc\\\\Door\\\\Door4Opn.wav"
}
sounds.update(custom_sounds)

streaks = [
    (3, "triplekill"),
    (5, "killingspree"),
    (7, "ultrakill"),
    (10, "rampage"),
    (15, "unstoppable"),
    (20, "godlike"),
]


hotTeam = "Team HOT - 10/29/2018 5.0a"
coldTeam = "Team COLD - 3oD[LaZeR]"

hotIndices = [i for i in range(4)]
coldIndices = [i for i in range(4, 8)]
allIndices = hotIndices + coldIndices

hotPlayers = [Player(i) for i in range(1, 5)]
coldPlayers = [Player(i) for i in range(5, 9)]
allPlayers = hotPlayers + coldPlayers

foes = "Foes"
all = "All"
cp = "Current Player"

sniper = "Terran Ghost"
exactly = "Exactly"
atMost = "At Most"
atLeast = "At Least"
setTo = "Set To"
kills = "Kills"
ore = "ore"
gas = "gas"
add = "Add"
subtract = "subtract"
flagUnit = "Flag"
neutral = 12
disabled = "disabled"
enabled = "enabled"
buildings = "Buildings"
razings = "Razings"

mvpUnit = "Zerg Defiler"
bottomLeftVisUnit = "Data Disc"
invincibilityExpiredUnit = "Zerg Zergling"
baseVisUnit = "Terran Marine"
#turretUnit = "Hyperion (Battlecruiser)"
turretUnit = "Sarah Kerrigan (Ghost)"
turretUnit2 = "Vulture Spider Mine"

leaderboardTransitionTime = 35

# Death counters
dc = {
    "kills": DC(cp),
    "deaths": DC(cp),
    "flags": DC(cp),
    "bonuses": DC(cp),
    "mvp": DC(cp),
    "resetMVP": DC(cp),
    "killsThisLife": DC(cp),
    "bonus": DC(cp),
    "hasFlag": DC(cp),
    "died": DC(cp),
    "rs": DC(cp),
    "rsTimer": DC(cp),
    "sounds": {
        name: DC(cp) for name, file in sounds.items()
    },
    "soundTimer": DC(cp),
    "leaderboard": DC(cp),
    "leaderboardTimer": DC(cp),
    "overtimeMessage": DC(cp),
    "baseVisTimer": DC(cp),
    "ssCenterView": DC(cp),
    "antiCampTimer": DC(cp),
}

hotFlagTaken = DC()
coldFlagTaken = DC()
hotAntiCamp = DC()
coldAntiCamp = DC()
timerPaused = DC()
swappedSides = DC()
hotWins = DC()
coldWins = DC()
hotWinsMessage = DC()
coldWinsMessage = DC()
gameOver = DC()

rsSwitch = Switch()


playerHasDiedMessages = [
    "\\x006Red has died!",
    "\\x011Orange has died!",
    "\\x003Yellow has died!",
    "\\x019Tan has died!",
    "\\x00eBlue has died!",
    "\\x00fTeal has died!",
    "\\x004White has died!",
    "\\x010Purple has died!"
]

fullTime = 30 * 60
halfTime = fullTime / 2
overtimeTime = 2 * 60

missionObjectives = "\\x013\\x006Capture the opposing teams flag\\r\\n\\x013\\x006&\\r\\n\\x013\\x006Bring it back to your base for points!\\r\\n\\x013\\x0051 Kill = 1 Point\\r\\n\\x013\\x0051 Flag = 15 Points\\r\\n\\r\\n\\x013\\x006Map By: 3oD[LaZeR]\\r\\n\\x013\\x005Join our Discord: http://tinyurl.com/SCSniperDiscord"


playerColorStartEPD = -8572
minimapColorStartEPD = -8548

# FoW update counter at http://farty1billion.dyndns.org/EUDdb/?pg=entry&id=771

# Player colors
# http://blog.naver.com/PostView.nhn?blogId=kein0011&logNo=221140953219#
# http://www.staredit.net/topic/17526/#11
# Default colors P1-12: Red, Blue, Teal, Purple, Orange, Brown, White, Yellow, ?, ?, ?, Neutral Blue
# Default colors P1-12: 111, 165, 159, 164, 156, 19, 84, 135, 185, 136, 134, 51

# Interesting colors:
# 181 Black
# 117 Bright green
# 178 Bright red
# 84 White
# 128 Cyan
# 57 Gold
# 115 Pink
# 94    # Maroon
# 57    # Gold
# 0 Deep  black
# 23 alternative red
# 42 dark blue

multiple = 10

base = multiple * 8

p1ColorCode = base   # Red
p2ColorCode = base+1   # Orange
p3ColorCode = base+2   # Yellow
p4ColorCode = base+3    # Gold
p5ColorCode = base+4   # Blue
p6ColorCode = base+5   # Cyan
p7ColorCode = base+6   # Pink
p8ColorCode = base+7    # Maroon

# Functions

# http://www.staredit.net/topic/17526/#11

# memory layout 0index minimap colors EPD: -8548

# 11u     11u     0       1               
# 2       3       4       5       -8547
# 6       7       ?       ?       -8546

# memory layout 0index player colors EPD:-8572
# 10s     11s     0       0
# 0       0       1       1
# 1       1       2       2
# 2       2       3       3
# 3       3       4       4
# 4       4       5       5
# 5       5       6       6
# 6       6       7       7
# 7       7       8..

def setPlayerColor(playerNumber, colorCode):
    playerIndex = playerNumber - 1
    return set_deaths("Int:" + str(playerColorStartEPD + 2 * playerIndex), "Terran Marine", setTo, colorCode * 65536)

def getFlag(i):
    if isHot(i):
        return hotFlagTaken
    else:
        return coldFlagTaken

def getOtherFlag(i):
    if isHot(i):
        return coldFlagTaken
    else:
        return hotFlagTaken

def getAntiCamp(i):
    if isHot(i):
        return hotAntiCamp
    else:
        return coldAntiCamp

def getOtherAntiCamp(i):
    if isHot(i):
        return coldAntiCamp
    else:
        return hotAntiCamp

def isHot(i):
    return 0 <= i and i <= 3

def getTeamLocations(i):
    if isHot(i):
        return loc["hotTeam"]
    else:
        return loc["coldTeam"]

def getOtherTeamLocations(i):
    if isHot(i):
        return loc["coldTeam"]
    else:
        return loc["hotTeam"]

def getReplaceFlag(i):
    if isHot(i):
        return hotReplaceFlag
    else:
        return coldReplaceFlag

def getOtherReplaceFlag(i):
    if isHot(i):
        return coldReplaceFlag
    else:
        return hotReplaceFlag

def getTeam(i):
    if isHot(i):
        return hotTeam
    else:
        return coldTeam

def getTeamPlayers(i):
    if isHot(i):
        return hotPlayers
    else:
        return coldPlayers
        
def getOtherTeamPlayers(i):
    if isHot(i):
        return coldPlayers
    else:
        return hotPlayers

def getOtherTeam(i):
    if isHot(i):
        return coldTeam
    else:
        return hotTeam

def isFlagPresent(team, teamLocations):
    return [
        T(A=[forceLocationToUpdate(teamLocations["flag"])]),
        T(C=[bring(team, flagUnit, teamLocations["flag"])], A=[True]),
    ]

def forceLocationToUpdate(location):
    return remove_unit_at_location(all_players, "Map Revealer", 1, location)

def displayWelcomeMessage():
    return [
        display_text("\\x016Snipers Remastered v5.0"),
        display_text(" "),
        display_text("\\x016Changes:"),
        display_text("\t\\x016• Improved pathing in BV"),
        display_text("\t\\x016• Revamped right side terrain"),
        display_text("\t\\x016• Added MVP leaderboard"),
        display_text("\t\\x016• Added anti-camp system"),
        display_text("\t\\x016• Added new sounds"),
        display_text("\t\\x016• Fixed flagging bugs"),
        display_text(" "),
        display_text("\t\\x016Good luck and have fun!"),
    ]

def disableUnits(unit):
    return [
        give_unit(neutral, 9, unit, 1, loc["everywhere"]),
        set_doodad_state(9, unit, loc["everywhere"], disabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        give_unit(9, 10, unit, 1, loc["everywhere"]),
        
        give_unit(neutral, 9, unit, 1, loc["everywhere"]),
        set_doodad_state(9, unit, loc["everywhere"], disabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        give_unit(9, 10, unit, 1, loc["everywhere"]),
        
        give_unit(neutral, 9, unit, 1, loc["everywhere"]),
        set_doodad_state(9, unit, loc["everywhere"], disabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        give_unit(9, 10, unit, 1, loc["everywhere"]),
        
        give_unit(neutral, 9, unit, 1, loc["everywhere"]),
        set_doodad_state(9, unit, loc["everywhere"], disabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        set_doodad_state(9, unit, loc["everywhere"], enabled),
        give_unit(9, 10, unit, 1, loc["everywhere"]),
        
        give_unit(10, neutral, unit, all, loc["everywhere"]),
    ]
    
def calculateByteConcatenation(b1, b2, b3, b4):
    return b1 + (b2 * 2**8) + (b3 * 2**16) + (b4 * 2**24)

def epdAction(epd, value):
    return set_deaths("Int:" + str(epd), "Terran Marine", setTo, value)

# Set Deaths("Int:209160", "Terran Marine", Set To, 21233678);
# Set Deaths("Int:209491", "Terran Marine", Set To, 158);
# Set Deaths("Int:209888", "Terran Marine", Set To, 15205037);
# Set Deaths("Int:222136", "Terran Marine", Set To, 117639947);
# https://docs.google.com/spreadsheets/d/195jZK7Ap71eO1-qdVskC2xsVl7EbNdVp0hbh7N3D38A/edit#gid=0
# Setup
T(P=[all_players], C=[always()], A=[
    set_countdown_timer(setTo, fullTime + 1),
    set_to_ally(all_players),
    set_invincibility(all_players, baseVisUnit, loc["everywhere"]),
    set_invincibility(all_players, turretUnit, loc["everywhere"]),
    set_mission_objectives(missionObjectives),
    displayWelcomeMessage(),
    dc["sounds"]["gameStart"].set_to(1),
    #disableUnits(turretUnit),
    # # Generated using StarcraftEPDTriggers
    
    # # Change icon for C-10 Concussion Rifle to Nuclear Missile
    # epdAction(209160, 21233678),
    
    # # Change graphic for weapon C-10 Concussion Rifle to Yamato Gun
    # epdAction(209491, 158),
    
    # # Change label for weapon C-10 Concussion Rifle to "Nuclear Strike"
    # epdAction(209888, 15205037),
    
    # # Change the sight range of Vulture Spider Mine to 11
    # epdAction(222136, 117639947),
    
    # Unit colors
    # setPlayerColor(1, p1ColorCode),
    # setPlayerColor(2, p2ColorCode),
    # setPlayerColor(3, p3ColorCode),
    # setPlayerColor(4, p4ColorCode),
    # setPlayerColor(5, p5ColorCode),
    # setPlayerColor(6, p6ColorCode),
    # setPlayerColor(7, p7ColorCode),
    # setPlayerColor(8, p8ColorCode),
    
    # # Minimap colors for P3-6. First two bytes are for P12's unit color
    # epdAction(-8548, calculateByteConcatenation(0, 0, p1ColorCode, p2ColorCode)),

    # # Minimap colors for P3-6
    # epdAction(-8547, calculateByteConcatenation(p3ColorCode, p4ColorCode, p5ColorCode, p6ColorCode)),
    
    # # Minimap colors for P7-8. Last two bytes map to some unknown region
    # epdAction(-8546, calculateByteConcatenation(p7ColorCode, p8ColorCode, 0, 0))
    
], just_once=True)

# Keep kerrigan energy up
T(P=[all_players], C=[always()], A=[
    modify_unit_energy(all_players, turretUnit, 100, all, loc["everywhere"]),
    move_unit(all_players, turretUnit, all, loc["everywhere"], loc["unreachable"])
])

# Unally prevention
T(P=[all_players], C=[command(foes)], A=[
    display_text("\\x013\\x006Do not un-ally"),
    set_to_ally(all_players),
])

# Remove unwanted neutral units
T(  P=[all_players],
    C=[
        always()
    ],
    A=[
        remove_unit(neutral, sniper),
    ]
)

for i in allIndices:
    teamLocations = getTeamLocations(i)
    otherTeamLocations = getOtherTeamLocations(i)
    player = allPlayers[i]
    team = getTeamPlayers(i)
    otherTeam = getOtherTeamPlayers(i)
    flag = getFlag(i)
    otherFlag = getOtherFlag(i)

    # Force stay still on SS
    T(  P=[player],
        C=[
            countdown_timer(atLeast, halfTime - 7),
            swappedSides == 1
        ],
        A=[
            T(C=[command(player, sniper, exactly, 0)], A=[create_unit(player, sniper, 1, loc["ss"][i])]), # create if needed
            move_unit(player, sniper, all, loc["everywhere"], loc["ss"][i])
        ]
    )
    # Center view on sniper SS
    T(  P=[player],
        C=[
            dc["ssCenterView"] == 1
        ],
        A=[
            center_view(loc["ss"][i]),
            dc["ssCenterView"].set_to(0)
        ]
    )

def teamSpecific(i):
    teamLocations = getTeamLocations(i)
    otherTeamLocations = getOtherTeamLocations(i)
    team = getTeam(i)
    otherTeam = getOtherTeam(i)
    flag = getFlag(i)
    otherFlag = getOtherFlag(i)
    antiCamp = getAntiCamp(i)
    otherAntiCamp = getOtherAntiCamp(i)
    currentPlayer = Player(cp)
    teamPlayers = getTeamPlayers(i)
    otherTeamPlayers = getOtherTeamPlayers(i)
    hot = isHot(i)

    # Kill
    T(  P=[team],
        C=[
            currentPlayer.kill(sniper)
        ],
        A=[
            currentPlayer.kill_sub(sniper),
            dc["bonus"] + 1,
            dc["killsThisLife"] + 1,
            dc["kills"] + 1,
            set_resources(team, add, 1, ore),
            set_resources(otherTeam, add, 1, gas)
        ]
    )
    
    # Bonus
    T(  P=[team],
        C=[
            dc["bonus"] == 5
        ],
        A=[
            dc["bonus"].set_to(0),
            set_resources(team, add, 5, ore),
            set_resources(otherTeam, add, 5, gas),
            set_score(currentPlayer, add, 1, "Custom"),
            dc["bonuses"] + 1,
            display_text("\\x005+5 Bonus")
        ]
    )
    
    # RS (after kill and bonus triggers to allow for DKs to give bonus)
    
    # Stop displaying death message (must be above death detection trigger)
    T(  P=[team],
        C=[
            dc["died"] == deathStates["DISPLAYING_MESSAGE"]
        ],
        A=[
            dc["died"].set_to(deathStates["WAITING_FOR_TIMER"])
        ]
    )
    
    # Detect death and begin RS process
    T(  P=[team],
        C=[
            command(player=cp, unit=sniper, qmod=exactly, num=0),
            dc["died"] == deathStates["ALIVE"],
            gameOver == 0,
        ],
        A=[
            dc["died"].set_to(deathStates["DISPLAYING_MESSAGE"]),
            dc["rsTimer"].set_to(96),
            dc["killsThisLife"].set_to(0),
            dc["bonus"].set_to(0),
            set_score(cp, add, 1, razings),
            dc["deaths"] + 1,
            T(
                C=[dc["hasFlag"] == 1],
                A=[
                    otherFlag.set_to(0),
                    set_deaths(otherTeamPlayers, dc["sounds"]["flag_returned"].unit, setTo, 1),
                    dc["hasFlag"].set_to(0),
                ]
            ),
            
            [
                T(
                    C=[command(i+1, turretUnit), command(neutral, turretUnit, exactly, 0)],
                    A=[
                        give_unit(i+1, neutral, turretUnit, all, loc["everywhere"]),
                        give_unit(neutral, i+1, turretUnit, all, loc["everywhere"]),
                    ]
                )
            for i in allIndices]
        ]
    )
    
    # Count down RS timer
    T(  P=[team],
        C=[dc["rsTimer"] > 0],
        A=[dc["rsTimer"] - 1]
    )
    
    # Begin respawning
    T(  P=[team],
        C=[
            dc["died"] == deathStates["WAITING_FOR_TIMER"],
            dc["rsTimer"] == 0
        ],
        A=[
            dc["died"].set_to(deathStates["RESPAWNING"]),
            dc["rs"].set_to(0)
        ]
    )
    
    # Randomise DC
    for j in range(31):
        T(  P=[team],
            C=[
                dc["died"] == deathStates["RESPAWNING"]
            ],
            A=[
                rsSwitch.randomize()
            ]
        )
        T(  P=[team],
            C=[
                dc["died"] == deathStates["RESPAWNING"],
                rsSwitch.is_set()
            ],
            A=[
                dc["rs"] + (2**j)
            ]
        )
    
    # Respawn
    T(  P=[team],
        C=[
            dc["died"] == deathStates["RESPAWNING"],
            gameOver == 0,
        ],
        A=[
            dc["died"].set_to(deathStates["ALIVE"]),
            
            # Left RS
            T(  C=[
                    dc["rs"] <= 715827882,
                ],
                A=[
                    create_unit(cp, sniper, 1, teamLocations["leftRs"])
                ]
            ),
            
            # Mid RS
            T(  C=[
                    dc["rs"] >= 715827883,
                    dc["rs"] <= 1431655765,
                ],
                A=[
                    create_unit(cp, sniper, 1, teamLocations["midRs"])
                ]
            ),
            
            # Right RS
            T(  C=[
                    dc["rs"] >= 1431655766,
                ],
                A=[
                    create_unit(cp, sniper, 1, teamLocations["rightRs"])
                ]
            ),
            
            # Reset RS DC
            dc["rs"].set_to(0),
            
            # Set anti-camp invincibility on RS
            T(
                C=[antiCamp == 1],
                A=[
                    set_invincibility(cp, sniper, loc["everywhere"]),
                    dc["antiCampTimer"].set_to(27),
                ]
            )
        ]
    )
    # Unset anti-camp invincibility
    T(
        P=[team],
        C=[
            [
                dc["antiCampTimer"] > 1,
                bring(cp, sniper, teamLocations["antiCamp"], exactly, 0),
            ],
            'o',
            dc["antiCampTimer"] == 1,
        ],
        A=[
            set_invincibility(cp, sniper, loc["everywhere"], disabled),
            move_location(cp, sniper, loc["everywhere"], loc["moveOverSniper"]),
            create_unit_with_properties(cp, invincibilityExpiredUnit, 1, loc["moveOverSniper"], "2"), # 2 set to invincible and hallucinated
            kill_unit(cp, invincibilityExpiredUnit),
            dc["antiCampTimer"].set_to(0),
        ]
    )
    # Count down anti-camp timer
    T(
        P=[team],
        C=[
            dc["antiCampTimer"] >= 1
        ],
        A=[
            dc["antiCampTimer"] - 1
        ]
    )
    # Enable anti-camp invincibility for other team
    T(
        P=[team],
        C=[
            otherFlag == 1,
            dc["hasFlag"] == 1,
            bring(cp, sniper, otherTeamLocations["antiCampBuffer"], exactly, 0),
        ],
        A=[
            otherAntiCamp.set_to(1),
        ]
    )
    # Disable anti-camp invincibility if flag is not taken
    T(
        P=[team],
        C=[
            flag == 0,
            antiCamp == 1,
        ],
        A=[
            antiCamp.set_to(0),
            set_invincibility(team, sniper, loc["everywhere"], disabled)
        ]
    )
    for teamPlayer in teamPlayers:
        # Display anti-camp enabled message
        enemyAntiCampMessageDiscretizer = Discretizer()
        T(
            P=[teamPlayer],
            C=[
                otherAntiCamp == 1
            ],
            A=[
                display_text("\\x013\\x006Anti camp enabled in enemy base")
            ],
            D=[enemyAntiCampMessageDiscretizer]
        )
        ourAntiCampMessageDiscretizer = Discretizer()
        T(
            P=[teamPlayer],
            C=[
                antiCamp == 1
            ],
            A=[
                display_text("\\x013\\x007Anti camp enabled in our base")
            ],
            D=[ourAntiCampMessageDiscretizer]
        )
    
    # for teamPlayer in teamPlayers:
        # # Display anti-camp disabled message
        # enemyAntiCampMessageDiscretizer = Discretizer()
        # T(
            # P=[teamPlayer],
            # C=[
                # otherAntiCamp == 0
            # ],
            # A=[
                # display_text("\\x013\\x005Anti camp disabled in enemy base")
            # ],
            # D=[enemyAntiCampMessageDiscretizer]
        # )
        # ourAntiCampMessageDiscretizer = Discretizer()
        # T(
            # P=[teamPlayer],
            # C=[
                # antiCamp == 0
            # ],
            # A=[
                # display_text("\\x013\\x005Anti camp disabled in our base")
            # ],
            # D=[ourAntiCampMessageDiscretizer]
        # )
    
    # Swap sides
    T(  P=[team],
        C=[
            countdown_timer(atMost, halfTime),
            swappedSides == 0,
            timerPaused == 0
        ],
        A=[
            swappedSides.set_to(1),
            [move_location(9, "Any unit", loc["topBase"][k], loc["coldTeam"][k]) for k, v in loc["topBase"].items()],
            [move_location(9, "Any unit", loc["bottomBase"][k], loc["hotTeam"][k]) for k, v in loc["bottomBase"].items()],
            set_deaths(all_players, dc["died"].unit, setTo, deathStates["ALIVE"]),
            set_deaths(all_players, dc["rsTimer"].unit, setTo, 0),
            set_deaths(all_players, dc["hasFlag"].unit, setTo, 0),
            set_deaths(all_players, dc["ssCenterView"].unit, setTo, 1),
            [T(C=[command(j+1), command(j+1, sniper, exactly, 0)], A=[create_unit(j+1, sniper, 1, loc["rightSide"])]) for j in allIndices],
            move_unit(all_players, sniper, all, loc["everywhere"], loc["rightSide"]),
            move_unit(all_players, turretUnit, all, loc["everywhere"], loc["rightSide"]),
            flag.set_to(0),
            otherFlag.set_to(0),
            move_unit(all_players, flagUnit, all, loc["everywhere"], loc["bottomLeftOtherUnits"]),
            
            # Disable all anti-camp
            antiCamp.set_to(0),
            otherAntiCamp.set_to(0),
            set_deaths(all_players, dc["antiCampTimer"].unit, setTo, 0),

        ]
    )
    
    # Taking the flag
    T(  P=[team],
        C=[
            otherFlag == 0,
            bring(cp, sniper, otherTeamLocations["flag"]),
            gameOver == 0,
        ],
        A=[
            otherFlag.set_to(1),
            dc["hasFlag"].set_to(1),
            display_text("\\x007Flag Captured!"),
            dc["sounds"]["flagCaptureEffect"].set_to(1),
            dc["sounds"]["flag_captured"].set_to(1),
        ]
    )

    # Returning the flag
    T(  P=[team],
        C=[
            otherFlag == 1,
            dc["hasFlag"] == 1,
            bring(cp, sniper, teamLocations["flag"])
        ],
        A=[
            # Update flag DCs
            otherFlag.set_to(0),
            dc["hasFlag"].set_to(0),

            # Disable anti-camp
            otherAntiCamp.set_to(0),

            # Notify player
            display_text("\\x007Flag Returned!"),
            dc["sounds"]["flagReturnEffect"].set_to(1),
            
            # Notify enemies
            set_deaths(otherTeamPlayers, dc["sounds"]["flag_returned"].unit, setTo, 1),
            
            # Update score
            set_resources(team, add, 15, ore),
            set_resources(otherTeam, add, 15, gas),
            
            # Update flags leaderboard
            set_score(cp, add, 1, buildings),
            
            # Update MVP calc
            dc["flags"] + 1
        ]
    )
    
    # Replace flag
    T(  P=[team],
        C=[
            flag == 0,
            'n', isFlagPresent(team, teamLocations),
        ],
        A=[
            move_unit(currentPlayer, flagUnit, all, loc["everywhere"], teamLocations["flag"]),
        ]
    )
    T(  P=[team],
        C=[
            flag == 1,
            isFlagPresent(team, teamLocations),
        ],
        A=[
            move_unit(currentPlayer, flagUnit, all, loc["everywhere"], loc["bottomLeftOtherUnits"]),
        ]
    )
    
    # Base vis
    
    # Give to next person when someone leaves
    T(  P=[team],
        C=[
            # command(neutral, baseVisUnit),
            # command(team, baseVisUnit, exactly, 0),
            command(neutral, turretUnit),
            command(team, turretUnit, exactly, 0)
        ],
        A=[    
            give_unit(neutral, cp, baseVisUnit, 2, loc["everywhere"]),
 
            give_unit(neutral, cp, turretUnit, 2, loc["everywhere"]),

            give_unit(neutral, cp, turretUnit2, 2, loc["everywhere"]),
            give_unit(neutral, cp, flagUnit, 1, loc["everywhere"]),
        ]
    )
    
    # Timer increment
    T(  P=[team],
        C=[
            always(),
        ],
        A=[
            dc["baseVisTimer"] + 1
            
        ]
    )
    
    # Move from bottom left to turret locations
    T(  P=[team],
        C=[
            dc["baseVisTimer"] == 49,
            command(cp, baseVisUnit)
        ],
        A=[
            move_unit(cp, baseVisUnit, 1, loc["bottomLeftBaseVisUnit"], teamLocations["leftTurret"]),
            move_unit(cp, baseVisUnit, 1, loc["bottomLeftBaseVisUnit"], teamLocations["rightTurret"]),
        ]
    )
    
    # Move from turret locations back to bottom left
    T(  P=[team],
        C=[
            dc["baseVisTimer"] == 50,
            command(cp, baseVisUnit)
        ],
        A=[
            move_unit(cp, baseVisUnit, all, loc["everywhere"], loc["bottomLeftBaseVisUnit"])
        ]
    )
    
    # Reset timer
    T(  P=[team],
        C=[
            dc["baseVisTimer"] == 50
        ],
        A=[
            dc["baseVisTimer"].set_to(0)
        ]
    )
    
    # Move turret units
    T(  P=[team],
        C=[
            command(cp, turretUnit),
            [
                bring(cp, turretUnit, teamLocations["leftTurret"], exactly, 0),
                'o',
                bring(cp, turretUnit, teamLocations["rightTurret"], exactly, 0)
            ],
            
        ],
        A=[
            give_unit(cp, neutral, turretUnit, 1, loc["everywhere"]),
            move_unit(cp, turretUnit, 1, loc["everywhere"], teamLocations["leftTurret"]),
            move_unit(neutral, turretUnit, 1, loc["everywhere"], teamLocations["rightTurret"]),
            give_unit(neutral, cp, turretUnit, 1, teamLocations["rightTurret"]),
        ]
    )
    
    T(  P=[team],
        C=[
            command(cp, turretUnit)
        ],
        A=[
            give_unit(cp, neutral, turretUnit, 2, teamLocations["base"]),
            give_unit(neutral, cp, turretUnit, 2, teamLocations["base"])
        ]
    )
    
    T(  P=[team],
        C=[
            command(cp, turretUnit2),
            [
                bring(cp, turretUnit2, teamLocations["leftTurret"], exactly, 0),
                'o',
                bring(cp, turretUnit2, teamLocations["rightTurret"], exactly, 0)
            ],
            
        ],
        A=[
            move_unit(cp, turretUnit2, all, loc["everywhere"], teamLocations["leftTurret"]),
            move_unit(cp, turretUnit2, 1, loc["everywhere"], teamLocations["rightTurret"])
        ]
    )
    
    T(  P=[team],
        C=[
            command(cp, turretUnit2)
        ],
        A=[
            give_unit(cp, neutral, turretUnit2, 2, loc["everywhere"]),
            give_unit(neutral, cp, turretUnit2, 2, loc["everywhere"]),
        ]
    )

    # Transmissions at start and SS
    T(  P=[teamPlayers],
        C=[
            isFlagPresent(team, teamLocations),
        ],
        A=[
            transmission(flagUnit, teamLocations["base"])
        ],
        just_once=True)
    T(  P=[teamPlayers],
        C=[
            swappedSides == 1,
            isFlagPresent(team, teamLocations),
        ],
        A=[transmission(flagUnit, teamLocations["base"])
    ], just_once=True)
    
    # End game
    T(  P=[team],
        C=[
            countdown_timer(exactly, 0),
            timerPaused == 0,
            gameOver == 0,
        ],
        A=[
            T(
                C=[
                    most_resources(ore if hot else gas),
                ],
                A=[
                    hotWins.set_to(1)
                ]
            ),
            T(
                C=[
                    most_resources(gas if hot else ore),
                ],
                A=[
                    coldWins.set_to(1)
                ]
            ),
            T(
                C=[
                    coldWins == 1,
                    hotWins == 1
                ],
                A=[
                    hotWins.set_to(0),
                    coldWins.set_to(0),
                    set_countdown_timer(setTo, overtimeTime),
                    set_deaths(all_players, dc["overtimeMessage"].unit, setTo, 1),
                ]
            ),
            T(
                C=[
                    coldWins == 0,
                    hotWins == 1,
                ],
                A=[
                    hotWinsMessage.set_to(1),
                    gameOver.set_to(1),
                ],
                just_once=True
            ),
            T( 
                C=[
                    coldWins == 1,
                    hotWins == 0,
                ],
                A=[
                    coldWinsMessage.set_to(1),
                    gameOver.set_to(1),
                ],
                just_once=True
            )
        ]
    )

    T(  P=[team],
        C=[
            coldWinsMessage == 1
        ],
        A=[
            display_text("\\x013\\x005Team cold wins!"),
            dc["sounds"]["lostmatch" if hot else "winner"].set_to(1),
        ],
        just_once=True
    )
    T(  P=[team],
        C=[
            hotWinsMessage == 1
        ],
        A=[
            display_text("\\x013\\x005Team hot wins!"),
            dc["sounds"]["winner" if hot else "lostmatch"].set_to(1),
        ],
        just_once=True
    )
    T(  P=[team],
        C=[
            gameOver == 1
        ],
        A=[
            remove_unit(all_players, sniper),
            flag.set_to(0),
            otherFlag.set_to(0),
        ]
    )

teamSpecific(0)
teamSpecific(4)
    
# Player specific
for i in allIndices:
    # Display player died message
    T(  P=[all_players],
        C=[
            deaths(i+1, dc["died"].unit, exactly, deathStates["DISPLAYING_MESSAGE"]),
            gameOver == 0
        ],
        A=[
            display_text(playerHasDiedMessages[i])
        ]
    )
# Remove extra snipers
T(  P=[all_players],
    C=[
        command(cp, sniper, atLeast, 2)
    ],
    A=[
        remove_unit_at_location(cp, sniper, 1, loc["everywhere"]),
        dc["died"].set_to(deathStates["ALIVE"]),
        dc["rsTimer"].set_to(0)
    ]
)
    
# Kill streak sounds
for (number, soundName) in streaks:
    streakDC = DC(cp)
    T(  P=[all_players],
        C=[
            dc["killsThisLife"] == number,
            streakDC == 0,
        ],
        A=[
            dc["sounds"][soundName].set_to(1),
            streakDC.set_to(1)
        ]
    )
    T(  P=[all_players],
        C=[
            'n', dc["killsThisLife"] == number
        ],
        A=[
            streakDC.set_to(0)
        ]
    )

# Side switch 1-minute warning
T(  P=[all_players],
    C=[
        countdown_timer(exactly, halfTime + 60),
    ],
    A=[
        display_text("\\x013\\x006Side-switch in 60 seconds!"),
        dc["sounds"]["cd1min"].set_to(1)
    ],
    just_once=True
)
# End game 1-minute warning
T(  P=[all_players],
    C=[
        countdown_timer(exactly, 60),
    ],
    A=[
        display_text("\\x013\\x006Game end in 60 seconds!"),
        dc["sounds"]["cd1min"].set_to(1),
    ],
    just_once=True
)

# Overtime
T(  P=[all_players],
    C=[
        dc["overtimeMessage"] == 1
    ],
    A=[
        display_text("\\x013\\x005Overtime!"),
        dc["overtimeMessage"].set_to(0)
    ]
)
    
# Pause timer at SS
T(  P=[all_players],
    C=[
        countdown_timer(atMost, halfTime + 1),
        [hotFlagTaken == 1, 'o', coldFlagTaken == 1],
        timerPaused == 0,
        swappedSides == 0
    ],
    A=[
        pause_timer(),
        timerPaused.set_to(1),
        set_countdown_timer(setTo, halfTime + 1),
    ]
)

# Pause timer at end
T(  P=[all_players],
    C=[
        countdown_timer(atMost, 1),
        [hotFlagTaken == 1, 'o', coldFlagTaken == 1],
        timerPaused == 0,
        gameOver == 0,
    ],
    A=[
        pause_timer(),
        timerPaused.set_to(1),
        set_countdown_timer(setTo, 1),
    ]
)

# Unpause timer at SS
# Unpause timer at end
T(  P=[all_players],
    C=[
        hotFlagTaken == 0,
        coldFlagTaken == 0,
        timerPaused == 1
    ],
    A=[
        unpause_timer(),
        timerPaused.set_to(0)
    ]
)
# Leaderboards
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["MVP"],
        dc["leaderboardTimer"] == 0
    ],
    A=[
        leaderboard_kills("\\x01eKills", sniper),
        leaderboard_computer_players(disabled),
        dc["leaderboardTimer"].set_to(leaderboardTransitionTime),
        dc["leaderboard"].set_to(leaderboardStates["KILLS"]),
        remove_unit(all_players, mvpUnit)
    ]
)
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["KILLS"],
        dc["leaderboardTimer"] == 0
    ],
    A=[
        leaderboard_points("\\x01eDeaths", razings),
        leaderboard_computer_players(disabled),
        dc["leaderboardTimer"].set_to(leaderboardTransitionTime),
        dc["leaderboard"].set_to(leaderboardStates["DEATHS"])
    ]
)
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["DEATHS"],
        dc["leaderboardTimer"] == 0
    ],
    A=[
        leaderboard_points("\\x01eBonuses", "Custom"),
        leaderboard_computer_players(disabled),
        dc["leaderboardTimer"].set_to(leaderboardTransitionTime),
        dc["leaderboard"].set_to(leaderboardStates["BONUSES"])
    ]
)
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["BONUSES"],
        dc["leaderboardTimer"] == 0
    ],
    A=[
        leaderboard_points("\\x01eFlags", buildings),
        leaderboard_computer_players(disabled),
        dc["leaderboardTimer"].set_to(leaderboardTransitionTime),
        dc["leaderboard"].set_to(leaderboardStates["FLAGS"])
    ]
)

T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["FLAGS"],
        dc["leaderboardTimer"] == 0
    ],
    A=[
        dc["leaderboardTimer"].set_to(leaderboardTransitionTime * 2),
        dc["leaderboard"].set_to(leaderboardStates["MVP"])
    ]
)

# Skip a couple of frames before recalculating mvp
T(  P=[all_players],
    C=[
        dc["resetMVP"] == 5,
    ],
    A=[
        dc["resetMVP"].set_to(0),
    ]
)
T(  P=[all_players],
    C=[
        dc["resetMVP"] == 4,
    ],
    A=[
        remove_unit(cp, mvpUnit),
    ]
)
T(  P=[all_players],
    C=[
        dc["resetMVP"] >= 1,
    ],
    A=[
        dc["resetMVP"] + 1,
    ]
)


# MVP math: MVP points = Kills + 3*Bonuses + 2*Flags - Deaths
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["MVP"],
        dc["resetMVP"] == 0,
    ],
    A=[
        dc["mvp"].set_to(0),
        
        dc["mvp"] + dc["kills"],
        
        dc["mvp"] + dc["bonuses"],
        dc["mvp"] + dc["bonuses"],
        dc["mvp"] + dc["bonuses"],
        
        dc["mvp"] + dc["flags"],
        dc["mvp"] + dc["flags"],
        
        dc["mvp"] - dc["deaths"],
    ]
)

# Convert mvp DC into actual units
for j in reversed(range(9)):
    T(  P=[all_players],
        C=[
            dc["leaderboard"] == leaderboardStates["MVP"],
            dc["resetMVP"] == 0,
            dc["mvp"] >= 2**j
        ],
        A=[
            dc["mvp"] - 2**j,
            create_unit_with_properties(cp, mvpUnit, 2**j, loc["bottomLeftOtherUnits"], "1") #1 set to burrowed and invincible
        ]
    )

# Move on to next stage of mvp calc
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["MVP"],
        dc["resetMVP"] == 0,
    ],
    A=[
        dc["resetMVP"].set_to(1),
    ]
)

# Make sure MVP units can't move
T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["MVP"]
    ],
    A=[
        move_unit(cp, mvpUnit, all, loc["everywhere"], loc["bottomLeftOtherUnits"]),
    ]
)

T(  P=[all_players],
    C=[
        dc["leaderboard"] == leaderboardStates["MVP"]
    ],
    A=[
        leaderboard_control("\\x01eMVP", mvpUnit)
    ]
)

#Leaderboard timer

T(  P=[all_players],
    C=[
        dc["leaderboardTimer"] >= 1
    ],
    A=[
        dc["leaderboardTimer"] - 1
    ]
)

# Cliff
T(  P=[all_players],
    C=[
        bring(cp, sniper, loc["topCliff"]["entryLow"])
    ],
    A=[
        move_unit(cp, sniper, all, loc["topCliff"]["entryLow"], loc["topCliff"]["entryHigh"])
    ]
)
T(  P=[all_players],
    C=[
        bring(cp, sniper, loc["topCliff"]["exitHigh"])
    ],
    A=[
        move_unit(cp, sniper, all, loc["topCliff"]["exitHigh"], loc["topCliff"]["exitLow"])
    ]
)
T(  P=[all_players],
    C=[
        bring(cp, sniper, loc["bottomCliff"]["entryLow"])
    ],
    A=[
        move_unit(cp, sniper, all, loc["bottomCliff"]["entryLow"], loc["bottomCliff"]["entryHigh"])
    ]
)
T(  P=[all_players],
    C=[
        bring(cp, sniper, loc["bottomCliff"]["exitHigh"])
    ],
    A=[
        move_unit(cp, sniper, all, loc["bottomCliff"]["exitHigh"], loc["bottomCliff"]["exitLow"])
    ]
)

# Set HP = number of kills
for j in range(1, 41):
    T(  P=[all_players],
        C=[
            dc["killsThisLife"] == j
        ],
        A=[
            modify_unit_hit_points(cp, sniper, j, all, loc["everywhere"])
        ]
    )

# Play sound. Timer prevents sounds from overlapping.
T(  P=[all_players],
    C=[
        dc["soundTimer"] == 0,
    ],
    A=[
        [
            T(
                C=[
                    dc["sounds"][name] == 1
                ],
                A=[
                    play_wav(sounds[name]),
                    dc["sounds"][name].set_to(0),
                    dc["soundTimer"].set_to(1),
                ]
            )
        for name, file in sounds.items()],
    ]
)
T(  P=[all_players],
    C=[
        dc["soundTimer"] >= 1
    ],
    A=[
        dc["soundTimer"] - 1
    ]
)

# Timer increment
T(  P=[8],
    C=[
        dc["baseVisTimer"] == 1
    ],
    A=[
        run_ai_script("SuiR")
        
    ]
)
    
# Hyper triggers
for i in range(4):
    T(P=[all_players], A=[wait(0) for j in range(62)])

#Keeping this at the end will display map stats in Command Prompt.
import TriGen_stats

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    