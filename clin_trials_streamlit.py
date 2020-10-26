import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os
os.chdir('/Users/beth/Documents/Metis/metis_project_3/metis_project_3')

with open('column_dict.pickle', 'rb') as read_file:
    column_dict = pickle.load(read_file)

with open('logistic_regression.pickle', 'rb') as read_file:
    lr = pickle.load(read_file)

with open('scaling.pickle', 'rb') as read_file:
    scaler = pickle.load(read_file)

with open('average.pickle', 'rb') as read_file:
    df = pickle.load(read_file)

with open('PPV_threholds.pickle', 'rb') as read_file:
    thresholds = pickle.load(read_file)

with open('PPV.pickle', 'rb') as read_file:
    PPVs = pickle.load(read_file)

average=df.copy()

pred = lr.predict_proba(df.reshape(1, -1))[:,1][0]

def graph_it(h):
  fig, ax = plt.subplots(figsize=(3,5))
  ax.bar(1,height=h,color='red')
  ax.set_ylim(0,100)
  ax.set_xticks([])
  ax.set_ylabel('%')
  ax.axhline(y=45,xmin=0,xmax=1,color='black')
  ax.text(x=0.9, y=h+5, s='{:0.2f} %'.format(h))
  ax.text(x=1.48, y=44, s='Average Study: 45%')
  st.sidebar.pyplot(fig)

st.write('''# Cancer Clinical Trial Feasibility App
''')

st.write('''Clinical trails can be terminated early for a number of reasons:
  - Low accrual
  - Poor interim analysis
  - Adverse events
  - Funding pulled

Using a model developed from over 18,000 interventional cancer clinical trials posted on clinicaltrials.gov, this app predicts the risk of a trial being terminated early.
It also allows users to explore how different factors affect trial feasibility.
''')

st.write('''# Basic Study Design
''')

purpose = st.selectbox(
    'Primary study purpose', ['Other']+
     sorted(['Treatment','Prevention','Supportive Care','Diagnostic']) )
if purpose != 'Other':
	df[column_dict[purpose]] = 1
if purpose == 'Other':
  for i in ['Treatment','Prevention','Supportive Care','Diagnostic']:
    df[column_dict[i]] = average[column_dict[i]]

phase = st.selectbox(
    'Phase', ['Other']+
     sorted(['Phase 2','Phase 3','Phase 1/Phase 2','Phase 2/Phase 3']) )
if phase != 'Other':
	df[column_dict[phase]] = 1
if phase == 'Other':
  for i in ['Phase 2','Phase 3','Phase 1/Phase 2','Phase 2/Phase 3']:
    df[column_dict[i]] = average[column_dict[i]]

option = st.selectbox(
    'Assignment Strategy',['Other']+
     sorted(['Single Group','Parallel','Crossover','Sequential','Factorial']) )
if option != 'Other':
	df[column_dict[option]] = 1
if option == 'Other':
  for i in ['Single Group','Parallel','Crossover','Sequential','Factorial']:
    df[column_dict[i]] = average[column_dict[i]]

left_column, right_column = st.beta_columns(2)

random = left_column.checkbox('Randomized', value=False)
if random == False:
	df[102] = 1
if random == True:
	df[103] = 1

oversight = right_column.checkbox('Has oversight committee', value=False)
if oversight == False:
  df[33] = 1
if oversight == True:
  df[34] = 1

blinded = st.selectbox(
    'Masking Combination',['Other']+
     sorted(['Participant|Care Provider|Investigator|Outcomes Assessor ', \
     	'Participant|Investigator','Participant|Care Provider|Investigator',\
     	'Participant','Participant|Investigator|Outcomes Assessor']) )
if blinded != 'Other':
	df[column_dict[blinded]] = 1
if blinded == 'Other':
  for i in ['Participant|Care Provider|Investigator|Outcomes Assessor ', \
      'Participant|Investigator','Participant|Care Provider|Investigator',\
      'Participant','Participant|Investigator|Outcomes Assessor']:
    df[column_dict[i]] = average[column_dict[i]]


condition_tags = sorted(['stage ii', 'stage iii', 'iv', 'breast', 'lymphoma', 'non-hodgkin', 'noncontiguous', 'prostate', \
        'lung', 'myeloma', 'leukemia', 'stomach', 'liver', 'colorectal', 'cervical', 'pancreatic', \
        'renal', 'melanoma', 'non small/large cell', 'small cell', 'squamous', 'diffuse', 'childhood', 'recurrent', \
        'metastatic', 'acute', 'triple negative'])

condition = st.multiselect(
    "Choose Condition Tags", condition_tags, ['stage iii', 'triple negative', 'breast'])

for i in condition:
	df[column_dict[i]] = 1

st.write('''# Intervention and Study Arms
''')

arms = st.selectbox(
	'Study Arms Design', ['Other']+
	sorted(['Experimental|Active Comparator', 'Experimental',
       'Experimental|Placebo Comparator', 'Experimental|Experimental',
       'Active Comparator|Active Comparator',
       'Experimental|Experimental|Experimental',
       'Experimental|No Intervention', 'Active Comparator|Placebo Comparator']))
if arms != 'Other':
	df[column_dict[arms]] = 1
if arms == 'Other':
  for i in ['Experimental|Active Comparator', 'Experimental',
       'Experimental|Placebo Comparator', 'Experimental|Experimental',
       'Active Comparator|Active Comparator',
       'Experimental|Experimental|Experimental',
       'Experimental|No Intervention', 'Active Comparator|Placebo Comparator']:
    df[column_dict[i]] = average[column_dict[i]]


num_arms = st.slider('Number of Arms (10 if more than 10)', 1, 10, 1 )
df[78] = num_arms

left_column, right_column = st.beta_columns(2)

FDAreg_drug = left_column.checkbox('Studies an FDA-regulated Drug', value=False)
if FDAreg_drug == False:
	df[27] = 1
if FDAreg_drug == True:
	df[28] = 1

FDAreg_device = right_column.checkbox('Studies an FDA-regulated Device', value=False)
if FDAreg_device == False:
	df[29] = 1
if FDAreg_device == True:
	df[30] = 1

access = st.checkbox('Has expanded access', value=False)
if access == False:
	df[31] = 1
if access == True:
	df[32] = 1

intervention_tags = ['biomarker', 'stem cell', 'cell transplantation', 'chemotherapy', \
            'radiation', 'placebo', 'surgery', 'docetaxel', 'bevacizumab', 'doxorubicin', \
             'paclitaxel', 'rituximab', 'cetuximab', 'daily', 'weekly', 'monthly', 'iv/intravenous', 'oral', \
             'injection', 'biologic']

intervention = st.multiselect(
    "Choose Intervention Tags (from any arm)", intervention_tags, ['daily', 'injection', 'biomarker'])
for i in intervention:
	df[column_dict[i]] = 1


st.write('''# Outcomes Assessment
''')

outcome_tags =['progression free', 'correlative studies', 'event free','disease free', 'relapse', 'failure free','toxcitiy and tolerability',\
         'overall survival','percent change','overall response rate','RECIST','complete response', 'remission','quality of life']

outcome = st.multiselect(
    "Choose Outcome Measurment Tags", outcome_tags, ['overall response rate', 'RECIST', 'quality of life'])
for i in outcome:
	df[column_dict[i]] = 1


longest_outcome_measurement = st.slider('Longest outcome measuement (weeks)', 1, 52*10, 52)
df[46] = longest_outcome_measurement * 7

number_timepoints = st.slider('Approx number of timepoints', 0, 30, 5)
df[47] = number_timepoints

number_primary_outcomes = st.slider('Number Primary Outcomes', 1, 10, 1)
df[48] = number_primary_outcomes 

number_secondary_outcomes = st.slider('Number Secondary Outcomes', 0, 10, 1)
df[49] = number_secondary_outcomes

st.write('''# Eligibility
''')

gender = st.selectbox(
    'Gender',
     sorted(['Female','Male','All']) )
df[column_dict[gender]] = 1

eligibility_tags =['biopsy confirmed', 'ECOG', 'who performance scale', 'resectable', 'vitamin levels', \
 'blood pressure', 'life expectancy', 'MRI', 'CAT', 'PET', 'imaging' \
 'hemoglobin','glucose', 'diabetes', 'liver function', 'renal function',\
 'medication', 'conditions', 'allergy/sensitivity', 'metastasis', 'lymph nodes', 'heart health', \
 'previously untreated', 'prior radiation', 'prior chemotherapy', 'infection', 'contraception', \
 'prior surgery']

eligibility = st.multiselect(
    "Eligibility tags", eligibility_tags, ['blood pressure', 'biopsy confirmed', 'prior chemotherapy'])
for i in eligibility:
	df[column_dict[i]] = 1

number_inclusion_criteria = st.slider('Number Inclusion Criteria', 1, 10, 10)
df[114] = number_inclusion_criteria

number_exclusion_criteria = st.slider('Number Exclusion Criteria', 0, 10, 10)
df[115] = number_exclusion_criteria

min_age = st.slider('Min Age (years)', 0, 100, 0)
df[113] = min_age * 365

max_age = st.slider('Max Age (years)', 0, 100, 100)
df[112] = max_age * 365


st.write('''# Sponsor and Investigators
''')

phase = st.selectbox(
    'Responsible Party Type',
     sorted(['Sponsor','Principal Investigator','Sponsor-Investigator']) )
df[column_dict[phase]] = 1

sponsor = st.selectbox(
    'Lead Sponsor',['Other']+
     sorted(['National Cancer Institute (NCI)','M.D. Anderson Cancer Center','Memorial Sloan Kettering Cancer Center', \
  'Novartis Pharmaceuticals','Eli Lilly and Company', 'Hoffmann-La Roche','Alliance for Clinical Trials in Oncology', \
  'Pfizer','Amgen','European Organisation for Research and Treatment of Cancer - EORTC']) )
if sponsor != 'Other':
	df[column_dict[sponsor]] = 1
if sponsor == 'Other':
  for i in ['National Cancer Institute (NCI)','M.D. Anderson Cancer Center','Memorial Sloan Kettering Cancer Center', \
  'Novartis Pharmaceuticals','Eli Lilly and Company', 'Hoffmann-La Roche','Alliance for Clinical Trials in Oncology', \
  'Pfizer','Amgen','European Organisation for Research and Treatment of Cancer - EORTC']:
    df[column_dict[i]] = average[column_dict[i]]

official = st.selectbox(
	'Lead Official', ['Other']+
	sorted(['M.D. Anderson Cancer Center ',
       'Memorial Sloan Kettering Cancer Center ',
       'Mayo Clinic ', 'Hoffmann-La Roche ',
       'Novartis Pharmaceuticals ', 'Eli Lilly and Company ',
       'Dana-Farber Cancer Institute ',
       'National Cancer Institute (NCI) ', 'Amgen ',
       'Pfizer ']) )
if official != 'Other':
	df[column_dict[official]] = 1
if official == 'Other':
  for i in ['M.D. Anderson Cancer Center ',
       'Memorial Sloan Kettering Cancer Center ',
       'Mayo Clinic ', 'Hoffmann-La Roche ',
       'Novartis Pharmaceuticals ', 'Eli Lilly and Company ',
       'Dana-Farber Cancer Institute ',
       'National Cancer Institute (NCI) ', 'Amgen ',
       'Pfizer ']:
    df[column_dict[i]] = average[column_dict[i]]

num_collabs = st.slider('Number Collaborators', 0, 10, 10)
df[155] = num_collabs

st.write('''# Study Locations
''')

cities_list = ['New York','Boston','Chicago','Houston','Seattle','Los Angeles','Philadelphia','Madrid', \
'London','Columbus','Seoul','Baltimore','Barcelona','Portland','Cleveland','Rochester','Dallas','Toronto', \
'Denver','Wichita','Saint Louis','Nashville','Paris','Ann Arbor','Omaha','Montreal','Atlanta','Kansas City','Indianapolis',\
'Detroit','Springfield','Des Moines','Pittsburgh','Minneapolis','Billings','Dayton','Birmingham','Peoria','San Antonio',\
'San Francisco','Washington','Cincinnati','Greenville','Toledo','Berlin','New Orleans','Las Vegas',\
'Milano','Salt Lake City','Moscow','Durham','Honolulu','Valencia','Tampa','Charleston','Aurora',\
'Winston-Salem','Milwaukee','Green Bay','Miami','Jacksonville','Bethesda','Athens','Vancouver','Richmond',\
'Budapest','Ottawa','Albuquerque','Oklahoma City','Tucson','Roma','Louisville','Sacramento','Madison',\
'Sioux City','San Diego','Sioux Falls','Columbia','Jackson','Beijing','Memphis','Tacoma','Taipei',\
'Buffalo','Orlando','Manchester','Grand Rapids','Kalamazoo','South Bend','Newark','Bronx','Charlotte','Bismarck',\
'Lexington','Lyon','Hamburg','La Jolla','Missoula']

countries_list = ['United States', 'China', 'France', 'Germany', 'Canada', \
          'Japan', 'Italy', 'Korea', 'Spain', 'Netherlands', 'Russia' \
          ,'India', 'Switzerland', 'Belgium', 'Brazil', 'Egypt', 'Greece', 'Australia', \
          'Denmark', 'Sweden', 'Taiwan', 'Singapore', 'Austria', 'Israel', 'Norway', 'Poland', \
          'Finland', 'Hong Kong', 'Turkey', 'Mexico', 'Argentina', 'Ireland', 'Thailand']


countries = st.multiselect(
    "Countries", countries_list, ['United States', 'China'])
for i in countries:
	df[column_dict[i]] = 1

cities = st.multiselect(
    "Cities", cities_list, ['New York', 'Paris'])
for i in cities:
	df[column_dict[i]] = 1

num_countries = st.slider('Number Countries', 0, 10, 1)
df[167] = num_countries

num_locations = st.slider('Number Sites', 0, 100, 1)
df[166] = num_locations

df_for_lr = scaler.transform(df.reshape(1, -1))

pred = lr.predict_proba(df_for_lr)[:,1][0]

#def get_PPV_corrected_pred(pred,thresholds,PPVs):
#  for i, v in enumerate(thresholds):
#    if pred > v:
#      corrected_pred = PPVs[i]
#      return corrected_pred
#      break

#corrected_pred = get_PPV_corrected_pred(pred,thresholds,PPVs)

st.sidebar.write('''# Probability of early trial termination
''')

st.sidebar.write('{:.2f} percent'.format(pred*100))

graph_it(pred*100)












