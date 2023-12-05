import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar dados do FCID e do FoodDB (Configurar o ambiente para estar na raíz do repositório.)
fcid_data = pd.read_csv('bases/fcid/FCID_Code_Description.csv')
fooddb_data = pd.read_csv('bases/foodb/Food.csv')

# Pré-processamento: converter todos os nomes para minúsculas
fcid_data['processed'] = fcid_data['FCID_Desc'].str.lower()
fooddb_data['processed'] = fooddb_data['name'].str.lower()

# Usar TF-IDF para converter os nomes em vetores
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(fcid_data['processed'].tolist() + fooddb_data['processed'].tolist())

# Calcular a similaridade de cosseno
cosine_sim = cosine_similarity(tfidf_matrix[:len(fcid_data)], tfidf_matrix[len(fcid_data):])

# Encontrar a melhor correspondência para cada alimento do FCID
matches = []
for idx, row in enumerate(cosine_sim):
    best_match_idx = row.argmax()
    fcid_food = fcid_data.iloc[idx]['FCID_Desc']
    fooddb_food = fooddb_data.iloc[best_match_idx]['name']
    matches.append((fcid_food, fooddb_food))

# Criar um DataFrame com as correspondências
matches_df = pd.DataFrame(matches, columns=['FCID_Food', 'FoodDB_Food'])

# Salvar o DataFrame em um arquivo CSV
matches_df.to_csv('bases/relação/food_matches.csv', index=False)
