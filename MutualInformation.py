import math

import pandas as pd
from itertools import chain



class MutualInformation:
    
#membuat variabel global
    
    
    listData=[]
    unique_word=[]
    label=[]
    MI=[]
    token = None
    dataset = None
    fitur = []
    MI_fitur=[]
    
   
    
    def __init__(self,dataset):
        

        self.dataframe = dataset
        self.listData=[]
        for text in self.dataframe['tweet']:
            self.token = text.split()
            self.listData.append(self.token)
        
        #print(self.listData)
        #print('panjang list data :')
        #print(len(self.listData))
       
        #print('panjang flatten list :')
        self.flatten_list = list(chain.from_iterable(self.listData))
        #print(len(self.flatten_list))
       
        #print(self.flatten_list)
    
        for i in self.flatten_list:
            if i not in self.unique_word:
                self.unique_word.append(i)     
       
                
        self.unique_word.sort()
        #print('panjang unique word :')
        #print(len(self.unique_word))
        #print(self.unique_word,"\n\n")
        
        
        for text in self.dataframe['label']:
            self.label.append(text)
        
        
        #print(self.label)
                
        print("Mutual Information jalan,")
        
    def process(self):
        #Nilai Kebenaran BB pada kelas Anger
        BB01=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]=='anger'):
                            count=count+1;
            BB01.append(count)

        #print(BB01[0])

        #Nilai Kebenaran BB pada kelas Happy
        BB02=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]=='happy'):
                            count=count+1;
            BB02.append(count)
        
        #print(BB02[0])

        #Nilai Kebenaran BB pada kelas Sadness
        BB03=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]=='sadness'):
                            count=count+1;
            BB03.append(count)
        
        #print(BB03[0])

        #Nilai Kebenaran BB pada kelas Fear
        BB04=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]=='fear'):
                            count=count+1;
            BB04.append(count)
        
        #print(BB03[0])

         #Nilai Kebenaran BB pada kelas Love
        BB05=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]=='love'):
                            count=count+1;
            BB05.append(count)
        
        #print(BB03[0])
        
        #Nilai Kebenaran SB pada kelas Anger
        SB01=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]=='anger'):
                            count=count+1;
            SB01.append(count)
        
        #print(SB01[0])
        
        #Nilai Kebenaran SB pada kelas Happy
        SB02=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]=='happy'):
                            count=count+1;
            SB02.append(count)
        
        #print(SB02[0])
        
        #Nilai Kebenaran SB pada kelas Sadness
        SB03=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]=='sadness'):
                            count=count+1;
            SB03.append(count)
        
        #print(SB03[0])

         #Nilai Kebenaran SB pada kelas Fear
        SB04=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]=='fear'):
                            count=count+1;
            SB04.append(count)
        
        #print(SB03[0])

         #Nilai Kebenaran SB pada kelas Love
        SB05=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]=='love'):
                            count=count+1;
            SB05.append(count)
        
        #print(SB03[0])
        
        #Nilai Kebenaran BS pada kelas Anger
        BS01=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]!='anger'):
                            count=count+1;
            BS01.append(count)
        
        #print(BS01[0])
        
        #Nilai Kebenaran BS pada kelas Happy
        BS02=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]!='happy'):
                            count=count+1;
            BS02.append(count)
        
        #print(BS02[0])
        
        #Nilai Kebenaran BS pada kelas Sadness
        BS03=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]!='sadness'):
                            count=count+1;
            BS03.append(count)
        
        #print(BS03[0])

         #Nilai Kebenaran BS pada Fear
        BS04=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]!='fear'):
                            count=count+1;
            BS04.append(count)
        
        #print(BS03[0])

         #Nilai Kebenaran BS pada kelas Love
        BS05=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]==self.listData[j][k]):
                        if(self.label[j]!='love'):
                            count=count+1;
            BS05.append(count)
        
        #print(BS03[0])
        #Nilai Kebenaran SS pada kelas Anger
        SS01=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]!='anger'):
                            count=count+1;
            SS01.append(count)
        
        #print(SS01[0])
        
        #Nilai Kebenaran SS pada kelas Happy
        SS02=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]!='happy'):
                            count=count+1;
            SS02.append(count)
        
        #print(SS02[0])
        
        #Nilai Kebenaran SS pada kelas Sadness
        SS03=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]!='sadness'):
                            count=count+1;
            SS03.append(count)
        
        #print(SS03[0])

        #Nilai Kebenaran SS pada kelas Fear
        SS04=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]!='fear'):
                            count=count+1;
            SS04.append(count)
        
        #print(SS03[0])

        #Nilai Kebenaran SS pada kelas Love
        SS05=[]
        for i in range (len(self.unique_word)):
            count=0;
            for j in range(len(self.listData)):
                for k in range (len(self.listData[j])):
                    if(self.unique_word[i]!=self.listData[j][k]):
                        if(self.label[j]!='love'):
                            count=count+1;
            SS05.append(count)
        
        #print(SS03[0])
        
        N = len(self.flatten_list)

        #N1. Kelas Anger
        N1t01=[]
        for i in range (len(self.unique_word)):
            hasil = BS01[i]+BB01[i]
            N1t01.append(hasil)
        #print(N1t01[0])
        
        #N1. Kelas Happy
        N1t02=[]
        for i in range (len(self.unique_word)):
            hasil = BS02[i]+BB02[i]
            N1t02.append(hasil)
        #print(N1t02[0])
        
        #N1. Kelas Sadness
        N1t03=[]
        for i in range (len(self.unique_word)):
            hasil = BS03[i]+BB03[i]
            N1t03.append(hasil)
        #print(N1t03[0])

        #N1. Kelas Fear
        N1t04=[]
        for i in range (len(self.unique_word)):
            hasil = BS04[i]+BB04[i]
            N1t04.append(hasil)
        #print(N1t03[0])

        #N1. Kelas Love
        N1t05=[]
        for i in range (len(self.unique_word)):
            hasil = BS05[i]+BB05[i]
            N1t05.append(hasil)
        #print(N1t03[0])
        
        #N1 Kelas Anger
        N101=[]
        for i in range (len(self.unique_word)):
            hasil = SB01[i]+BB01[i]
            N101.append(hasil)
        #print(N101[0])
        
        #N1 Kelas Happy
        N102=[]
        for i in range (len(self.unique_word)):
            hasil = SB02[i]+BB02[i]
            N102.append(hasil)
        #print(N102[0])
        
        #N1 Kelas Sadness
        N103=[]
        for i in range (len(self.unique_word)):
            hasil = SB03[i]+BB03[i]
            N103.append(hasil)
        #print(N103[0])

        #N1 Kelas Fear
        N104=[]
        for i in range (len(self.unique_word)):
            hasil = SB04[i]+BB04[i]
            N104.append(hasil)
        #print(N103[0])

        #N1 Kelas Love
        N105=[]
        for i in range (len(self.unique_word)):
            hasil = SB05[i]+BB05[i]
            N105.append(hasil)
        #print(N103[0])
        
        #N0t Kelas Anger
        N0t01=[]
        for i in range (len(self.unique_word)):
            hasil = SB01[i]+SS01[i]
            N0t01.append(hasil)
        #print(N0t01[0])
        
        #N0t Kelas Happy
        N0t02=[]
        for i in range (len(self.unique_word)):
            hasil = SB02[i]+SS02[i]
            N0t02.append(hasil)
        #print(N0t02[0])
        
        #N0t Kelas Sadness
        N0t03=[]
        for i in range (len(self.unique_word)):
            hasil = SB03[i]+SS03[i]
            N0t03.append(hasil)
        #print(N0t03[0])

         #N0t Kelas Fear
        N0t04=[]
        for i in range (len(self.unique_word)):
            hasil = SB04[i]+SS04[i]
            N0t04.append(hasil)
        #print(N0t03[0])

         #N0t Kelas Love
        N0t05=[]
        for i in range (len(self.unique_word)):
            hasil = SB05[i]+SS05[i]
            N0t05.append(hasil)
        #print(N0t03[0])
        
        #N0 Kelas Anger
        N001=[]
        for i in range (len(self.unique_word)):
            hasil = BS01[i]+SS01[i]
            N001.append(hasil)
        #print(N001[0])
        
        #N0 Kelas Happy
        N002=[]
        for i in range (len(self.unique_word)):
            hasil = BS02[i]+SS02[i]
            N002.append(hasil)
        #print(N002[0])
        
        #N0 Kelas Sadness
        N003=[]
        for i in range (len(self.unique_word)):
            hasil = BS03[i]+SS03[i]
            N003.append(hasil)
        #print(N003[0])

         #N0 Kelas Fear
        N004=[]
        for i in range (len(self.unique_word)):
            hasil = BS04[i]+SS04[i]
            N004.append(hasil)
        #print(N003[0])

         #N0 Kelas Love
        N005=[]
        for i in range (len(self.unique_word)):
            hasil = BS05[i]+SS05[i]
            N005.append(hasil)
        #print(N003[0])
        
        #Mutual Informatin Kelas Anger
        MI01=[]
        
        for i in range(len(self.unique_word)):
            #proses 1 
            hasil1_1 = (N*BB01[i])/(N1t01[i]*N101[i])
            if(hasil1_1 == 0):
                hasil1_2 = 0
            else:
                hasil1_2=math.log2(hasil1_1)
            hasil1 = (BB01[i]/N)*hasil1_2
            
            #proses 2
            hasil2_1 = (N*SB01[i])/(N0t01[i]*N101[i])
            if(hasil2_1 == 0):
                hasil2_2 = 0
            else:
                hasil2_2=math.log2(hasil2_1)
            hasil2 = (SB01[i]/N)*hasil2_2
            
            #proses 3
            hasil3_1 = (N*BS01[i])/(N1t01[i]*N001[i])
            if(hasil3_1 == 0):
                hasil3_2 = 0
            else:
                hasil3_2=math.log2(hasil3_1)
            hasil3 = (BS01[i]/N)*hasil3_2
            
            #proses 4
            hasil4_1 = (N*SS01[i])/(N0t01[i]*N001[i])
            if(hasil4_1 == 0):
                hasil4_2 = 0
            else:
                hasil4_2=math.log2(hasil4_1)
            hasil4 = (SS01[i]/N)*hasil4_2
            
            hasil = hasil1+hasil2+hasil3+hasil4
            MI01.append(hasil)
        
        #print(MI01[0])
        #Mutual Informatin Kelas Happy
        MI02=[]
        
        for i in range(len(self.unique_word)):
            #proses 1 
            hasil1_1 = (N*BB02[i])/(N1t02[i]*N102[i])
            if(hasil1_1 == 0):
                hasil1_2 = 0
            else:
                hasil1_2=math.log2(hasil1_1)
            hasil1 = (BB02[i]/N)*hasil1_2
            
            #proses 2
            hasil2_1 = (N*SB02[i])/(N0t02[i]*N102[i])
            if(hasil2_1 == 0):
                hasil2_2 = 0
            else:
                hasil2_2=math.log2(hasil2_1)
            hasil2 = (SB02[i]/N)*hasil2_2
            
            #proses 3
            hasil3_1 = (N*BS02[i])/(N1t02[i]*N002[i])
            if(hasil3_1 == 0):
                hasil3_2 = 0
            else:
                hasil3_2=math.log2(hasil3_1)
            hasil3 = (BS02[i]/N)*hasil3_2
            
            #proses 4
            hasil4_1 = (N*SS02[i])/(N0t02[i]*N002[i])
            if(hasil4_1 == 0):
                hasil4_2 = 0
            else:
                hasil4_2=math.log2(hasil4_1)
            hasil4 = (SS02[i]/N)*hasil4_2
            
            hasil = hasil1+hasil2+hasil3+hasil4
            MI02.append(hasil)
        
        #print(MI02[0])
        
        #Mutual Informatin Kelas Sadness
        MI03=[]
        
        for i in range(len(self.unique_word)):
            #proses 1 
            hasil1_1 = (N*BB03[i])/(N1t03[i]*N103[i])
            if(hasil1_1 == 0):
                hasil1_2 = 0
            else:
                hasil1_2=math.log2(hasil1_1)
            hasil1 = (BB03[i]/N)*hasil1_2
            
            #proses 2
            hasil2_1 = (N*SB03[i])/(N0t03[i]*N103[i])
            if(hasil2_1 == 0):
                hasil2_2 = 0
            else:
                hasil2_2=math.log2(hasil2_1)
            hasil2 = (SB03[i]/N)*hasil2_2
            
            #proses 3
            hasil3_1 = (N*BS03[i])/(N1t03[i]*N003[i])
            if(hasil3_1 == 0):
                hasil3_2 = 0
            else:
                hasil3_2=math.log2(hasil3_1)
            hasil3 = (BS03[i]/N)*hasil3_2
            
            #proses 4
            hasil4_1 = (N*SS03[i])/(N0t03[i]*N003[i])
            if(hasil4_1 == 0):
                hasil4_2 = 0
            else:
                hasil4_2=math.log2(hasil4_1)
            hasil4 = (SS03[i]/N)*hasil4_2
            
            hasil = hasil1+hasil2+hasil3+hasil4
            MI03.append(hasil)
        
        #print(MI03[0])

        #Mutual Informatin Kelas Fear
        MI04=[]
        
        for i in range(len(self.unique_word)):
            #proses 1 
            hasil1_1 = (N*BB04[i])/(N1t04[i]*N104[i])
            if(hasil1_1 == 0):
                hasil1_2 = 0
            else:
                hasil1_2=math.log2(hasil1_1)
            hasil1 = (BB04[i]/N)*hasil1_2
            
            #proses 2
            hasil2_1 = (N*SB04[i])/(N0t04[i]*N104[i])
            if(hasil2_1 == 0):
                hasil2_2 = 0
            else:
                hasil2_2=math.log2(hasil2_1)
            hasil2 = (SB04[i]/N)*hasil2_2
            
            #proses 3
            hasil3_1 = (N*BS04[i])/(N1t04[i]*N004[i])
            if(hasil3_1 == 0):
                hasil3_2 = 0
            else:
                hasil3_2=math.log2(hasil3_1)
            hasil3 = (BS04[i]/N)*hasil3_2
            
            #proses 4
            hasil4_1 = (N*SS04[i])/(N0t04[i]*N004[i])
            if(hasil4_1 == 0):
                hasil4_2 = 0
            else:
                hasil4_2=math.log2(hasil4_1)
            hasil4 = (SS04[i]/N)*hasil4_2
            
            hasil = hasil1+hasil2+hasil3+hasil4
            MI04.append(hasil)
        
        #print(MI03[0])

        #Mutual Informatin Kelas Love
        MI05=[]
        
        for i in range(len(self.unique_word)):
            #proses 1 
            hasil1_1 = (N*BB05[i])/(N1t05[i]*N105[i])
            if(hasil1_1 == 0):
                hasil1_2 = 0
            else:
                hasil1_2=math.log2(hasil1_1)
            hasil1 = (BB05[i]/N)*hasil1_2
            
            #proses 2
            hasil2_1 = (N*SB05[i])/(N0t05[i]*N105[i])
            if(hasil2_1 == 0):
                hasil2_2 = 0
            else:
                hasil2_2=math.log2(hasil2_1)
            hasil2 = (SB05[i]/N)*hasil2_2
            
            #proses 3
            hasil3_1 = (N*BS05[i])/(N1t05[i]*N005[i])
            if(hasil3_1 == 0):
                hasil3_2 = 0
            else:
                hasil3_2=math.log2(hasil3_1)
            hasil3 = (BS05[i]/N)*hasil3_2
            
            #proses 4
            hasil4_1 = (N*SS05[i])/(N0t05[i]*N005[i])
            if(hasil4_1 == 0):
                hasil4_2 = 0
            else:
                hasil4_2=math.log2(hasil4_1)
            hasil4 = (SS05[i]/N)*hasil4_2
            
            hasil = hasil1+hasil2+hasil3+hasil4
            MI05.append(hasil)
        
        #print(MI03[0])
        
        
        for i in range(len(self.unique_word)):
            nilai = max(MI01[i],MI02[i],MI03[i],MI04[i],MI05[i])
            self.MI.append(nilai)

        print(nilai)
        print(self.MI,"\n\n")
        
    #method penyaring dan memperbaru dataset dengan treshold masukan oleh pengguna    
    # print('Proses Perhitungan Mi Selesai')
    
    
    def filtering(self,treshold):
        print('Proses Filtering Jalan')
        fitur = []
        MI_fitur=[]
        miData=[]
        for i in range (len(self.unique_word)):
            if(self.MI[i]>=treshold):
                fitur.append(self.unique_word[i])
                MI_fitur.append(self.MI[i])
                
        for i in range (len(self.listData)):
            value=''
            for j in range (len(self.listData[i])):
                for x in range (len(fitur)):
                    if(self.listData[i][j]==fitur[x]):
                        if(value == ''):
                            value = self.listData[i][j]
                        else:
                            value = value + '//' + self.listData[i][j]
            value = value.replace('//',' ')
            miData.append(value)    
        
         
        df_mi = {
            "tweet" : miData,
            "label" : self.dataframe['label']
        }

        df_mi = pd.DataFrame(df_mi)
        return(df_mi)
    