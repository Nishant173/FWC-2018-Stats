# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 11:15:54 2018

@author: Nishant
"""

""" FIFA WORLD CUP 2018 - Statistics """


# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
df = pd.read_csv("fifa-2018-statistics.csv")
df.head()

# display columns (features)
columns = df.columns
print(columns)

# no. of games played per team
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Number of games played", fontsize = 30)
plt.xlabel("count", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
# plt.xticks(np.arange(8), ("Begins", "MD1", "MD2", "MD3", "RO 16", "Quarters", "Semis", "3rd place playoff & Final"))
plt.xticks([0,1,2,3,4,5,6,7])
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
df['Team'].value_counts().plot(kind = 'barh', color = "#008080")
plt.text(4, 14, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("001 - Number of games played.png")

# no. of games played per team by stages
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Number of games played (by stages)", fontsize = 30)
plt.xlabel("Stage", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks(np.arange(8), ("Begins", "MD1", "MD2", "MD3", "RO 16", "Quarters", "Semis", "3rd place playoff & Final"))
# plt.xticks([0,1,2,3,4,5,6,7])
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
df['Team'].value_counts().plot(kind = 'barh', color = "#FA8072")
plt.text(4, 14, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='black',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("001_by_stages - Number of games played (by stages).png")


# checking
df["Team"]
df["Ball Possession %"]


# print fixtures
i = 0; j = 1; # initialize indices

while(j < 128):
    for k in range(1, int(len(df)/2) + 1):        
        print("Match #", k, ":")
        print(df["Team"][i]); print("vs."); print(df["Team"][j]); print("\n\n")
        i+=2;
        j+=2;

pso = df[df["PSO"] == "Yes"]
pso = pso.reset_index(drop = True)
print("\n\n Number of games that went to penalties: ", int(pso.PSO.value_counts()[0]/2))

# print only games that went to penalties
i = 0; j = 1;

while(j < 8):
    for k in range(1, int(len(pso)/2) + 1):        
        print("Penalty Shoot-Out Match #", k, ":")
        print(pso["Team"][i]); print("vs."); print(pso["Team"][j]); print("\n\n")
        i+=2;
        j+=2;

# no. of motm per team
motm = df[df['Man of the Match'] == "Yes"]
# motm.Team.value_counts().plot(kind = 'barh')

plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Number of MOTM awards (by team)", fontsize = 30)
plt.xlabel("count", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
motm.Team.value_counts().plot(kind = 'barh', color = "#17E175")
plt.text(4, 14, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='black',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("002 - Number of MOTM awards (by team).png")


""" # cards received! """

"""
# no. of red cards per team
red_cards = df[df['Red'] == 1]
red_cards.Team.value_counts().plot(kind = 'barh')

yellow_red_cards = df[df['Yellow & Red'] != 0]
yellow_red_cards.Team.value_counts().plot(kind = 'barh')
"""

# no. of yellow cards per team
yellow_cards = df[df['Yellow Card'] != 0]
yellow_cards.Team.value_counts().plot(kind = 'barh')

yellow_cards.Team.value_counts() # numerator
df.Team.value_counts() # denominator

# normalizing per 90 mins
yellow_cards_per_90 = yellow_cards.Team.value_counts()/df.Team.value_counts()
# yellow_cards_per_90.sort_values(ascending = False).plot(kind = 'barh')


for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Yellow Card'].mean()
    print("\n Average yellow cards per game by ", df['Team'].unique()[i], ": ", rus['Yellow Card'].mean())



# initialize empty lists --- 1) team name & 2) avg yellows per game
list_hist_team_name = []
list_hist_yellows = []

# appends team_name & respective avg possession from "rus" dataframe (sorted per team)
for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_team_name.append(rus.Team.unique()[0])

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_yellows.append(float(rus['Yellow Card'].mean()))

# sorting process
# create dataframe
df_for_yc = {"Team name":list_hist_team_name,
              "YCs":list_hist_yellows
              }

df_for_yc = pd.DataFrame(df_for_yc)

# sort it
df_for_yc_sorted = df_for_yc.sort_values(by = "YCs", ascending = False)

# plot (sorted)
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Yellow Cards received per match", fontsize = 30)
plt.xlabel("count", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
# plt.xlim(0, float(df_for_attempts_sorted["Attempts"].max() + 1)) # keeping a constant x-limit for easier comparisons
plt.barh(df_for_yc_sorted["Team name"], df_for_yc_sorted["YCs"], color = "#FFFF00")
plt.legend(loc = 'best', fontsize = 15)
plt.text(2, 14, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='black',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("003 - Yellow Cards received per match.png")


""" # histogram - goals scored per game b/w 2 teams """
# initialize empty list
list_hist_gspg = []

# append each value of gspg b/w 2 teams (using a stepsize of 2)
for i in range(0, 127, 2):
    print(df['Goal Scored'][i] + df['Goal Scored'][i+1])
    list_hist_gspg.append(df['Goal Scored'][i] + df['Goal Scored'][i+1])

# initialize no. of matches for x-axis
x_axis = np.arange(0,64)
x_axis

# calculate avg gspg from the list created
sum_calc = 0;

for k in range(0, 64):
    sum_calc += list_hist_gspg[k]

print("\n Avg. no. of goals scored per game is: ", "{:.2f}".format(sum_calc/64))

# plot
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Goals scored in each game", fontsize = 30)
plt.xlabel("Match number", fontsize = 20)
plt.ylabel("Goals scored (count)", fontsize = 20)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.bar(x_axis, list_hist_gspg)
plt.axhline(y = float(sum_calc/64), color = '#DA3D0B', linewidth = 4, label = "Average over all matches") # horizontal line showing the avg
plt.legend(loc = 'best', fontsize = 20)
plt.text(32, 5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='black',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("004 - Goals scored in each game.png")


""" # possession comparison b/w alll 64 teams """
# initialize empty lists --- 1) team name & 2) avg ball possession
list_hist_team_name = []
list_hist_pos = []

# appends team_name & respective avg possession from "rus" dataframe (sorted per team)
for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_team_name.append(rus.Team.unique()[0])

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_pos.append(float(rus['Ball Possession %'].mean()))

# sorting
# create dataframe
df_for_pos = {"Team name":list_hist_team_name,
              "Possessions":list_hist_pos
              }

df_for_pos = pd.DataFrame(df_for_pos)

# sort it
df_for_pos_sorted = df_for_pos.sort_values(by = "Possessions", ascending = False)

# plot (sorted)
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Average Ball Possession", fontsize = 30)
plt.xlabel("Ball Possession %", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks([10,20,30,40,50,60,70,80,90,100], fontsize = 14)
plt.yticks(fontsize = 14)
# plt.xlim(0, 100) # keeping a constant x-limit for easier comparisons
plt.barh(df_for_pos_sorted["Team name"], df_for_pos_sorted["Possessions"], color = "#8A2BE2")
plt.legend(loc = 'best', fontsize = 15)
plt.text(30, 18, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("005 - Average Ball Possession.png")



""" # Attempts made """
# initialize empty lists --- 1) team name & 2) avg attempts per game
list_hist_team_name = []
list_hist_attempts = []

# appends team_name & respective avg possession from "rus" dataframe (sorted per team)
for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_team_name.append(rus.Team.unique()[0])

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_attempts.append(float(rus['Attempts'].mean()))

# sorting
# create dataframe
df_for_attempts = {"Team name":list_hist_team_name,
              "Attempts":list_hist_attempts
              }

df_for_attempts = pd.DataFrame(df_for_attempts)

# sort it
df_for_attempts_sorted = df_for_attempts.sort_values(by = "Attempts", ascending = False)

# plot (sorted)
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Average Attempts made per game", fontsize = 30)
plt.xlabel("Attempts made (count)", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
# plt.xlim(0, float(df_for_attempts_sorted["Attempts"].max() + 1)) # keeping a constant x-limit for easier comparisons
plt.barh(df_for_attempts_sorted["Team name"], df_for_attempts_sorted["Attempts"], color = "#6B8E23")
plt.legend(loc = 'best', fontsize = 15)
plt.text(13, 18, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("006 - Average Attempts made per game.png")



""" # Goals scored per attempt OR Attempts taken per goal scored """
# initialize empty lists --- 1) team name & 2) avg attempts per game
list_hist_team_name = []
list_hist_attempts = []
list_hist_gs = []
list_conv_rate = []
list_conv_rate_2dp = [] # list with conv_rate of 2 decimal places

# appends team_name & respective avg attempts & GS from "rus" dataframe (sorted per team)
for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_team_name.append(rus.Team.unique()[0])

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_attempts.append(float(rus['Attempts'].mean()))

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    list_hist_gs.append(float(rus['Goal Scored'].mean()))

for i in range(0, 32):
    list_conv_rate.append(list_hist_attempts[i]/list_hist_gs[i])

for i in range(0, 32):
    list_conv_rate_2dp.append(float("{:.2f}".format(list_conv_rate[i])))


# create dataframe
# conversion_rate = attempts per goals scored (higher the worse, lower the better)
conversion_rate = {"Team name":list_hist_team_name,
              "Attempts":list_hist_attempts,
              "Goals Scored":list_hist_gs,
              "Conversion Rate":list_conv_rate,
              "Conv Rate 2d":list_conv_rate_2dp
              }

conversion_rate = pd.DataFrame(conversion_rate)

# sort it
conversion_rate_sorted = conversion_rate.sort_values(by = "Conversion Rate", ascending = False)

# plot (sorted)
plt.figure(figsize = (25,14))
plt.title("FIFA World Cup 2018 - Attempts made per goal scored (Lower the better)", fontsize = 30)
plt.xlabel("Attempts made (count)", fontsize = 20)
plt.ylabel("Team", fontsize = 20)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.xlim(0, conversion_rate_sorted["Conversion Rate"].max() + 1) # keeping a constant x-limit for easier comparisons
plt.barh(conversion_rate_sorted["Team name"], conversion_rate_sorted["Conversion Rate"], color = "#00008B")
plt.legend(loc = 'best', fontsize = 15)
plt.text(19, 18, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
plt.savefig("007 - Attempts made per goal scored (Lower the better).png")


# ---------------------------------------------------------------------------------------------

""" # fouls committed per team, & their avgs """
# rus = df[df.Team.str.contains('Russia')==True].reset_index() # initially coded for 1 team
# "rus" is a variable for a team name (initially stood for Russia)
# Avg fouls committed per team per game
for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Fouls Committed'].mean() # calculates the avg
    print("\n Average fouls committed per game by ", df['Team'].unique()[i], ": ", rus['Fouls Committed'].mean())


# loop to create 32 graphs labelled 0 - 31, for 32 teams' Fouls committed per game, & avg
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Fouls committed per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("count", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Fouls Committed'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Fouls Committed'].plot(kind = 'barh', color = '#2C8DCF', label = "Fouls committed in each individual match")
    plt.axvline(x = int(rus['Fouls Committed'].mean()), color = '#C60A0A', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(12, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Fouls committed per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" # distance covered in kms, per team, + avgs """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Distance Covered (Kms)'].mean() # calculates the avg
    print("\n Average distance covered per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Distance Covered (Kms)'].mean()), "kms\n")

# loop to create 32 graphs labelled 0 - 31, for 32 teams' Dist. covered per game, & avg
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Distance Covered (Kms) per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("distance (in kms)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Distance Covered (Kms)'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Distance Covered (Kms)'].plot(kind = 'barh', color = '#42D125', label = "Distance Covered (Kms) in each individual match")
    plt.axvline(x = int(rus['Distance Covered (Kms)'].mean()), color = '#D418D1', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(80, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='orange',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Distance Covered (Kms) per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" # passes """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Passes'].mean() # calculates the avg
    print("\n Passes per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Passes'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' passes
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Passes per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("passes (count)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Passes'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Passes'].plot(kind = 'barh', color = '#DA43AC', label = "Passes in each individual match")
    plt.axvline(x = int(rus['Passes'].mean()), color = '#C5D70B', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(500, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='black',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Passes per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" # Pass Accuracy % """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Pass Accuracy %'].mean() # calculates the avg
    print("\n Pass Accuracy % per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Pass Accuracy %'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' pass acc. %
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Pass Accuracy % per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Pass Accuracy %", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, 100) # keeping a constant x-limit for easier comparisons
    rus['Pass Accuracy %'].plot(kind = 'barh', color = '#C4BB19', label = "Pass Accuracy % in each individual match")
    plt.axvline(x = int(rus['Pass Accuracy %'].mean()), color = '#C06534', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(50, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Pass Accuracy percentage per game - %s - Accuracy.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.




""" Goals Scored per team """

i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Goal Scored'].mean() # calculates the avg
    print("\n Goals Scored per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Goal Scored'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' GSPG
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Goals Scored per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Goals Scored (count)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, float(df['Goal Scored'].max() + 0.1)) # keeping a constant x-limit for easier comparisons
    rus['Goal Scored'].plot(kind = 'barh', color = '#0B32C8', label = "Goals Scored in each individual match")
    plt.axvline(x = float(rus['Goal Scored'].mean()), color = '#020313', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(3, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Goals Scored per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" Ball Possession % per team """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Ball Possession %'].mean() # calculates the avg
    print("\n Ball Possession % per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Ball Possession %'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' possession
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Ball Possession % per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Ball Possession %", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks([10,20,30,40,50,60,70,80,90,100], fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, 100) # keeping a constant x-limit for easier comparisons
    rus['Ball Possession %'].plot(kind = 'barh', color = '#2BC1D7', label = "Ball Possession % in each individual match")
    plt.axvline(x = float(rus['Ball Possession %'].mean()), color = '#DC3E8F', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(50, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Ball Possession percentage per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.




""" Saves per game """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Saves'].mean() # calculates the avg
    print("\n Saves per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Saves'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' saves
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Saves per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Saves (count)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Saves'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Saves'].plot(kind = 'barh', color = '#1CA04B', label = "Saves in each individual match")
    plt.axvline(x = int(rus['Saves'].mean()), color = '#E84A10', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(4.5, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Saves per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" Free Kicks won per game """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Free Kicks'].mean() # calculates the avg
    print("\n Free Kicks won per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Free Kicks'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' free kicks
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Free Kicks won per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Free Kicks won (count)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Free Kicks'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Free Kicks'].plot(kind = 'barh', color = '#A22727', label = "Free Kicks won in each individual match")
    plt.axvline(x = float(rus['Free Kicks'].mean()), color = '#10D5D7', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(12, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Free Kicks won per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.


""" Corners won per game """
i = 0;

for i in range(0, 32):
    # print(df['Team'].unique()[i])
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index() # Team is --- df['Team'].unique()[i]
    rus['Corners'].mean() # calculates the avg
    print("\n Corners won per game by ", df['Team'].unique()[i], ": ", "{:.2f}".format(rus['Corners'].mean()))

# loop to create 32 graphs labelled 0 - 31, for 32 teams' corners
i = 0;

for i in range(0, 32):
    rus = df[df.Team.str.contains(df['Team'].unique()[i])==True].reset_index()
    rus.index = np.arange(1, len(rus) + 1)
    rus.Team.unique()[0] # shows name of team

    plt.figure(figsize = (25,14))
    #plt.title("FIFA World Cup 2018 - Fouls committed per game", fontsize = 30)
    plt.title("FIFA World Cup 2018 - Corners won per game - " + str(rus.Team.unique()[0]), fontsize = 30)
    plt.xlabel("Corners won (count)", fontsize = 20)
    plt.ylabel("Match number", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.xlim(0, int(df['Corners'].max() + 2)) # keeping a constant x-limit for easier comparisons
    rus['Corners'].plot(kind = 'barh', color = '#1D8625', label = "Corners won in each individual match")
    plt.axvline(x = float(rus['Corners'].mean()), color = '#7D4C4C', linewidth = 4, label = "Average over all matches for this team") # vertical line showing the avg
    plt.legend(loc = 'best', fontsize = 15)
    #plt.savefig("004_supposedly.png")
    #plt.savefig("%i.png" % i) # integer indexing
    plt.text(5, 1.5, 'Created by Nishant Rao (Twitter: @nishant173)',
         fontsize=40, color='grey',
         horizontalalignment='center',
         verticalalignment='center', alpha=0.8)
    plt.savefig("Corners won per game - %s.png" % rus.Team.unique()[0]) # indexing by name of team, using strings
# break the loop.

# END.