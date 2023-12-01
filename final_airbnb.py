import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import psycopg2
from psycopg2 import sql
import plotly.express as px
import pymongo




st.set_page_config(page_title="Airbnb Analysis", page_icon="",layout="wide", initial_sidebar_state="expanded")
st.title(":rainbow[Airbnb Analysis]")


with st.sidebar:
    selected = option_menu(
        menu_title="",  # required
        options=["Home","---","Tabelau Dashboard","Data Visualization", "About"],  # required
        styles={"nav-link": {"--hover-color": "brown"}},
        orientation="vertical")

if selected == 'Home':
    st.subheader("Python Scripting:")
    st.write("Gain proficiency in Python programming for data analysis, manipulation, and visualization.")
    st.subheader("Data Preprocessing:")
    st.write("Learn techniques for cleaning, transforming, and preparing raw data for analysis.")
    st.subheader("Visualization:")
    st.write("Develop skills in creating meaningful visualizations using libraries like Matplotlib, Seaborn, or Plotly in Python.")
    st.subheader("Exploratory Data Analysis (EDA):")
    st.write("Master EDA techniques to understand data distributions, correlations, and patterns.")
    st.subheader("Streamlit:")
    st.write("Learn to create interactive web applications for data visualization and exploration using Streamlit.")
    st.subheader("MongoDB:")
    st.write("Understand NoSQL databases and gain hands-on experience with MongoDB for storing and retrieving data efficiently.")
    st.subheader("Tableau:")
    st.write("Learn data visualization tools like PowerBI or Tableau for creating interactive dashboards and reports.")


if selected == "Tabelau Dashboard":
    tableau_code = """
    <div class='tableauPlaceholder' id='viz1700625216933' style='position: relative'>
        <noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;AI&#47;AIRBNB_ANALYSIS&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='AIRBNB_ANALYSIS&#47;Dashboard2' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;AI&#47;AIRBNB_ANALYSIS&#47;Dashboard2&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1700625216933');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else if ( divElement.offsetWidth > 500 ) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.height='2827px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """

    # Use streamlit.components.v1 to embed the Tableau code
    st.components.v1.html(tableau_code, height=4000, scrolling=True)

client=pymongo.MongoClient("mongodb+srv://RAJESHK513:Rajeshkraji@cluster0.uf5udo7.mongodb.net/?retryWrites=true&w=majority")
db=client["sample_airbnb"]
collection=db["listingsAndReviews"]

df=pd.read_csv("/Users/rajesh/Desktop/Airbnb_analysis.csv")

if selected =="Data Visualization":
    tab1, tab2, tab3 = st.tabs(["COUNTRY VS PRICE", "BED VS CANCELLATION POLICY & HOST RESPONSE TIME", "PROPERTY TYPE VS MAX NIGHTS AND MINIMUM NIGHTS"])

    with tab1:

        st.bar_chart(df, x="country", y="price", color=["#FF4564"])
        st.map(df,
               latitude='latitude',
               longitude='longitude',
               size='price',
                color='#FF4564')
    with tab2:
        st.scatter_chart(
        df,
        x='property_type',
        y='bed_type',
        color='host_response_time',
        size='host_id',
    )
        st.line_chart(df, x="property_type", y="bed_type", color="host_response_time")
        st.bar_chart(df, x="bed_type", y="cancellation_policy", color="security_deposit")
    with tab3:
        st.scatter_chart(
        df,
        x='property_type',
        y='bed_type',
        color='maximum_nights',
        size='minimum_nights')
        st.line_chart(df, x="property_type", y="bed_type", color="maximum_nights")
        st.line_chart(df, x="property_type", y="bed_type", color="minimum_nights")


if selected == "About":
    st.markdown("""
    Certainly! If you're interested in an analysis of Airbnb, I can provide some general insights based on information available up to my last knowledge update in January 2022. Keep in mind that the situation may have evolved since then. Here are some key points:

    Business Model:
    Airbnb operates as an online marketplace that connects travelers with individuals who have extra space in their homes, such as spare rooms, entire homes, or unique accommodations. Hosts list their properties, and guests can book them for short-term stays.

    Global Presence:
    As of my last update, Airbnb had a significant global presence, with listings in numerous countries and cities. The platform gained popularity for offering a wide range of accommodation options, from budget-friendly to luxury properties.

    COVID-19 Impact:
    The travel and hospitality industry, including Airbnb, faced challenges due to the COVID-19 pandemic. Travel restrictions, lockdowns, and safety concerns led to a decline in bookings, impacting both hosts and Airbnb's revenue. The company had to adapt its strategies to navigate the pandemic's uncertainties.

    Regulatory Challenges:
    Airbnb has faced regulatory challenges in various cities and countries. Local authorities have raised concerns about the impact of short-term rentals on housing markets, neighborhood dynamics, and compliance with local regulations.

    Diversification:
    In addition to traditional accommodations, Airbnb expanded its offerings to include experiences and activities hosted by locals. This move aimed to provide travelers with a more immersive and authentic experience beyond lodging.

    Financials and IPO:
    Airbnb went public through an initial public offering (IPO) in December 2020. The IPO was well-received, reflecting investor confidence in the company's long-term prospects. The financial performance of Airbnb was closely watched in the stock market.

    Technology and Innovation:
    Airbnb relies heavily on technology for its platform, including user-friendly interfaces, secure payment systems, and algorithms for matching guests with suitable listings. Continuous innovation in technology and user experience is crucial for staying competitive.

    Sustainability Initiatives:
    There has been an increasing focus on sustainability in the travel industry. Airbnb has explored initiatives to encourage eco-friendly practices among hosts and guests. This includes promoting energy-efficient accommodations and responsible tourism.

    For the most up-to-date and detailed information, please refer to Airbnb's latest financial reports, news releases, and other official sources. Keep in mind that the business landscape can change rapidly, and staying informed about recent developments is crucial for a comprehensive analysis.""")