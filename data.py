import json

ARQUIVO = 'despesas.json'

def carregar_despesas():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Lista vazia se não existir
    except Exception as e:
        print(f"Erro ao carregar despesas: {e}")
        return []

def salvar_despesas(despesas):
    try:
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(despesas, f, ensure_ascii=False, indent=4)
        print("Despesas salvas com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar: {e}")