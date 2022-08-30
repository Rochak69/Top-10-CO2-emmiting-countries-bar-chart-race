from operator import truediv
from pickletools import int4, long1
from tokenize import Double
import bar_chart_race as bcr
import pandas as pd

df= pd.read_csv("countries.csv", index_col="Year")

print(df.head)


df.fillna(0.0, inplace=True)




df["Nepal"]= df["Nepal"].str.replace('[\,\,]', "")
df["Brazil"]= df["Brazil"].str.replace('[\,\,]', "")
df["China"]= df["China"].str.replace('[\,\,]', "")
df["Iran"]= df["Iran"].str.replace('[\,\,]', "")
df["Kazakhstan"]= df["Kazakhstan"].str.replace('[\,\,]', "")
df["Malaysia"]= df["Malaysia"].str.replace('[\,\,]', "")
df["Mexico"]= df["Mexico"].str.replace('[\,\,]', "")
df["Russia"]= df["Russia"].str.replace('[\,\,]', "")
df["SouthAfrica"]= df["SouthAfrica"].str.replace('[\,\,]', "")
df["Thailand"]= df["Thailand"].str.replace('[\,\,]', "")
df["USA"]= df["USA"].str.replace('[\,\,]', "")
df["India"]= df["India"].str.replace('[\,\,]', "")
df["Japan"]= df["Japan"].str.replace('[\,\,]', "")
df["Germany"]= df["Germany"].str.replace('[\,\,]', "")
df["Indonesia"]= df["Indonesia"].str.replace('[\,\,]', "")
df["South_Korea"]= df["South_Korea"].str.replace('[\,\,]', "")
df["Canada"]= df["Canada"].str.replace('[\,\,]', "")
df["Saudi_Arabia"]= df["Saudi_Arabia"].str.replace('[\,\,]', "")
df["United_Kingdom"]= df["United_Kingdom"].str.replace('[\,\,]', "")
df["Australia"]= df["Australia"].str.replace('[\,\,]', "")
df["Italy"]= df["Italy"].str.replace('[\,\,]', "")
df["France"]= df["France"].str.replace('[\,\,]', "")
df["Spain"]= df["Spain"].str.replace('[\,\,]', "")
df["Poland"]= df["Poland"].str.replace('[\,\,]', "")
df["UAE"]= df["UAE"].str.replace('[\,\,]', "")
df["Turkey"]= df["Turkey"].str.replace('[\,\,]', "")

print(df.head)


df["Nepal"]= df["Nepal"].astype(float)
df["Brazil"]= df["Brazil"].astype(float)
df["China"]= df["China"].astype(float)
df["Iran"]= df["Iran"].astype(float)
df["Kazakhstan"]= df["Kazakhstan"].astype(float)
df["Malaysia"]= df["Malaysia"].astype(float)
df["Mexico"]= df["Mexico"].astype(float)
df["Russia"]= df["Russia"].astype(float)
df["SouthAfrica"]= df["SouthAfrica"].astype(float)
df["Thailand"]= df["Thailand"].astype(float)
df["Turkey"]= df["Turkey"].astype(float)
df["USA"]= df["USA"].astype(float)
df["India"]= df["India"].astype(float)
df["Japan"]= df["Japan"].astype(float)
df["Germany"]= df["Germany"].astype(float)
df["Indonesia"]= df["Indonesia"].astype(float)
df["South_Korea"]= df["South_Korea"].astype(float)
df["Canada"]= df["Canada"].astype(float)
df["Saudi_Arabia"]= df["Saudi_Arabia"].astype(float)
df["United_Kingdom"]= df["United_Kingdom"].astype(float)
df["Australia"]= df["Australia"].astype(float)
df["Italy"]= df["Italy"].astype(float)
df["France"]= df["France"].astype(float)
df["Spain"]= df["Spain"].astype(float)
df["Poland"]= df["Poland"].astype(float)
df["UAE"]= df["UAE"].astype(float)




print(df.head)





bcr.bar_chart_race(
    df=df,
    filename= "video.mp4",
    img_label_folder= "bar_image_labels",
    fig_kwargs={
        'figsize': (24, 14),
        'dpi':120,
        'facecolor': '#F8FAFF'

    },
     n_bars=10,
     steps_per_period= 45,
     period_length=1500,
     colors=[
        '#6ECBCE', '#FF2243', '#FFC33D', '#CE9673', '#FFA0FF', '#6501E5', '#F79522', '#699AF8', '#34718E', '#00DBCD',
        '#00A3FF', '#F8A737', '#56BD5B', '#D40CE5', '#6936F9', '#FF317B', '#0000F3', '#FFA0A0', '#31FF83', '#0556F3',
        '#CD5C5C', '#CCCCFF', '#6495ED', '#9FE2BF', '#40E0D0', '#808000', '#008080', '#800080'


    ],

     title={
        'label': "Top 10 CO2 emitting countries (in Kilotons)",
        'size': 48,
        'weight': 'bold',
        'pad': 40
     },
     period_label={
        'x': 0.95, 'y': 0.15,
        'ha': 'right', 'va': 'center',
        'size': 85, 'weight':'semibold',

     },
     bar_label_font={'size':27},
     tick_label_font={'size':27},
     bar_kwargs={
        'alpha':0.99,
        'lw':0
     },
     period_template='{x:.0f}'
   
)



