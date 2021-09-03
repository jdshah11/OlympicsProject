import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

athletes_df = pd.read_csv('C:/Users/DC/Downloads/athlete_events.csv')
noc_regions = pd.read_csv('C:/Users/DC/Downloads/noc_regions.csv')
athletes_df.head()
top_10_countries  = athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.title("overall data")
sns.barplot(x=top_10_countries.index,y=top_10_countries,palette='Set2')
plt.show()
#winter_sports = athletes_df(athletes_df.season == 'Winter')
# print(athletes_df.head())
nan_values = athletes_df.isna()
#print(nan_values)'''
#print(noc_regions)
#print(athletes_df)
#NHK (31)
#print(winter_sports = atheles_df (atheles_df.Season == 'Winter').Sport.unique())

gender_count = atheles_df.Sex.value_counts()
#print(gender_count)
#plt.figure(figsize=(12,6))
#plt.title('Gender Distribution')
#plt.pie(gender_count , labels=gender_count.index, autopct='%1.1f%%', startangle=150, shadow=True);
#plt.show()

#total medals
#print(atheles_df.Medal.value_counts())

# ERRO   NHK (39)
#female_partic = atheles_df[(atheles_df.Sex == 'F') & (atheles_df.Season == 'Summer')][['Sex', 'Season']]
#female_partic = female_partic.groupby('Year').count().reset_index()
#print(female_partic.head(10))

women_participation = atheles_df[(atheles_df.Sex == 'F') & (atheles_df.Season == 'Summer')]
#print(women_participation)


#sns.set(style='darkgrid')
#plt.figure(figsize=(20,10))
#sns.countplot(x='Year', data=women_participation, palette='Spectral')
#plt.title('Women Participation')
#plt.show()

#part=women_participation.groupby('Year')['Sex'].value_counts()
#plt.figure(figsize=(20,10))
#part.loc[:,'F'].plot()
#plt.title('Plot of female atheletes over time')
#plt.show()

gold_medal=atheles_df[(atheles_df.Medal == 'Gold')]
#print(gold_medal.head(10))

#takes value different from Nan
gold_medal = gold_medal[np.isfinite(gold_medal['Age'])]
#print(gold_medal)

#print(gold_medal['ID'][gold_medal ['Age'] > 60].count())

sporting_event= gold_medal['Sport'][gold_medal['Age']>60]
#print(sporting_event)

#plt.figure(figsize=(10,5))
#plt.tight_layout()
#sns.countplot(sporting_event)
#plt.title('Gold Medal for athelete having age over 60')
#plt.show()

#medals/country
#print(gold_medal.region.value_counts().reset_index(name='Medal').head(5))

#totalgoldmedals = gold_medal.region.value_counts().reset_index(name='Medal').head(6)
#g=sns.catplot(x='index', y='Medal', data=totalgoldmedals, height=5 , kind="bar", palette="rocket")
#g.despine(left=True)
#g.set_xlabels("Top 6 countries")
#g.set_ylabels("Number of Medals")
#plt.title('GOld Medal per Country')
#plt.show()

# Latest OLYMPiC
max_year= atheles_df.Year.max()
#print(max_year)
team_names=atheles_df[(atheles_df.Year == max_year) & (atheles_df.Medal == 'Gold')].Team
#print(team_names.value_counts().head(10))

#sns.barplot(x=team_names.value_counts().head(20), y=team_names.value_counts().head(20).index)
#plt.ylabel(None);
#plt.xlabel('Countrywise Medal for 2016')
#plt.show()

not_null_medal= atheles_df[(atheles_df['Height'].notnull()) & (atheles_df['Weight'].notnull())]
#print(not_null_medal)

#plt.figure(figsize=(12,10))
#axis= sns.scatterplot(x="Height" , y="Weight", data=not_null_medal , hue="Sex")
#plt.title('Height vs Weight of Medalist')
#plt.show()