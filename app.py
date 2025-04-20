import streamlit as st

def buscar_criterios(especialidade):
    esp = especialidade.lower()
    # Preencha cada bloco com os critérios descritivos da Nota Técnica de cada fila de acordo com o padrão SES DF!
    if "oncologia" in esp or "câncer" in esp or "oncológico" in esp:
        return {
            "nota": "Nota Técnica 16/2024 - Oncologia Clínica",
            "protocolo": "Protocolo de avaliação do paciente oncológico",
            "criterios": {
                "Vermelho": "Critérios de risco definidos na Nota Técnica 16/2024: [Preencher com os critérios exatos da nota, ex: metástases com sintomas de compressão medular, etc.]",
                "Amarelo": "Critérios de prioridade intermediária definidos na Nota Técnica 16/2024: [Preencher com exemplos conforme a nota]",
                "Verde": "Critérios de prioridade baixa definidos na Nota Técnica 16/2024: [Preencher com exemplos conforme a nota]",
                "Insuficiente": "Os dados registrados não permitem classificar o risco corretamente, conforme Nota Técnica 16/2024."
            }
        }
    elif "cardio" in esp:
        return {
            "nota": "Nota Técnica 08/2023 - Cardiologia",
            "protocolo": "Protocolo de encaminhamento para cardiologia",
            "criterios": {
                "Vermelho": "Critérios segundo Nota Técnica 08/2023: [Exemplos exatos da nota, ex: angina instável, etc.]",
                "Amarelo": "Critérios segundo Nota Técnica 08/2023: [Exemplos intermediários]",
                "Verde": "Critérios segundo Nota Técnica 08/2023: [Exemplos de rotina]",
                "Insuficiente": "Os dados registrados não permitem classificar o risco corretamente, conforme Nota Técnica 08/2023."
            }
        }
    else:
        return {
            "nota": "Nota Técnica não localizada",
            "protocolo": "-",
            "criterios": {
                "Insuficiente": "Não foi possível identificar critérios específicos. Registre complementação das informações e consulte as Notas Técnicas e Protocolos da SES DF."
            }
        }

def classificar_risco(resumo, criterios):
    resumo_lower = resumo.lower()
    # *** Adapte aqui para reproduzir a lógica da NOTA TÉCNICA da fila! ***
    # Exemplo de simulação:
    if "critério vermelho" in resumo_lower:
        return "Vermelho", criterios.get("Vermelho")
    elif "critério amarelo" in resumo_lower:
        return "Amarelo", criterios.get("Amarelo")
    elif "critério verde" in resumo_lower:
        return "Verde", criterios.get("Verde")
    elif resumo_lower.strip() == "" or "insuficiente" in resumo_lower:
        return "Insuficiente", criterios.get("Insuficiente")
    else:
        return "Insuficiente", criterios.get("Insuficiente")

def analise_reguladora(especialidade, resumo):
    base = buscar_criterios(especialidade)
    cor, justificativa_cor = classificar_risco(resumo, base["criterios"])

    if base["nota"] == "Nota Técnica não localizada":
        situacao = "Insuficiência de informações"
        justificativa = base["criterios"]["Insuficiente"]
    elif resumo.strip() == "":
        situacao = "Insuficiência de informações"
        justificativa = base["criterios"]["Insuficiente"]
    else:
        situacao = "Apto"
        justificativa = f"Solicitação analisada conforme os critérios da {base['nota']}."

    # Montagem do texto da regulação:
    return f"""
**1. Descritivo do Caso Clínico:**
{resumo if resumo.strip() else '--'}

**2. Avaliação da Solicitação:**
Fila: {especialidade if especialidade.strip() else '--'}

**3. Análise Final:**  
- Situação: **{situacao}**
- Justificativa: {justificativa}

**4. Classificação de risco sugerida:**  
- Cor: **{cor}**
- Justificativa: {justificativa_cor}

**Critérios para cada cor definidos em Nota Técnica:**  
- Vermelho: {base["criterios"].get("Vermelho", "-")}
- Amarelo: {base["criterios"].get("Amarelo", "-")}
- Verde: {base["criterios"].get("Verde", "-")}

**Fonte utilizada:**  
- {base['nota']}  
- {base['protocolo']}

-----------------
*Revisar antes de registrar no SISREG III. Análise baseada em nota técnica vigente da SES DF.*
"""

# --- INTERFACE STREAMLIT ---
st.title("Apoio ao Médico Regulador – Classificação de Risco por Cor – SISREG III / SES DF")
st.write("Preencha os campos abaixo para gerar uma análise padronizada de regulação, conforme critérios da nota técnica da fila.")

especialidade = st.text_input("Especialidade/Fila (*)", "")
resumo = st.text_area("Descritivo do caso clínico/resumo do encaminhamento", "")

if st.button("Analisar Solicitação"):
    if not especialidade.strip():
        st.error("Preencha o campo 'Especialidade/Fila'.")
    else:
        resultado = analise_reguladora(especialidade, resumo)
        st.markdown(resultado)
        "Vermelho": "Paciente classificado como vermelho conforme NT: presença de critério X, Y ou Z descritos na NT.",
"Amarelo": "Paciente classificado como amarelo conforme NT: ...",
"Verde": "Paciente classificado como verde conforme NT: ...",
