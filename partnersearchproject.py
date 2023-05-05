# -*- coding: utf-8 -*-
"""PartnerSearchProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mGD1iUgxdgwDQIMDUYT1464YlWvIFJXg
"""

import pandas as pd
dfprojects = pd.read_excel('projects.xlsx')
dfparticipants = pd.read_excel('participants.xlsx')
dfcountries = pd.read_excel('countries.xlsx')
dfresult = dfprojects.groupby('year').agg('sum')
#dfresult = dfresult['ecMaxContribution'].values
dfresult

import pandas as pd
dfprojects = pd.read_excel('projects.xlsx')
dfparticipants = pd.read_excel('participants.xlsx')
dfcountries = pd.read_excel('countries.xlsx')
dfresult = dfprojects.groupby('year').agg('sum')
dfresult['ecMaxContribution'].plot.bar()

import pandas as pd
dfprojects = pd.read_excel('projects.xlsx')
dfparticipants = pd.read_excel('participants.xlsx')
dfcountries = pd.read_excel('countries.xlsx')
dfresult = dfprojects.groupby('year').agg('sum')
dfresult = dfresult['ecMaxContribution']
dfresult.describe()

def country_check(country):
    # COUNTRY DETECTION
    # dfcountries.loc[boolean_mask, 'Acronym'] returns a new dataframe that contains the rows where the boolean mask is True,
    # and the 'Acronym' column.
    # dfcountries['Country'] == country returns a boolean mask that is True for the rows where the 'Country' column equals the country parameter.
    # iloc[0] returns the first (and only) value in the resulting series.
    country_code = dfcountries.loc[dfcountries['Country'] == country, 'Acronym'].iloc[0]
    print("The country is: ", country, "and the corresponding code is: ", country_code)
    
    # FILTER THE DF TO JUST OUR COUNTRY
    country_selection_df = dfparticipants[dfparticipants['country'] == country_code]

    # SPECIFY THE COLUMNS WE WANT IN OUR OUTPUT DF AND THE CALCULATIONS FOR EACH COLUMN
    aggregations = {"name": "first", "projectID": "count", "ecContribution": "sum"}

    # GROUP THE OUTPUT DF BY NAME + COLUMNS ABOVE
    country_selection_df = country_selection_df.groupby("name").agg(aggregations)
    
    # EXPORT THE NEW DF TO AN EXCEL
    country_selection_df.to_excel('result.xlsx', index=False)

import pandas as pd

# Assume that 'df' is the DataFrame containing the generated dataset
df.to_excel('received_grants_per_partner.xlsx', index=False)
print('Dataset saved to received_grants_per_partner.xlsx