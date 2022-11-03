#%%
import numpy as np
import pandas as pd
from scipy.stats import random_correlation, ttest_ind
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupShuffleSplit, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, confusion_matrix
from sklearn import datasets
#%%
############################
# Dummy clasification data
############################

def load_iris():
    # load iris dataset
    iris = datasets.load_iris()
    # Since this is a bunch, create a dataframe
    iris_df=pd.DataFrame(iris.data)
    iris_df['class']=iris.target

    iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    iris_df.dropna(how="all", inplace=True) # remove any empty lines

    #selecting only first 4 columns as they are the independent(X) variable
    # any kind of feature selection or correlation analysis should be first done on these
    iris_X=iris_df.iloc[:,[0,1,2,3]]
    iris_y = iris_df['class']
    return iris_X, iris_y

############################
# EDA
############################

#%%
def target_correlation(dataset, target_column):
    """
    Calculate Pearson correlation coefficient of 
    numeric features with target

    Args:
        dataframe with feature and target columns
        name of target variable. Fills missing with 0
        and drops rows with missing target variable
    
    Returns:
        data frame with feature name and Pearson coeeficient
    """
    data = dataset.copy()

    # select numeric columns
    data = data.select_dtypes(include=['float64', 'int64', 'int32']).fillna(0)

    # make correlation df
    corr = pd.DataFrame(np.corrcoef(data.T))
    corr.columns = data.columns
    corr.index = data.columns
    corr_matrix = abs(corr)
    corr_matrix.values[tuple([np.arange(corr_matrix.shape[0])]*2)] = np.NaN

    # Calculate correlation with target
    target_cor = pd.DataFrame(corr_matrix[target_column].dropna())
    target_cor['feature'] = target_cor.index
    target_cor.reset_index(drop=True, inplace=True)
    target_cor.columns = ['target_correlation', 'features']

    return target_cor.sort_values('target_correlation', ascending=False)


#%%

############################
# Pre-processing
############################

# train test split with target stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train test split with groups, no stratification 
gss = GroupShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
train_idx, test_idx = next(gss.split(X, y, groups=X['id'].values))
train = X.iloc[train_idx]
test = X.iloc[test_idx]

# Scaling
std_scaler = StandardScaler() #default, minimises impact of outliers. MinMaxScaler lighter touch / non-normal dist
X_train_std = std_scaler.fit_transform(X_train)
X_test_std = std_scaler.transform(X_test)

# Catagorical encoding
# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
wheather_encoded=le.fit_transform(wheather)
print (wheather_encoded)

# Tfidf


