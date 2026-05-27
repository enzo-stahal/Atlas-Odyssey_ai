nome_missao = "Atlas Odyssey"
nome_equipe = "Orbit Engineers"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"

    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"

    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"

    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):

    if valor < 30:
        return "CRÍTICO", 2, "Comunicação crítica"

    elif valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"

    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):

    if valor < 20:
        return "CRÍTICO", 2, "Bateria crítica"

    elif valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"

    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):

    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio crítico"

    elif valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"

    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):

    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade crítica"

    elif valor <= 69:
        return "ATENÇÃO", 1, "Estabilidade reduzida"

    else:
        return "NORMAL", 0, "Estabilidade adequada"


def classificar_ciclo(pontos):

    if pontos <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontos <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(primeiro, ultimo):

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável."


def gerar_recomendacao(
    status_temperatura,
    status_comunicacao,
    status_bateria,
    status_oxigenio,
    status_estabilidade
):

    recomendacoes = []

    
    if status_temperatura == "CRÍTICO":
        recomendacoes.append(
            "Verificar controle térmico da missão."
        )

    elif status_temperatura == "ATENÇÃO":
        recomendacoes.append(
            "Monitorar aumento de temperatura."
        )

    
    if status_comunicacao == "CRÍTICO":
        recomendacoes.append(
            "Tentar restabelecer contato com a base."
        )

    elif status_comunicacao == "ATENÇÃO":
        recomendacoes.append(
            "Monitorar estabilidade da comunicação."
        )

    
    if status_bateria == "CRÍTICO":
        recomendacoes.append(
            "Ativar modo de economia de energia."
        )

    elif status_bateria == "ATENÇÃO":
        recomendacoes.append(
            "Reduzir consumo energético."
        )

    
    if status_oxigenio == "CRÍTICO":
        recomendacoes.append(
            "Acionar protocolo de suporte à vida."
        )

    elif status_oxigenio == "ATENÇÃO":
        recomendacoes.append(
            "Monitorar níveis de oxigênio."
        )

    
    if status_estabilidade == "CRÍTICO":
        recomendacoes.append(
            "Reduzir operações não essenciais."
        )

    elif status_estabilidade == "ATENÇÃO":
        recomendacoes.append(
            "Revisar estabilidade operacional."
        )

    
    if len(recomendacoes) == 0:
        return "Manter operação normal e continuar monitoramento."

    return " | ".join(recomendacoes)



print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos: {len(dados_missao)}")

print("=" * 60)

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

for i, ciclo in enumerate(dados_missao):

    print(f"\nCICLO {i + 1}")
    print("-" * 50)

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    analises = [
        analisar_temperatura(temperatura),
        analisar_comunicacao(comunicacao),
        analisar_bateria(bateria),
        analisar_oxigenio(oxigenio),
        analisar_estabilidade(estabilidade)
    ]

    nomes = [
        "Temperatura",
        "Comunicação",
        "Bateria",
        "Oxigênio",
        "Estabilidade"
    ]

    valores = [
        temperatura,
        comunicacao,
        bateria,
        oxigenio,
        estabilidade
    ]

    unidades = ["°C", "%", "%", "%", "%"]

    risco_total = 0

    for j in range(5):

        status, pontos, mensagem = analises[j]

        risco_total += pontos
        pontuacao_areas[j] += pontos

        print(
            f"{nomes[j]}: "
            f"{valores[j]}{unidades[j]} | "
            f"{status} | "
            f"{mensagem}"
        )

    classificacao = classificar_ciclo(risco_total)

    status_temperatura = analises[0][0]
    status_comunicacao = analises[1][0]
    status_bateria = analises[2][0]
    status_oxigenio = analises[3][0]
    status_estabilidade = analises[4][0]

    recomendacao = gerar_recomendacao(
        status_temperatura,
        status_comunicacao,
        status_bateria,
        status_oxigenio,
        status_estabilidade
    )

    print(f"\nPontuação de risco: {risco_total}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")

    riscos_ciclos.append(risco_total)


print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

media_temperatura = sum([c[0] for c in dados_missao]) / len(dados_missao)
media_comunicacao = sum([c[1] for c in dados_missao]) / len(dados_missao)
media_bateria = sum([c[2] for c in dados_missao]) / len(dados_missao)
media_oxigenio = sum([c[3] for c in dados_missao]) / len(dados_missao)
media_estabilidade = sum([c[4] for c in dados_missao]) / len(dados_missao)

print(f"Média temperatura: {media_temperatura:.2f} °C")
print(f"Média comunicação: {media_comunicacao:.2f}%")
print(f"Média bateria: {media_bateria:.2f}%")
print(f"Média oxigênio: {media_oxigenio:.2f}%")
print(f"Média estabilidade: {media_estabilidade:.2f}%")

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
print(f"Maior risco: {maior_risco}")

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

print(f"Risco médio: {risco_medio:.2f}")

ciclos_criticos = 0

for risco in riscos_ciclos:

    if risco >= 6:
        ciclos_criticos += 1

print(f"Ciclos críticos: {ciclos_criticos}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1]))

print("\nPontuação por área:")

for i in range(len(areas_monitoradas)):

    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

maior_area = max(pontuacao_areas)
indice_area = pontuacao_areas.index(maior_area)

print("\nÁrea mais afetada:")
print(areas_monitoradas[indice_area])

classificacao_final = classificar_ciclo(int(risco_medio))

print("\nClassificação final:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão operou dentro dos parâmetros esperados.")

elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidades moderadas.")

else:
    print("A missão apresentou risco operacional elevado.")
