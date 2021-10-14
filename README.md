## Team_4max
# COVID Diagnosis and Analysis
COVID-19 had has an enomormous impact on lifestyle of poople in the last 2 years. Nonprofits, universities and other academic institutions around the world are turning to artificial intelligence (AI) and data analytics to help us better understand COVID-19 and its impact on communities—especially vulnerable populations and healthcare workers.

We made a Web Application with the help of the Streamlit API, in the Web Application we will be conducting both a diagnosis using a machine learning modelon the first page of the web application and then on the 2nd page we will show Exploratory Data Analysis(EDA) on the covid cases data to see the variations of confirmed cases, cured cases, deaths over time as well as density of cases in various states in India and represented them graphically on scatter plots, line graph and bar graph for convenience.

We have also implemented a trained classification model to predict if a person has covid or not from a set of his/her symptoms.The interface in created in streamlit.

## Databases
### corona_tested_individuals_preprocessed.csv
This dataset was utilized for the diagnosis prediction. The dataset contains a sample of symptoms collected from over 200,000 people. The symptoms include cough, fever, sore throat, shortness of breath and head ache. It also considers the age of the person and their previous experiences with COVID. We trained our classification ML model using this dataset.

### covid_19_india_preprocessed.csv
This dataset was used for the analysis and visualization of COVID cases in India. The dataset contains data on the number of people who contracted, recovered and died due to COVID from each state and union territory along with the dates the numbers were sampled.

## Screenshots:
# Line Chart:
![image](https://user-images.githubusercontent.com/57794377/137308112-3aabf435-4f0a-4a98-8d0e-0894b9c8a936.png)
# Bar Chart:
![image](https://user-images.githubusercontent.com/57794377/137307610-a8bb167c-1f3e-4d04-9e6f-fc704e4efa45.png)
# Plotly:
![image](https://user-images.githubusercontent.com/57794377/137308080-2853e9e6-1954-4999-909f-0f23d8348dd7.png)
## Demo:
https://user-images.githubusercontent.com/71788604/137308823-e07a5e53-1d52-49f8-b19d-f9d0c44cfe48.mp4

# How to run:
Step 1. Clone the repository

Step 2. Go to the root folder in the repository and type ```streamlit run app.py```

Step 3. Enoy the app!
