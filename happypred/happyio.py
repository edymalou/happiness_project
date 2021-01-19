import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Create function

def  whdata_to_csv(whdata_excel_file_path):
    """ Read the World Happiness data at the provided path and extract training
        data (years 2006 to 2018) and testing data (year 2019 only). 
        
        For each training and testing dataset the label y is the "Life Ladder", and
        the features X include "Log GDP per capita", "Social support", 
        "Healthy life expectancy at birth", "Freedom to make life choices", "Generosity"
        and "Perceptions of corruption".
        
        The data are saved as the following CSV files which are also returned by the
        function in the following order:
        X_train.csv, y_train.csv, X_test.csv, y_test.csv
    
        Parameters
        ----------
        whdata_excel_file_path
            The path to the World Happiness data in Excel format

        Returns
        -------
        X_train_path
            Path to the training data feature matrix
        y_train_path
            Path to the training data label vector
        X_test_path
            Path to the testing data feature matrix
        y_test_path
            Path to the testing data label vector
    """
    #Extracting the file
    data_dir = os.path.dirname(whdata_excel_file_path)
    wh_all_df = pd.read_excel(whdata_excel_file_path)
    #Cleaning the dataset
    cols_of_interest = wh_all_df.columns[1:9]
    wh_withna_df = wh_all_df[cols_of_interest]
    wh_df = wh_withna_df.dropna()
    #set X_train, y_train: create masks
    wh_df_wo_ladder = wh_df[['year', 'Log GDP per capita', 'Social support',
       'Healthy life expectancy at birth', 'Freedom to make life choices',
       'Generosity', 'Perceptions of corruption']]
    wh_df_ladder = wh_df[['Life Ladder']]
    mask_year = (wh_df['year'] < 2018) & (wh_df['year'] >= 2006)
    mask_year_test = wh_df['year'] == 2019
    
    X_train_df = wh_df_wo_ladder[mask_year]
    y_train_df = wh_df_ladder[mask_year]
    X_test_df = wh_df_wo_ladder[mask_year_test]
    y_test_df = wh_df_ladder[mask_year_test]  
    #files directories
    X_train_path = os.path.join(data_dir, 'X_train_df.csv')
    y_train_path = os.path.join(data_dir, 'y_train_df.csv')
    X_test_path = os.path.join(data_dir, 'X_test_df.csv')
    y_test_path = os.path.join(data_dir, 'y_test_df.csv')
    #save the new data frames
    X_train_df.to_csv(X_train_path, index=False)
    y_train_df.to_csv(y_train_path, index=False)
    X_test_df.to_csv(X_test_path, index=False)
    y_test_df.to_csv(y_test_path, index=False)

    return(X_train_path, y_train_path, X_test_path, y_test_path)





