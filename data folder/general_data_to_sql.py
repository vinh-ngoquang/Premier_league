import pymysql
import pandas as pd 
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '', #your password
    cursorclass = pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()

file_path = '' #yourPath
table_name = 'general_data'
table = pd.read_csv(f'{file_path}/{table_name}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS premier_league.general_data (
                playerId INT(11) PRIMARY KEY,
                goals INT(11),
                goalAssist INT(11),
                appearances INT(11),
                minutePlayed INT(11),
                yellowCard INT(11),
                redCard INT(11),
                totalSubOn INT(11),
                totalSubOff INT(11),
                FOREIGN KEY(playerId) REFERENCES premier_league.players_info(playerId)
                )
        ''')
for i in range(len(table)):
        cursor.execute(f'''
            INSERT INTO premier_league.general_data (
                    `playerId`,
                    `goals`,
                    `goalAssist`,
                    `appearances`,
                    `minutePlayed`,
                    `yellowCard`,
                    `redCard`,
                    `totalSubOn`,
                    `totalSubOff`)
            VALUES (
                    {table['playerId'][i]},
                    {table['goals'][i]},
                    {table['goalAssist'][i]},
                    {table['appearances'][i]},
                    {table['minutePlayed'][i]},
                    {table['yellowCard'][i]},
                    {table['redCard'][i]},
                    {table['totalSubOn'][i]},
                    {table['totalSubOff'][i]}
                    );
            ''')

mysql_client.commit()