#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib as mpl 
import matplotlib.pyplot as plt
import os
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = stopwords.words('english')

os.getcwd()
os.chdir('C:/Users/ubaid.LAPTOP-60AEGHFJ/Desktop/Ait580')
os.getcwd()


# In[6]:


# open, read, and display the ABC News input file
ABCNews_textfile = open('FDACovidVaccineKids_ABCNEWS.txt', mode='r', encoding='utf-8')
ABCNews_CovidVaccine = ABCNews_textfile.read()
print(ABCNews_CovidVaccine)


# In[7]:


# open, read, and display the New York Times input file
NYTimes_textfile = open('CovidShotsForChildren_NYTimes.txt', mode='r', encoding='utf-8')
NYTimes_CovidShots = NYTimes_textfile.read()
print(NYTimes_CovidShots)


# In[5]:


# extract the words, convert all to lower case for ABCNews_textfile(ABCNews_CovidVaccine)
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(ABCNews_CovidVaccine.lower())
print(tokens)


# In[8]:


# extract the words, convert all to lower case for NYTimes_textfile(NYTimes_CovidShots)
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
NYTimes_tokens2 = tokenizer.tokenize(NYTimes_CovidShots.lower())
print(NYTimes_tokens2)


# In[10]:


# recreate token list without stopwords for ABCNews_textfile(ABCNews_CovidVaccine)
from nltk.corpus import stopwords
token = [token for token in token if token not in stopwords.words('english')]
print(token)


# In[3]:


# recreate token list without stopwords for NYTimes_textfile(NYTimes_CovidShots)
from nltk.corpus import stopwords
NYTimes_tokens2 = [token for token in NYTimes_tokens2 if token not in stopwords.words('english')]
print(NYTimes_tokens2)


# In[12]:


# display and graph the word frequncies, plus a few specific words 
freq_dist = nltk.FreqDist(tokens)
freq_dist
freq_dist['covid']
freq_dist['vaccine']
freq_dist['children']

print(freq_dist)
print(freq_dist.most_common(25))
freq_dist.plot(25)


# In[13]:


# display and graph the word frequncies, plus a few specific words 
freq_dist = nltk.FreqDist(NYTimes_tokens2)
freq_dist
freq_dist['covid']
freq_dist['vaccine']
freq_dist['children']

print(freq_dist)
print(freq_dist.most_common(25))
freq_dist.plot(25)

