import streamlit as st
import pandas as pd
import plotly.express as px
import imp
from PIL import Image


st.set_page_config(page_title='Alberto Prototype')
st.header('App for Forecasting')
st.subheader('Lets try it!!!!')


excel_file='app1.xlsx'
sheet_name='Sheet1'

df_1= pd.read_excel(excel_file, sheet_name = sheet_name, usecols='A:B', header=0)
df_1.dropna(inplace=False)

st.dataframe(df_1)

#df_1.shape

#df_1.insert(2,'C1', ['x','y','z'],True)

#st.dataframe(df_1)

df_1['Score'] = df_1['Rating'] * 20
st.dataframe(df_1)

bar_chart= px.bar(df_1, title = 'BAR CHART TITLE', x='Age',y='Score')

st.plotly_chart(bar_chart)

pie_chart= px.pie(df_1, title = 'PIE CHART TITLE', values = 'Rating', names = 'Age')

st.plotly_chart(pie_chart)

image = Image.open('images/down.jpg')
st.image(image,caption='1st image', use_column_width=True) #or width=300

# Filter/Group DataFrame

ages=df_1['Age'].unique().tolist()
ratings=df_1['Rating'].unique().tolist()

ratingselection=st.slider('Title1:',min_value=min(ratings),max_value=max(ratings),value=(min(ratings),max(ratings)))

ageselection=st.multiselect('Title2:',ages, default=ages)

#filter based on selection
mask=(df_1['Rating'].between(*ratingselection)) & (df_1['Age'].isin(ageselection))
noofresult= df_1[mask].shape[0]
st.markdown(f'*Available results: {noofresult}*') 
