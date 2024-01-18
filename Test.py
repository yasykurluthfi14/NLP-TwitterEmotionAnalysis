import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.feature_selection import mutual_info_classif
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import multilabel_confusion_matrix
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('Asset/data.xlsx')

# Preprocessing
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def preprocess(text):
    text = re.sub(r'http\S+', '', text) # remove URLs
    text = re.sub('@[^\s]+', '', text) # remove usernames
    text = text.lower() # convert to lowercase
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove punctuations
    text = re.sub('\w*\d\w*', '', text) # remove digits
    text = re.sub('[‘’“”…]', '', text) # remove special characters
    text = text.strip() # remove leading/trailing whitespaces
    tokens = nltk.word_tokenize(text) # tokenize
    tokens = [token for token in tokens if token not in stopwords.words('english')] # remove stopwords
    lemmatizer = WordNetLemmatizer() 
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # lemmatize
    return ' '.join(tokens)

df['tweet'] = df['tweet'].apply(preprocess)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['tweet'], df.drop('tweet', axis=1).values, test_size=0.2, random_state=42)

# TF-IDF
vectorizer = TfidfVectorizer(token_pattern=r'\b\w+\b')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Compute mutual information scores
mi_scores = mutual_info_classif(X_train_tfidf, y_train)
print(mi_scores)

# Sort MI scores for each label
sorted_mi_scores = np.argsort(mi_scores)[::-1]
print(sorted_mi_scores)

# # Plot top MI scores for each label
# n_labels = y_train.shape[1]
# fig, axs = plt.subplots(n_labels, 1, figsize=(10, 20))
# for i in range(n_labels):
#     top_k = 20  # show top 20 MI scores for each label
#     axs[i].bar(range(top_k), mi_scores[sorted_mi_scores[:top_k], i][::-1])
#     axs[i].set_title('Top MI scores for label {}'.format(i))
#     axs[i].set_yticks(range(top_k))
#     axs[i].set_yticklabels(vectorizer.get_feature_names_out()[sorted_mi_scores[:top_k]][::-1])
# plt.tight_layout()

# # Train model
# clf = OneVsRestClassifier(LinearSVC(random_state=42))
# clf.fit(X_train_tfidf, y_train)

# # Predict
# y_pred = clf.predict(X_test_tfidf)

# # Evaluate
# confusion_matrix = multilabel_confusion_matrix(y_test, y_pred)
# print(confusion_matrix)