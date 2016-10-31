# Instructions for labeling and data wrangling
#from csv to pandas to xlsx

#clientrhy4spss
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from numpy.random import randn
from pandas import Series, DataFrame
from pandas_datareader import data, wb

#Read file into pandas
clientrhy4 = pd.read_csv('clientrhy4spss.csv')

#Change the values in SSN Data Quality to descriptive labels, including 99 as NaN
clientrhy4['ssndataquality'].replace(99, np.nan, inplace=True)
clientrhy4['ssndataquality'].replace(1, 'full', inplace=True)
clientrhy4['ssndataquality'].replace(2, 'partial', inplace=True)
clientrhy4['ssndataquality'].replace(8, 'client doesn\'t know', inplace=True)
clientrhy4['ssndataquality'].replace(9, 'client refused', inplace=True)

#Change the values in DoB Data Quality to descriptive labels, including 99 as NaN
clientrhy4['dobdataquality'].replace(99, np.nan, inplace=True)
clientrhy4['dobdataquality'].replace(1, 'full', inplace=True)
clientrhy4['dobdataquality'].replace(2, 'partial', inplace=True)
clientrhy4['dobdataquality'].replace(8, 'client doesn\'t know', inplace=True)
clientrhy4['dobdataquality'].replace(9, 'refused', inplace=True)

#Convert first entry date into dateformat
clientrhy4['firstentrydate'] = pd.to_datetime(clientrhy4['firstentrydate'])

#Capitalize state
clientrhy4['state'] = clientrhy4['state'].str.upper()

#Change the five project types into the names of the project types
clientrhy4['isbcpp'].replace(1, 'BCP-HP', inplace=True)
clientrhy4['isbcpes'].replace(1, 'BCP-ES', inplace=True)
clientrhy4['istlp'].replace(1, 'TLP', inplace=True)
clientrhy4['ismgh'].replace(1, 'MGH', inplace=True)
clientrhy4['issop'].replace(1, 'SOP', inplace=True)

#Concatenate the five project type columns into one program column. There is an easier 
#way to do it in pandas using the concat function, but for some reason, this function cut
#a number of records out, where there were two project types.
clientrhy4['program'] = Series(np.where(pd.isnull(clientrhy4['isbcpes']),clientrhy4['isbcpp'],clientrhy4['isbces']))
clientrhy4['program'] = Series(np.where(pd.isnull(clientrhy4['program']),clientrhy4['istlp'],clientrhy4['program']))
clientrhy4['program'] = Series(np.where(pd.isnull(clientrhy4['program']),clientrhy4['ismgh'],clientrhy4['program']))
clientrhy4['program'] = Series(np.where(pd.isnull(clientrhy4['program']),clientrhy4['issop'],clientrhy4['program']))

#Need to ask Keith about whenupdateddate

#Change age fields with 999 into Nan
clientrhy4['cleandashage'].replace(999, np.nan, inplace=True)

#Need to ask Keith on race codes

#Change the ethnicity codes into descriptive labels
clientrhy4['cleandashethnicity'].replace(np.nan, 'Non-Hispanic/Non-Latino', inplace=True)
clientrhy4['cleandashethnicity'].replace(8, 'Client doesn\'t know', inplace=True)
clientrhy4['cleandashethnicity'].replace(9, 'Refused', inplace=True)
clientrhy4['cleandashethnicity'].replace(999, np.nan, inplace=True)

#Change the gender codes intodescriptive labels
clientrhy4['cleandashgender'].replace(np.nan, 'Female', inplace=True)
clientrhy4['cleandashgender'].replace(1, 'Male', inplace=True)
clientrhy4['cleandashgender'].replace(2, 'Transgender male to female', inplace=True)
clientrhy4['cleandashgender'].replace(3, 'Transgender female to male', inplace=True)
clientrhy4['cleandashgender'].replace(4, 'Other', inplace=True)
clientrhy4['cleandashgender'].replace(8, 'Client doesn\'t know', inplace=True)
clientrhy4['cleandashgender'].replace(9, 'Refused', inplace=True)
clientrhy4['cleandashgender'].replace(999, np.nan, inplace=True)


#Why 42 states?
#Why 221 where it's both BCP-p and BCP-es?

#the end
#Recommend moving to xlsx rather than csv, as this preserves the dateformats
clientrhy4.to_excel('client4rhy.xlsx', sheet_name='client4rhy', na_rep="N/A")
