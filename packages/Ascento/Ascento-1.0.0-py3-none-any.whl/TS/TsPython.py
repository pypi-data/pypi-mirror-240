from sklearn.preprocessing import LabelEncoder
import re
import datetime

ohe = LabelEncoder()

# Function for Key Generation Dynamice
def KeyGen(df,*args,key):
    for _,i in enumerate(args):
        if _ == 0:
            df[key]=df[i].astype(str)
        else:
            df[key]=df[key].astype(str)+"_"+df[i].astype(str)
            df[key]=df[key].apply(lambda x:re.sub("[^0-9A-Za-z_]","",x))
    return df

# Droping the null values in different format
def DropNan(df,var):
    df = df[(df[var]!='nan')|(df[var]!='')|(df[var]!='NaN')]
    return df[df[var].isin(df[var].dropna())]

#When we are loading Old files format liks xlsb, python converted that data into time foramt data into integer fomat
def IntTimeStamp(value):
    Timestamp = (float(value)-25569)*86400
    Temp = datetime.fromtimestamp(Timestamp).strftime('%y-%m-%d')
    return Temp

# Encoder
def LabelEncode(df):
    ohe = LabelEncoder()
    Temp = []
    for i in df.columns:
        t1 = ohe.fit_transform(df[i])
        t2 = list(ohe.inverse_transform(t1))
        dic={i:j for i,j in zip(t2,t1)}
        Temp.append(dic)
    dic1 = {i:j for i,j in zip(df.columns,Temp)}
    print("Your Encoding Json Format Data Is Ready!")
    return dic1

# Decoding
def LabelDecode(EncodeData,variable,column):
    try:
        value = EncodeData[column][variable]
        return value+1
    except:
        return 0
        