import streamlit as st
import pandas as pd
import plotly.express as px
import imp
from PIL import Image


st.set_page_config(page_title='Alberto Prototype')
st.header('App for Forecasting')
st.subheader('Lets try it!!!!')


#excel_file='app1.xlsx'
#sheet_name='Sheet1'


sheet_id='16m0FZF0PHeIhogDO8731Q42j5Gc5Y-Wh'
sheet_name='Sheet1'

URL= 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
   sheet_id, sheet_name)


#@st.cache
#def load_data(nrows):
 #       data=pd.read_csv(URL)
  #      return data

data=pd.read_csv(URL)
#data_load_state = st.text('Loading Alberto pls wait')
#data =load_data(10000)
#data_load_state.text('Done Bro!')

st.dataframe(data)

#df_1= pd.read_excel(excel_file, sheet_name = sheet_name, usecols='A:B', header=0)
#df_1.dropna(inplace=False)

data.dropna(inplace=False)
#st.dataframe(df_1)

#df_1.shape

#df_1.insert(2,'C1', ['x','y','z'],True)
st.text('*Note:We can add calculated columns to existing dataframe') 

data['Score'] = data['Rating'] * 20
st.dataframe(data)

bar_chart= px.bar(data, title = 'BAR CHART TITLE', x='Age',y='Score')

st.plotly_chart(bar_chart)

pie_chart= px.pie(data, title = 'PIE CHART TITLE', values = 'Rating', names = 'Age')

st.plotly_chart(pie_chart)

#image = Image.open('images/down.jpg')
#st.image(image,caption='1st image', use_column_width=True) #or width=300

# Filter/Group DataFrame

st.text('*Note: Filtering and selecting the data only what we seek for')

ages=data['Age'].unique().tolist()
ratings=data['Rating'].unique().tolist()

ratingselection=st.slider('Title1:',min_value=min(ratings),max_value=max(ratings),value=(min(ratings),max(ratings)))

ageselection=st.multiselect('Title2:',ages, default=ages)

#filter based on selection
mask=(data['Rating'].between(*ratingselection)) & (data['Age'].isin(ageselection))
noofresult= data[mask].shape[0]
st.markdown(f'*Available results: {noofresult}*') 
