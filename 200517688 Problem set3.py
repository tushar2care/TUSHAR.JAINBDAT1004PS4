#!/usr/bin/env python
# coding: utf-8

# In[2]:


# QUESTION 1
import pandas as pd
url1 = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url1, sep = '|')
print(users.to_string()) 


# In[4]:


# step IV
users.groupby('occupation')['age'].mean()


# In[16]:


# step VI
calc=users.groupby('occupation')['age']
calc.agg(['max','min'])


# In[6]:


#step VII
users.groupby(['gender','occupation'])['age'].mean()


# # Question 2
# 

# In[25]:


import pandas as pd
url2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url2)
euro12['Goals'] #select the goal column only



# In[27]:


#step V
euro12['Team'].count()


# In[30]:


# step VI
column = len(euro12.columns)
column


# In[34]:


#step VII
discipline = euro12[['Team','Yellow Cards','Red Cards']]
discipline


# In[36]:


#step VIII
discipline.sort_values(by=['Red Cards','Yellow Cards'])


# In[42]:


#step IX
meanteamyellow=euro12.groupby(['Team'])['Yellow Cards'].mean()
meanteamyellow


# In[48]:


#stepX
euro12[euro12['Goals']>6]


# In[52]:


#stepXI
euro12[euro12['Team'].str.contains('G')]


# In[53]:


#stepXII
euro12[euro12.columns[:7]]


# In[57]:


#stepXIII
euro12[euro12.columns[:-3]]


# In[64]:


#step XIV
teamsacuuracy=euro12[euro12.Team.isin(['England','Italy','Russia'])]
teamsacuuracy[['Shooting Accuracy','Team']]


# # Question 3
# 

# In[74]:


import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randint(low=1, high=5, size=100, dtype='l'))
s1


# In[70]:


s2 = pd.Series(np.random.randint(low=1, high=4, size=100, dtype='l'))
s2


# In[77]:


s3 = pd.Series(np.random.randint(low=10000, high=30001, size=100, dtype='l'))
s3


# In[82]:


#step III
newseries = pd.DataFrame({'Series1':s1,'Series2':s2,'Series3':s3})
newseries


# In[85]:


#step IV
rename=newseries.rename(columns={'Series1':'bedrs','Series2':'bathrs', 'Series3':'price_sqr_meter'})
rename


# In[90]:


#step V
#reference kuldeep singh

bigcolumn = pd.concat([s1,s2,s3])
bigcolumn = bigcolumn.to_frame()
bigcolumn


# In[97]:


#step VI
if (max(bigcolumn.index)==99):
 print('Yes it is True')
else:
 print('No it is False')


# In[100]:


#step VII
bigcolumn.reset_index(drop=True)


# # Question 4
# 

# In[102]:


import pandas as pd
import numpy as np
data = pd.read_csv ('wind.txt', sep = '\s+')
data.head()


# In[118]:


#step III
data.rename(columns = {'Yr':'Year', 'Mo':'Month', 'Dy':'Day'})


# In[121]:


#step V
data.dtypes


# In[122]:


#step VI
data = data.dropna()
data.isnull().sum()


# In[123]:


#step VII
data.count()


# # Question 5

# In[127]:


import pandas as pd
import numpy as np
url3 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep = '\t')
chipo = url3
chipo


# In[128]:


#step IV
chipo.head(10)


# In[134]:


#step V
print("The number of observations in a dataset are")
chipo.shape[0]


# In[135]:


#step VI
print("The number of columns in a dataset are")
chipo.shape[1]


# In[136]:


#step VII
chipo.columns


# In[137]:


#step VIII
chipo.index


# In[140]:


#step IX
chipo['item_name'].value_counts()


# # step X
# from the above observation chicken bowl is ordered 726 times

# In[141]:


# step XI
chipo['choice_description'].value_counts()


# In[142]:


# the most ordered item in the choice description column is Diet coke


# In[143]:


#step XII
print('total items ordered')
chipo['quantity'].sum()


# In[145]:


#step XIII


# # Question 6
# 

# In[154]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file2 = pd.read_csv('us-marriages-divorces-1867-2014.csv')
plt.plot(file2['Year'], file2['Marriages_per_1000'], color='pink', label='Marriages')
plt.plot(file2['Year'], file2['Divorces_per_1000'],color='brown', label='Divorces')
plt.xlabel('Total Years')
plt.ylabel('Total no. of cases')
plt.title('Marriages and Divorces per capita in U.S in year 1867 to 2014')
plt.grid(True)
plt.legend()


# # Question 7

# In[161]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
file3 = pd.read_csv('us-marriages-divorces-1867-2014.csv')
newfile = file3[(file3.Year == 1900) | (file3.Year == 1950) | (file3.Year == 2000)]
newfile = newfile.drop(columns = ['Marriages', 'Divorces', 'Population'])
newfile = newfile.set_index('Year')
newfile.plot.bar()
plt.xlabel('Years--->')
plt.ylabel('Total Numbers')
plt.title('Marriages and divorces per capita in the U.S. between 1900, 1950, and 2000')

#Reference https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/


# # Question 8
# 

# In[171]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
file4 = pd.read_csv('actor_kill_counts.csv')
file4 = file4.sort_values(by="Count")
plt.barh(file4['Actor'], file4['Count'], label='Kill', color='red')
plt.legend()
plt.title('Count of kills by Actors')
plt.xlabel('Total no. of kills')
plt.ylabel('Actors Name')

plt.show()


# # Question 9

# In[175]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
file5 = pd.read_csv('roman-emperor-reigns.csv')
deathcause = file5.groupby('Cause_of_Death').count()[['Emperor']]
deathcause


# In[197]:


Emperor = pd.Series(deathcause['Emperor'])
death = pd.Series(deathcause.index)
explode = (0.4,0,0,0,0,0,0,0)
fig, axis = plt.subplots()
axis.pie(Emperor, explode=explode, labels=death,autopct='%1.1f%%', shadow=True, startangle=260)
axis.axis('equal')
plt.title('Fraction of roman empires assasinated')
plt.show()


# # Question 10

# In[208]:


#Reference :https://pythongeeks.org/python-scatter-plot/
import pandas as pd
import seaborn as sb

fiel5 = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')
fiel5 = fiel5.rename(columns={'Total Arcade Revenue (billions)': 'Earned revenue by arcade', 'Computer Science Doctorates Awarded (US)': 'No. P.hd Awarded in U.S'})
axis = sb.scatterplot(x='Earned revenue by arcade', y='No. P.hd Awarded in U.S', hue="Year", data=fiel5)
axis.set_title('Revenue earned by Arcade V/S No. of P.hd awarded in U.S')


# In[ ]:




