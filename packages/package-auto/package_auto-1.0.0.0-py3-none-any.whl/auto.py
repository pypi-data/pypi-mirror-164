# 경고 메세지 무시

def test_package():
    print("This is package test")


import warnings
from ctgan import CTGANSynthesizer
from pycaret.classification import *
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN


with warnings.catch_warnings():
    # ignore all caught warnings
    warnings.filterwarnings("ignore")
    # execute code that will generate warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

# CTGAN 
class imbalance:
        
    def __init__(self, something):
        self.something = something
        print(something)
    
    def imbalance_CTGAN(self):
        #print(sum(train_data.Group==0), sum(train_data.Group==1) )
        #print(sum(test_data.Group==0), sum(test_data.Group==1) )

        train_data_0= self[self.Group==0]
        train_data_1= self[self.Group==1]

        ### len(train_data_0)-len(train_data_1)개 생성
        random_sample= len(train_data_0)-len(train_data_1)

        data = train_data_1
        ctgan = CTGANSynthesizer(epochs=100)
        ctgan.set_random_state(123)
        ctgan.fit(data,['Group'])
        samples_129_1 = ctgan.sample(random_sample)
        samples_129_1.Group = 1
        train_129 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
        train_data =pd.concat([train_data_0 , train_129], axis = 0)
        return train_data

    # ADASYN

    def imbalance_ADASYN(self):

        ada = ADASYN(random_state=42)
        X, y = train_data.drop("Group", axis = 1), train_data.Group
        X_res, y_res = ada.fit_sample(X, y)
        df_X_res = pd.DataFrame(X_res)
        df_y_res = pd.DataFrame(y_res)
        df_X_res.columns = X.columns
        #df_y_res.columns

        train_data = pd.concat([df_X_res, df_y_res.Group] , axis = 1)

        return train_data

    # UNDERSAMPLING 

    def imbalance_UNDER(self):
        train_data_0= train_data[train_data.Group==0]
        train_data_1= train_data[train_data.Group==1]

        test_data_0= test_data[test_data.Group==0]
        test_data_1= test_data[test_data.Group==1]
        train_data = pd.concat([train_data_0.sample(len(train_data_1)),train_data_1], axis = 0).reset_index(drop= True)
        return train_data

    #SMOTE

    def imbalance_SMOTE(self):

        smote = SMOTE(random_state=0)
        X_train_over,y_train_over = smote.fit_sample(train_data.drop('Group', axis = 1),train_data.Group)
        train_data = pd.concat([X_train_over, y_train_over], axis = 1) 
        return train_data

