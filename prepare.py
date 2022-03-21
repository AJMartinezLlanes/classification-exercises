import pandas as pd
from sklearn.model_selection import train_test_split
def prep_iris(iris_df):
    iris_df.drop(columns=['species_id'], inplace=True)
    iris_df.rename(columns={'species_name':'species'}, inplace=True)
    dummy_iris = pd.get_dummies(iris_df[['species']], dummy_na=False, drop_first=[True])
    iris_df = pd.concat([iris_df, dummy_iris], axis=1)
    return iris_df


def prep_titanic(titanic_df):
    titanic_df.drop(columns=['deck', 'age', 'embarked', 'class', 'passenger_id'], inplace=True)
    titanic_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    dummy_titanic = pd.get_dummies(titanic_df[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    titanic_df = pd.concat([titanic_df, dummy_titanic], axis=1)
    titanic_df.drop(columns=['sex', 'embark_town'], inplace=True)
    return titanic_df

def split_titanic_data(df):
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.survived)
    return train, validate, test

def prep_telco(telco_df):
    telco_df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'], inplace=True)
    telco_df.total_charges = telco_df.total_charges.str.strip()
    telco_df = telco_df[telco_df.total_charges != '']
    telco_df['total_charges'] = telco_df.total_charges.astype(float)
    telco_df['gender_encoded'] = telco_df.gender.map({'Female': 1, 'Male': 0})
    telco_df['partner_encoded'] = telco_df.partner.map({'Yes': 1, 'No': 0})
    telco_df['dependents_encoded'] = telco_df.dependents.map({'Yes': 1, 'No': 0})
    telco_df['phone_service_encoded'] = telco_df.phone_service.map({'Yes': 1, 'No': 0})
    telco_df['paperless_billing_encoded'] = telco_df.paperless_billing.map({'Yes': 1, 'No': 0})
    telco_df['churn_encoded'] = telco_df.churn.map({'Yes': 1, 'No': 0})
    dummy_df = pd.get_dummies(telco_df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=True)
    telco_df = pd.concat([telco_df, dummy_df], axis=1)
    return telco_df

