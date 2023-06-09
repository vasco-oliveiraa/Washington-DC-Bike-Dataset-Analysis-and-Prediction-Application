import streamlit as st

def ExecutiveSummary(display=True):
    if display == True:
        
        st.title('Executive Summary')

        st.subheader("Introduction")

        # Add text
        st.write("This project aims to provide an ***in-depth analysis of the bike-sharing service present in Washington D.C from 2011 to 2012***. Our ***objective*** is to build an interactive and insightful report that will ***help the transportation department optimize their bike provisioning and costs*** incurred from outsourcing transportation companies. To achieve this, we will be ***building a predictive model that can predict the total number of bicycle users on an hourly basis***.")

        # Add subheader
        st.subheader("Data Overview")

        # Add text
        st.write("We will be using the ***Capital Bikeshare system data*** provided by the city of ***Washington D.C.*** This dataset includes various attributes such as `date`, `time`, `weather conditions`, `holiday`, `number of bikes rented`, among others. The data is split into two years, ***2011*** and ***2012***.")

        # Add subheader
        st.subheader("Analysis and Insights")

        # Add text
        st.write("To provide a ***deep analysis*** of the bike-sharing service in the city, we have ***explored*** the following:")
        st.write("1. The ***overall usage of the bike-sharing service*** in the city, including peak usage times and patterns.")
        st.write("2. The effect of ***weather conditions*** and ***holidays*** on bike rentals.")
        st.write("3. The ***popularity of bike stations*** in the city and the ***availability of bikes***.")
        st.write("4. The ***relationship*** between bike usage and ***other variables*** such as ***season, weekday***, and ***time of day***.")

        # Add subheader
        st.subheader("Predictive Model")

        # Add text
        st.write("To build the predictive model, we have ***checked various machine learning algorithms*** such as ***Linear Regression, Random Forest Regression, Extra Trees, CatBoost Regressor***, among others. We have used the ***Root Mean Squared Error (RMSE)*** and ***R-squared (R2)*** score to evaluate the model's performance. Based on our analysis, we have found that the ***Cat Boost Regression model*** has the best performance with an ***RMSE of 64*** and an ***R2 score of 0.91*** on the test data. Catboost is a gradient boosting algorithm that uses a combination of techniques to build an ensemble of decision trees ")


        # Add subheader
        st.subheader("Conclusion")

        # Add text
        st.write("Our analysis has ***provided insights into the usage of the bike-sharing service*** in Washington D.C. and how it can be optimized to reduce costs and improve service. The ***predictive model*** we have built can help the transportation department ***anticipate bike provisioning better and optimize the costs*** incurred from the outsourcing transportation company. Our ***report will assist*** the transportation department in ***making data-driven decisions to improve the bike-sharing service in the city***.")
