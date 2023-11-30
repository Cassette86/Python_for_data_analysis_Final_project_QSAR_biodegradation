# Importation des librairies
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

def index_visualization():
    template=loader.get_template("template2.html")
    if (request.GET['model'] == 'Outliers_Removal'):
        plot_html=Remove_outliers()
    # elif (request.GET['model'] == 'Correlation Matrix'):
    #     plot_html=matrix()
    # elif (request.GET['model'] == '% RB/NRB'):
    #     plot_html=RB_NRB()
    # elif (request.GET['model'] == 'Data Distribution'):
    #     plot_html=distribution()
    context={
        "plot_html":plot_html,
    }
    return HttpResponse(template.render(context, request))
# the resq


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






def Remove_outliers():
    # plt.figure(figsize=(10,8))
    # plt.scatter(X_1.iloc[outlier_index,0],X_1.iloc[outlier_index,1],color="blue",s=50,label="outliers")

    # plt.scatter(X_1.iloc[:,0],X_1.iloc[:,1],color="k",s=3,label="data points")

    # radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
    # outlier_score["radius"] = radius
    # plt.scatter(X_1.iloc[:,0],X_1.iloc[:,1],s=1000*radius,edgecolors="r",facecolors="none",label="outlier scores")
    # plt.legend()
    fig=px.scatter(X_1.iloc[:,0],X_1.iloc[:,1],color="k",s=3,label="data points")
    fig.update_layout(
        title="Outliers Removal",
        xaxis_title="",
        yaxis_title="",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    plol_html=fig.to_html(full_html=False, default_height=500, default_width=700)


def modeling(request):
    template = loader.get_template("template3.html")
    context={
    }
    return render(request, "template3.html", context)