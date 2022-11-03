from django.shortcuts import render

from joblib import load
model = load('./savedModel/model.joblib')

def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        chest = request.POST['chest']
        restingbp = request.POST['restingbp']
        cholestrol = request.POST['cholestrol']
        sugar = request.POST['sugar']
        ecg = request.POST['ecg']
        heartrate = request.POST['heartrate']
        exercise = request.POST['exercise']
        strate = request.POST['strate']
        stdepth = request.POST['stdepth']
        TA,ATA,NP=0,0,0
        M=0
        NORMAL,ST=0,0
        ANG=0
        FLAT,UP=0,0
        if chest=='ATA':
            ATA=1
            TA=NP=0
        elif chest=='TA':
            TA=1
            ATA=NP=0
        elif chest=='NP':
            NP=1
            ATA=TA=0
        
        if gender=='M':
            M=1
        else:
            M=0
        
        if ecg=='normal':
            NORMAL=1
            ST=0
        elif ecg=='ST':
            ST=1
            NORMAL=0

        if exercise=='Y':
            ANG=1
        else:
            ANG=0
        
        if stdepth=='up':
            UP=1
            FLAT=0
        elif stdepth=='flat':
            UP=0
            FLAT=1


        age = int('0' + age)
        restingbp = int('0' + restingbp)
        cholestrol = int('0' + cholestrol)
        sugar = int('0' + sugar)
        heartrate = int('0' + heartrate)
        strate = float('0' + strate)

        y_pred = model.predict([[age,restingbp,cholestrol,sugar,heartrate,strate,M,ATA,NP,TA,NORMAL,ST,ANG,FLAT,UP]])
        if y_pred[0] == 0:
            y_pred = 'Great'
        elif y_pred[0] == 1:
            y_pred = 'Bad'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')
