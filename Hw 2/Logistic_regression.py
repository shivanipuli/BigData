### Logistic regression

# Perform the logistic regression

import statsmodels.api as sm
import pandas as pd

def Logistic_regression(X,y):
    '''
       Perform the logistic regression to predict default situation

       Input:
       X       : Numeric matrix, explainable variable
       y       : Boolean value, 0 for non-default and 1 for default

       Output:
       Model summary information
       p_value: p value for each variable in X
       result : The fitted model
       '''
    ##############################################################################
    ### TODO: Perform the logistic regression to predict default situation     ###
    ##############################################################################
    # Step 1. Construct the logistic model
    # You may consider using sm.Logit(y,X) method    
    X = sm.add_constant(X)
    log_reg = sm.Logit(y, X).fit()
    
    # Step 2. Get the p_value for each variable. 
    # You may consider using result.pvalues attribute
    p_value = log_reg.pvalues
    return p_value, log_reg

    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################
    