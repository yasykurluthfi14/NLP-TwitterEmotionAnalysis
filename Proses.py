import pathlib
import pandas as pd
from sklearn import svm
import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from MutualInformation import MutualInformation
import string
import re
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import numpy as np
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.model_selection import KFold
import time
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import swifter
import ast
import nltk
nltk.download('stopwords')

  

class Proses:
    
    dataset = None
    model = None
    listData = []

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    term_dict = {}

    
    def input_data(self, path):
        
        file = pathlib.Path(path)
        if file.exists():
            self.dataset = pd.read_excel(path)
        else:
            print('Path error : tidak ada data pada path ->',path)

# --------------Tokenizing ---------------
    def remove_tweet_special(self, text):
    # remove tab, new line, ans back slice
        text = text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\',"")
    # remove non ASCII (emoticon, chinese word, .etc)
        text = text.encode('ascii', 'replace').decode('ascii')
    # remove mention, link, hashtag
        text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)"," ", text).split())
    # remove incomplete URL
        return text.replace("http://", " ").replace("https://", " ")
    
    def remove_username(self, text):
    # menghilangkan tanda [USERNAME]
        processed_text = text.replace('username', '')
        return processed_text

    def remove_number(self, text):
        return  re.sub(r"\d+", "", text)

    def remove_punctuation(self, text):
        return text.translate(str.maketrans("","",string.punctuation))

    def remove_whitespace_LT(self, text):
        return text.strip()

    def remove_whitespace_multiple(self, text):
        return re.sub('\s+',' ',text)

    def remove_singl_char(self, text):
        return re.sub(r"\b[a-zA-Z]\b", "", text)    

    def word_tokenize_wrapper(self, text):
        return word_tokenize(text)

  #----------------End Tokenizing---------------------      
    
    def stopwords_removal(self, words):
        list_stopwords = stopwords.words('indonesian')
        list_stopwords.extend(["yg", "dg", "rt", "dgn", "ny", "d", 'klo', 
                       'kalo', 'amp', 'biar', 'bikin', 'bilang', 
                       'gak', 'ga', 'krn', 'nya', 'nih', 'sih', 
                       'si', 'tau', 'tdk', 'tuh', 'utk', 'ya', 
                       'jd', 'jgn', 'sdh', 'aja', 'n', 't', 
                       'nyg', 'hehe', 'pen', 'u', 'nan', 'loh', 'rt',
                       '&amp', 'yah'])
        list_stopwords = set(list_stopwords)
        return [word for word in words if word not in list_stopwords]

    def normalized_term(self, document):
        normalizad_word = pd.read_excel("Asset/normalisasi.xlsx")

        normalizad_word_dict = {}

        for index, row in normalizad_word.iterrows():
            if row[0] not in normalizad_word_dict:
                normalizad_word_dict[row[0]] = row[1] 

        return [normalizad_word_dict[term] if term in normalizad_word_dict else term for term in document]  

    def stemmed_wrapper(self, term):
        return self.stemmer.stem(term)

    def get_stemmed_term(self, document):
        term_list = self.term_dict
        return [term_list[term] for term in document]

              

    def praprosses_data(self):
        if self.dataset is not None:
            print('Running Preprocessing...')
            data_pc = self.dataset
            tokenizing_remove = self.remove_tweet_special
            remove_username = self.remove_username
            remove_number = self.remove_number
            remove_punctuation = self.remove_punctuation
            remove_whitespace_LT = self.remove_whitespace_LT
            remove_whitespace_multiple = self.remove_whitespace_multiple
            remove_singl_char = self.remove_singl_char
            tokenizing = self.word_tokenize_wrapper
            data_stopwords = self.stopwords_removal  
            normalized = self.normalized_term
            term_list = self.term_dict
            stem_wrapper = self.stemmed_wrapper
            get_stem = self.get_stemmed_term


            print('Self Dataset Selesai')

            data_pc['tweet'] = data_pc['tweet'].str.lower()
            print('Case Folding Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(lambda text: re.sub('@[^\s]+', '', text))
            
            data_pc['tweet'] = data_pc['tweet'].apply(lambda text: re.sub(r'#([^\s]+)', '', text))
            

            data_pc['tweet'] = data_pc['tweet'].apply(lambda text: re.sub(r"[^a-zA-Z0-9]+", ' ', text))
            print('Noise Removal 1 Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(lambda text: re.sub(r'(.)\1{2,}', r'\1', text))    
            print('Noise Removal 2 Selesai')  

            data_pc['tweet'] = data_pc['tweet'].apply(remove_username)
            

            # ------------------Proses Tokenizing ------------------

            data_pc['tweet'] = data_pc['tweet'].apply(tokenizing_remove)
            print('Remove Special Character Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(remove_number)
            print('Remove Number Selesai')
            
            data_pc['tweet'] = data_pc['tweet'].apply(remove_punctuation)
            print('Remove Punctuation Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(remove_whitespace_LT)
            data_pc['tweet'] = data_pc['tweet'].apply(remove_whitespace_multiple)
            print('Remove Whitespace Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(remove_singl_char)

            data_pc['tweet'] = data_pc['tweet'].apply(tokenizing)
            print('Tokenizing Selesai')

            #------------------ End Proses Tokenizing -------------------

            # data_pc['tweet'] = data_pc['tweet'].apply(normalized)
            # print('Normalized Selesai') 


            # data_pc['tweet'] = data_pc['tweet'].apply(data_stopwords)
            # print('Stopword Removal Selesai')
         
      

            # for document in data_pc['tweet']:
            #     for term in document:
            #         if term not in term_list:
            #             term_list[term] = ' '

            # print(len(term_list))
            # print("-------------------------------------")

            # for term in term_list:
            #     term_list[term] = stem_wrapper(term)
            #     print(term,":" ,term_list[term])
    
            # print(term_list)
            # print("------------------------")

            # data_pc['tweet'] = data_pc['tweet'].swifter.apply(get_stem)
            # print('Stemming Selesai')

            data_pc['tweet'] = data_pc['tweet'].apply(' ' .join)

            data_pc.to_excel("Asset/datahasilPreprocessing.xlsx")
            print('Data Berhasil Disimpan !!')  

        return data_pc
           
    def tanpa_feature_selection(self):
        if self.dataset is not None:
            dataframe = self.dataset.copy()
            return dataframe
            
        else:
            print('Proses error : dataset tidak terdeteksi') 
         
            
    def feature_selectionMI(self,treshold):
        if self.dataset is not None:
            dataframe = self.dataset.copy()
            mutualInformation= MutualInformation(dataframe)
            mutualInformation.process()
            print('Proses Perhitungan MI Selesai')
            return mutualInformation.filtering(treshold)
        else:
            print('Proses error : dataset tidak terdeteksi')
            
    def get_dataset(self):
        return self.dataset
    
    def get_total_feature(self,dataset):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(dataset['tweet'].astype('U').values)
        return X.shape[1]

    def join_text_list(self,texts):
        texts = ast.literal_eval(str(texts))
        return ' '.join([text for text in texts])
    
    def classify(self,dataset,kernel_clf,c_clf):
        print(dataset)
        print(kernel_clf)
        print(c_clf)

        dataset = dataset.sample(frac=1).reset_index(drop=True)
        vectorizer = TfidfVectorizer(use_idf=True)

        X = vectorizer.fit_transform(dataset['tweet'].astype('U').values)
        Y = dataset['label']
        SVM = OneVsOneClassifier(svm.SVC(C=c_clf,kernel=kernel_clf))
        scores = []
        scores.append(['Uji ke','TP','FP','TN','FN','Akurasi','Precision','Recall','F-Measure','Waktu Komputasi'])
        cv = KFold(n_splits=10)
        index_hasil = 1

        for train_index, test_index in cv.split(X):
            X_train, X_test, Y_train, Y_test = X[train_index], X[test_index], Y[train_index], Y[test_index]
            start_time = time.time()
            SVM.fit(X_train,Y_train) #training
            Y_pred = SVM.predict(X_test) #test
            Cm = confusion_matrix(Y_test, Y_pred)
            print(Cm)
            Tp = (Cm[1][1])
            Fn = (Cm[1][0])
            Fp = (Cm[0][1])   
            Tn = (Cm[0][0])
            acc = round(accuracy_score(Y_test,Y_pred),2)
            prec = round(precision_score(Y_test,Y_pred, average = 'macro'),2)
            rec = round(recall_score(Y_test,Y_pred, average = 'macro'),2)
            f1 = round(f1_score(Y_test,Y_pred, average = 'macro'),2)
            #f1 = f1_score(Y_test,Y_pred)
            execution_time = round((time.time() - start_time),2)
            scores.append([index_hasil,Tp,Fp,Tn,Fn,acc,prec,rec,f1,execution_time])
            index_hasil +=1
            
        temp = ['Rata-rata', ' ',' ',' ',' ',0,0,0,0,0]
        for i in range(1,11):
            for j in range(5,10):
                temp[j] += scores[i][j]
        
        for i in range(5,10):
            temp[i] = round((temp[i]/10),2)
                
        scores.append(temp)
        print(scores)

        self.model = SVM
        return scores
    
    

    def predicttanpaseleksifitur(self,text):
        datas = pd.Series(data = [text])
        tokenizing_remove = self.remove_tweet_special
        remove_username = self.remove_username
        remove_number = self.remove_number
        remove_punctuation = self.remove_punctuation
        remove_whitespace_LT = self.remove_whitespace_LT
        remove_whitespace_multiple = self.remove_whitespace_multiple
        remove_singl_char = self.remove_singl_char
        tokenizing = self.word_tokenize_wrapper
        # data_stopwords = self.stopwords_removal  
        # normalized = self.normalized_term
        # term_list = self.term_dict
        # stem_wrapper = self.stemmed_wrapper
        # get_stem = self.get_stemmed_term


        datas = datas.str.lower()
        datas = datas.apply(lambda text: re.sub('@[^\s]+', '', text))       
        datas = datas.apply(lambda text: re.sub(r'#([^\s]+)', '', text))
        datas = datas.apply(lambda text: re.sub(r"[^a-zA-Z0-9]+", ' ', text))
        datas = datas.apply(lambda text: re.sub(r'(.)\1{2,}', r'\1', text))    
    
        datas = datas.apply(remove_username)
            

            # ------------------Proses Tokenizing ------------------

        datas = datas.apply(tokenizing_remove)
        datas = datas.apply(remove_number)
        datas = datas.apply(remove_punctuation)
        datas = datas.apply(remove_whitespace_LT)
        datas = datas.apply(remove_whitespace_multiple)
        datas = datas.apply(remove_singl_char)
        datas = datas.apply(tokenizing)
        
        #------------------ End Proses Tokenizing -------------------
        # datas = datas.apply(normalized)
       
        # datas = datas.apply(data_stopwords)
      
        
    
        # for document in datas:
        #     for term in document:
        #         if term not in term_list:
        #             term_list[term] = ' '
        # print(len(term_list))
        # print("-------------------------------------")
        # for term in term_list:
        #     term_list[term] = stem_wrapper(term)
        #     print(term,":" ,term_list[term])

        # print(term_list)
        # print("------------------------")
        # datas = datas.swifter.apply(get_stem)
    
        datas = datas.apply(' ' .join)
        
        
        vectorizer = TfidfVectorizer(use_idf=True)
        
        TF_IDF = vectorizer.fit(self.dataset['tweet'].astype('U').values)
        datas = TF_IDF.transform(datas.astype('U').values)
        
        prediction = self.model.predict(datas)
        print(prediction)
        if prediction == 'anger':
            return "Emosi Anger"
        elif prediction == 'happy':
            return "Emosi Happy"
        elif prediction == 'fear':
            return "Emosi Fear"
        elif prediction == 'love':
            return "Emosi love"     
        else :
            return "Emosi Sadness"
    
   
             
    def predictseleksifiturMI(self,text):
        datas = pd.Series(data = [text])
        tokenizing_remove = self.remove_tweet_special
        remove_username = self.remove_username
        remove_number = self.remove_number
        remove_punctuation = self.remove_punctuation
        remove_whitespace_LT = self.remove_whitespace_LT
        remove_whitespace_multiple = self.remove_whitespace_multiple
        remove_singl_char = self.remove_singl_char
        tokenizing = self.word_tokenize_wrapper
        data_stopwords = self.stopwords_removal  
        normalized = self.normalized_term
        term_list = self.term_dict
        stem_wrapper = self.stemmed_wrapper
        get_stem = self.get_stemmed_term


        datas = datas.str.lower()
        datas = datas.apply(lambda text: re.sub('@[^\s]+', '', text))       
        datas = datas.apply(lambda text: re.sub(r'#([^\s]+)', '', text))
        datas = datas.apply(lambda text: re.sub(r"[^a-zA-Z0-9]+", ' ', text))
        datas = datas.apply(lambda text: re.sub(r'(.)\1{2,}', r'\1', text))    
    
        datas = datas.apply(remove_username)
            

            # ------------------Proses Tokenizing ------------------

        datas = datas.apply(tokenizing_remove)
        datas = datas.apply(remove_number)
        datas = datas.apply(remove_punctuation)
        datas = datas.apply(remove_whitespace_LT)
        datas = datas.apply(remove_whitespace_multiple)
        datas = datas.apply(remove_singl_char)
        datas = datas.apply(tokenizing)
        
        #------------------ End Proses Tokenizing -------------------
        datas = datas.apply(normalized)
       
        datas = datas.apply(data_stopwords)
      
        
    
        for document in datas:
            for term in document:
                if term not in term_list:
                    term_list[term] = ' '
        print(len(term_list))
        print("-------------------------------------")
        for term in term_list:
            term_list[term] = stem_wrapper(term)
            print(term,":" ,term_list[term])

        print(term_list)
        print("------------------------")
        datas = datas.swifter.apply(get_stem)
    
        datas = datas.apply(' ' .join)
        
                
                
        vectorizer = TfidfVectorizer(use_idf=True)
        read=pd.read_excel('Asset/datasethasilMI.xlsx')
        TF_IDF = vectorizer.fit(read['tweet'].astype('U').values)
        datas = TF_IDF.transform(datas.astype('U').values)
        
        prediction = self.model.predict(datas)
        print(prediction)
                
        if prediction == 'anger':
            return "Emosi Anger"
        elif prediction == 'happy':
            return "Emosi Happy"
        elif prediction == 'fear':
            return "Emosi Fear"
        elif prediction == 'love':
            return "Emosi love"     
        else :
            return "Emosi Sadness"
        
        
       

    