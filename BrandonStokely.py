# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write("""
   # Brandon Stokely Chart           
 """)

stokely_data = pd.read_html('https://www.pro-football-reference.com/players/S/StokBr00.htm', header=1)[0]

careerDelete = r"\s*Career\s*"
yrsDelete = r"\d\s*yrs*"
filter = stokely_data['Year'].str.contains(careerDelete) | stokely_data['Year'].str.contains(yrsDelete)

stokely_data = stokely_data[~filter]
stokely_data.columns = stokely_data.columns.str.replace(' ', '')
stokely_data['YrWithTeam'] = stokely_data.groupby('Tm').cumcount()+1;

ax = sns.barplot(data=stokely_data, x='YrWithTeam', y='Yds', hue='Tm')
ax.set(xlabel='Year With Team', ylabel='Yards')
plt.legend(loc='upper right', title='Team')
plt.title('Brandon Stokely Yards by Year with Team')
sns.set(rc={'figure.figsize':(11,7.5)})
st.pyplot(plt)
