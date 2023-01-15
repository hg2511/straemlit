import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

st.sidebar.title("India ka vizualization")

# state wise list

list_of_states = sorted(list(df['State'].unique()))
list_of_states.insert(0,'Overall India')

# list of states
selected_state = st.sidebar.selectbox("Select a State", list_of_states)

# list of categories
category_list = sorted(df.columns[5:])
category_list.insert(0,'Select a category')
primary_parameter = st.sidebar.selectbox('Select primary parameter', category_list)
secondary_parameter = st.sidebar.selectbox('Select secondary parameter', category_list)

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represents Primary parameters")
    st.text("Color represents Secondary parameters")
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                zoom=5, size=primary_parameter, color=secondary_parameter,size_max=50,
                                mapbox_style='carto-positron',color_continuous_scale=px.colors.cyclical.IceFire,
                                hover_data=['State','District','Population'],
                                width=1200,height=800)
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",
                                zoom=6, size=primary_parameter, color=secondary_parameter,size_max=50,
                                mapbox_style='carto-positron',color_continuous_scale=px.colors.cyclical.IceFire,
                                hover_data=['State', 'District', 'Population'],
                                width=1200,height=800)
        st.plotly_chart(fig, use_container_width=True)
