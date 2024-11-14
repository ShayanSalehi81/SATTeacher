import csv
import torch
import joblib
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

preprocessed_data = joblib.load("./embedded_questions.joblib")
answer_path = "./SATCorpus_persian.csv"

tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")
embedding_model = AutoModel.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")

def generate_embedding(sentence):
    tokens = tokenizer.tokenize(sentence)
    input_ids = torch.tensor([tokenizer.convert_tokens_to_ids(tokens)])

    with torch.no_grad():
        outputs = embedding_model(input_ids)
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze()

    return embedding.tolist()

def find_most_similar_row(input_sentence, preprocessed_csv_data):
    input_embedding = generate_embedding(input_sentence)

    max_similarity = float('-inf')
    best_row_idx = -1

    for idx, row in enumerate(preprocessed_csv_data):
        for sent_embedding in row:
          similarity = cosine_similarity([input_embedding], [sent_embedding])[0][0]
          if similarity > max_similarity:
              max_similarity = similarity
              best_row_idx = idx

    return best_row_idx

def find_answer(csv_path, row_idx):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            if idx == row_idx:
                return row[1]

def get_answer(input_sentence):
    row_index = find_most_similar_row(input_sentence, preprocessed_data)
    return find_answer(answer_path, row_index)

input_sentences = [
    'تو کیستی؟',
    'تمرین سوم',
    'تمرین هفت چیست؟',
    'تکلیف درس چهارم را بگو',
    'راجب درس ۵ توضیح بده',
    'چگونه با کودک می‌توانم ارتباط بگیرم؟',
    'سلام',
    'چرا باید با صدای بلند با کودک صبحت کنم؟',
    'چرا باید به طبیعت دلبست؟'
]
for tmp_sentence in input_sentences:
    print(get_answer(tmp_sentence))