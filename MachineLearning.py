
def visEducationVsIncome(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Limit
    pyplot.scatter(Credit.Education, Credit.Income)
    pyplot.xlabel("Education")
    pyplot.ylabel("Income")
    pyplot.title("Education VS Income")
    pyplot.show()
    pyplot.clf()

def visEducationVsRating(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Limit
    pyplot.scatter(Credit.Education, Credit.Rating)
    pyplot.xlabel("Education")
    pyplot.ylabel("Credit Rating")
    pyplot.title("Credit Rating VS Education")
    pyplot.show()
    pyplot.clf()

def visEducation(Credit, pyplot):
    #Plot the Distribution of Education
    pyplot.hist(Credit.Education)
    pyplot.xlabel("Education")
    pyplot.ylabel("Frequency")
    pyplot.title("Education")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Education)
    pyplot.xlabel("Education")
    pyplot.title("Education")
    pyplot.show()
    pyplot.clf()

def visAgeVsRating(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Limit
    pyplot.scatter(Credit.Age, Credit.Rating)
    pyplot.xlabel("Age")
    pyplot.ylabel("Credit Rating")
    pyplot.title("Credit Rating VS Age")
    pyplot.show()
    pyplot.clf()

def visAgeVsLimit(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Limit
    pyplot.scatter(Credit.Age, Credit.Limit)
    pyplot.xlabel("Age")
    pyplot.ylabel("Credit Limit")
    pyplot.title("Credit Limit VS Age")
    pyplot.show()
    pyplot.clf()

def visAge(Credit, pyplot):
    #Plot the Distribution of Age
    pyplot.hist(Credit.Age)
    pyplot.xlabel("Age")
    pyplot.ylabel("Frequency")
    pyplot.title("Age")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Age)
    pyplot.xlabel("Age")
    pyplot.title("Age")
    pyplot.show()
    pyplot.clf()

def visCardsVsLimit(Credit, pyplot, NP):
    #Compare Distrobutions of Number of Credit Cards VS Credit Limit
    pyplot.scatter(Credit.Limit, Credit.Cards)
    pyplot.xlabel("Credit Limit")
    pyplot.ylabel("Number of Credit Cards")
    pyplot.title("Credit Limit VS Number of Credit Cards")
    pyplot.show()
    pyplot.clf()

def visCardsVsIncome(Credit, pyplot, NP):
    #Compare Distrobutions of number of Credit Cards VS Credit Limit
    pyplot.scatter(Credit.Income, Credit.Cards)
    pyplot.xlabel("Income")
    pyplot.ylabel("Number of Credit Cards")
    pyplot.title("Income VS Number of Credit Cards")
    pyplot.show()
    pyplot.clf()

def visCards(Credit, pyplot):
    #Plot the Distribution of Number of Credit Cards
    pyplot.hist(Credit.Cards)
    pyplot.xlabel("Number of Credit Cards")
    pyplot.ylabel("Frequency")
    pyplot.title("Credit Cards")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Cards)
    pyplot.xlabel("Frequency")
    pyplot.title("Credit Cards")
    pyplot.show()
    pyplot.clf()

def visRatingVsLimit(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Limit
    z = NP.polyfit(Credit.Limit, Credit.Rating, 1)
    p = NP.poly1d(z)
    pyplot.scatter(Credit.Limit, Credit.Rating)
    pyplot.xlabel("Credit Limit")
    pyplot.ylabel("Credit Rating")
    pyplot.title("Credit Limit VS Credit Rating")
    pyplot.plot(Credit.Limit, p(Credit.Limit), "r--")
    pyplot.text(2500, 100, "Credit.Rating = %.6f(Credit.Limit) + %.6f" % (z[0], z[1]))
    pyplot.show()
    pyplot.clf()

def visRatingVsIncome(Credit, pyplot, NP):
    #Compare Distrobutions of Credit Rating VS Credit Income
    z = NP.polyfit(Credit.Income, Credit.Rating, 1)
    p = NP.poly1d(z)
    pyplot.scatter(Credit.Income, Credit.Rating)
    pyplot.xlabel("Income")
    pyplot.ylabel("Credit Rating")
    pyplot.title("Income VS Credit Rating")
    pyplot.plot(Credit.Income, p(Credit.Income), "r--")
    pyplot.text(40, 100, "Credit.Rating = %.6f(Credit.Income) + %.6f" % (z[0], z[1]))
    pyplot.show()
    pyplot.clf()

def visRating(Credit, pyplot):
    #Plot the Distribution of Income
    pyplot.hist(Credit.Rating)
    pyplot.xlabel("Credit Rating")
    pyplot.ylabel("Frequency")
    pyplot.title("Credit Rating")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Rating)
    pyplot.xlabel("Frequency")
    pyplot.title("Credit Rating")
    pyplot.show()
    pyplot.clf()

def visIncome(Credit, pyplot):
    #Plot the Distribution of Income
    pyplot.hist(Credit.Income)
    pyplot.xlabel("Income in Thousands")
    pyplot.ylabel("Frequency")
    pyplot.title("Income")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Income)
    pyplot.xlabel("Frequency")
    pyplot.title("Income")
    pyplot.show()
    pyplot.clf()

def visLimit(Credit, pyplot):
    #Plot the Distribution of Credit Limit
    pyplot.hist(Credit.Limit)
    pyplot.xlabel("Credit Limit in Thousands")
    pyplot.ylabel("Frequency")
    pyplot.title("Credit Limit")
    pyplot.show()
    pyplot.clf()

    pyplot.boxplot(Credit.Limit)
    pyplot.xlabel("Frequency")
    pyplot.title("Credit Limit")
    pyplot.show()
    pyplot.clf()

def visIncomeVsCredit(Credit, pyplot, NP):
    #Compare Distrobutions of Income VS Credit Limit
    z = NP.polyfit(Credit.Income, Credit.Limit, 1)
    p = NP.poly1d(z)
    pyplot.scatter(Credit.Income, Credit.Limit)
    pyplot.xlabel("Income")
    pyplot.ylabel("Credit Limit")
    pyplot.title("Income VS Credit Limit\nIn Thousands")
    pyplot.plot(Credit.Income, p(Credit.Income), "r--")
    pyplot.text(30,500, "Credit.Limit = %.6f(Credit.Income) + %.6f"%(z[0],z[1]))
    pyplot.show()
    pyplot.clf()

def linearRegression(data,pyplot,sbn,log,train_test_split,linear_model,sm):

    f, ax = pyplot.subplots(figsize=(10, 10))
    sbn.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
    pyplot.show()

    #removing limit as it is highly correlated with income

    data['Student'] = data['Student'].str.lower().replace({'yes': 1, 'no': 0})
    #data['Gender'] = data['Gender'].str.lower().replace({'male': 1, 'female': 0})
    data['Married'] = data['Married'].str.lower().replace({'yes': 1, 'no': 0})
    data['Ethnicity'] = data['Ethnicity'].str.lower().replace({'african american': 1, 'asian': 2, 'caucasian': 3})


    y=data.loc[:,"Rating"]
    X=data.loc[:,["Income","Cards",	"Age",	"Education",
                 "Student",	"Married",	"Ethnicity","Balance"]]
    X["Income"]=X["Income"].apply(lambda x: log(x))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    lm=linear_model.LinearRegression()
    lm.fit(X_train,y_train)

    print lm.score(X_train,y_train)
    yPred = lm.predict(X_test)
    print lm.score(X_test,y_test)

    X = sm.add_constant(X)
    lm = sm.OLS(y, X).fit()

    print lm.summary()

def decisionTree(data,metrics,train_test_split,DecisionTreeRegressor,NP,log):

    data['Student'] = data['Student'].str.lower().replace({'yes': 1, 'no': 0})
    # data['Gender'] = data['Gender'].str.lower().replace({'male': 1, 'female': 0})
    data['Married'] = data['Married'].str.lower().replace({'yes': 1, 'no': 0})
    data['Ethnicity'] = data['Ethnicity'].str.lower().replace({'african american': 1, 'asian': 2, 'caucasian': 3})

    y = data.loc[:, "Rating"]
    X = data.loc[:, ["Income", "Cards", "Age", "Education",
                     "Student", "Married", "Ethnicity", "Balance"]]
    X["Income"] = X["Income"].apply(lambda x: log(x))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    tree=DecisionTreeRegressor(criterion="mse",min_samples_leaf=5)
    tree.fit(X_train,y_train)

    print tree.score(X_train,y_train)
    print tree.score(X_test,y_test)

    pred_train=tree.predict(X_train)
    print('R square for training:',metrics.r2_score(y_train,pred_train))
    print('Root mean square error training:', NP.sqrt(metrics.mean_squared_error(y_train, pred_train)))
    y_pred=tree.predict(X_test)
    print('R square for test:', metrics.r2_score(y_test, y_pred))
    print('Root mean square error test:', NP.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    print dict(zip(X,tree.feature_importances_))


############# TREND LINE ############################

def main():
    # Install and import all required packages:
    import pandas as PD
    import numpy as NP
    import matplotlib as MAT
    import matplotlib.pyplot as pyplot
    import seaborn as sbn
    from sklearn import linear_model
    import statsmodels.api as sm
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeRegressor
    from sklearn import metrics
    #from statsmodels.tools.eval_measures import rmse
    from math import sqrt, log, exp


    # Load in and view the Credit Data Set.
    Credit = PD.read_csv("D:/UIC/IDS 400/Project/Credit.csv")
    Credit = PD.DataFrame(Credit)



    # Names of the Collumns
    Credit.columns

    # Remove the first column because it doesn't have a purpose
    Credit = Credit.drop(columns="Unnamed: 0")
    Credit = Credit.drop(columns="ID")

    X = input("What would you like to view? (Feature Visualizations, Data Visualization, or Predictive Models)")

    if X == "Feature Visualizations":
        #Visualizations
        V = input("Income, Limit, Rating, Cards, Age, Education, Gender, Student, Married, Ethnicity, Balance, NONE.")
        if V == "Income":
            visIncome(Credit, pyplot)
            visIncomeVsCredit(Credit, pyplot, NP)
            visRatingVsIncome(Credit, pyplot, NP)
            visEducationVsIncome(Credit, pyplot, NP)

        elif V == "Limit":
            visLimit(Credit, pyplot)
            visIncomeVsCredit(Credit, pyplot, NP)
            visRatingVsLimit(Credit, pyplot, NP)

        elif V == "Rating":
            visRating(Credit, pyplot)
            visRatingVsIncome(Credit, pyplot, NP)
            visRatingVsLimit(Credit, pyplot, NP)

        elif V == "Cards":
            visCards(Credit, pyplot)
            visCardsVsIncome(Credit, pyplot, NP)
            visCardsVsLimit(Credit, pyplot, NP)

        elif V == "Age":
            visAge(Credit, pyplot)
            visAgeVsRating(Credit, pyplot, NP)
            visAgeVsLimit(Credit, pyplot, NP)

        elif V == "Education":
            visEducation(Credit, pyplot)
            visEducationVsRating(Credit, pyplot, NP)
            visEducationVsIncome(Credit, pyplot, NP)

        elif V == "Gender":
            pass

    elif X  == "Data Visualization":
        #Show Correlation plot
        #Finds Correlation for all the numerical features.
        PD.plotting.scatter_matrix(Credit)
        pyplot.show()
        pyplot.clf()

        pyplot.matshow(Credit.corr(), fignum= 1, cmap='RdBu')
        pyplot.xticks(NP.arange(7), labels=["Income", "Limit", "Rating", "Cards", "Age", "Education", "Balance"])
        pyplot.yticks(NP.arange(7), labels=["Income", "Limit", "Rating", "Cards", "Age", "Education", "Balance"])
        pyplot.title("Correlation between Numerical Features")
        pyplot.colorbar()
        pyplot.show()
        pyplot.clf()

        print(Credit.corr())


    elif X == "Predictive Models":
        ###PREDICTIVE MODELS HERE####
        V=input("Which model? Linear regression or Decision Tree")
        if V=="Linear regression":
            linearRegression(Credit,pyplot,sbn,log,train_test_split,linear_model,sm)
        elif V=="Decision Tree":
            decisionTree(Credit,metrics,train_test_split,DecisionTreeRegressor,NP,log)

main()
