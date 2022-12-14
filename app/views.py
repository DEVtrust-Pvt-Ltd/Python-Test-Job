from django.shortcuts import render # for render template
from django.http import HttpResponse # for return message
import pandas as pd # for make dataframe 
import os

def home(request):
    return render(request,'index.html')
    

def index(request):

    # get data from dropdown 
    if request.method=='POST':                                      
        dropdown1 = request.POST.getlist('drop1')
        dropdown2 = request.POST.getlist('drop2')
        dropdown3 = request.POST.getlist('drop3')
    # create dataframe and read csv file 
        try:         
            df = pd.DataFrame({'column1':dropdown1,'column2':dropdown2,'column3':dropdown3})
            path = os.getcwd()+'/csv'+f'/{dropdown1[0]}_{dropdown2[0]}_{dropdown3[0]}.csv'
            data = pd.read_csv(path)
        except:
            pass
    # data redirect on home page 
        return render(request,'index.html',{'columns': data.columns, 'rows': data.to_dict('records') ,'drop1':dropdown1[0],'drop2':dropdown2[0],'drop3':dropdown3[0]})
    return HttpResponse('method not post')



































      # for csvfile in v:
            #     if csvfile==f'{dropdown1[0]}_{dropdown2[0]}_{dropdown3[0]}.csv':
            #         df1 = pd.read_csv(path)
            #         print('*******',df1)
            #         df3 = pd.concat([df, df1], axis=0)
            #         print('qwwwwwwwwwwwww',df3)
            #         df3.to_csv(path,index=False)
            #     else:
            #         continue                    