import openai
import ast
import torch.nn.functional as F
openai.api_key = ""
def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input = text
    )
    return response["data"][0]["embedding"]

def cosine_similarity(vector_a, vector_b):

    similarity = F.cosine_similarity(vector_a, vector_b, dim=0)

    return similarity

def find_genre(text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant who understand the intent of the user's question."},
            {"role": "user", "content": f"Which genre does the sentence below belong to:'Adventure', 'Fantasy', 'Animation', 'Drama', 'Horror', 'Action', 'Comedy', 'History', 'Western', 'Thriller', 'Crime', 'Documentary', 'SF', 'Mystery', 'Music', 'Romance', 'Family', 'War', 'TV Movie'. give me top 3 genre name in order of highest probability by [genre1,genre2,genre3] i don't need reason please give me only list \n context : {text}' \n"},
            # {"role": "assistant", "content": "i need [] only list or empty list output no sentence"}
        ]
    )


    return completion['choices'][0]['message']['content']


def to_list(string):
    start = None
    end = None
    for i in range(len(string)):
        if string[i] == '[':
            start = i
        elif string[i] == ']':
            end = i
            break
    if start == None:
        return []
    else:
        print(string[start+1:end].split(","))
        return string[start+1:end].split(",")
