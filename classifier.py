import pickle
import numpy as np

with open('models/Consumo_Energetico_PorIAeDATACenter.pkl', 'rb') as f:
    modelo = pickle.load(f)

def fazer_predicao(capacidade_mw, eficiencia_energetica, sistema_resfriamento, eficiencia_agua, consumo_agua_galoes):
    dados = np.array([[capacidade_mw, eficiencia_energetica, sistema_resfriamento, eficiencia_agua, consumo_agua_galoes]])
    predicao = modelo.predict(dados)
    return round(predicao[0], 2)