import streamlit as st

# ------- FUNÇÃO: CRITÉRIOS ESPECÍFICOS DA FILA/ESPECIALIDADE -------
def buscar_criterios(especialidade):
    esp = especialidade.lower()
    # Ajuste com os critérios reais de cada Nota Técnica
    if "oncologia" in esp:
        return {
            "fila": "Oncologia",
            "nota_num": "16/2024",
            "nota_nome": "Nota Técnica 16/2024 - Oncologia Clínica",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios": [
                "Presença de diagnóstico histopatológico confirmado.",
                "Encaminhamento com laudos e informações clínicas completas.",
                "Classificação de risco segundo a nota técnica."
            ],
            "cores": {
                "Vermelho": "Critérios de prioridade máxima (conforme Nota Técnica 16/2024): [Exemplo: compressão de medula, sangramento ativo, obstrução iminente].",
                "Amarelo": "Prioridade intermediária (conforme Nota Técnica 16/2024): [Exemplo: doença localmente avançada sem sinais críticos, necessidade de início rápido do tratamento].",
                "Verde": "Prioridade baixa (conforme Nota Técnica 16/2024): [Exemplo: paciente estável aguardando segmento, ausência de urgência]."
            }
        }
    elif "cardio" in esp:
        return {
            "fila": "Cardiologia",
            "nota_num": "08/2023",
            "nota_nome": "Nota Técnica 08/2023 - Cardiologia",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios": [
                "Encaminhamento com Eletrocardiograma e exames complementares.",
                "Descrição dos sintomas e classificação de risco.",
                "Atendimento conforme protocolos clínicos da especialidade."
            ],
            "cores": {
                "Vermelho": "Prioridade máxima (Nota Técnica 08/2023): situações agudas/instáveis, ex: dor torácica aguda, insuficiência cardíaca descompensada.",
                "Amarelo": "Prioridade intermediária (Nota Técnica 08/2023): sintomas controlados ou exames alterados sem instabilidade.",
                "Verde": "Prioridade baixa (Nota Técnica 08/2023): pacientes estáveis para acompanhamento e segmento ambulatorial."
            }
        }
    else:
        return {
            "fila": especialidade,
            "nota_num": "--",
            "nota_nome": "Nota Técnica não localizada",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios": [
                "Não foi possível identificar critérios específicos. Consulte manualmente a nota técnica da especialidade."
            ],
            "cores": {
                "Vermelho": "-",
                "Amarelo": "-",
                "Verde": "-"
            }
        }

# ------- FUNÇÃO: ANÁLISE E JUSTIFICATIVA -------
def analisar_pedido(resumo, criterios):
    resumo_lower = resumo.lower()
    criterios_ = criterios["criterios"]

    # Simulação de lógica — ADAPTE conforme realidade/nota técnica!
    if not resumo.strip():
        apto, justificativa = False, "Solicito complementação do descritivo/laudos para avaliação."
        status = "Insuficiência de Informações"
        redirecionamento = ""
    elif "não atende" in resumo_lower:
        apto, justificativa = False, f"Solicitação não atende aos critérios da Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}. Descrever critérios não atendidos objetivamente."
        status = "Não Apto"
        redirecionamento = f"Redirecionar para: [Fila adequada], conforme [www.saude.df.gov.br]({criterios['fonte']})"
    elif "atende" in resumo_lower or "histopatológico" in resumo_lower:
        apto, justificativa = True, f"Solicitação atende aos critérios da Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}. Aguarda vaga."
        status = "Apto"
        redirecionamento = ""
    else:
        apto, justificativa = False, "Solicito complementação do descritivo/laudos para avaliação."
        status = "Insuficiência de Informações"
        redirecionamento = ""

    return status, justificativa, redirecionamento

def avaliar_classificacao_risco(registrada, criterios):
    # Classifica como adequada, inadequada ou insuficiente
    cor = registrada.strip().capitalize()
    cores = ["Vermelho", "Amarelo", "Verde"]

    if cor in cores:
        status = "Adequada"
        texto = f"Classificação de risco adequada, conforme Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}."
    elif cor == "" or cor == "Insuficiente" or cor not in cores:
        status = "Dados Insuficientes"
        texto = "Os dados apresentados não permitem determinar a classificação de risco adequada, pois faltam informações essenciais para a análise."
    else:
        status = "Inadequada"
        texto = "Classificação de risco inadequada."
    return status, texto

def sugerir_reclassificacao(resumo, criterios):
    # Simula identificação de cor (ADAPTE ao critério real da nota técnica)
    resumo_lower = resumo.lower()
    cores = criterios["cores"]
    if "critério vermelho" in resumo_lower:
        cor = "Vermelho"
        justificativa = cores["Vermelho"]
    elif "critério amarelo" in resumo_lower:
        cor = "Amarelo"
        justificativa = cores["Amarelo"]
    elif "critério verde" in resumo_lower:
        cor = "Verde"
        justificativa = cores["Verde"]
    else:
        cor = "Insuficiente"
        justificativa = criterios["cores"].get("Insuficiente", "Os dados não permitem classificação, pois faltam informações essenciais.")
    return cor, justificativa

# ------------- INTERFACE ---------
st.title("Apoio ao Regulador – Modelo Padronizado de Parecer – SISREG III / SES DF")
st.write("""
Preencha os campos conforme a regulação, para obter um parecer estruturado.
""")

descritivo = st.text_area("1. Descritivo do Caso Clínico:", "")
especialidade = st.text_input("2. Fila / Especialidade:", "")
classif_registrada = st.selectbox("Classificação de Risco Registrada:", ["", "Vermelho", "Amarelo", "Verde", "Insuficiente"])

if st.button("Gerar Análise Reguladora"):
    # Busca critérios da fila
    criterios = buscar_criterios(especialidade)
    # Análise da solicitação
    status, justificativa, redirecionamento = analisar_pedido(descritivo, criterios)
    # Análise da classificação de risco registrada
    risco_status, risco_texto = avaliar_classificacao_risco(classif_registrada, criterios)
    # Reclassificação sugerida, se necessário
    cor_sugerida, justificativa_cor = sugerir_reclassificacao(descritivo, criterios)
    # Monta e exibe parecer
    resultado = f"""
----------------
**1. Descritivo do Caso Clínico:**  
{descritivo if descritivo else '[ ]'}

**2. Avaliação da Solicitação:**  
Fila: {criterios['fila'] if criterios['fila'] else '[ ]'}  
Classificação de Risco Registrada: {classif_registrada if classif_registrada else '[ ]'}

**3. Análise Final:**  
{('(X) Apto:\n' + justificativa) if status=='Apto' else ''}
{('(X) Não Apto:\n' + justificativa + ('\n' + redirecionamento if redirecionamento else '')) if status=='Não Apto' else ''}
{('(X) Insuficiência de Informações:\nSolicito complementação do descritivo/laudos para avaliação.') if status=='Insuficiência de Informações' else ''}

**4. Classificação de Risco:**  
{('(X) Adequada:\n' + risco_texto) if risco_status == 'Adequada' else ''}
{('(X) Inadequada:\n' + risco_texto) if risco_status == 'Inadequada' else ''}
{('(X) Dados Insuficientes:\n' + risco_texto) if risco_status == 'Dados Insuficientes' else ''}

{"*"*5 if risco_status != 'Dados Insuficientes' else ''}
{"Caso seja possível classificar com os dados disponíveis, a reclassificação deve considerar os seguintes critérios de prioridade, conforme a Nota Técnica Nº " + criterios['nota_num'] + " - " + criterios['nota_nome'] + ":" if risco_status == 'Dados Insuficientes' or risco_status == 'Inadequada' else ''}

    ( ) Vermelho: {criterios['cores'].get('Vermelho','-')}
    ( ) Amarelo: {criterios['cores'].get('Amarelo','-')}
    ( ) Verde: {criterios['cores'].get('Verde','-')}

Portanto, recomenda-se reclassificar para: [ {cor_sugerida} ].
Justificativa: {justificativa_cor}

**5. Fonte:**  
Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}  
e [www.saude.df.gov.br]({criterios['fonte']})  
----------------
"""
    st.markdown(resultado)
