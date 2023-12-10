# Files: games.csv

- [games.csv](https://bw0-my.sharepoint.com/:x:/g/personal/spaul_bw_edu/Ed4l-bFTNm9BsAt4buUMo4QBHCmSn9R6TX7bMyoCQVAmdA?e=P4Oicf)

### Documentation: Varible description

- GAME_DATE_EST: Game's date
- GAME_ID: ID of the game
- GAME_STATUS_TEXT: Status - Final means that the is completed
- HOME_TEAM_ID: ID of the home team
- VISITOR_TEAM_ID: ID of the visitor team
- SEASON: Season when the game occured
- TEAM_ID_home: ID of the home team (dupplicate of HOME_TEAM_ID)
- PTS_home: Number of points scored by home team
- FG_PCT_home: Field Goal Percentage home team
- FT_PCT_home: Free Throw Percentage of the home team
- FG3_PCT_home: Three Point Percentageof the home team
- AST_home: Assists of the home team
- REB_home: Rebounds of the home team
- TEAM_ID_away: ID of the away team (dupplicate of VISITOR_TEAM_ID)
- PTS_away: Number of points scored by away team
- FG_PCT_away: Field Goal Percentage away team
- FT_PCT_away: Free Throw Percentage of the away team
- FG3_PCT_away: Three Point Percentage of the away team
- AST_away: Assists of the away team
- REB_away: Rebounds of the away team
- HOME_TEAM_WINS: If home team won the game

***

# Files: games_details.csv

- [games_details.csv](https://bw0-my.sharepoint.com/:x:/g/personal/spaul_bw_edu/EScieKh8Qo5Kl52kbiHuClABuhhySuaDGsz2wucAL6gbdw?e=XHUw4K)

### Documentation: Varible description

- GAME_ID: ID of the game
- TEAM_ID: ID of the team
- TEAM_ABBREVIATION: Team's abbreviation
- TEAM_CITY: City where the game was played
- PLAYER_ID: ID of the player
- PLAYER_NAME: Player's name
- NICKNAME: Position of the player (if nothing then he's on the bench)
- START_POSITION: Comment
- COMMENT: Minutes played
- MIN: Field Goals Made
- FGM: Field Goals Attempted
- FGA: Field Goal Percentage
- FG_PCT: Three Pointers Made
- FG3M: Three Pointers Attempted
- FG3A: Three Point Percentage
- FG3_PCT: Free Throws Made
- FTM: Free Throws Attempted
- FTA: Free Throw Percentage
- FT_PCT: Offensive Rebounds
- OREB: Defensive Rebounds
- DREB: Rebounds
- REB: Assists
- AST: Steals
- STL: Blocked shots
- BLK: Turnovers
- TO: Personnal Foul
- PF: Number of points scored by the player
- PTS: Plus - Minus
- PLUS_MINUS

***

# Files: players.csv

- [players.csv](https://bw0-my.sharepoint.com/:x:/g/personal/spaul_bw_edu/EYUkEfrt7XdNrN39z471MuMBfczJq_hX8AxPTx-pai3R9w?e=4Ear9D)

### Documentation: Varible description

- PLAYER_NAME: Player's name
- TEAM_ID: ID of the team
- PLAYER_ID: ID of the player
- SEASON: Season

***

# Files: ranking.csv

- [ranking.csv](https://bw0-my.sharepoint.com/:x:/g/personal/spaul_bw_edu/ES-1_VelIxRKjmxWm7osx7sB29Kx42RPUZ-GJx0fWzBpZA?e=4SDGK4)

### Documentation: Varible description

- TEAM_ID: ID of the team
- LEAGUE_ID: ID of the league (here only NBA)
- SEASON_ID: Season
- STANDINGSDATE: Standings date
- CONFERENCE: Conference (west or east)
- TEAM: Team name
- G: Number of games played on the season
- W: Number of winning games on the season
- L: Number of loosing games on the season
- W_PCT: Win %
- HOME_RECORD: Home record on the season
- ROAD_RECORD: Road record on the season
- RETURNTOPLAY

***

# Files: teams.csv

- [teams.csv](https://bw0-my.sharepoint.com/:x:/g/personal/spaul_bw_edu/EX9n81B4ohFJlaI05FFOXcAB34TlUJLNlp5Pl26Putm3xw?e=jwibxZ)

### Documentation: Varible description

- LEAGUE_ID: ID of the league (here only NBA)
- TEAM_ID: ID of the team
- MIN_YEAR: Minimum year of the team into NBA championship
- MAX_YEAR: Maximum year of the team into NBA championship
- ABBREVIATION: Abbreviation of team name
- NICKNAME: Team's nickname
- YEARFOUNDED: Founded Year
- CITY: Team's city
- ARENA: Team's stadium
- ARENACAPACITY: Capacity of the stadium
- OWNER: Owner of the team (last one)
- GENERALMANAGER: General manager
- HEADCOACH: Head coach
- DLEAGUEAFFILIATION: League Affiliation

***

- To read all these file into R, use this R code - [read_data.R](https://raw.githubusercontent.com/sureshlazaruspaul/BUS662-practice-datasets/main/nba/read_data.R) .

***
