import pandas as pd
import plotly.express as px

fields = ['date',' Annual % Change']

# x=[]
# y=[]

df = pd.read_csv('united-states-population-2022-03-03.csv', usecols=fields)

fig = px.line(df, x='date', y=' Annual % Change', title='percentage change over the years')
#df = df.head()

# with open('united-states-population-2022-03-03.csv') as csvfile: 
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines: 
#         x.append(row[0])
#         y.append(int(row[1]))
# plt.plot(x, y, color='g', linestyle = 'dashed', marker = 'o', label = "US population")
# plt.xticks(rotation = 25)
# plt.xlabel('Dates')
# plt.ylabel('Births')
# plt.title('Births', fontsize = 20)
# plt.grid()
# plt.legend()
# plt.show()
# df.keys()

#print (df.date)

fig.show()