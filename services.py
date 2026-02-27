from data import carregar_despesas, salvar_despesas
from datetime import datetime

class Despesa:
    def __init__(self, descricao, categoria, valor, data=None):
        self.descricao = descricao
        self.categoria = categoria  # ex: 'Alimentação', 'Transporte', 'Lazer'
        self.valor = float(valor)
        # Data atual se não passar
        self.data = data if data else datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'descricao': self.descricao,
            'categoria': self.categoria,
            'valor': self.valor,
            'data': self.data
        }

    def __str__(self):
        return f"{self.data} | {self.categoria} | {self.descricao} | R$ {self.valor:.2f}"

def adicionar_despesa(descricao, categoria, valor):
    despesas = [Despesa(**d) for d in carregar_despesas()]  # Converte dicts pra objetos
    nova = Despesa(descricao, categoria, valor)
    despesas.append(nova)
    # Salva como lista de dicts
    salvar_despesas([d.to_dict() for d in despesas])
    print(f"Despesa adicionada: {nova}")

def listar_despesas():
    dados = carregar_despesas()
    if not dados:
        print("Nenhuma despesa cadastrada ainda.")
        return
    total = 0
    print("\n=== Suas Despesas ===")
    for i, d in enumerate(dados, 1):
        desp = Despesa(**d)
        print(f"{i}. {desp}")
        total += desp.valor
    print(f"\nTotal gasto: R$ {total:.2f}")

def total_por_categoria():
    dados = carregar_despesas()
    if not dados:
        print("Sem despesas.")
        return
    categorias = {}
    for d in dados:
        cat = d['categoria']
        categorias[cat] = categorias.get(cat, 0) + d['valor']
    print("\n=== Gastos por Categoria ===")
    for cat, valor in sorted(categorias.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat}: R$ {valor:.2f}")

# Pode adicionar mais: deletar, editar, filtrar por data, etc.