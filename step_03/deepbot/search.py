from tqdm import tqdm
from konlpy.tag import Okt
tagger = Okt()


f = open("__data__.txt", 'r')
lines = f.readlines()

match_key = "님 : "
setences = []

for line in tqdm(lines):
  if(match_key in line):
    line = line[line.index(match_key)+4:]
    line = line.replace("\n", ".")
    setences.append(line)

f.close()


from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


stop_words = ""

tfidf = TfidfVectorizer(stop_words=stop_words.split(' '))
matrix = tfidf.fit_transform(setences)


def search_engine(title):
    setences.append(title)
    matrix = tfidf.fit_transform(setences)

    from sklearn.metrics.pairwise import linear_kernel
    cosine_sim = linear_kernel(matrix, matrix)

    indices = {v: k for k, v in enumerate(setences)}

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]

    sentence_indices = [i[0] for i in sim_scores]
    setences.remove(title)
    return [setences[sentence_indices[1]],setences[sentence_indices[2]]]
