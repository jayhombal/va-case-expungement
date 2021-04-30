

expunge_eligible_case_dispositions = ['Dismissed',
                                      'Noile Prosequi',
                                      'Not Guilty', 
                                      'Withdrawn', 
                                      'Not Found', 
                                      'No Indictment Presented',
                                      'No Longer Under Advisement',
                                      'Not True Bill']

"""
Spark UDF function to encode case as candidate for expungement
"""
def encode_expungement_candidate(final_disposition):
    if final_disposition in (expunge_eligible_case_dispositions):
        return 1
    else:
        return 0
    


"""
Spark UDF function to encode case_class and charge_type columns together into a 
to a numeric value
"""

def encode_class_and_chargetype(case_class, charge_type):
    if charge_type == 'Felony':
            if case_class == "1":
                return 11
            elif case_class == "2":
                return 10
            elif case_class == "3":
                return 9
            elif case_class == "4":
                return 7
            elif case_class == "5":
                return 6
            elif case_class == "6":
                return 5
            elif case_class == "O":
                return 8
            elif case_class == "U":
                return 8
            else:
                return 0
    elif charge_type == 'Misdemeanor':
            if case_class == "1":
                return 4
            elif case_class == "2":
                return 3
            elif case_class == "3":
                return 2
            elif case_class == "4":
                return 1
            else:
                return 0
            

"""
class imbalance down-sample the dataset
"""

def downsample(df, target='candidate', positive_label=1, negative_label=0, seed=42):
    """
    df              spark dataframe
    target          str, target variable
    positive_label  int, value of positive label
    negative_label  int, value of negative label
    
    """
    
    majority_df = df.filter(col(target) == negative_label)
    print(f"majority class count: {majority_df.count()}")
    minority_df = df.filter(col(target) == positive_label)
    print(f"minority class count: {minority_df.count()}")
    ratio = majority_df.count()/minority_df.count()
    print(f"sampling ratio : {ratio}")
    
    sample_majority_df = majority_df.sample(False, fraction=1/ratio, seed= seed)
    df_b = sample_majority_df.unionAll(minority_df)
    return df_b

'''
Evaluate Model
'''

def evaluate_model(predDF , model_name= 'Logistic Regression'):
    lr_evaluator1 = BinaryClassificationEvaluator(metricName='areaUnderROC',labelCol='candidate')
    lr_auroc = lr_evaluator1.evaluate(predDF)
    print(f'The AUROC for {model_name} Model is {lr_auroc}')

    lr_evaluator = BinaryClassificationEvaluator(metricName='areaUnderPR', labelCol='candidate')
    lr_aupr = lr_evaluator2.evaluate(predDF)
    print(f'The AUPR under precision recall for {model_name} Model is {lr_aupr}')

    FP =  predDF.filter('prediction = 1 AND candidate = 0').count()
    print("False Positive : ",FP)
    
    TP =  predDF.filter('prediction = 1 AND candidate = 1').count()
    print("True Positive : ",TP)
    
    FN =  predDF.filter('prediction = 0 AND candidate = 1').count()
    print("False Negative : ",FN)

    TN =  predDF.filter('prediction = 0 AND candidate = 0').count()
    print("True Negative : ",TN)
    
    Y_test = predDF.select('candidate').toPandas()['candidate']
    Y_Pred = predDF.select('prediction').toPandas()['prediction']
    
    print(f'{model_name} model Acccuracy: {accuracy_score(Y_test, Y_Pred)}')
    print(classification_report(Y_test, Y_Pred))

    # get confusion matrix
    cf_matrix = confusion_matrix(Y_test, Y_Pred)
    print(f'{model_name} Confusion Matrix:\n {cf_matrix}')
    

'''
ROC Dataframe
'''
def plotROC(roc_dataframe):
    plt.plot(roc['FPR'],roc['TPR'])
    plt.ylabel('False Positive Rate')
    plt.xlabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()
    print('Training set areaUnderROC: ' + str(trainingSummary.areaUnderROC))