import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')
def remove_stop_words(string):
    stop_words = set(stopwords.words())
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    new_string = ' '.join(filtered_words)
    return new_string
def freq(str):
  # break the string into list of words
  str_list = str.split()
 
  # create an empty dictionary
  frequency = {}
 
  # count frequency of each word
  for word in str_list:
      frequency[word] = frequency.setdefault(word, 0) + 1
 
  # print the frequency of each word
  for key, value in frequency.items():
      print(key, ':', value)
with open('paragraphs.txt','r') as file:
    # Read the contents of the file
    file_contents = file.read()
newText =  str(remove_stop_words(file_contents))

freq(newText)     