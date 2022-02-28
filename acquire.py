from importlib import import_module
import pandas as pd
from pydataset import data
from env import get_db_url
import os

# 1. Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. 
#    Obtain your data from the Codeup Data Science Database.

def get_titanic_data():    
    filename = 'titanic.csv'
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
      
    query = '''
    SELECT *
    FROM passengers    
    '''
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('titanic_db'))
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. 
#    The returned data frame should include the actual name of the species in addition to the species_ids. 
#    Obtain your data from the Codeup Data Science Database

def get_iris_data():
    filename = 'iris.csv'
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
      
    query = '''
    SELECT * 
    FROM measurements
    JOIN species USING (species_id)   
    '''
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('iris_db'))
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

# 3. Make a function named get_telco_data that returns the data from the telco_churn database in SQL. 
#    In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains all the contract, payment, and internet service options. 
#    Obtain your data from the Codeup Data Science Database.

def get_telco_data(use_cache=True):
    filename = 'telco.csv'
    if os.path.exists(filename) and use_cache:
        print('Reading from csv file...')
        return pd.read_csv(filename)
      
    query = '''
    SELECT * 
    FROM customers
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN contract_types USING (contract_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('telco_churn'))
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

