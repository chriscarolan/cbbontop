from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


### NET Rankings Page
net_url = 'https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings'

net_page = requests.get(net_url)

net_soup = BeautifulSoup(net_page.text, 'html')

net_table = net_soup.find('table')

net_world_titles = net_table.find_all('th')

net_world_tables_titles = [title.text for title in net_world_titles]


net_df = pd.DataFrame(columns = net_world_tables_titles)

net_column_data = net_table.find_all('tr')


for net_row in net_column_data[1:]:
  net_row_data = net_row.find_all('td')
  net_individual_row_data = [data.text for data in net_row_data]

  length = len(net_df)
  net_df.loc[length] = net_individual_row_data

net_df[['Wins', 'Losses']] = net_df['Record'].str.split('-', expand=True)
net_df[['Quad_1_Wins', 'Quad_1_Losses']] = net_df['Quad 1'].str.split('-', expand=True)
net_df = net_df.drop(['Quad 1'], axis=1)
net_df[['Quad_2_Wins', 'Quad_2_Losses']] = net_df['Quad 2'].str.split('-', expand=True)
net_df = net_df.drop(['Quad 2'], axis=1)
net_df[['Quad_3_Wins', 'Quad_3_Losses']] = net_df['Quad 3'].str.split('-', expand=True)
net_df = net_df.drop(['Quad 3'], axis=1)
net_df[['Quad_4_Wins', 'Quad_4_Losses']] = net_df['Quad 4'].str.split('-', expand=True)
net_df = net_df.drop(['Quad 4'], axis=1)

net_df['Rank'] = net_df['Rank'].astype('int64')
net_df['Previous'] = net_df['Previous'].astype('int64')
net_df['WAB'] = net_df['WAB'].astype('int64')
net_df['Wins'] = net_df['Wins'].astype('int64')
net_df['Losses'] = net_df['Losses'].astype('int64')
net_df['Quad_1_Wins'] = net_df['Quad_1_Wins'].astype('int64')
net_df['Quad_1_Losses'] = net_df['Quad_1_Losses'].astype('int64')
net_df['Quad_2_Wins'] = net_df['Quad_2_Wins'].astype('int64')
net_df['Quad_2_Losses'] = net_df['Quad_2_Losses'].astype('int64')
net_df['Quad_3_Wins'] = net_df['Quad_3_Wins'].astype('int64')
net_df['Quad_3_Losses'] = net_df['Quad_3_Losses'].astype('int64')
net_df['Quad_4_Wins'] = net_df['Quad_4_Wins'].astype('int64')
net_df['Quad_4_Losses'] = net_df['Quad_4_Losses'].astype('int64')


### Team Stats
offense_url = 'https://basketball.realgm.com/ncaa/team-stats/2025/Averages/Team_Totals/0'
offense_page = requests.get(offense_url)
offense_soup = BeautifulSoup(offense_page.text, 'html')

offense_table = offense_soup.find('table')

offense_world_titles = offense_table.find_all('th')

offense_world_tables_titles = [title.text for title in offense_world_titles]

offense_df = pd.DataFrame(columns = offense_world_tables_titles)

offense_column_data = offense_table.find_all('tr')

for offense_row in offense_column_data[1:]:
  offense_row_data = offense_row.find_all('td')
  offense_individual_row_data = [data.text for data in offense_row_data]

  length = len(offense_df)
  offense_df.loc[length] = offense_individual_row_data

offense_df = offense_df.drop(['GP'], axis=1)
offense_df = offense_df.drop(['MPG'], axis=1)
offense_df = offense_df.drop(['#'], axis=1)
offense_df = offense_df.rename(columns={'Team': 'School'})




### Opponent Stats
opp_url = 'https://basketball.realgm.com/ncaa/team-stats/2025/Averages/Opponent_Totals/0'
opp_page = requests.get(opp_url)
opp_soup = BeautifulSoup(opp_page.text, 'html')

opp_table = opp_soup.find('table')

opp_world_titles = opp_table.find_all('th')

opp_world_tables_titles = [title.text for title in opp_world_titles]

opp_df = pd.DataFrame(columns = opp_world_tables_titles)

opp_column_data = opp_table.find_all('tr')

for opp_row in opp_column_data[1:]:
  opp_row_data = opp_row.find_all('td')
  opp_individual_row_data = [data.text for data in opp_row_data]

  length = len(opp_df)
  opp_df.loc[length] = opp_individual_row_data

opp_df = opp_df.drop(['#'], axis=1)
opp_df = opp_df.drop(['GP'], axis=1)
opp_df = opp_df.drop(['MPG'], axis=1)
opp_df = opp_df.rename(columns={'Team': 'School'})

opp_df = opp_df.rename(columns={'PPG': 'Opp_PPG', 'FGM': 'Opp_FGM', 'FGA': 'Opp_FGA',
                                'FG%': 'Opp_FG%', '3PM': 'Opp_3PM', '3PA': 'Opp_3PA',
                                '3P%': 'Opp_3P%', 'FTM': 'Opp_FTM', 'FTA': 'Opp_FTA',
                                'FT%': 'Opp_FT%', 'ORB': 'Opp_ORB', 'DRB': 'Opp_DRB',
                                'RPG': 'Opp_RPG', 'APG': 'Opp_APG', 'SPG': 'Opp_SPG',
                                'BPG': 'Opp_BPG', 'TOV': 'Opp_TOV', 'PF': 'Opp_PF'})




# Merge all of them
merged_off_def = pd.merge(offense_df, opp_df, on='School', how='inner')
merged_off_def_alph = merged_off_def.sort_values(by='School')

net_alph = net_df.sort_values(by='School')

net_alph['School'] = net_df['School'].replace({'A&M-Corpus Christi': 'Texas A&M-CC',
                                             'Alcorn': 'Alcorn St.',
                                             'App State': 'App St.',
                                             'Ark.-Pine Bluff': 'Arkansas Pine Bluff',
                                               'Army West Point': 'Army',
                                               'Boston U.': 'Boston University',
                                               'Central Ark.': 'Central Arkansas',
                                               'Central Conn. St.': 'Central Connecticut St.',
                                               'UAlbany': 'Albany',
                                               'Central Mich.': 'Central Michigan',
                                               'Charleston So.': 'Charleston Southern',
                                               'Col. of Charleston': 'Charleston',
                                               'ETSU': 'East Tennessee State',
                                               'Eastern Ill.': 'Eastern Illinois',
                                               'Eastern Ky.': 'Eastern Kentucky',
                                               'Eastern Mich.': 'Eastern Michigan',
                                               'Eastern Wash.': 'Eastern Washington',
                                               'FDU': 'Fairleigh Dickinson',
                                               'FGCU': 'Florida Gulf Coast',
                                               'FIU': 'Florida International',
                                               'Fla. Atlantic': 'Florida Atlantic',
                                               'Ga. Southern': 'Georgia Southern',
                                               'UIW': 'Incarnate Word',
                                               'LIU': 'Long Island',
                                               'LMU (CA)': 'Loyola Marymount',
                                               'Lamar University': 'Lamar',
                                               'Massachusets': 'UMass',
                                               'Middle Tenn.': 'Middle Tennessee St.',
                                               'Mississippi Val.': 'Mississippi Valley St.',
                                               'N.C. A&T': 'North Carolina A&T',
                                               'N.C. Central': 'North Carolina Central',
                                               'NIU': 'Northern Illinois',
                                               'North Ala.': 'North Alabama',
                                               'Northern Ariz.': 'Northern Arizona',
                                               'Northern Colo.': 'Northern Colorado',
                                               'Northern Ky.': 'Northern Kentucky',
                                               'UNI': 'Northern Iowa',
                                               'Penn': 'UPenn',
                                               'Prairie View': 'Prairie View A&M',
                                               'Queens (NC)': 'Queens',
                                               'SFA': 'Stephen F. Austin',
                                               "Saint Mary's (CA)": "Saint Mary's",
                                               'Seattle U': 'Seattle',
                                               'South Fla.': 'South Florida',
                                               'Southeast Mo. St.': 'Southeast Missouri State',
                                               'Southeastern La.': 'Southeastern Louisiana',
                                               'Southern California': 'USC',
                                               'Southern Ill.': 'Southern Illinois',
                                               'Southern Ind.': 'Southern Indiana',
                                               'Southern Miss.': 'Southern Mississippi',
                                               'Southern U.': 'Southern',
                                               "St. John's (NY)": "St. John's",
                                               'St. Thomas (MN)': 'St. Thomas',
                                               'UNCW': 'UNC Wilmington',
                                               'West Ga.': 'West Georgia',
                                               'Western Caro.': 'Western Carolina',
                                               'Western Ill.': 'Western Illinois',
                                               'Western Ky.': 'Western Kentucky',
                                               'Western Mich.': 'Western Michigan'
                                               })
                      
merged_off_def_alph['School'] = merged_off_def['School'].replace({'Alabama State': 'Alabama St.',
                                                             'Alcorn State': 'Alcorn St.',
                                                             'American University': 'American',
                                                             'Appalachian State': 'App St.',
                                                             'Arizona State': 'Arizona St.',
                                                                  'Army West Point': 'Army',
                                                                  'Arkansas-Pine Bluff ': 'Arkansas Pine Bluff',
                                                                  'Arkansas State': 'Arkansas St.',
                                                                  'Ball State': 'Ball St.',
                                                                  'Boise State': 'Boise St.',
                                                                  'Brigham Young': 'BYU',
                                                                  'Cal State Bakersfield': 'CSU Bakersfield',
                                                                  'Cal State Fullerton': 'Cal St. Fullerton',
                                                                  'Cal State Northridge': 'CSUN',
                                                                  'Central Connecticut State': 'Central Connecticut St.',
                                                                  'Chicago State': 'Chicago St.',
                                                                  'Cleveland State': 'Cleveland St.',
                                                                  'Colorado State': 'Colorado St.',
                                                                  'Coppin State': 'Coppin St.',
                                                                  'Delaware State': 'Delaware St.',
                                                                  'Detroit-Mercy': 'Detroit Mercy',
                                                                  'Florida Atlantic ': 'Florida Atlantic',
                                                                  'Florida State': 'Florida St.',
                                                                  'Fort Wayne': 'Purdue Fort Wayne',
                                                                  'Fresno State': 'Fresno St.',
                                                                  'Georgia State': 'Georgia St.',
                                                                  'Grambling State': 'Grambling',
                                                                  'Idaho State': 'Idaho St.',
                                                                  'Illinois State': 'Illinois St.',
                                                                  'Illinois-Chicago': 'UIC',
                                                                  'Indiana State': 'Indiana St.',
                                                                  'Iowa State': 'Iowa St.',
                                                                  'Jackson State': 'Jackson St.',
                                                                  'Jacksonville State': 'Jacksonville St.',
                                                                  'UMKC': 'Kansas City',
                                                                  'Kansas State': 'Kansas St.',
                                                                  'Kennesaw State': 'Kennesaw St.',
                                                                  'Kent State': 'Kent St.',
                                                                  'Long Beach State': 'Long Beach St.',
                                                                  'Louisiana-Monroe ': 'ULM',
                                                                  'Loyola (IL)': 'Loyola Chicago',
                                                                  'Loyola (MD)': 'Loyola Maryland',
                                                                  'Maryland-Eastern Shore': 'UMES',
                                                                  'McNeese State': 'McNeese',
                                                                  'Merrimack College': 'Merrimack',
                                                                  'Michigan State': 'Michigan St.',
                                                                  'Middle Tennessee State': 'Middle Tennessee St.',
                                                                  'Mississippi State': 'Mississippi St.',
                                                                  'Mississippi Valley State': 'Mississippi Valley St.',
                                                                  'Missouri State': 'Missouri St.',
                                                                  'Montana State': 'Montana St.',
                                                                  'Morehead State': 'Morehead St.',
                                                                  'Morgan State': 'Morgan St.',
                                                                  'Murray State': 'Murray St.',
                                                                  'N.J.I.T.': 'NJIT',
                                                                  'New Mexico State': 'New Mexico St.',
                                                                  'Nicholls State': 'Nicholls',
                                                                  'Norfolk State': 'Norfolk St.',
                                                                  'North Dakota State': 'North Dakota St.',
                                                                  'Northwestern State': 'Northwestern St.',
                                                                  'Ohio State': 'Ohio St.',
                                                                  'Oklahoma State': 'Oklahoma St.',
                                                                  'Oregon State': 'Oregon St.',
                                                                  'Pennsylvania ': 'UPenn',
                                                                  'Penn State': 'Penn St.',
                                                                  'Portland State': 'Portland St.',
                                                                  'Queens University': 'Queens',
                                                                  'SIU-Edwardsville': 'SIUE',
                                                                  'Southern Methodist': 'SMU',
                                                                  'Sacramento State': 'Sacramento St.',
                                                                  'St. Francis (PA)': 'Saint Francis',
                                                                  'Sam Houston State': 'Sam Houston',
                                                                  'San Diego State': 'San Diego St.',
                                                                  'San Jose State': 'San Jose St.',
                                                                  'South Carolina State': 'South Carolina St.',
                                                                  'South Dakota State': 'South Dakota St.',
                                                                  'Tarleton State': 'Tarleton St.',
                                                                  'Tennessee State': 'Tennessee St.',
                                                                  'Tennessee-Martin': 'UT Martin',
                                                                  'Texas State': 'Texas St.',
                                                                  'Texas-Arlington': 'UT Arlington',
                                                                  'Texas-RGV': 'UTRGV',
                                                                  'Texas-San Antonio': 'UTSA',
                                                                  'Utah State': 'Utah St.',
                                                                  'Virginia Military': 'VMI',
                                                                  'Washington State': 'Washington St.',
                                                                  'Weber State': 'Weber St.',
                                                                  'Wichita State': 'Wichita St.',
                                                                  'Wright State': 'Wright St.',
                                                                  'Youngstown State': 'Youngstown St.',
                                                                  'Alabama A&M ': 'Alabama A&M',
                                                                  'Tennessee Tech ': 'Tennessee Tech'
                                                                  })


merge_all = pd.merge(net_alph, merged_off_def_alph, on = 'School', how = 'inner')
merge_all_alph = merge_all.sort_values(by='School')

merge_all_alph['PPG'] = merge_all_alph['PPG'].astype('float64')
merge_all_alph['FGM'] = merge_all_alph['FGM'].astype('float64')
merge_all_alph['FGA'] = merge_all_alph['FGA'].astype('float64')
merge_all_alph['FG%'] = merge_all_alph['FG%'].astype('float64')
merge_all_alph['3PM'] = merge_all_alph['3PM'].astype('float64')
merge_all_alph['3PA'] = merge_all_alph['3PA'].astype('float64')
merge_all_alph['3P%'] = merge_all_alph['3P%'].astype('float64')
merge_all_alph['FTM'] = merge_all_alph['FTM'].astype('float64')
merge_all_alph['FTA'] = merge_all_alph['FTA'].astype('float64')
merge_all_alph['FT%'] = merge_all_alph['FT%'].astype('float64')
merge_all_alph['ORB'] = merge_all_alph['ORB'].astype('float64')
merge_all_alph['DRB'] = merge_all_alph['DRB'].astype('float64')
merge_all_alph['RPG'] = merge_all_alph['RPG'].astype('float64')
merge_all_alph['APG'] = merge_all_alph['APG'].astype('float64')
merge_all_alph['SPG'] = merge_all_alph['SPG'].astype('float64')
merge_all_alph['BPG'] = merge_all_alph['BPG'].astype('float64')
merge_all_alph['TOV'] = merge_all_alph['TOV'].astype('float64')
merge_all_alph['PF'] = merge_all_alph['PF'].astype('float64')
merge_all_alph['Opp_PPG'] = merge_all_alph['Opp_PPG'].astype('float64')
merge_all_alph['Opp_FGM'] = merge_all_alph['Opp_FGM'].astype('float64')
merge_all_alph['Opp_FGA'] = merge_all_alph['Opp_FGA'].astype('float64')
merge_all_alph['Opp_FG%'] = merge_all_alph['Opp_FG%'].astype('float64')
merge_all_alph['Opp_3PM'] = merge_all_alph['Opp_3PM'].astype('float64')
merge_all_alph['Opp_3PA'] = merge_all_alph['Opp_3PA'].astype('float64')
merge_all_alph['Opp_3P%'] = merge_all_alph['Opp_3P%'].astype('float64')
merge_all_alph['Opp_FTM'] = merge_all_alph['Opp_FTM'].astype('float64')
merge_all_alph['Opp_FTA'] = merge_all_alph['Opp_FTA'].astype('float64')
merge_all_alph['Opp_FT%'] = merge_all_alph['Opp_FT%'].astype('float64')
merge_all_alph['Opp_ORB'] = merge_all_alph['Opp_ORB'].astype('float64')
merge_all_alph['Opp_DRB'] = merge_all_alph['Opp_DRB'].astype('float64')
merge_all_alph['Opp_RPG'] = merge_all_alph['Opp_RPG'].astype('float64')
merge_all_alph['Opp_APG'] = merge_all_alph['Opp_APG'].astype('float64')
merge_all_alph['Opp_SPG'] = merge_all_alph['Opp_SPG'].astype('float64')
merge_all_alph['Opp_BPG'] = merge_all_alph['Opp_BPG'].astype('float64')
merge_all_alph['Opp_TOV'] = merge_all_alph['Opp_TOV'].astype('float64')
merge_all_alph['Opp_PF'] = merge_all_alph['Opp_PF'].astype('float64')








cbbontop_score = merge_all_alph
cbbontop_score = cbbontop_score.assign(Cbbontop_Score = cbbontop_score.Quad_1_Wins * 10
                                             - cbbontop_score.Quad_1_Losses * 6
                                             + cbbontop_score.Quad_2_Wins * 8
                                             - cbbontop_score.Quad_2_Losses * 7
                                             + cbbontop_score.Quad_3_Wins * 4
                                             - cbbontop_score.Quad_3_Losses * 10
                                             + cbbontop_score.Quad_4_Wins * 2
                                             - cbbontop_score.Quad_4_Losses * 15 
                                       + cbbontop_score.PPG *1.5
                                       - cbbontop_score.Opp_PPG *1.25
                                       - cbbontop_score.TOV * 5
                                       + cbbontop_score.Opp_TOV * 5
                                       + cbbontop_score['3P%'] * 110
                                       + cbbontop_score['FT%'] * 75
                                       + cbbontop_score.ORB * 3
                                       - cbbontop_score.Opp_ORB * 3
                                       + cbbontop_score.APG * 1.5
                                       + cbbontop_score.BPG * 2.5
                                       - cbbontop_score.Opp_BPG * 2.5
                                       ) 
cbbontop_score.sort_values(by=['Cbbontop_Score'], ascending=[False], inplace=True)
cbbontop_score['Cbbontop_Rank'] = cbbontop_score['Cbbontop_Score'].rank(ascending=False)

# Save rankings for web display
rankings_df = cbbontop_score[['School', 'Conference', 'Record', 'Cbbontop_Score', 'Cbbontop_Rank']].copy()
rankings_df['Cbbontop_Rank'] = rankings_df['Cbbontop_Rank'].astype(int)
rankings_df['Cbbontop_Score'] = rankings_df['Cbbontop_Score'].round(2)
rankings_data = rankings_df.to_dict('records')
with open('cbbontop_rankings.json', 'w') as f:
    json.dump(rankings_data, f, indent=2)

#cbbontop_score[['School', 'Conference', 'Record', 'Cbbontop_Score', 'Cbbontop_Rank']]

cbbontop_score.to_pickle('cbbontop_score.pkl')