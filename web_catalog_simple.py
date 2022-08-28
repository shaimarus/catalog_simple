from flask import Flask, request, render_template
import pandas as pd
import pickle
import time
app = Flask(__name__)
#df=pickle.load(open('catalog.pkl','rb'))
df=pd.read_excel('catalog_v1.xlsx',sheet_name='1')

@app.route('/', methods=['POST','GET'])    
def my_form_post():

    start = time.time()    
    a='' 
    
    if request.method=="POST":
        a=request.form.get('name2')
        
    qs = a.lower().strip().split()

    match = lambda s: sum(min(3, s.lower().count(qp)) for qp in qs)
    pairs = []
    for pid, p in df['NAME'].items():
        score = 0.0
        score += 1.0 * match(p)
        if score > 0:
            pairs.append((score, pid))

    pairs.sort(reverse=True)
    pids = [p[1] for p in pairs]
    scores = [p[0] for p in pairs]

    d1=df.iloc[pids][['CODE','NAME']].reset_index()

    code=d1['CODE']
    name=d1['NAME']
    score=scores

    keys=['name','code','score']
    values=[name,code,score]

    newList = []
    for i in range(len(values[0])):

        tmp = {}
        for j, key in enumerate(keys):
            tmp[key] = values[j][i]

        newList.append(tmp)
    end = time.time()
    return render_template('catalog_simple.html',data=newList,time_calc=round(end-start,3))        


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5016, debug=False)