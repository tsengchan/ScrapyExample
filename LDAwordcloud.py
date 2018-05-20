#complete code
import json

with open('result3.json') as json_data:
    data = json.load(json_data)
    print(data)


bag_words = []

#enumerate so can work with indices as integer instead of strings
for x, y in enumerate(data):
    for key, values in data[x].items(): #need inices here for x
        for value in values:
            bag_words.append(value)

#to bag_of_words matrix

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect.fit(bag_words)

#LDA clustering


vect = CountVectorizer(max_features=10000, max_df=.15)
X = vect.fit_transform(bag_words)

from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_topics=10, learning_method="batch",
max_iter=25, random_state=0)

document_topics = lda.fit_transform(X)

import numpy as np
import mglearn

sorting = np.argsort(lda.components_, axis=1)[:, ::-1]
# Get the feature names from the vectorizer
feature_names = np.array(vect.get_feature_names())

# Print out the 10 topics:
mglearn.tools.print_topics(topics=range(10), feature_names=feature_names,
sorting=sorting, topics_per_chunk=5, n_words=10)


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

word_string = " ".join(bag_words)

wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                      max_words=1000
                         ).generate(word_string)
plt.clf()
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('plot.png', dpi = 100)
plt.show()
