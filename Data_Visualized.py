from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly as plotly
import plotly.graph_objects as go

cbbontop_score = pd.read_pickle('cbbontop_score.pkl')
testing_df = cbbontop_score
Logos = {
     "Houston":"https://upload.wikimedia.org/wikipedia/commons/2/2a/University_of_Houston_Logo.svg",
      'Duke':"https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg",
     'Auburn':'https://upload.wikimedia.org/wikipedia/commons/1/15/Auburn_Tigers_logo.svg',
     'Florida':'https://upload.wikimedia.org/wikipedia/en/1/14/Florida_Gators_gator_logo.svg',
     "St. John's":'https://upload.wikimedia.org/wikipedia/commons/6/62/St._John%27s_Red_Storm_logo.svg',
     'Michigan St.':'https://upload.wikimedia.org/wikipedia/commons/5/56/Michigan_State_Spartans_script.svg',
     'Tennessee':'https://upload.wikimedia.org/wikipedia/commons/e/e3/Tennessee_Volunteers_logo.svg',
     'Alabama':'https://upload.wikimedia.org/wikipedia/commons/1/1b/Alabama_Crimson_Tide_logo.svg',
     'Maryland':'https://upload.wikimedia.org/wikipedia/commons/a/a6/Maryland_Terrapins_logo.svg',
     'Iowa St.':'https://upload.wikimedia.org/wikipedia/commons/f/f9/Iowa_State_Cyclones_logo.svg', #10
     'Texas Tech': 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Texas_Tech_Athletics_logo.svg',
     'Clemson': 'https://upload.wikimedia.org/wikipedia/commons/7/72/Clemson_Tigers_logo.svg',
     'Louisville': 'https://upload.wikimedia.org/wikipedia/en/5/59/Louisville_Cardinals_logo.svg',
     'Wisconsin': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Wisconsin_Badgers_logo.svg',
     "Saint Mary's": 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Saint_Mary%27s_College_Gaels_logo.svg',
     'UC San Diego': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/UC_San_Diego_Tritons_wordmark.svg',
     'Gonzaga': 'https://upload.wikimedia.org/wikipedia/en/b/bd/Gonzaga_Bulldogs_logo.svg',
     'Memphis': 'https://upload.wikimedia.org/wikipedia/en/4/45/Memphis_Tigers_logo.svg',
     'Oregon': 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Oregon_Ducks_logo.svg',
     'Drake': "https://upload.wikimedia.org/wikipedia/en/f/fc/Drake_Bulldogs_logo.svg", #20
     'Michigan': 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Michigan_Wolverines_logo.svg',
     'UCLA': 'https://upload.wikimedia.org/wikipedia/commons/e/ef/UCLA_Bruins_logo.svg',
     'BYU': 'https://upload.wikimedia.org/wikipedia/commons/9/95/BYU_Cougars_logo.svg',
     'Marquette': 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Marquette_Golden_Eagles_logo.svg',
     'New Mexico': 'https://upload.wikimedia.org/wikipedia/en/4/45/New_Mexico_Lobos_logo.svg',
     'VCU': 'https://upload.wikimedia.org/wikipedia/commons/b/bf/VCU_Rams_logo.svg',
     'UConn': 'https://upload.wikimedia.org/wikipedia/en/b/b0/Connecticut_Huskies_logo.svg',
     'Utah St.': 'https://upload.wikimedia.org/wikipedia/commons/5/59/Utah_State_Aggies_logo.svg',
     'Purdue': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Purdue_Boilermakers_logo.svg',
     'Arizona': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Arizona_Wildcats_logo.svg', #30
     'Texas A&M': 'https://upload.wikimedia.org/wikipedia/commons/e/ee/Texas_A%26M_University_logo.svg',
     'Ole Miss': 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Ole-miss_logo_from_NCAA.svg',
     'Kentucky': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Kentucky_Wildcats_logo.svg',
     'Missouri': 'https://upload.wikimedia.org/wikipedia/en/2/2c/Missouri_Tigers_logo.svg',
     'Mississippi St.': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Mississippi_State_Bulldogs_logo.svg',
     'Illinois': 'https://upload.wikimedia.org/wikipedia/commons/9/91/Illinois_Fighting_Illini_logo.svg',
     'Kansas': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Kansas_Jayhawks_1946_logo.svg',
     'Colorado St.': 'https://upload.wikimedia.org/wikipedia/en/1/14/Colorado_State_Rams_logo.svg',
     'UC Irvine': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/UC_Irvine_Anteaters_logo.svg',
     'Creighton': 'https://upload.wikimedia.org/wikipedia/en/6/6f/Creighton_Bluejays_logo.svg', #40
     'Liberty': 'https://upload.wikimedia.org/wikipedia/commons/5/53/Liberty_Flames_wordmark.svg',
     'SMU': 'https://upload.wikimedia.org/wikipedia/commons/3/33/SMU_Mustang_logo.svg',
     'Vanderbilt': 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Vanderbilt_Commodores_%282022%29_logo.svg',
     'Xavier': 'https://upload.wikimedia.org/wikipedia/commons/d/db/Xavier_Musketeers_logo.svg',
     'McNeese': 'https://upload.wikimedia.org/wikipedia/en/f/f7/McNeese_State_Athletics_logo.svg',
     'Boise St.': 'https://upload.wikimedia.org/wikipedia/en/9/94/Primary_Boise_State_Broncos_Athletics_Logo.svg',
     'Baylor': 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Baylor_Athletics_logo.svg',
     'Akron': 'https://upload.wikimedia.org/wikipedia/commons/0/01/Akron_Zips_logo_2022.svg',
     'San Diego St.': 'https://upload.wikimedia.org/wikipedia/commons/7/7c/San_Diego_State_Aztecs_logo.svg',
     'San Francisco': 'https://upload.wikimedia.org/wikipedia/commons/a/af/San_Francisco_Dons_logo.svg', #50
     'West Virginia': 'https://upload.wikimedia.org/wikipedia/commons/7/75/20150608194834%21West_Virginia_Mountaineers_logo.svg',
     'Oklahoma': 'https://upload.wikimedia.org/wikipedia/commons/3/30/OU-Logo.svg',
     'High Point': 'https://upload.wikimedia.org/wikipedia/commons/2/2c/High_Point_Panthers_logo.svg',
     'Dayton': 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Dayton_Flyers_logo.svg',
     'Bradley': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Bradley_Braves_logo.svg',
     'North Texas': 'https://upload.wikimedia.org/wikipedia/en/a/a2/North_Texas_Mean_Green_logo.svg',
     'Arkansas': 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Arkansas_text_logo.svg',
     'Texas': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Texas_Longhorns_logo.svg',
     'North Carolina': 'https://upload.wikimedia.org/wikipedia/commons/d/d7/North_Carolina_Tar_Heels_logo.svg',
     'Georgia': 'https://upload.wikimedia.org/wikipedia/commons/8/80/Georgia_Athletics_logo.svg', #60
     'Grand Canyon': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Grand_Canyon_University_2023_Logo_Update.svg',
     'Indiana': 'https://upload.wikimedia.org/wikipedia/commons/4/47/Indiana_Hoosiers_logo.svg',
     'Wake Forest': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Wake_Forest_University_Athletic_logo.svg',
     'Cincinnati': 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Cincinnati_Bearcats_logo.svg',
     'George Mason': 'https://upload.wikimedia.org/wikipedia/commons/c/c0/George_Mason_baseball_logo.svg',
     'Yale': 'https://upload.wikimedia.org/wikipedia/commons/2/2b/Yale_Bulldogs_script.svg',
     'Ohio St.': 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Ohio_State_Buckeyes_logo.svg',
     'Northwestern': 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Northwestern_Wildcats_logo.svg',
     'Samford': 'https://upload.wikimedia.org/wikipedia/en/b/b9/Samford_Bulldogs_logo.svg',
     'Santa Clara': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Santa-clara_logo_from_NCAA.svg', #70
     'Nebraska': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Nebraska_Cornhuskers_logo.svg',
     'Robert Morris': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Robert_Morris_University_logo.svg',
     'Iowa': 'https://upload.wikimedia.org/wikipedia/en/7/7b/Iowa_Hawkeyes_logo.svg',
     'Utah Valley': 'https://upload.wikimedia.org/wikipedia/en/c/c8/Utah_Valley_Wolverines_logo.svg',
     'Stanford': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Stanford_Cardinal_logo.svg',
     'Chattanooga': 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Chattanooga_Mocs_logo.svg',
     'UNC Wilmington': 'https://upload.wikimedia.org/wikipedia/commons/f/f1/UNC_Wilmington_Seahawks_wordmark.svg',
     'Villanova': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Villanova_Wildcats_logo.svg',
     'Arkansas St.': 'https://upload.wikimedia.org/wikipedia/en/3/36/Arkansas_State_Red_Wolves_logo.svg',
     'Furman': 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Furman_Paladins_logo.svg', #80
     'St. Thomas': 'https://upload.wikimedia.org/wikipedia/commons/3/3f/St-thomas-mn_logo_from_NCAA.svg',
     'Lipscomb': 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Lipscomb_logo_from_NCAA.svg',
     'CSUN': 'https://upload.wikimedia.org/wikipedia/commons/9/94/CSUN_Matadors_wordmark.svg',
     'Miami (OH)': 'https://upload.wikimedia.org/wikipedia/commons/b/b4/Miami_Redhawks_logo.svg',
     'St. Bonaventure': 'https://upload.wikimedia.org/wikipedia/commons/0/04/St_bona_wordmark_2016.png',
     'Pittsburgh': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Pitt_Panthers_wordmark.svg',
     'UAB': 'https://cdn.freebiesupply.com/logos/large/2x/alabama-birmingham-blazers-logo-svg-vector.svg',
     'UCF': 'https://upload.wikimedia.org/wikipedia/commons/f/fd/UCF_Knights_logo.svg',
     "Saint Joseph's": 'https://upload.wikimedia.org/wikipedia/en/7/76/Saint_Joseph%27s_Hawks_logo.svg',
     'Loyola Chicago': 'https://upload.wikimedia.org/wikipedia/en/6/69/Loyola_Ramblers_logo.svg', #90
     'Penn St.': 'https://sports.cbsimg.net/fly/images/team-logos/765.svg',
     'Montana': 'https://upload.wikimedia.org/wikipedia/commons/0/06/Montana_logo_from_NCAA.svg',
     'Belmont': 'https://upload.wikimedia.org/wikipedia/en/d/d6/Belmont_Bruins_logo.svg',
     'TCU': 'https://upload.wikimedia.org/wikipedia/commons/1/15/TCU_Horned_Frogs_logo.svg',
     'Middle Tennessee St.': 'https://upload.wikimedia.org/wikipedia/commons/e/ea/Middle_Tennessee_MT_Logomark.svg',
     'Oregon St.': 'https://upload.wikimedia.org/wikipedia/en/1/1b/Oregon_State_Beavers_logo.svg',
     'Northern Colorado': 'https://upload.wikimedia.org/wikipedia/en/f/f9/Northern_Colorado_Bears_logo.svg',
     'North Alabama': 'https://www.ncaa.com/sites/default/files/images/logos/schools/bgd/north-ala.svg',
     'Charleston': 'https://upload.wikimedia.org/wikipedia/commons/0/05/College_of_Charleston_Cougars_logo.svg',
     'Central Connecticut St.': 'https://upload.wikimedia.org/wikipedia/en/9/90/Central_Connecticut_Blue_Devils_logo.svg', #100
     'Kansas St.': 'https://upload.wikimedia.org/wikipedia/commons/6/6f/Kansas_State_Wildcats_baseball_logo.svg',
     'Troy': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Troy_Trojans_logo.svg',
     'USC': 'https://upload.wikimedia.org/wikipedia/commons/9/94/USC_Trojans_logo.svg',
     'Rutgers': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Rutgers_Scarlet_Knights_logo.svg',
     'Northern Iowa': 'https://upload.wikimedia.org/wikipedia/en/8/86/Northern_Iowa_Panters_logo.svg',
     'Minnesota': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/University_of_Minnesota_Logo.svg',
     'Georgetown': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Georgetown_Hoyas_logo.svg',
     'Utah': 'https://upload.wikimedia.org/wikipedia/commons/5/53/Utah_Utes_primary_logo.svg',
     'UC Riverside': 'https://upload.wikimedia.org/wikipedia/commons/2/21/UC_Riverside_Highlanders_logo.svg',
     'Towson': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Towson_Tigers_wordmark.svg', #110
     'Princeton': 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Princeton_Tigers_logo.svg',
     'Nevada': 'https://upload.wikimedia.org/wikipedia/en/2/21/Nevada_Wolf_Pack_logo.svg',
     'UNC Asheville': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Unc_asheville_second_logo_2004.png',
     'Jacksonville St.': 'https://upload.wikimedia.org/wikipedia/en/2/20/Jacksonville_State_Gamecocks_logo.svg',
     'UNLV': 'https://upload.wikimedia.org/wikipedia/commons/f/f6/UNLV_Rebels_wordmark.svg',
     'Norfolk St.': 'https://upload.wikimedia.org/wikipedia/en/7/78/Norfork_State_Spartans_logo.svg',
     'Cleveland St.': 'https://upload.wikimedia.org/wikipedia/en/7/70/Cleveland_State_Vikings_logo.svg',
     'Oklahoma St.': 'https://upload.wikimedia.org/wikipedia/commons/7/71/Oklahoma_State_Athletics_logo_%282014-2019%29.svg',
     'Kent St.': 'https://upload.wikimedia.org/wikipedia/en/a/a6/Kent_State_athletic_logo.svg',
     'Milwaukee': 'https://upload.wikimedia.org/wikipedia/en/0/00/Milwaukee_panthers_main_logo.png', #120
     'Florida St.': 'https://upload.wikimedia.org/wikipedia/en/d/d5/Florida_State_Seminoles_logo.svg',
     'Washington St.': 'https://upload.wikimedia.org/wikipedia/commons/8/80/Washington_State_Cougars_wordmark.svg',
     'Winthrop': 'https://upload.wikimedia.org/wikipedia/en/d/df/Winthrop_Eagles_logo.svg',
     'South Alabama': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/South_Alabama_Jaguars_wordmark.png',
     'Bryant': 'https://upload.wikimedia.org/wikipedia/en/c/ca/Bryant_Bulldogs_logo.svg',
     'UNC Greensboro': 'https://upload.wikimedia.org/wikipedia/en/7/70/UNCG_Spartans_logo.svg',
     'Cornell': 'https://upload.wikimedia.org/wikipedia/en/9/9b/Cornell_Big_Red_logo.svg',
     'Louisiana Tech': 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Louisiana_Tech_bgd_logo_from_NCAA.svg',
     'George Washington': 'https://upload.wikimedia.org/wikipedia/commons/1/12/George_Washington_Athletics_logo.svg',
     'James Madison': 'https://upload.wikimedia.org/wikipedia/commons/6/6d/James_Madison_University_Athletics_logo.svg', #130
     'North Dakota St.': 'https://upload.wikimedia.org/wikipedia/en/7/74/North_Dakota_State_Bison_logo.svg',
     'Georgia Tech': 'https://upload.wikimedia.org/wikipedia/commons/b/bf/Georgia_Tech_Yellow_Jackets_logo.svg',
     'UTEP': 'https://upload.wikimedia.org/wikipedia/en/0/06/UTEP_Miners_logo.svg',
     'Purdue Fort Wayne': 'https://upload.wikimedia.org/wikipedia/en/1/14/Purdue_Fort_Wayne_Mastodons_logo.svg',
     'Arizona St.': 'https://upload.wikimedia.org/wikipedia/en/0/0a/Arizona_State_Sun_Devils_logo.svg',
     'UC Santa Barbara': 'https://upload.wikimedia.org/wikipedia/en/a/a8/UC_Santa_Barbara_Gauchos_logo.svg',
     'Omaha': 'https://upload.wikimedia.org/wikipedia/commons/7/73/Omaha_Mavericks_logo.svg',
     'Washington': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Washington_Huskies_logo.svg',
     'South Dakota St.': 'https://upload.wikimedia.org/wikipedia/en/2/25/South_Dakota_State_Jackrabbits_logo.svg',
     'Southern': 'https://upload.wikimedia.org/wikipedia/commons/8/81/Southern-u_bgd_logo_from_NCAA.svg', #140
     'South Carolina St.': 'https://upload.wikimedia.org/wikipedia/en/a/ac/South_Carolina_State_Bulldogs_logo.svg',
     'Saint Louis': 'https://upload.wikimedia.org/wikipedia/en/0/03/Saint_Louis_Billikens_logo.svg',
     'Illinois St.': 'https://upload.wikimedia.org/wikipedia/en/f/f8/Illinois_State_Athletics_logo.svg',
     'Kennesaw St.': 'https://upload.wikimedia.org/wikipedia/commons/6/63/Kennesaw_State_Owls_logo.svg',
     'East Tennessee State': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/East_Tennessee_State_Buccaneers_logo.svg',
     'Virginia': 'https://upload.wikimedia.org/wikipedia/en/1/1e/Virginia_Cavaliers_logo.svg',
     'Radford': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Radford_Highlanders_logo.svg',
     'LSU': 'https://upload.wikimedia.org/wikipedia/commons/4/4a/LSU_Athletics_logo.svg',
     'Rhode Island': 'https://upload.wikimedia.org/wikipedia/commons/8/80/Rhode_Island_Rams_logo.svg',
     'Wofford': 'https://upload.wikimedia.org/wikipedia/en/5/5b/Wofford_Terriers_logo.svg', #150
     'Colorado': 'https://upload.wikimedia.org/wikipedia/en/d/d3/Colorado_Buffaloes_logo.svg',
     'Nicholls': 'https://upload.wikimedia.org/wikipedia/en/b/bb/Nicholls_State_Colonels_logo.svg',
     'East Carolina': 'https://upload.wikimedia.org/wikipedia/en/c/c7/East_Carolina_Pirates_logo.svg',
     'Tulane': 'https://upload.wikimedia.org/wikipedia/en/2/28/Tulane_Green_Wave_logo.svg',
     'Florida Atlantic': 'https://upload.wikimedia.org/wikipedia/en/4/40/Florida_Atlantic_Owls_logo.svg',
     'Eastern Kentucky': 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Eastern_Kentucky_Colonels_logo.svg',
     'UIC': 'https://upload.wikimedia.org/wikipedia/commons/a/a3/UIC_Flames_wordmark.svg',
     'Youngstown St.': 'https://upload.wikimedia.org/wikipedia/commons/8/84/Youngstown_State_Penguins_logo.svg',
     'Jacksonville': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Jacksonville_logo_from_NCAA.svg',
     'Wichita St.': 'https://upload.wikimedia.org/wikipedia/en/9/90/Wichita_State_Shockers_logo.svg', #160
     'Marshall': 'https://upload.wikimedia.org/wikipedia/commons/5/51/Marshall_University_logo.svg',
     'Loyola Marymount': 'https://upload.wikimedia.org/wikipedia/commons/6/62/LMU_Lions_logo.svg',
     'Notre Dame': 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Notre_Dame_Fighting_Irish_logo.svg',
     'Southeast Missouri State': 'https://upload.wikimedia.org/wikipedia/en/b/bb/Southeast_Missouri_State_Redhawks_logo.svg',
     'Lamar': 'https://upload.wikimedia.org/wikipedia/en/7/7a/Lamar_Cardinals_logo.svg',
     'SIUE': 'https://upload.wikimedia.org/wikipedia/commons/5/51/SIUE_Cougars_logo.svg',
     'Davidson': 'https://sports.cbsimg.net/fly/images/team-logos/551.svg',
     'Butler': 'https://upload.wikimedia.org/wikipedia/en/0/06/Butler_Bulldogs_logo.svg',
     'NC State': 'https://upload.wikimedia.org/wikipedia/en/4/41/NC_State_Wolfpack_logo.svg',
     'New Mexico St.': 'https://upload.wikimedia.org/wikipedia/en/c/c8/New_Mexico_State_Aggies_logo.svg', #170
     'Queens': 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Cdnlogo.com_queens-royals.svg',
     'California Baptist': 'https://upload.wikimedia.org/wikipedia/commons/6/69/California_Baptist_Lancers_wordmark.svg',
     'Portland St.': 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Portland-st_logo_from_NCAA.svg',
     'California': 'https://upload.wikimedia.org/wikipedia/commons/8/8b/California_Golden_Bears_logo.svg',
     'South Dakota': 'https://upload.wikimedia.org/wikipedia/en/a/ae/South_Dakota_Coyotes_logo.svg',
     'DePaul': 'https://upload.wikimedia.org/wikipedia/en/7/79/DePaul_Blue_Demons_logo.svg',
     'Western Kentucky': 'https://upload.wikimedia.org/wikipedia/en/1/1d/WKU_Athletics_logo.svg',
     'Toledo': 'https://upload.wikimedia.org/wikipedia/en/f/fa/Toledo_Rockets_logo.svg',
     'American': 'https://upload.wikimedia.org/wikipedia/commons/e/e6/American_logo_from_NCAA.svg',
     'Temple': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Temple_T_logo.svg', #180
     'Vermont': 'https://upload.wikimedia.org/wikipedia/en/3/34/Vermont_Catamounts_logo.svg',
     'Murray St.': 'https://upload.wikimedia.org/wikipedia/en/c/c9/Murray_State_Racers_logo.svg',
     'Longwood': 'https://upload.wikimedia.org/wikipedia/en/5/5f/Longwood_Lancers_logo.svg',
     'Texas A&M-CC': 'https://upload.wikimedia.org/wikipedia/en/e/eb/Texas_A%26M%E2%80%93Corpus_Christi_Islanders_logo.svg',
     'Syracuse': 'https://upload.wikimedia.org/wikipedia/commons/4/49/Syracuse_Orange_logo.svg',
     'Idaho St.': 'https://upload.wikimedia.org/wikipedia/en/6/63/Idaho_State_Bengals_logo.svg',
     'South Carolina': 'https://upload.wikimedia.org/wikipedia/commons/9/94/South_Carolina_Gamecocks_logo.svg',
     'Providence': 'https://upload.wikimedia.org/wikipedia/en/9/9d/Providence_Friars_logo.svg',
     'Marist': 'https://upload.wikimedia.org/wikipedia/en/5/5b/Marist_Red_Foxes_logo.svg',
     'Florida Gulf Coast': 'https://upload.wikimedia.org/wikipedia/en/9/95/Florida_Gulf_Coast_Eagles_logo.svg', #190
     'Maine': 'https://upload.wikimedia.org/wikipedia/en/d/d3/Maine_Black_Bears_logo.svg',
     'Virginia Tech': 'https://upload.wikimedia.org/wikipedia/commons/6/60/Virginia_Tech_Hokies_logo.svg',
     'Delaware St.': 'https://upload.wikimedia.org/wikipedia/en/d/db/Delaware_State_Hornets_logo.svg',
     'Brown': 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Brown_Bears_Athletics_logo.svg',
     'Hampton': 'https://upload.wikimedia.org/wikipedia/en/7/71/Hampton_pirates_athletics_logo.png',
     'Quinnipiac': 'https://upload.wikimedia.org/wikipedia/en/2/2c/Quinnipiac_Bobcats_logo.svg',
     'Little Rock': 'https://upload.wikimedia.org/wikipedia/en/d/d0/Little_Rock_Trojans_logo.svg',
     'Alabama St.': 'https://upload.wikimedia.org/wikipedia/en/7/7f/Alabama_State_Hornets_logo.svg',
     'Texas St.': 'https://upload.wikimedia.org/wikipedia/en/9/97/Texas_State_Bobcats_logo.svg',
     'San Jose St.': 'https://upload.wikimedia.org/wikipedia/en/e/ec/San_Jose_State_Spartans_logo.svg', #200
     "Mount St. Mary's": 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Mt-st-marys_logo_from_NCAA.svg',
     'Boston College': 'https://upload.wikimedia.org/wikipedia/en/9/96/Boston_College_Eagles_logo.svg',
     'Southeastern Louisiana': 'https://upload.wikimedia.org/wikipedia/en/3/33/Southeastern_Louisiana_Lions_logo.svg',
     'Northern Kentucky': 'https://upload.wikimedia.org/wikipedia/en/4/45/Northern_Kentucky_Norse_logo.svg',
     'William & Mary': 'https://upload.wikimedia.org/wikipedia/commons/9/98/William_%26_Mary_Athletics_logo.svg',
     'Ohio': 'https://upload.wikimedia.org/wikipedia/en/7/78/Ohio_Bobcats_logo.svg',
     'Valparaiso': 'https://upload.wikimedia.org/wikipedia/en/4/42/Valparaiso_Beacons_logo.svg',
     'Drexel': 'https://upload.wikimedia.org/wikipedia/en/1/16/Drexel_Dragons_logo.svg',
     'Northwestern St.': 'https://upload.wikimedia.org/wikipedia/en/3/3d/Northwestern_State_Demons_logo.svg',
     'La Salle': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/La_Salle_Explorers_primary_logo.svg', #210
     'Dartmouth': 'https://upload.wikimedia.org/wikipedia/commons/a/af/Dartmouth_College_Big_Green_logo.svg',
     'Duquesne': 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Duquesne_Dukes_logo.svg',
     'UC Davis': 'https://upload.wikimedia.org/wikipedia/commons/1/13/UC_Davis_Aggies_logo.svg',
     'Seattle': 'https://upload.wikimedia.org/wikipedia/commons/2/23/Seattle_redhawks_logo.png',
     'Merrimack': 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Merrimack_Warriors.svg',
     'UTRGV': 'https://upload.wikimedia.org/wikipedia/en/f/f6/UTRGV_Athletics_logo.svg',
     'App St.': 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Appalachian_State_Mountaineers_logo.svg',
     'Cal Poly': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Cal_Poly_Mustangs_logo.svg',
     'Sam Houston': 'https://upload.wikimedia.org/wikipedia/en/d/de/SHSU_athletics_logo.svg',
     'Northern Arizona': 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Northern_Arizona_Athletics_logo.svg', #220
     'UTSA': 'https://upload.wikimedia.org/wikipedia/en/1/1b/UTSA_Athletics_logo.svg',
     'Northeastern': 'https://upload.wikimedia.org/wikipedia/en/4/4d/Northeastern_Huskies_primary_logo.svg',
     'Abilene Christian': 'https://upload.wikimedia.org/wikipedia/en/6/6c/Abilene_Christian_Wildcats_logo.svg',
     'Oakland': 'https://upload.wikimedia.org/wikipedia/en/8/86/Oakland_Golden_Grizzlies_logo.svg',
     'Columbia': 'https://upload.wikimedia.org/wikipedia/en/5/5f/Columbia_Lions_logo.svg',
     'UMass Lowell': 'https://upload.wikimedia.org/wikipedia/en/4/43/UMass_Lowell_River_Hawks_logo.svg',
     'South Florida': 'https://upload.wikimedia.org/wikipedia/commons/1/13/Official_USF_Bulls_Athletic_Logo.png',
     'Central Michigan': 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Central_Michigan_Chippewas_logo.svg',
     'Elon': 'https://upload.wikimedia.org/wikipedia/en/3/3c/Elon_Phoenix_logo.svg',
     'Manhattan': 'https://upload.wikimedia.org/wikipedia/commons/0/06/Manhattan_Jaspers_logo.svg', #230
     'Incarnate Word': 'https://upload.wikimedia.org/wikipedia/en/e/ea/Incarnate_Word_Cardinals_logo.svg',
     'Hawaii': 'https://upload.wikimedia.org/wikipedia/commons/d/de/Hawaii_Warriors_logo.svg',
     'CSU Bakersfield': 'https://upload.wikimedia.org/wikipedia/en/c/cc/Cal_State_Bakersfield_Roadrunners_logo.svg',
     'Georgia Southern': 'https://upload.wikimedia.org/wikipedia/en/2/2a/Georgia_Southern_Eagles_logo.svg',
     'Eastern Michigan': 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Eastern_Michigan_Eagles_logo.svg',
     'Harvard': 'https://upload.wikimedia.org/wikipedia/commons/7/76/Harvard_Crimson_logo.svg',
     'Indiana St.': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Indiana_State_Sycamores_logo.svg',
     'Jackson St.': 'https://upload.wikimedia.org/wikipedia/commons/3/3c/Jackson_State_athletics_logo.svg',
     'Montana St.': 'https://upload.wikimedia.org/wikipedia/en/2/2f/Montana_State_Bobcats_logo.svg',
     'Bucknell': 'https://upload.wikimedia.org/wikipedia/en/3/3a/Bucknell_Bison_logo.svg', #240
     'Southern Illinois': 'https://upload.wikimedia.org/wikipedia/en/9/9f/Southern_Illinois_Salukis_logo.svg',
     'Campbell': 'https://upload.wikimedia.org/wikipedia/en/8/84/Campbell_Fighting_Camels_logo.svg',
     'Albany': 'https://upload.wikimedia.org/wikipedia/commons/0/03/Albany_Great_Danes_logo.svg',
     'Mercer': 'https://upload.wikimedia.org/wikipedia/en/f/fa/Mercer_Bears_logo.svg',
     'Bethune-Cookman': 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Bethune%E2%80%93Cookman_Wildcats_logo.svg',
     'Wyoming': 'https://upload.wikimedia.org/wikipedia/commons/9/91/Wyoming_Athletics_logo.svg',
     'North Florida': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Northflorida_ospreys_wmark_2014.svg',
     'Mercyhurst': 'https://upload.wikimedia.org/wikipedia/commons/9/95/Mercyhurst_logo_from_NCAA.svg',
     'Texas Southern': 'https://upload.wikimedia.org/wikipedia/en/9/9b/Texas_Southern_Tigers_logo.svg',
     'Massachusetts': 'https://upload.wikimedia.org/wikipedia/commons/1/1d/UMass_Athletics_wordmark.svg', #250
     'Wright St.': 'https://upload.wikimedia.org/wikipedia/en/c/c2/Wright_State_Raiders_logo.svg',
     'Rice': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Rice_Owls_logo.svg',
     'Kansas City': 'https://upload.wikimedia.org/wikipedia/en/7/75/Kansas_City_Roos_logo.svg',
     'Army': 'https://upload.wikimedia.org/wikipedia/commons/0/01/Army_West_Point_logo.svg',
     'Pepperdine': 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Pepperdine_logo_from_NCAA.svg',
     'VMI': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Virginia_Military_Institute_logo.png',
     'Tennessee St.': 'https://upload.wikimedia.org/wikipedia/en/d/d3/Tennessee_State_Athletics_logo.svg',
     'UT Arlington': 'https://upload.wikimedia.org/wikipedia/en/3/35/UT_Arlington_Mavericks_logo.svg',
     'Long Island': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/Long_Island_Sharks_wordmark_LIU.svg',
     'Austin Peay': 'https://upload.wikimedia.org/wikipedia/en/a/a8/Austin_Peay_Governors_logo.svg', #260
     'Hofstra': 'https://upload.wikimedia.org/wikipedia/commons/3/3f/Hofstra_athletics_H_logo.svg',
     'Fordham': 'https://upload.wikimedia.org/wikipedia/en/b/bb/Fordham_Rams_logo.svg',
     'Presbyterian': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Presbyterian_College_logo.png',
     'Iona': 'https://upload.wikimedia.org/wikipedia/en/1/19/Iona_Gaels_logo.svg',
     'Saint Francis': 'https://upload.wikimedia.org/wikipedia/commons/5/59/St-francis-pa_logo_from_NCAA.svg',
     'Wagner': 'https://upload.wikimedia.org/wikipedia/en/6/63/Wagner_Seahawks_logo.svg',
     'Monmouth': 'https://upload.wikimedia.org/wikipedia/en/1/18/Monmouth_Hawks.svg',
     'Seton Hall': 'https://upload.wikimedia.org/wikipedia/en/e/e1/Seton_Hall_Pirates_logo.svg',
     'Lindenwood': 'https://upload.wikimedia.org/wikipedia/en/7/74/Lindenwood_Lions_logo.svg', 
     'Miami (FL)': 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Miami_Hurricanes_logo.svg', #270
     'Portland': 'https://upload.wikimedia.org/wikipedia/en/4/43/Portland_pilots_anchor_logo.png',
     'Idaho': 'https://upload.wikimedia.org/wikipedia/commons/0/03/Idaho_Vandals_logo.svg',
     'Ball St.': 'https://upload.wikimedia.org/wikipedia/en/e/e4/Ball_State_Cardinals_logo.svg',
     'Siena': 'https://upload.wikimedia.org/wikipedia/en/9/91/Siena_Saints_New_Logo.png',
     'Florida A&M': 'https://upload.wikimedia.org/wikipedia/en/5/54/Florida_A%26M_Rattlers_logo.svg',
     'Sacred Heart': 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Sacred_Heart_Pioneers_logo.svg',
     'Bowling Green': 'https://upload.wikimedia.org/wikipedia/en/2/2b/Bowling_Green_Falcons_logo.svg',
     'Colgate': 'https://upload.wikimedia.org/wikipedia/commons/8/84/Colgate_Raiders_%282020%29_logo.svg',
     'Stephen F. Austin': 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Stephen_F._Austin_Athletics_wordmark.svg',
     'Georgia St.': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Georgia_State_Athletics_logo.svg', #280
     'Tarleton St.': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Tarleton-st_logo_from_NCAA.svg',
     'Richmond': 'https://upload.wikimedia.org/wikipedia/en/c/c3/Richmond_Spiders_logo.svg',
     'North Carolina Central': 'https://upload.wikimedia.org/wikipedia/en/1/13/NCCU_Eagles_head_mark_logo.svg',
     'Tennessee Tech': 'https://upload.wikimedia.org/wikipedia/en/f/f8/Tennessee_Tech_Golden_Eagles_logo.svg',
     'Delaware': 'https://upload.wikimedia.org/wikipedia/en/1/13/Delaware_Fightin%27_Blue_Hens_logo.svg',
     'Evansville': 'https://upload.wikimedia.org/wikipedia/commons/5/5b/Evansville_Athletics_logo.svg',
     'Boston University': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Boston_University_Terriers_wordmark.svg',
     'Stonehill': 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Stonehill_Skyhawks_logo.svg',
     'Morehead St.': 'https://upload.wikimedia.org/wikipedia/en/1/12/Morehead_State_Eagles_logo.svg',
     'Tulsa': 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Tulsa_Golden_Hurricane_logo.svg', #290
     "Saint Peter's": 'https://upload.wikimedia.org/wikipedia/en/9/97/Saint_Peter%27s_Peacocks_logo.svg',
     'Morgan St.': 'https://upload.wikimedia.org/wikipedia/en/8/8f/Morgan_State_Bears_logo.svg',
     'Western Michigan': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Western_Michigan_Broncos_text_logo.svg',
     'Alcorn St.': 'https://upload.wikimedia.org/wikipedia/commons/4/45/Alcorn_logo_from_NCAA.svg',
     'North Dakota': 'https://upload.wikimedia.org/wikipedia/en/9/92/North_Dakota_Fighting_Hawks_logo.svg',
     'Howard': 'https://upload.wikimedia.org/wikipedia/en/b/b4/Howard_Bison_logo.svg',
     'Eastern Illinois': 'https://upload.wikimedia.org/wikipedia/en/8/86/Eastern_Illinois_Panthers_logo.svg',
     'UPenn': 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Penn_Quakers_logo.svg',
     'Navy': 'https://upload.wikimedia.org/wikipedia/commons/a/a5/Navy_Athletics_logo.svg',
     'Florida International': 'https://upload.wikimedia.org/wikipedia/en/1/1d/FIU_Panthers_logo.svg', #300
     'Charlotte': 'https://upload.wikimedia.org/wikipedia/commons/3/33/Charlotte_49ers_logo.svg',
     'Southern Utah': 'https://upload.wikimedia.org/wikipedia/en/e/e7/Southern_Utah_Thunderbirds_logo.svg',
     'Denver': 'https://upload.wikimedia.org/wikipedia/commons/3/33/Denver_Pioneers_Athletics_logo.svg',
     'UT Martin': 'https://upload.wikimedia.org/wikipedia/en/2/2c/UT_Martin_Skyhawks_logo.svg',
     'UMBC': 'https://upload.wikimedia.org/wikipedia/en/c/cc/UMBC_Retrievers_logo.svg',
     'Fairleigh Dickinson': 'https://upload.wikimedia.org/wikipedia/en/a/a4/Fdu_knights_main_logo.png',
     'Rider': 'https://upload.wikimedia.org/wikipedia/en/6/62/Rider_Broncs.svg',
     'Old Dominion': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Old_Dominion_Athletics_logo_wordmark.svg',
     'Houston Christian': 'https://upload.wikimedia.org/wikipedia/en/b/b8/Houston_Baptist_Huskies_logo.svg',
     'Binghamton': 'https://upload.wikimedia.org/wikipedia/en/d/d8/Binghamton_Bearcats_logo.svg', #310
     'Missouri St.': 'https://upload.wikimedia.org/wikipedia/en/4/4e/Missouri_State_Athletics_logo.svg',
     'Eastern Washington': 'https://upload.wikimedia.org/wikipedia/en/8/80/Eastern_Washington_Eagles_logo.svg',
     'Lafayette': 'https://upload.wikimedia.org/wikipedia/en/8/8f/Lafayette_Leopards_logo.svg',
     'Louisiana': 'https://upload.wikimedia.org/wikipedia/commons/9/9b/La-lafayette_logo_from_NCAA.svg',
     'Loyola Maryland': 'https://upload.wikimedia.org/wikipedia/commons/3/32/Loyola-maryland_logo_from_NCAA.svg',
     'Gardner-Webb': 'https://upload.wikimedia.org/wikipedia/en/a/a3/Gardner%E2%80%93Webb_Runnin%27_Bulldogs_logo.svg',
     'IU Indy': 'https://upload.wikimedia.org/wikipedia/en/2/27/IU_indy_jaguars_logo.png',
     'Weber St.': 'https://upload.wikimedia.org/wikipedia/en/f/f2/Weber_State_Wildcats_logo.svg',
     'Lehigh': 'https://upload.wikimedia.org/wikipedia/en/6/65/LehighMountainHawks.svg',
     'Holy Cross': 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Holy_Cross_Crusaders_logo.svg', #320
     'Pacific': 'https://upload.wikimedia.org/wikipedia/en/5/5e/Pacific_Tigers_logo.svg',
     'Fairfield': 'https://upload.wikimedia.org/wikipedia/commons/0/0f/Fairfield_Stags_logo.svg',
     'Western Carolina': 'https://upload.wikimedia.org/wikipedia/en/5/50/Western_Carolina_Catamounts_logo.svg',
     'Western Illinois': 'https://upload.wikimedia.org/wikipedia/en/1/16/Western_Illinois_Leathernecks_logo.svg',
     'Southern Mississippi': 'https://upload.wikimedia.org/wikipedia/en/5/5d/Southern_Miss_Athletics_logo.svg',
     'Fresno St.': 'https://upload.wikimedia.org/wikipedia/en/7/7c/Fresno_State_Bulldogs_logo.svg',
     'Charleston Southern': 'https://upload.wikimedia.org/wikipedia/en/8/86/Charleston_Southern_Buccaneers_logo.svg',
     'Oral Roberts': 'https://upload.wikimedia.org/wikipedia/en/d/d8/Oral_Roberts_Golden_Eagles_logo.svg',
     'Southern Indiana': 'https://upload.wikimedia.org/wikipedia/en/1/12/Southern_Indiana_Screaming_Eagles_logo.svg',
     'Niagara': 'https://upload.wikimedia.org/wikipedia/en/1/1e/Niagara_Purple_Eagles_New_Logo.svg', #330
     'Grambling': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Grambling_State_Tigers_logo.svg',
     'Buffalo': 'https://upload.wikimedia.org/wikipedia/en/5/5e/Buffalo_Bulls_Athletic_Logo.svg',
     'Long Beach St.': 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Long-beach-st_logo_from_NCAA.svg',
     'Central Arkansas': 'https://upload.wikimedia.org/wikipedia/en/6/6d/Central_Arkansas_Athletics_logo.svg',
     'Alabama A&M': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Alabama_a%26m_bulldog_logo.png',
     'Coastal Carolina': 'https://upload.wikimedia.org/wikipedia/en/e/ef/Coastal_Carolina_Chanticleers_logo.svg',
     'Utah Tech': 'https://upload.wikimedia.org/wikipedia/en/e/ec/Utah_Tech_Trailblazers_logo_2022.svg',
     'Detroit Mercy': 'https://upload.wikimedia.org/wikipedia/en/a/a6/Detroit_Titans_logo.svg',
     'San Diego': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/San_Diego_Toreros_logo.svg',
     'North Carolina A&T': 'https://upload.wikimedia.org/wikipedia/commons/4/42/North_Carolina_A%26T_Aggies_logo.svg',
     'Air Force': 'https://upload.wikimedia.org/wikipedia/commons/d/dc/Air_Force_Falcons_logo.svg',
     'West Georgia': 'https://upload.wikimedia.org/wikipedia/commons/c/ca/West_Georgia_Wolves_logo.svg',
     'Stony Brook': 'https://upload.wikimedia.org/wikipedia/en/3/35/Stony_Brook_Seawolves_logo.svg',
     'Le Moyne': 'https://upload.wikimedia.org/wikipedia/en/c/cc/Le_Moyne_Dolphins_logo.svg',
     'Northern Illinois': 'https://upload.wikimedia.org/wikipedia/en/8/87/Northern_Illinois_Huskies_logo.svg',
     'ULM': 'https://upload.wikimedia.org/wikipedia/en/c/c9/Louisiana-Monroe_Warhawks_logo.svg',
     'Coppin St.': 'https://upload.wikimedia.org/wikipedia/en/8/85/Coppin_State_Eagles_logo.svg',
     'Sacramento St.': 'https://upload.wikimedia.org/wikipedia/commons/6/61/Sacramento_State_Hornets_logo.svg',
     'Cal St. Fullerton': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Cal-st-fullerton_logo_from_NCAA.svg',
     'Stetson': 'https://upload.wikimedia.org/wikipedia/en/6/61/Stetson_Hatters_current_logo.svg',
     'The Citadel': 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Citadel_Bulldogs_logo.svg',
     'Bellarmine': 'https://upload.wikimedia.org/wikipedia/en/9/92/Bellarmine_knights_logo20.png',
     'East Texas A&M': 'https://upload.wikimedia.org/wikipedia/en/f/f8/Texas_A%26M%E2%80%93Commerce_Lions_logo.svg',
     'USC Upstate': 'https://upload.wikimedia.org/wikipedia/commons/8/8e/USC_Upstate_Spartans_logo.svg',
     'Green Bay': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Green_Bay_Phoenix_logo.svg',
     'UMES': 'https://upload.wikimedia.org/wikipedia/en/6/65/Maryland_Eastern_Shore_Hawks_logo.svg',
     'New Hampshire': 'https://upload.wikimedia.org/wikipedia/en/6/62/New_Hampshire_Wildcats_logo.svg',
     'NJIT': 'https://upload.wikimedia.org/wikipedia/en/3/30/NJIT_Highlanders_logo.svg',
     'Prairie View A&M': 'https://upload.wikimedia.org/wikipedia/commons/8/81/Prairie_view_univ_athletics_textlogo.png',
     'New Orleans': 'https://upload.wikimedia.org/wikipedia/commons/9/91/New_Orleans_Privateers_wordmark.svg',
     'Chicago St.': 'https://upload.wikimedia.org/wikipedia/en/b/b2/Chicago_State_Cougars_logo.svg',
     'Arkansas Pine Bluff': 'https://upload.wikimedia.org/wikipedia/en/a/a6/Arkansas%E2%80%93Pine_Bluff_Golden_Lions_logo.svg',
     'Canisius': 'https://upload.wikimedia.org/wikipedia/en/6/69/Canisius_Golden_Griffins_Logo.svg',
     'Mississippi Valley St.': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Mississippi_Valley_State_University_athletics_logo.svg'
}


logos_df = pd.DataFrame(list(Logos.items()), columns=['School', 'Logo'])
testing_df_2 = testing_df.merge(logos_df, on='School', how='left')



import plotly.graph_objects as go

cols = [ "Cbbontop_Score", "Wins", "Losses", "Quad_1_Wins", "Quad_2_Wins", "Quad_3_Wins", "Quad_4_Wins", "Quad_1_Losses", "Quad_2_Losses", "Quad_3_Losses", 
        "Quad_4_Losses", "WAB", "PPG", "FGM", 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'ORB', 'RPG', 'APG', 'SPG', 'BPG', 'TOV', 'PF', 'Opp_PPG', 
         'Opp_FGM', 'Opp_FGA', 'Opp_FG%', 'Opp_3PM', 'Opp_3PA', 'Opp_3P%', 'Opp_FTM', 'Opp_FTA', 'Opp_ORB', 'Opp_RPG', 'Opp_APG', 'Opp_SPG', 'Opp_BPG', 'Opp_TOV',
         'Opp_PF']
rel_size = 0.1  # logo size as a fraction of axis span

def axis_range_for(col, df, pad=0.05):
    vmin, vmax = df[col].min(), df[col].max()
    span = vmax - vmin
    return [vmin - span*pad, vmax + span*pad]

# INITIAL STATE
x_init = "Cbbontop_Score"
y_init = "Wins"

# Build figure and initial scatter
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=testing_df_2[x_init],
    y=testing_df_2[y_init],
    text=testing_df_2['School'],
    mode='markers',
    opacity=0,              # hide dots; we’re using logos
    name='Schools',
))

# Initial ranges + logo sizes
xr = axis_range_for(x_init, testing_df_2)
yr = axis_range_for(y_init, testing_df_2)
xspan = xr[1] - xr[0]
yspan = yr[1] - yr[0]

# Add logos once, in a fixed order
images = []
for _, row in testing_df_2.iterrows():
    images.append(dict(
        source=row["Logo"],
        x=row[x_init], y=row[y_init],
        xref="x", yref="y",
        sizex=xspan*rel_size, sizey=yspan*rel_size,
        xanchor="center", yanchor="middle",
        layer="above"
    ))

fig.update_layout(
    images=images,
    xaxis=dict(title=x_init, range=xr),  # Should be "Cbbontop_Score"
    yaxis=dict(title=y_init, range=yr)   # Should be "Wins"
)

# --- DROPDOWNS ---

# X-axis menu: update x data, xaxis, and ONLY images[*].x / images[*].sizex
x_dropdown_buttons = []
for col in cols:
    xr = axis_range_for(col, testing_df_2)
    xspan = xr[1] - xr[0]

    layout_update = {
        "xaxis.title": col,
        "xaxis.range": xr,
    }
    # update every image's x and sizex, leave y & sizey untouched
    for i, val in enumerate(testing_df_2[col].tolist()):
        layout_update[f"images[{i}].x"] = val
        layout_update[f"images[{i}].sizex"] = xspan * rel_size

    x_dropdown_buttons.append({
        "label": col,  # This should show the actual column name
        "method": "update",
        "args": [
            {"x": [testing_df_2[col]]},  # trace 0 x
            layout_update
        ]
    })

# Y-axis menu: update y data, yaxis, and ONLY images[*].y / images[*].sizey
y_dropdown_buttons = []
for col in cols:
    yr = axis_range_for(col, testing_df_2)
    yspan = yr[1] - yr[0]

    layout_update = {
        "yaxis.title": col,
        "yaxis.range": yr,
    }
    # update every image's y and sizey, leave x & sizex untouched
    for i, val in enumerate(testing_df_2[col].tolist()):
        layout_update[f"images[{i}].y"] = val
        layout_update[f"images[{i}].sizey"] = yspan * rel_size

    y_dropdown_buttons.append({
        "label": col,
        "method": "update",
        "args": [
            {"y": [testing_df_2[col]]},  # trace 0 y
            layout_update
        ]
    })

fig.update_layout(
    updatemenus=[
        {"buttons": x_dropdown_buttons, "direction": "down", "x": 1.1, "y": 1.15, "showactive": True},
        {"buttons": y_dropdown_buttons, "direction": "down", "x": 1.1, "y": 1.05, "showactive": True},
    ]
)

#fig.show()

plot_html = fig.to_html(include_plotlyjs=True)
with open('scatter_plot.html', 'w', encoding='utf-8') as f:
    f.write(plot_html)