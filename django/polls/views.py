# Importation des librairies
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import geopandas as gpd
from django.db import models
from django_matplotlib import MatplotlibFigureField
import plotly.express as px
import plotly.graph_objects as go

#import des datasets
df=pd.read_csv('biodeg.csv',sep=';')
df = df.dropna(axis=1)
df.replace(["RB","NRB"],[1,0], inplace = True)



# page d'accueil (pour choisir entre l'année 2022 et la comparaison)
def Accueil(request):
    template = loader.get_template("template0.html")
    context={
    }
    return HttpResponse(template.render(context, request))

def info_data(request):
    template = loader.get_template("template1.html")
    context={
    }
    return render(request, "template1.html", context)

def visualization(request):
    template = loader.get_template("template2.html")
    context={
    }
    return render(request, "template2.html", context)

def index_visualization(request):
    template=loader.get_template("template2.html")
    # if (request.GET['visu'] == 'Outliers_Removal'):
    #     plot_html=Remove_outliers()
    if (request.GET['visu'] == 'Correlation_Matrix'):
        plot_html=matrix()
    # elif (request.GET['visu'] == '% RB/NRB'):
    #     plot_html=RB_NRB()
    # elif (request.GET['visu'] == 'Data_Distribution'):
    #     plot_html=distribution()
    context={
        "plot_html":plot_html,
    }
    return HttpResponse(template.render(context, request))



## for the outliers
df.rename(columns = {"experimental class": "exp"}, inplace = True)
from sklearn.neighbors import LocalOutlierFactor
y=df['exp']
X_1=df.drop(['exp'],axis=1)
clf = LocalOutlierFactor()
y_pred = clf.fit_predict(X_1)
X_scores = clf.negative_outlier_factor_
outlier_score = pd.DataFrame()
outlier_score["score"] = X_scores
threshold = -2.5
filer = outlier_score["score"] < threshold
outlier_index = outlier_score[filer].index.tolist()

# for the correlation matrix
def matrix():
    correlation_matrix = df.corr()
    strong_correlations = correlation_matrix[abs(correlation_matrix) > 0.85]
    fig=px.imshow(strong_correlations, color_continuous_scale='Spectral_r')
    fig.update_layout(title="Correlation Matrix")
    fig.update_xaxes(side="top")
    fig.update_layout(
        autosize=False,
        width=1000,
        height=1000,)
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

# for the % RB/NRB


def modeling(request):
    template = loader.get_template("template3.html")
    context={
    }
    return render(request, "template3.html", context)

# {% comment %} on cherche a creer un choix de model
#       si l'utilisateur choisi Random Forest, on affiche les resultats de Random Forest
#       si l'utilisateur choisi KNN, on affiche les resultats de KNN
#       si l'utilisateur choisi SVM, on affiche les resultats de SVM
#       si l'utilisateur choisi Logistic Regression, on affiche les resultats de Logistic Regression {% endcomment %}
      
#       {% comment %} #on cree un formulaire pour que l'utilisateur puisse choisir le model qu'il veut {% endcomment %}
#       <form action="/result" method="post">
#         <label for="model">Choose a model:</label>
#         <select name="model" id="model">
#           <option value="Random Forest">Random Forest</option>
#           <option value="KNN">KNN</option>
#           <option value="SVM">SVM</option>
#           <option value="Logistic Regression">Logistic Regression</option>
#         </select>
#         <input type="submit" value="Submit">
#       </form>

#sur cette partie on veut faire le index_modeling pour que l'utilisateur puisse choisir le model qu'il veut
def index_modeling(request):
    template=loader.get_template("template3.html")
    if (request.GET['model'] == 'Mean_Square_Error'):
        plot_html=Mean_Square_Error()
    elif (request.GET['model'] == 'Precision_Score'):
        plot_html=Precision_Score()
    elif (request.GET['model'] == 'Recall_Score'):
        plot_html=Recall_Score()
    elif (request.GET['model'] == 'F1_Score'):
        plot_html=F1_Score()
    elif (request.GET['model'] == 'Accuracy_Score'):
        plot_html=Accuracy_Score()
    context={
        "plot_html":plot_html,
    }
    return HttpResponse(template.render(context, request))


    
        


#4 models : Random Forest, KNN, SVM, Logistic Regression
#Random Forest
# 0.3333333333333333 : mean square error
# 0.8285714285714286 : precision score
# 0.8405797101449275 : recall score
# 0.8345323741007195 : f1 score 
# 0.8888888888888888 : accuracy score
# 131.8028564453125 seconds : time
Random_Forest = [33.3, 82.9, 84.1, 83.5, 88.8, 131.8, "green"]

#SVM
# 0.34752402342845795 : mean square error
# 0.8235294117647058 : precision score
# 0.8115942028985508 : recall score 
# 0.8175182481751825 : f1 score
# 0.8792270531400966 : accuracy score
# 209.68421578407288 seconds : time
SVM = [34.8, 82.4, 81.2, 81.7, 87.9, 209.7, "red"]


#Logistic Regression
# 0.3086066999241838 : mean square error
# 0.8450704225352113 : precision score 
# 0.8695652173913043 : recall score 
# 0.8571428571428571 : f1 score
# 0.9033816425120773 : accuracy score
# 282.1229441165924 seconds : time
Logistic_Regression = [30.8, 84.5, 86.9, 85.7, 90.3, 282.1, "blue"]

#KNN
# 0.3108349360801046 : mean square error
# 0.8450704225352113 : precision score 
# 0.8695652173913043 : recall score 
# 0.8571428571428571 : f1 score
# 0.9033816425120773 : accuracy score
# 43.4437313079834 seconds : time
KNN = [31.1, 84.5, 86.9, 85.7, 90.3, 43.4, "yellow"]

#on veut plot des barres pour chaque valeur de chaque model et les classer de la plus petite a la plus grande

def Mean_Square_Error():
    #on veut des plot barres triees par ordre croissant
    mse_values=[Random_Forest[0], SVM[0], Logistic_Regression[0], KNN[0]]
    models=["Random Forest", "SVM", "Logistic Regression", "KNN"]
    colors=[Random_Forest[6], SVM[6], Logistic_Regression[6], KNN[6]]
    #on fait la figure avec les valeurs qu'on doit trier
    fig=px.bar(x=models, y=mse_values, color=colors)
    fig.update_layout(title="Mean Square Error")
    #on convertit la figure en html
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)


def Precision_Score():
    precision_values=[Random_Forest[1], SVM[1], Logistic_Regression[1], KNN[1]]
    models=["Random Forest", "SVM", "Logistic Regression", "KNN"]
    fig=px.bar(x=models, y=precision_values, color=precision_values, color_continuous_scale='Spectral_r')
    fig.update_layout(title="Precision Score")
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def Recall_Score():
    recall_values=[Random_Forest[2], SVM[2], Logistic_Regression[2], KNN[2]]
    models=["Random Forest", "SVM", "Logistic Regression", "KNN"]
    fig=px.bar(x=models, y=recall_values, color=recall_values, color_continuous_scale='Spectral_r')
    fig.update_layout(title="Recall Score")
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def F1_Score():
    f1_values=[Random_Forest[3], SVM[3], Logistic_Regression[3], KNN[3]]
    models=["Random Forest", "SVM", "Logistic Regression", "KNN"]
    fig=px.bar(x=models, y=f1_values, color=f1_values, color_continuous_scale='Spectral_r')
    fig.update_layout(title="F1 Score")
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def Accuracy_Score():
    accuracy_values=[Random_Forest[4], SVM[4], Logistic_Regression[4], KNN[4]]
    models=["Random Forest", "SVM", "Logistic Regression", "KNN"]
    fig=px.bar(x=models, y=accuracy_values, color=accuracy_values, color_continuous_scale='Spectral_r')
    fig.update_layout(title="Accuracy Score")
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html
