import streamlit as st
criterios_filas = {
" UROGINECOLOGIA - 0710797": {
        "PROLAPSO UTERINO": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução e outras informações relevantes)",
                "Exame físico, abdominal e exame ginecológico completo",
                "Tratamento em uso ou já realizado para prolapso (medicamentos usados com posologia)",
                "Ultrassonografia transvaginal ou pélvica, com data",
                "Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)"
            ],
            "criterios_classificacao_risco": {
                "Vermelho": "Prolapso uterino com exteriorização do órgão, com manifestado desejo para retirar o útero.",
              "Amarelo": "Prolapso uterino sem exteriorização do órgão, com manifestado desejo para retirar o útero."
            }
        },
        "PROLAPSO DE CÚPULA VAGINAL": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução, outras informações relevantes)",
“Exame físico, abdominal e exame ginecológico completo",
“Cirurgia prévia se realizada, com data", 
“Ultrassonografia transvaginal ou pélvica, com data", 
“Tratamento em uso ou já realizado (medicamentos usados com posologia)."
            ],
            "criterios_classificacao_risco": {
                "Vermelho": " Prolapso de cúpula vaginal com exteriorização.",
"Amarelo": " Prolapso de cúpula vaginal sem exteriorização."
            }
        }
    },
 " FÍSTULA GINECOLÓGICA": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "• Sinais e sintomas (tempo de evolução, outras informações relevantes)",
‘Exame físico, abdominal e exame ginecológico completo",
“Tratamento em uso ou já realizado (medicamentos usados com posologia)",
” Descrição do exame de imagem, com data”,
’’Ultrassonografia transvaginal ou pélvica, com data",
“Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano). "
            ],
            "criterios_classificacao_risco": {
                "Vermelho": "  Fístula ginecológica, fístula vesico-uterina, fístula reto-vaginal, fístula uretrovaginal, fístula vesicovaginal.",
            }
        }
    },
 " INCONTINÊNCIA URINÁRIA": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução, outras informações relevantes)’,
“Exame físico, abdominal e exame ginecológico completo",
“Tratamento em uso ou já realizado (medicamentos usados com posologia)",
“Descrição do exame de imagem, com data",
‘Ultrassonografia transvaginal ou pélvica, com data",
“Resultado de urocultura, com data;"
            ],
            "criterios_classificacao_risco": {
                 "Amarelo": " continência urinária de esforço (“stress”) em mulheres de qualquer idade, refratária a tratamento clínico e ou fisioterápico por 6 meses",
‘B - Incontinência urinária mista em mulheres de qualquer idade, refratária a tratamento clínico e fisioterápico por 6 meses."              
            }
        }
    },
 " CISTOCELE, RETOCELE E LACERAÇÃO DE PERÍNEO": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução, outras informações relevantes)",
“Exame físico, abdominal e exame ginecológico completo",
“Tratamento em uso ou já realizado (medicamentos usados com posologia)", ‘Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)."
            ],
            "criterios_classificacao_risco": {
                "Vermelho": " Laceração de períneo de terceiro ou quarto grau (Grau III ou IV), com ou sem cistocele e / ou retocele",
                 "Amarelo": " - Laceração de períneo de segundo grau (Grau II), com ou sem cistocele e / ou retocele",
                 "Verde": " Laceração de períneo de primeiro grau (Grau I), com ou sem cistocele e / ou retocele, não responsivo ao tratamento fisioterapico"
            }
        }
    },
 " INCONTINÊNCIA URINÁRIA": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução, outras informações relevantes)",
“Exame físico, abdominal e exame ginecológico completo",
“Descrição do exame de imagem, com data",
“Ultrassonografia transvaginal ou pélvica, com data",
“Resultado de urocultura, com data",
‘Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)."
            ],
            "criterios_classificacao_risco": {
                 "Amarelo": "A - Incontinência urinária de esforço (“stress”) em mulheres de qualquer idade, refratária a tratamento clínico e fisioterápico por 6 meses',
“B - Incontinência urinária mista em mulheres de qualquer idade, refratária a tratamento clínico e fisioterápico por 6 meses."      
              }
        }
    }
}
" CIRURGIA GINECOLÓGICA": {  
        " LEIOMIOMA DO ÚTERO OU MIOMA DO ÚTERO": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": " MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA.",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (características do sangramento, tempo de evolução e outras informações relevantes)",
“Exame físico, abdominal e exame ginecológico completo",
“Tratamento em uso ou já realizado para miomatose (medicamentos usados com posologia)",
‘Hemograma completo, com data",
“Ultrassonografia transvaginal ou pélvica, com data",
“Descrição do exame de imagem, com data",
‘Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)"
            ],
            "criterios_classificacao_risco": {
                 "Vermelho": " A - Mioma(s) em útero com mais de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero",
“ Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero com mais de 250 cm³, em mulheres no menacme, com sangramento uterino anormal, causando anemia, com desejo de preservação do útero, com desejo reprodutivo",
                 "Amarelo": " B - Mioma(s) em útero com menos de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero",
“C - Mioma(s) em útero de qualquer tamanho, em mulheres com prole definida, com dor pélvica ou dismenorréia moderada ou grave, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero.",
“ Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero com menos de 250 cm³, em mulheres no menacme, com sangramento uterino anormal, causando ou não anemia, refratário a tratamento clínico por 6 meses; com desejo de preservação do útero, com desejo reprodutivo",
“ C - Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero de qualquer tamanho, em mulheres no menacme, com dor pélvica ou dismenorréia moderada ou grave, refratário a tratamento clínico por 6 meses, com desejo de preservação do útero, com desejo reprodutivo",
“ D - Mioma(s) ) submucoso maior 4 cm, intramural e/ou subseroso, em útero de qualquer tamanho, em mulheres no menacme, assintomática, com desejo de preservação do útero, com desejo reprodutivo imediato",
                 "Verde": " D - Mioma(s) em útero com menos de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, sem causar anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero",
“ E - Mioma(s) em útero acima de 250 cm³, em mulheres com prole definida, assintomática, ou com dor pélvica ou dismenorréia leve, refratária à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero.",
“E - Mioma(s) de qualquer localização, em útero acima de 250 cm³ em mulheres no menacme, assintomáticas, com desejo reprodutivo.”
           
        }
    }
},

     " ADENOMIOSE": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (características do sangramento, tempo de evolução e outras informações relevantes)",
‘Exame físico, abdominal e exame ginecológico completo",
‘Tratamento em uso ou já realizado para adenomiose (medicamentos usados com posologia",
“Hemograma completo, com data",
“Ultrassonografia transvaginal ou pélvica com data",
‘Descrição do exame de imagem, com data confirmando o diagnóstico",
’Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)."
            ],
            "criterios_classificacao_risco": {
                "Vermelho": "A - Adenomiose em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário a tratamento clínico por 6 meses, com manifestado desejo para retirar o útero. ",
                 "Amarelo": " B - Adenomiose em mulheres com prole definida, com sangramento uterino anormal, sem causar anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero.",
                 "Verde": "C - Adenomiose em mulheres com prole definida, com útero acima de 250 cm³, assintomática, com manifestado desejo para reti "
            }
        }
    },

     "ESPESSAMENTO ENDOMETRIAL, PÓLIPO ENDOMETRIAL (SUSPEITA DE PÓLIPO) ou SANGRAMENTO UTERINO ANORMAL ": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (características do sangramento, tempo de evolução, outras informações relevantes)",
“Exame físico, abdominal e ginecológico completo com exame especular e toque vaginal",
“Descrição da fase da mulher, se menacme, perimenopausa ou pós-menopausa",
Tratamento em uso ou já realizado para o sangramento uterino anormal (medicamentos utilizados e posologia",
“Hemograma completo com data",
“Ultrassonografia transvaginal ou pélvica, na primeira METADE da primeira fase do ciclo para as pacientes que ainda menstruam ou em qualquer momento para as menopausadas sem terapia hormonal ou após sangramento da supressão hormonal naquelas com terapia hormanal, com data",
“Mamografia atualizada de rotina se indicada, obedecendo a recomendação do MS",
“Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano). "
            ],
            "criterios_classificacao_risco": {
                "Vermelho": " A - Espessamento endometrial na ultrassonografia transvaginal nas mulheres na pós-menopausa, assintomáticas: o Espessura ≥ 14 mm naquelas sem terapia hormonal; o Espessura ≥ 14 mm persistente na ultrassonografia de reavaliação após sangramento da supressão hormonal naquelas com terapia hormonal.",
“B - Sangramento uterino anormal na presença de alteração estrutural ou não, em mulheres no menacme, COM anemia, sem resposta ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal; ",
“C - Sangramento pós-menopausa nas mulheres sem terapia hormonal com espessura ≥ 14 mm ou causando anemia independente da espessura;",
“D - Sangramento uterino anormal e exame de imagem com lesão suspeita de neoplasia de endométrio;",
“E - Pólipo endometrial em mulheres no menacme, com sangramento uterino anormal, causando anemia;",
“F - Pólipo endometrial de qualquer tamanho, em mulheres na pós-menopausa, com sangramento uterino anormal, causando anemia ou não.”,
                 "Amarelo": " G - Espessamento endometrial na ultrassonografia transvaginal nas mulheres na pós-menopausa, assintomáticas: o Espessura ≥ 7 mm naquelas sem terapia hormonal; o Espessura ≥ 7 mm persistente na ultrassonografia de reavaliação após sangramento da supressão hormonal naquelas com terapia hormonal. ",
“H - Sangramento uterino anormal na presença de alteração estrutural ou não, em mulheres no menacme, SEM anemia, sem resposta ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal",
“I - Sangramento pós-menopausa nas mulheres sem terapia hormonal com espessura ≥ 7 mm e < 14 mm, sem anemia",
“J - Pólipo endometrial em mulheres na menacme, com sangramento uterino anormal, sem anemia, ou com dismenorreia;",
“L - Pólipo endometrial de qualquer tamanho, em mulheres na pós-menopausa, assintomáticas, com fator de risco para câncer de endométrio como obesidade, hipertensão, diabetes ou usuária de Tamoxifeno",
                 "Verde": "M - Sangramento pós-menopausa nas mulheres sem terapia hormonal e/ou com espessura > 4 mm e < 7 mm, sem anemia;",
“N - Pólipo endometrial, em mulheres na pós-menopausa, assintomáticas",
“O - Pólipo endometrial, em mulheres na menacme, assintomáticas "
            }
        }
    },

    
 " TUMORES ANEXIAIS": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                "Sinais e sintomas (tempo de evolução e infertilidade, outras informações relevantes);",
‘Exame físico, abdominal e exame ginecológico completo; ",
‘• Tratamento em uso ou já realizado (medicamentos usados com posologia); ",
‘• Ultrassonografia transvaginal ou pélvica, com data; ",
‘• Descrição do exame de imagem, com data;",
‘ • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)."
            ],
            "criterios_classificacao_risco": {
                "Vermelho": "A - Neoplasias benignas do ovário, em mulheres no menacme, abaixo de 35 anos, maiores que 10 cm, com as outras características de benignidade pelo IOTA presentes: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâmetro ",
                 "Amarelo": " B - Neoplasias benignas do ovário, doenças das trompas, em mulheres de qualquer idade com características de benignidade pelo IOTA: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâmetro < 10 cm, sem ascite ou sem fluxo ao doppler. Com desejo reprodutivo imediato.;",
                 "Verde": "C - Neoplasias benignas do ovário, doenças das trompas, em mulheres de qualquer idade com características de benignidade pelo IOTA: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâmetro < 10 cm, sem ascite ou sem fluxo ao doppler. Sem desejo reprodutivo imediato. ",
“D - Alterações funcionais dos ovários, cistos foliculares, cistos lúteos ou tecaluteínicos, em mulheres no menacme que persistem acima de 5 cm após 12 semanas com controle ultrasonogáfico."
            }
        }
    },

  	"CONTRACEPÇÃO CIRÚRGICA ": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                " "
            ],
            "criterios_classificacao_risco": {
                "Vermelho": " ",
                 "Amarelo": " ",
                 "Verde": " "
            }
        }
    },

  " ": {
            "nota_num": "nota técnica n 12/2023 - SES/SAIS/CATES/DUAEC",
            "nota_nome": "MOTIVOS DE ENCAMINHAMENTO PARA CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
            "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
            "criterios_acesso": [
                " • Sinais e sintomas (tempo de evolução, outras informações relevantes); ",
‘• Exame físico, abdominal e exame ginecológico completo; ",
“• Tratamento em uso ou já realizado (medicamentos usados com posologia);",
“• Ultrassonografia transvaginal ou pélvica, com data; ",
“• Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)"
            ],
            "criterios_classificacao_risco": {
                "Vermelho": " A - Mulheres no menacme com comorbidade de risco de vida elevado se engravidar, necessidade imediata de esterilização cirúrgica conforme relatório de especialidade médica, com desejo de esterilização cirúrgica definitiva, desde que atendidos os demais critérios definidos na Lei;",
“ B - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, com 04 (quatro) filhos OU mais, desde que atendidos os demais critérios definidos na Lei;",
                 "Amarelo": " D - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, com 02 (dois) ou 03 (três), desde que atendidos os demais critérios definidos na Lei.",
“ E - Mulheres no menacme com necessidades especiais ou comorbidades que dificultem ou contraindiquem o uso dos métodos contraceptivos disponíveis na atenção primária, desde que atendidos os demais critérios definidos na Lei",
                 "Verde": "F - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, laqueadura tubária, desde que atendidos os definidos por lei "
            }
        }
    },

   import streamlit as st

# (Código da estrutura de dados criterios_filas conforme o exemplo acima)

# 1. Criar os seletores
fila_selecionada = st.selectbox("Selecione a Fila:", list(criterios_filas.keys()))
situacoes_acesso = list(criterios_filas[fila_selecionada].keys())
situacao_selecionada = st.selectbox("Selecione a Situação de Acesso:", situacoes_acesso)

# 2. Criar os campos de entrada para o regulador
descritivo = st.text_area("1. Descritivo do Caso Clínico:", "")

# 3. Criar o seletor da classificação de risco registrada
classificacao_registrada = st.selectbox(
    "4. Classificação de Risco Registrada:",
    ("Vermelho", "Amarelo", "Verde", "Dados Insuficientes")
)

# 4. Criar as opções de análise final
st.write("### 5. Análise Final:")
apto = st.radio(
    "A solicitação atende aos critérios de acesso?",
    ("Sim", "Não", "Insuficiência de Informações"),
    index=2  # Define "Insuficiência de Informações" como padrão
)

# 5. Função para analisar os critérios de acesso
def analisar_criterios_acesso(descritivo, criterios_acesso):
    criterios_atendidos = True
    for criterio in criterios_acesso:
        if criterio.lower() not in descritivo.lower():
            criterios_atendidos = False
            criterio_faltante = criterio
            break

    if criterios_atendidos:
        return "Apto: Solicitação atende aos critérios da Nota Técnica Nº {} - {}. Aguarda vaga.".format(criterios["nota_num"], criterios["nota_nome"])
    else:
        return "Não Apto: Solicitação não atende aos critérios da Nota Técnica Nº {} - {}. Critério não atendido: {}. Redirecionar para: [Fila adequada], conforme www.saude.df.gov.br".format(criterios["nota_num"], criterios["nota_nome"], criterio_faltante)

# 6. Função para analisar a classificação de risco
def analisar_classificacao_risco(classificacao_registrada, criterios_classificacao_risco):
    if classificacao_registrada == "Dados Insuficientes":
        return "Dados Insuficientes: Os dados apresentados não permitem determinar a classificação de risco adequada, pois faltam informações essenciais para a análise."
    elif classificacao_registrada in criterios_classificacao_risco:
        return f"Adequada: Classificação de risco adequada, conforme Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}."
    else:
        return "Inadequada: Classificação de risco inadequada."

# 7. Exibir o laudo final
if st.button("Gerar Laudo"):
    # Obter os critérios da situação de acesso selecionada
    criterios = criterios_filas[fila_selecionada][situacao_selecionada]

    # Analisar os critérios de acesso
    analise_acesso = analisar_criterios_acesso(descritivo, criterios["criterios_acesso"])

    # Analisar a classificação de risco
    analise_risco = analisar_classificacao_risco(classificacao_registrada, criterios["criterios_classificacao_risco"])

    # Exibir o laudo final
    st.write("### Laudo Final:")
    st.write(f"**1. Descritivo do Caso Clínico:**\n{descritivo}")
    st.write(f"**3. Análise Final (Critérios de Acesso):**\n{analise_acesso}")
    st.write(f"**4. Classificação de Risco:**\n{analise_risco}")

    # Adicionar a nota para o regulador
    st.write("---")
    st.write("Observação: Registre a avaliação e a classificação de risco no sistema.")
