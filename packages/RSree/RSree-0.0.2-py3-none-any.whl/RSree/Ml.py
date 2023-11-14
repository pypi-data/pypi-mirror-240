import numpy as np
import pandas as pd

def X_mu(data):
    X = []
    for p in data.columns:
        jk = []
        mu = data[p].mean()
        for g in data[p]:
            jk.append(g-mu)
        X.append(jk)
    return np.array(X)


def PCA_DR(Ddata,Rt):
    meancx = pd.DataFrame({i:Ddata[i]-np.mean(Ddata[i]) for i in Ddata.columns})
    Corel = meancx.transpose().dot(meancx)
    #Corel = meancx.cov()
    egval,eginvector = np.linalg.eig(Corel)
    reqeginvec = np.transpose(eginvector[:,:Rt])
    X = X_mu(Ddata)
    redfe =np.transpose(np.dot(reqeginvec,X))
    reduced_Feture = pd.DataFrame(redfe,columns=[f'Feature_{p}' for p in range(1,len(redfe[0])+1)])
    return reduced_Feture

def corel(x,y):
        menx = np.mean(x)
        meny = np.mean(y)
        temp,temp1,temp2 = 0,0,0
        for i,j in zip(x,y):
            temp += (i-menx)*(round(j,2)-meny)
            temp1 += (i-menx)**2
            temp2 += (j-meny)**2
        r = temp/(temp1*temp2)**0.5
        return r


def correl_Tablel(da,mcol):
    colda = list(da.columns)
    if mcol == "all":
        mcol = colda
    #colda.remove(mcol)
    corellis = []
    gg = []
    for o in mcol:
        for _ in colda:
            corellis.append(round(corel(da[o],da[_]),2))
        gg.append(corellis)
        corellis = []
    table = pd.DataFrame({b:n for b,n in zip(mcol,gg)},index=colda)
    return table


def Outlier_remover(inf):
    temp = []
    qurtile = np.quantile(inf,[0,0.25,0.50,0.75,1])
    IQR = qurtile[3] - qurtile[1]
    lbound = qurtile[1] - 1.5*IQR
    ubound = qurtile[3] + 1.5*IQR
    for i,j in enumerate(inf):
        if j<lbound:
            #print(i,j)
            inf[j] = np.median(inf)
            #print(inf[j])
            temp.append(inf[j])
        elif j>ubound:
            #print(i,j)
            inf[j] = np.median(inf)
            #print(inf[j])
            temp.append(inf[j])
        else:
            temp.append(j)
    return temp

def rmse(x,y):
    x = np.array(x)
    y = np.array(y)
    N = len(x)
    Sum = 0
    for _ in range(N):
        Sum += (x[_] - y[_])**2 
    return (Sum/N)**0.5


def repret(lis):
    s = list(set(list(lis)))
    k = [lis.count(x) for x in s]
    return s[k.index(max(k))]


def eculidean(a,b):
    Sum = 0
    for i in range(len(a)):
        Sum += (a[i] - b[i])**2
    return Sum**0.5


def Knn(trnD,trnDL,TstD,TstDL,k=3):
    relApre = []
    for i,j in zip(TstD,TstDL):
        temp = {}
        for k,l in zip(trnD,trnDL):
            temp[eculidean(i,k)] = l
        sort = sorted(temp.keys())[:3]
        sortlabel = [temp[_] for _ in sort]
        relApre.append([repret(sortlabel),j])
    return pd.DataFrame(relApre,columns=['Predicted','Actual'])

def mean(da):
    temp = 0
    for i in da:
        temp += i
    return temp/len(da)
def Std(da):
    mu = mean(da)
    temp = 0
    for i in da:
        temp += (i-mu)**2
    return (temp/len(da))**0.5


def normal_dist(x, data):
        prob_density = (np.pi*Std(data)) * np.exp(-0.5*((x-mean(data))/Std(data))**2)
        return prob_density


def Accur_per(Cm):
    sup = 0
    for b in range(len(Cm)):
        sup += Cm[b][b]
    return (sup/np.sum(Cm))*100


def SumXn(dat,n):
    temp = 0
    for i in dat:
        temp += i**n
    return temp

def SumXY(x,y):
    temp = 0
    for i,j in zip(x,y):
        temp += i*j
    return temp


def AvP(tx,ty,model):
    predictions = []
    for s in tx:
        predictions.append(model(s))
    AvP = pd.DataFrame({"Actual":ty,"Prediction":predictions}).reset_index().iloc[:,1:]
    return AvP