import streamlit as st

st.title("Apoio à Regulação SUS - Consulta de Critérios")

st.write("Preencha as informações e clique em 'Buscar Regras e Analisar'.")

especialidade = st.text_input("Especialidade/Suspeita Clínica (*)")
resumo = st.text_area("Resumo da solicitação (motivo do encaminhamento)")

def buscar_criterios(especialidade):
    if "câncer" in especialidade.lower() or "oncologia" in especialidade.lower():
        return {
            "nota": "Nota Técnica 16/2024 - Oncologia Clínica",
            "protocolos": [
                "Protocolo de avaliação inicial do paciente oncológico",
                "Fluxo de tratamento oncológico"
            ],
            "criterios": [
                "Confirmação diagnóstica por histopatológico",
                "Classificação de risco segundo critérios clínicos e laboratoriais",
                "Prioridade: casos graves ou instabilidade = URGENTES"
            ]
        }
    else:
        return {
            "nota": "Nota Técnica não localizada",
            "protocolos": [],
            "criterios": [
                "Não foi possível identificar critérios específicos. Consulte as notas técnicas manualmente."
            ]
        }

if st.button("Buscar Regras e Analisar"):
    criterios = buscar_criterios(especialidade)
    if criterios["nota"] == "Nota Técnica não localizada":
        decisao = "Não foi possível identificar nota técnica ou protocolo exato para sua solicitação. Sugerimos revisão manual."
    else:
        if "urgente" in resumo.lower() or "grave" in resumo.lower():
            prioridade = "Prioridade Alta (Urgente)"
            motivo = "Paciente apresenta possível risco elevado. Encaminhamento deve ser realizado rapidamente!"
        else:
            prioridade = "Prioridade Média/Baixa"
            motivo = "Não há indicação clara de urgência extrema pelo resumo apresentado, revise as queixas clínicas."
        decisao = f"{prioridade}\nMotivo: {motivo}"

    st.write("### RESUMO DA ANÁLISE")
    st.write(f"**Especialidade:** {especialidade}")
    st.write(f"**Nota Técnica Sugerida:** {criterios['nota']}")
    st.write(f"**Protocolos Relacionados:** {', '.join(criterios['protocolos']) if criterios['protocolos'] else '-'}")
    st.write(f"**Critérios principais:**")
    for c in criterios['criterios']:
        st.write(f"- {c}")
    st.write("**DECISÃO DO PROGRAMA:**")
    st.write(decisao)
    st.info("Revise as informações antes de registrar esta resposta no SISREG III.")
