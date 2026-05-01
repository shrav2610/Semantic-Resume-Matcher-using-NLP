<<<<<<< HEAD
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    emb1 = model.encode([text1])[0]
    emb2 = model.encode([text2])[0]

=======
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    emb1 = model.encode([text1])[0]
    emb2 = model.encode([text2])[0]

>>>>>>> 02572dc4207c60c45eac41d52f36227373f10187
    return cosine_similarity([emb1], [emb2])[0][0]