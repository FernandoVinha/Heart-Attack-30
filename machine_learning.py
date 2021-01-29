import pandas as pd
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

data = pd.read_csv('/home/ec2-user/Heart-Attack-30/cardio_train.csv')

#Separando as variáveis entre preditoras e variável alvo 
y = data['cardio'] 
x = data.drop('cardio', axis = 1)

#criando os conjuntos de dados de treino e teste: 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
#Criação do modelo: 
modelo = ExtraTreesClassifier(n_estimatore=100) 
modelo.fit(x_treino, y_treino)
#Imprimindo resultados: 
precisao = modelo.score(x_teste, y_teste) 
print("Precisão:", precisao)
