#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# read_data.R reads all five nba datasets.
# written by,
#  Suresh Paul, C.Phil, M.S., B.E.
#   Lecturer II, Balwin Wallace University
#   Founder & Sr. Data Scientist, Algorithm Basics LLC
# Copy of this code is available at,
#  https://raw.githubusercontent.com/sureshlazaruspaul/BUS662-practice-datasets/main/nba/read_data1.R
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# load packages ...

library("tidyverse")
library("data.table")


path <- "C:/data/nba/"



#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# file: games.csv
#------------------------------------------------------------------------------
# GAME_DATE_EST: Game's date
# GAME_ID: ID of the game
# GAME_STATUS_TEXT: Status - Final means that the is completed
# HOME_TEAM_ID: ID of the home team
# VISITOR_TEAM_ID: ID of the visitor team
# SEASON: Season when the game occured
# TEAM_ID_home: ID of the home team (dupplicate of HOME_TEAM_ID)
# PTS_home: Number of points scored by home team
# FG_PCT_home: Field Goal Percentage home team
# FT_PCT_home: Free Throw Percentage of the home team
# FG3_PCT_home: Three Point Percentageof the home team
# AST_home: Assists of the home team
# REB_home: Rebounds of the home team
# TEAM_ID_away: ID of the away team (dupplicate of VISITOR_TEAM_ID)
# PTS_away: Number of points scored by away team
# FG_PCT_away: Field Goal Percentage away team
# FT_PCT_away: Free Throw Percentage of the away team
# FG3_PCT_away: Three Point Percentage of the away team
# AST_away: Assists of the away team
# REB_away: Rebounds of the away team
# HOME_TEAM_WINS: If home team won the game
#------------------------------------------------------------------------------

# read csv files

games <- fread(paste0(path, "games.csv")) # using data.table package

#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# file: games_details.csv
#------------------------------------------------------------------------------
# GAME_ID: ID of the game
# TEAM_ID: ID of the team
# TEAM_ABBREVIATION: Team's abbreviation
# TEAM_CITY: City where the game was played
# PLAYER_ID: ID of the player
# PLAYER_NAME: Player's name
# NICKNAME: Position of the player (if nothing then he's on the bench)
# START_POSITION: Comment
# COMMENT: Minutes played
# MIN: Field Goals Made
# FGM: Field Goals Attempted
# FGA: Field Goal Percentage
# FG_PCT: Three Pointers Made
# FG3M: Three Pointers Attempted
# FG3A: Three Point Percentage
# FG3_PCT: Free Throws Made
# FTM: Free Throws Attempted
# FTA: Free Throw Percentage
# FT_PCT: Offensive Rebounds
# OREB: Defensive Rebounds
# DREB: Rebounds
# REB: Assists
# AST: Steals
# STL: Blocked shots
# BLK: Turnovers
# TO: Personnal Foul
# PF: Number of points scored by the player
# PTS: Plus - Minus
# PLUS_MINUS
#------------------------------------------------------------------------------

# read csv files

games_details <- fread(paste0(path, "games_details.csv")) 


#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# file: players.csv
#------------------------------------------------------------------------------
# PLAYER_NAME: Player's name
# TEAM_ID: ID of the team
# PLAYER_ID: ID of the player
# SEASON: Season
#------------------------------------------------------------------------------

# read csv files

players <- fread(paste0(path, "players.csv"))

#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# file: ranking.csv
#------------------------------------------------------------------------------
# TEAM_ID: ID of the team
# LEAGUE_ID: ID of the league (here only NBA)
# SEASON_ID: Season
# STANDINGSDATE: Standings date
# CONFERENCE: Conference (west or east)
# TEAM: Team name
# G: Number of games played on the season
# W: Number of winning games on the season
# L: Number of loosing games on the season
# W_PCT: Win %
# HOME_RECORD: Home record on the season
# ROAD_RECORD: Road record on the season
# RETURNTOPLAY
#------------------------------------------------------------------------------

# read csv files

ranking <- fread(paste0(path, "ranking.csv"))



#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# file: teams.csv
#------------------------------------------------------------------------------
# LEAGUE_ID: ID of the league (here only NBA)
# TEAM_ID: ID of the team
# MIN_YEAR: Minimum year of the team into NBA championship
# MAX_YEAR: Maximum year of the team into NBA championship
# ABBREVIATION: Abbreviation of team name
# NICKNAME: Team's nickname
# YEARFOUNDED: Founded Year
# CITY: Team's city
# ARENA: Team's stadium
# ARENACAPACITY: Capacity of the stadium
# OWNER: Owner of the team (last one)
# GENERALMANAGER: General manager
# HEADCOACH: Head coach
# DLEAGUEAFFILIATION: League Affiliation
#------------------------------------------------------------------------------

# read csv files

teams <- fread(paste0(path, "teams.csv"))


