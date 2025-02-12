from flask import Flask, jsonify
app = Flask(__name__)

#primeira rota Retorna um resumo dos dados do Facebook, incluindo o total de cliques, gastos e o custo por clique.

# Dados de exemplo (substitua por dados reais da API)
dados_facebook = [
    {"nome_anuncio": "Promoção de Verão", "cliques": 100, "gastos": 50},
    {"nome_anuncio": "Liquidação de Inverno", "cliques": 150, "gastos": 75},
]
# segunda rota Retorna um resumo dos dados do YouTube, incluindo o total de cliques, gastos e o custo por clique
dados_youtube = [
    {"nome_anuncio": "Nova Coleção", "cliques": 50, "gastos": 25},
    {"nome_anuncio": "Oferta Especial", "cliques": 75, "gastos": 37.50},
]

# Funções para calcular totais  terceira retorna todos os dados do Facebook e YouTube
def calcular_total_cliques(dados):
    return sum(anuncio["cliques"] for anuncio in dados)

def calcular_total_gastos(dados):
    return sum(anuncio["gastos"] for anuncio in dados)

def calcular_custo_por_clique(gastos, cliques):
    if cliques > 0:
        return gastos / cliques
    return 0

# 4 Rota Retorna um resumo geral dos dados do Facebook e YouTube
@app.route("/facebook/resumo")
def resumo_facebook():
    total_cliques = calcular_total_cliques(dados_facebook)
    total_gastos = calcular_total_gastos(dados_facebook)
    custo_por_clique = calcular_custo_por_clique(total_gastos, total_cliques)
    return jsonify({
        "plataforma": "Facebook",
        "cliques": total_cliques,
        "gastos": total_gastos,
        "custo_por_clique": custo_por_clique,
    })

@app.route("/youtube/resumo")
def resumo_youtube():
    total_cliques = calcular_total_cliques(dados_youtube)
    total_gastos = calcular_total_gastos(dados_youtube)
    custo_por_clique = calcular_custo_por_clique(total_gastos, total_cliques)
    return jsonify({
        "plataforma": "YouTube",
        "cliques": total_cliques,
        "gastos": total_gastos,
        "custo_por_clique": custo_por_clique,
    })

@app.route("/geral")
def geral():
    # Adiciona o custo por clique aos dados
    for anuncio in dados_facebook:
        anuncio["custo_por_clique"] = calcular_custo_por_clique(anuncio["gastos"], anuncio["cliques"])
    for anuncio in dados_youtube:
        anuncio["custo_por_clique"] = calcular_custo_por_clique(anuncio["gastos"], anuncio["cliques"])
    return jsonify({"facebook": dados_facebook, "youtube": dados_youtube})

@app.route("/geral/resumo")
def resumo_geral():
    total_cliques_facebook = calcular_total_cliques(dados_facebook)
    total_gastos_facebook = calcular_total_gastos(dados_facebook)
    custo_por_clique_facebook = calcular_custo_por_clique(total_gastos_facebook, total_cliques_facebook)

    total_cliques_youtube = calcular_total_cliques(dados_youtube)
    total_gastos_youtube = calcular_total_gastos(dados_youtube)
    custo_por_clique_youtube = calcular_custo_por_clique(total_gastos_youtube, total_cliques_youtube)

    return jsonify({
        "facebook": {
            "cliques": total_cliques_facebook,
            "gastos": total_gastos_facebook,
            "custo_por_clique": custo_por_clique_facebook,
        },
        "youtube": {
            "cliques": total_cliques_youtube,
            "gastos": total_gastos_youtube,
            "custo_por_clique": custo_por_clique_youtube,
        },
    })

if __name__ == "__main__":
    app.run(debug=True)