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

from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(dataset: pd.DataFrame, med_threshold=1, high_threshold=5.0) -> pd.DataFrame:
    """
    Calculate Variance Inflation Factor for numeric features to 
    detect multicollinearity between features.

    VIF: https://www.statisticshowto.com/variance-inflation-factor/ 
    VIF ranges from 1 upwards. Shows what percentage the variance is 
    inflated for each coefficient. E.g. VIF of 1.9 tells you that the 
    variance of a particular coefficient is 90% bigger than what you 
    would expect if there was no multicollinearity (no correlation 
    with other predictors). A rule of thumb:

    1 = not correlated.
    Between 1 and 5 = moderately correlated. 
    Greater than 5 highly correlated.

    Args:
        dataset: data frame containing features
    """

    data = dataset.copy()
    data = data.fillna(0)

    # Calculate VIF on numeric values
    X = data.select_dtypes(include=["float64", 'int64'])  
    vif = pd.DataFrame()
    vif['features'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif['VIF_status'] = vif['VIF'].map(lambda x: 'high' if x > high_threshold else \
                                        ('medium' if x > med_threshold else 'none'))

    print(f"calculated VIF for {range(X.shape[1])} features")

    return vif.round(1)


from pyod.models.knn import KNN
from pyod.models.iforest import IForest
from pyod.models.pca import PCA as PCA_od

def detect_outliers(dataset, contamination=0.20, methods=['knn', 'iso','pca']): 
    """
    Args:
        contamination: proportion of dataset expected as outliers
    """
    # only do this on the numeric columns
    data = dataset.select_dtypes(include=["float64", "int64"]).copy()

    if 'knn' in methods:
        knn = KNN(contamination=contamination) 
        knn.fit(data)
        knn_predict = knn.predict(data)# binary labels (0: inliers, 1: outliers)
        data['knn'] = knn_predict

    if 'iso' in methods:
        iso = IForest(contamination=contamination, random_state=42, behaviour='new')
        iso_predict = iso.predict(data)
        iso.fit(data)
        data['iso'] = iso_predict

    if 'pca' in methods:
        pca = PCA_od(contamination=contamination, random_state=42)
        pca.fit(data)
        pca_predict = pca.predict(data)
        data['pca'] = pca_predict

    data['vote_outlier'] = 0

    for i in methods:
        data['vote_outlier'] = data['vote_outlier'] + data[i]

    # only select if all methods agree on outliers 
    outliers = data[data['vote_outlier'] == len(methods)]
    print('Outlier size {0}'.format(len(outliers)))

    print(dataset[[True if i in outliers.index else False for i in dataset.index]])

    return data
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

# Random Forest. 
# Good place to start is Random Forest as this does not require much hyperparameter tuning besides number of trees, 
# and because the ensemble model is quite robust to noise from the individual trees
# Suggest setting max_depth, min_samples_leaf to non-null to constrain depth of trees

rf = RandomForestClassifier(criterion='entropy', # info gain objective
                            n_estimators=100, 
                            random_state=0,
                            n_jobs=-1) # use all cores for parallel processing

rf.fit(X_train, y_train)
rf_pred = rf.predict_proba(X_test)[:, 1]

# Logistic Regression
# Uses L2 regularisation by default
logit = LogisticRegression(C=1, max_iter=200) # C = 1/lambda. Smaller values specify stronger regularisation.
logit.fit(X_train, y_train)
logit_test_pred = logit.predict_proba(X_test)[:, 1]

# TODO
# Tfidf



