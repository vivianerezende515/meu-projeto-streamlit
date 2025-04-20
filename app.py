import streamlit as st

def buscar_criterios(especialidade):
    esp = especialidade.lower()
    # Preencha com os critérios de ACESSO/ELEGIBILIDADE/DESCRITIVO MÍNIMO retirados da nota técnica REAL da fila!
    if "oncologia" in esp:
        return {
            "fila": "Oncologia",
            "nota_num": "16/2024",
            "nota_nome": "Nota Técnica 16/2024 - Oncologia Clínica",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Diagnóstico confirmado por histopatológico",
                "Laudos clínicos detalhados",
                "Paciente residente e atendido no DF",
                "Solicitação completa (anamnese, exame físico, etc.)"
            ],
            "criterios_cores": {
                "Vermelho": "Prioridade máxima: sinais de compressão medular, sangramento ativo, risco vital imediato (Vide NT 16/2024 item X.X).",
                "Amarelo": "Prioridade intermediária: doença avançada sem urgência, necessidade de início rápido do tratamento.",
                "Verde": "Prioridade baixa: paciente estável, para segmento ambulatorial, sem piora clínica recente."
            }
        }
    elif "cardio" in esp:
        return {
            "fila": "Cardiologia",
            "nota_num": "08/2023",
            "nota_nome": "Nota Técnica 08/2023 - Cardiologia",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Encaminhamento da Atenção Primária",
                "Eletrocardiograma e exames anexados",
                "Relato clínico completo (sintomas, comorbidades)",
                "Residir no DF ou áreas pactuadas"
            ],
            "criterios_cores": {
                "Vermelho": "Prioridade máxima: Situações como dor torácica aguda instável, IC descompensada, arritmia maligna.",
                "Amarelo": "Situações controladas ou risco intermediário: alteração de exames sem gravidade, sintomas crônicos agravados.",
                "Verde": "Segmento ou avaliação de rotina, estável, sem alteração aguda."
            }
        }
    else:
        return {
            "fila": especialidade,
            "nota_num": "--",
            "nota_nome": "Nota Técnica não localizada",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Não foi possível identificar critérios específicos para esta especialidade. Consulte manualmente a nota técnica da fila."
            ],
            "criterios_cores": {
                "Vermelho": "-",
                "Amarelo": "-",
                "Verde": "-"
            }
        }

def analisar_solicitacao(descritivo, criterios):
    descritivo_lower = descritivo.lower()
    # SIMULAÇÃO: ajuste a lógica conforme critérios reais!
    # Aqui, só como exemplo didático:
    criterios_atendidos = []
    criterios_nao_atendidos = []

    if not descritivo.strip():
        status = "Insuficiência de Informações"
        justificativa = "Solicito complementação do descritivo/laudos para avaliação."
        apto = "Insuficiência de Informações"
    else:
        # Verifica cada critério de acesso
        for criterio in criterios["criterios_acesso"]:
            if criterio.lower() in descritivo_lower:
                criterios_atendidos.append(criterio)
            else:
                criterios_nao_atendidos.append(criterio)

        if criterios_nao_atendidos:
            status = "Não Apto"
            justificativa = f"Solicitação não atende aos seguintes critérios de acesso/elegibilidade: {', '.join(criterios_nao_atendidos)}."
            apto = "Não Apto"
        else:
            status = "Apto"
            justificativa = f"Solicitação atende aos critérios de acesso/elegibilidade definidos na Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}. Aguarda vaga."
            apto = "Apto"
    return apto, justificativa, criterios_nao_atendidos

def avaliar_classificacao_risco(classif_registrada, criterios):
    classif_registrada = classif_registrada.capitalize()
    cores = ["Vermelho", "Amarelo", "Verde"]
    if classif_registrada in cores:
        status = "Adequada"
        justificativa = f"Classificação de risco adequada conforme critérios da Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}."
    elif not classif_registrada or classif_registrada == "Insuficiente":
        status = "Dados Insuficientes"
        justificativa = "Os dados apresentados não permitem determinar a classificação de risco adequada. Faltam informações essenciais."
    else:
        status = "Inadequada"
        justificativa = "Classificação de risco inadequada."
    return status, justificativa

def sugerir_reclassificacao(descritivo, criterios):
    descritivo_lower = descritivo.lower()
    # SIMULAÇÃO – ajuste conforme literatura real das notas técnicas:
    c_cores = criterios["criterios_cores"]
    if "critério vermelho" in descritivo_lower:
        cor = "Vermelho"
        justificativa = c_cores["Vermelho"]
    elif "critério amarelo" in descritivo_lower:
        cor = "Amarelo"
        justificativa = c_cores["Amarelo"]
    elif "critério verde" in descritivo_lower or descritivo:
        cor = "Verde"
        justificativa = c_cores["Verde"]
    else:
        cor = "Dados Insuficientes"
        justificativa = "Os dados apresentados não permitem classificar corretamente o risco."
    return cor, justificativa

# ------- INTERFACE STREAMLIT -------
st.title("Regulação SES DF – Análise Técnica Padronizada SISREG III")
st.write("""Preencha os campos conforme rotina, para laudo estruturado. Os critérios de acesso/elegibilidade estarão destacados no parecer.""")
descritivo = st.text_area("1. Descritivo do Caso Clínico:", "")
especialidade = st.text_input("2. Fila / Especialidade:", "")
classif_registrada = st.selectbox("Classificação de Risco Registrada:", ["", "Vermelho", "Amarelo", "Verde", "Insuficiente"])

if st.button("Gerar Análise Reguladora"):
    criterios = buscar_criterios(especialidade)
    apto, justificativa, criterios_faltantes = analisar_solicitacao(descritivo, criterios)
    risco_status, risco_justi = avaliar_classificacao_risco(classif_registrada, criterios)
    cor_recomendada, justificativa_cor = sugerir_reclassificacao(descritivo, criterios)
    
    resultado = f"""
-------------------------
**1. Descritivo do Caso Clínico:**  
{descritivo if descritivo else '[ ]'}

**2. Critérios de Acesso/Elegibilidade (segundo a Nota Técnica):**  
*Atenção: Verifique se o caso atende a todos os critérios abaixo:*
    - {"\n    - ".join(criterios['criterios_acesso'])}

**3. Avaliação da Solicitação:**  
Fila: {criterios['fila'] if criterios['fila'] else '[ ]'}  
Classificação de Risco Registrada: {classif_registrada if classif_registrada else '[ ]'}

**4. Análise Final:**  
{'(X) Apto:\n' + justificativa if apto=='Apto' else ''}
{'(X) Não Apto:\n' + justificativa + '\nCritérios não atendidos: ' + ', '.join(criterios_faltantes) if apto=='Não Apto' else ''}
{'(X) Insuficiência de Informações:\nSolicito complementação do descritivo/laudos para avaliação.' if apto=='Insuficiência de Informações' else ''}

**5. Classificação de Risco:**  
{'(X) Adequada:\n' + risco_justi if risco_status == "Adequada" else ''}
{'(X) Inadequada:\n' + risco_justi if risco_status == "Inadequada" else ''}
{'(X) Dados Insuficientes:\n' + risco_justi if risco_status == "Dados Insuficientes" else ''}

* Caso precise reclassificar, utilize critérios:
    - ( ) Vermelho: {criterios['criterios_cores'].get('Vermelho','-')}
    - ( ) Amarelo: {criterios['criterios_cores'].get('Amarelo','-')}
    - ( ) Verde: {criterios['criterios_cores'].get('Verde','-')}
Portanto, recomenda-se reclassificar para: **{cor_recomendada}**  
Justificativa: {justificativa_cor}

**6. Fonte:**  
Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}  
e [www.saude.df.gov.br]({criterios['fonte']})  
-------------------------
"""
    st.markdown(resultado)
