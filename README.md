# metis_project_3

**Overall Survival of Clinical Trials:**
*Classification models to predict early trial termination*

Clinical trials can end early for a variety of reasons such as low accrual, interim analysis suggesting the intervention has low efficacy, adverse events and loss of funding or interest. I wanted to see if I could create a classification model to predict whether or not a trial would be terminated early or completed.

Clinical trails in the United States are required to be reported clinicaltrials.gov, however many still go unreported or are missing information. I used the clinicaltrials.gov API to collect data on study design, outcome measures, eligibility, investigators/sponsor and study locations for over 18,000 cancer interventional trials designated as 'Terminated' or 'Completed' from clinicaltrials.gov. This data was stored in a PostgresSQL database.

I one hot encoded the categorial data fields and engineered several new features using regex and text extraction from the free text fields, resulting in 400 total features. 

[**Features Notebook**](https://github.com/Beth526/metis_project_3/blob/main/Project3_features.ipynb)

Model optimization was performed using:

-scikit-learn

-imblearn

-xgboost

Models tested:

-kNN

-Logistic Regression

-SVC

-Naive Bayes

-Random Forest

-XGBoost

-Ensembled models

I used standardscaler to normalize the data and kNN imputation to impute values for some features with missing values. Only about 1/3 of the trials in the dataset were 'Terminated' causing a class imbalance, so I used either ADASYN oversampling or balanced model class weights when available. Models were optimized with gridsearch and most models reached similar F1 scores and AUCs for calling the "Terminated" class of ~0.4 and ~0.65, respectively. I acheived mild class seperation and a recall of 60-70% for "Terminated" trials but recall could not be improved further without the optimal models calling all cases "Terminated". Ensembling only improved the scores of kNN and Logistic Regression.

[**Model Optimization Notebook**](https://github.com/Beth526/metis_project_3/blob/main/Project3_model_optimization.ipynb)

[**Model Ensembling Notebook**](https://github.com/Beth526/metis_project_3/blob/main/Project3_model_ensembles.ipynb)

[**Model Evaluation Notebook**](https://github.com/Beth526/metis_project_3/blob/main/Project%203_model_test.ipynb)

I made a Streamlit app to allow users to interact directly with the logistic regression model and see how almost all the features affect the predictions for trial termination.

[**App screenshot**](https://github.com/Beth526/metis_project_3/blob/main/streamlit%20app%20screen%20shot.png)

[**Streamlit App**](https://github.com/Beth526/metis_project_3/blob/main/clin_trials_streamlit.py)

[**Presentation**](https://github.com/Beth526/metis_project_3/blob/main/Project%203%20presentation.pdf)

