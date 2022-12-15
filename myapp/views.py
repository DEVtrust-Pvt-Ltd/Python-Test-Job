from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
import seaborn as sns
import os
def home(request):
    return render(request,'index.html')
def index(request):
        df = pd.read_csv('csv/heatmap.csv')
        df = pd.DataFrame(df)
        
        return render(request,'myapp/index.html',{'df':df,'columns': df.columns, 'rows': df.to_dict('records')})










    




    


   