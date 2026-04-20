import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    page_icon="",
    layout="wide"
)

st.title("Dashboard 📊📈")
# st.caption("---")
col1,col2 = st.columns([1,1],gap="small")
#--------------------------File Uploader----------------------------------------------#
with col1:
    df = None
    x_flag = False
    y_flag = False
    agg = False
    file = st.file_uploader("Upload your file",["csv","xlsx"])
    if file:
        read = pd.read_csv(file)
        df = pd.DataFrame(read)
    
    col3,col4,col5 = st.columns([1,1,1])
#--------------------------File Uploader----------------------------------------------#
    with col3:
        if df is not None:
            graph_selection = st.selectbox("Select the graph: ",["Select","Bar","Histogram","Line","Scatter","Pie","Heatmap"])
            if graph_selection == "Histogram":
                y_flag = True
            if graph_selection == "Heatmap":
                x_flag = True
                y_flag = True
            if graph_selection == "Pie":
                agg = st.selectbox("Select the Aggregation:",["Count","Sum"])
        else:
            graph_selection = st.selectbox("Select the graph",["None"])
#--------------------------X Axis Selection----------------------------------------------#
    with col4:
        if df is not None:
            column_x = st.selectbox("Select X axis",df.columns,disabled=x_flag)
        else:
            column_x = st.selectbox("Select X axis",["None"])
#--------------------------Y Axis Selection----------------------------------------------#
    with col5:
        if df is not None:
            column_y = st.selectbox("Select Y axis",df.columns,disabled=y_flag)
        else:
            column_y = st.selectbox("Select Y axis",["None"])
#--------------------------Head n Describe tabs----------------------------------------------#
    if file:
        tab1,tab2 = st.tabs(["Head","Describe"])
        with tab1:
                st.write(df.head())
        with tab2:
                st.write(df.describe())
#--------------------------Graph Section----------------------------------------------# 
with col2:
    if file: 
        st.caption("")
        with st.expander(graph_selection,expanded=True):
            ax = px.bar()

            if graph_selection == "Bar":
                sums = df.groupby(column_x)[column_y].sum().reset_index()
                ax = px.bar(sums,x=column_x,y=column_y,color=column_x,text_auto=True)

            if graph_selection == "Histogram":
                ax = px.histogram(df,column_x,text_auto=True)

            if graph_selection == "Line":
                df = df.sort_values(by=column_x)
                ax = px.line(df,column_x,column_y)

            if graph_selection == "Scatter":
                ax = px.scatter(df,column_x,column_y)

            if graph_selection == "Pie":
                if agg == "Count":
                    counts = df.groupby(column_x)[column_y].count().reset_index()
                    ax = px.pie(counts,names=column_x,values=column_y)
                if agg == "Sum":
                    sums = df.groupby(column_x)[column_y].sum().reset_index()
                    ax = px.pie(sums,names=column_x,values=column_y)

            if graph_selection == "Heatmap":
                ax = px.imshow(df.corr(numeric_only=True),text_auto=".2f",color_continuous_scale="RdBu_r")

            st.plotly_chart(ax)