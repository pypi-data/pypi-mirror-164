# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest with RandomizedSearchCV
 - Random Forest with GridSearchCV

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated.
 - Mean squared error, Root mean squaerd error, Mean absolute error metrics are used to evaluate the model
## To excute the script's
>There are three scripts need to run for evaluating the model

    $ python ingest_data.py -p raw

you can run this script with specifying where you want to place the downloaded data and also with default arguments

    $ python train.py -x housing_prepared.csv -y housing_labes.csv

you can run this script with specifying dependent and independent variables and also with no argument passed

    $ python score.py -m final_model.pkl -d test_set.csv

you can run this script with specifying which ML model want to use and with what dataset to score metrics

