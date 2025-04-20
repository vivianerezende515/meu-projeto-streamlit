import streamlit as st
# 1. Definir os critérios para cada fila
criterios_filas = {
    "CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3": {
        "nota_num": "12/2023",
        "nota_nome": "CONDIÇÕES CLÍNICAS PARA ENCAMINHAMENTO PARA REGULAÇÃO DE CIRURGIA GINECOLÓGICA ELETIVA - UROGINECOLOGIA - PANORAMA 3",
        "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
        "critérios acesso ": {
            "Prolapso Uterino": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (tempo de evolução e outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado para miomatose (medicamentos usados com posologia); • Ultrassonografia transvaginal ou pélvica, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).
             ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": "Prolapso uterino com exteriorização do órgão, com manifestado desejo para retirar o útero.",
            "Amarelo": "Prolapso uterino sem exteriorização do órgão, com manifestado desejo para retirar o útero."
        }
    },


  "PROLAPSO DE CÚPULA VAGINAL": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Cirurgia prévia se realizada, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Tratamento em uso ou já realizado (medicamentos usados com posologia).",
            ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": "Prolapso de cúpula de vagina com exteriorização.",
            "Amarelo": "Prolapso de cúpula vaginal sem exteriorização",     }
    },

  "FÍSTULA GINECOLÓGICA": [
                "Descritivo mínimo que o encaminhamento deve conter: •  Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Descrição do exame de imagem, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)..",
            ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": " Fístula ginecológica, fístula vesico-uterina, fístula reto-vaginal, fístula uretrovaginal, fístula vesicovaginal..",      }
    },

  " INCONTINÊNCIA URINÁRIA": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Descrição do exame de imagem, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Resultado de urocultura, com data;.",
  "CISTOCELE E OU RETOCELE, COM OU SEM LACERAÇÃO DE PERÍNEO SEM INCONTINÊNCIA URINÁRIA DE TENSÃO": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)..",
            ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": " Laceração de períneo de terceiro ou quarto grau (Grau III ou IV), com ou sem cistocele e / ou retocele",
            "Amarelo": " Laceração de períneo de segundo grau (Grau II), com ou sem cistocele e / ou retocele",
     "Verde": " ceração de períneo de primereio grau (Grau I), com ou sem cistocele e / ou retocele, não responsivo a tratmento fisioterápico",     }
    },


  "INCONTINÊNCIA URINÁRIA": [
                "• Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Descrição do exame de imagem, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Resultado de urocultura, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)..",
            ]
        },
        "criterios_classificacao_risco": {
            "Amarelo": " continência urinária de esforço (“stress”) em mulheres de qualquer idade, refratária a tratamento clínico e fisioterápico por 6 meses; B - Incontinência urinária mista em mulheres de qualquer idade, refratária a tratamento clínico e fisioterápico por 6 meses.",

       }
    },
}
# 1. Definir os critérios para cada fila
criterios_filas = {
    "ENDOMETRIOISE PROFUNDA ": {
        "nota_num": "SEI/GDF - 116959308 - Nota Técnica",
        "nota_nome": "ENDOMETRIOSE PROFUNDA, PARA os AMBULATÓRIOS DE ENDOMETRIOSE PROFUNDA na Atenção Ambulatorial Terciária nos hospitais em PANORAMA 3: CONSULTA EM GINECOLOGIA - ENDOMETRIOSE PROFUNDA - Código Interno: 2018857",
        "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
        "critérios acesso ": {
            "ENDOMETRIOSE PROFUNDA": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (caracterização do quadro, descrição do hábito intestinal e urinário, exame físico e ginecológico completo); • Tratamento em uso ou já realizado (medicamentos utilizados com posologia); • História de cirurgias abdominais ou ginecológicas prévias; • Exame físico, abdominal e ginecológico completo com exame especular e toque vaginal; • Descrição da fase da mulher, se menacme, perimenopausa ou pós-menopausa; • Resultado dos exames da propedêutica mínima, com data; • Mulheres no menacme: CA125, Beta-HCG, TSH, FSH, Prolactina; • Ultrassonografia de Abdômen total, com data. • Colonoscopia ou Cistoscopia, com data. • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).”
             ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": A - Pacientes com diagnóstico de endometriose profunda infiltrativa por exames de imagem, * com estreitamento de reto sigmóide, e/ou * com hidroneforose devido obstrução de ureter, e * com sintomatologia álgica sem resposta a analgesia por via oral. B - Pacientes com diagnóstico de endometriose profunda infiltrativa por exames de imagem, com desejo reprodutivo",
            "Amarelo": "iagnóstico de endometriose profunda infiltrativa por exames de imagem, * sem estreitamento de reto sigmóide, ou * sem hidroneforose devido compressão de ureter, e * com sintomatologia álgica leve ou moderada. 
       }
    },

# 1. Definir os critérios para cada fila
criterios_filas = {
    "CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3": {
        "nota_num": "Nota Técnica N.º 12/2023 - SES/SAIS/CATES/DUAEC ANEXO 1",
        "nota_nome": "CIRURGIA GINECOLÓGICA ELETIVA - PANORAMA 3",
        "fonte": "https://www.saude.df.gov.br/notas-tecnicas",
        "critérios acesso ": {
            "1.1 LEIOMIOMA DO ÚTERO OU MIOMA DO ÚTERO SEM PROLAPSO": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (características do sangramento, tempo de evolução e outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado para miomatose (medicamentos usados com posologia); • Hemograma completo, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Descrição do exame de imagem, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).;.”
             ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": " em útero com mais de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero ",
            "Amarelo": " Mioma(s) em útero com menos de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero; C - moderada ou grave, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero.”
            "verde":  “D - Mioma(s) em útero com menos de 250 cm³, em mulheres com prole definida, com sangramento uterino anormal, sem causar anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero; E - Mioma(s) em útero acima de 250 cm³, em mulheres com prole definida, assintomática, ou com dor pélvica ou dismenorréia leve, refratária à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero.”
            ]
        "1.2 ADENOMIOSE": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (características do sangramento, tempo de evolução e outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado para adenomiose (medicamentos usados com posologia; • Hemograma completo, com data; • Ultrassonografia transvaginal ou pélvica com data; • Descrição do exame de imagem, com data confirmando o diagnóstico; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano);.”
      ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": "  Adenomiose em mulheres com prole definida, com sangramento uterino anormal, causando anemia, refratário a tratamento clínico por 6 meses, com manifestado desejo para retirar o útero ",
            "Amarelo": " B - Adenomiose em mulheres com prole definida, com sangramento uterino anormal, sem causar anemia, refratário à tratamento clínico por 6 meses, com manifestado desejo para retirar o útero”
            "verde":  “- Adenomiose em mulheres com prole definida, com útero acima de 250 cm³, assintomática, com manifestado desejo para retirar o útero”
            ]
  "1.3 SANGRAMENTO UTERINO ANORMAL SEM PATOLOGIAS ESTRUTURAIS": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (características do sangramento, tempo de evolução e outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado para adenomiose (medicamentos usados com posologia; • Hemograma completo, com data; • Ultrassonografia transvaginal ou pélvica com data; • Descrição do exame de imagem, com data confirmando o diagnóstico; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).;.”
       ]
        },

        "criterios_classificacao_risco": {
            "Vermelho": "  Sangramento uterino anormal não-estrutural, em mulheres com prole constituída, causando anemia, não responsivo ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal, com encaminhamento da ginecologia endócrina, com manifestado desejo para retirar o útero.",
            "Amarelo": " B - Sangramento uterino anormal não-estrutural, em mulheres com prole constituída, sem causar anemia, não responsivo ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal, com encaminhamento da ginecologia endócrina, com manifestado desejo para retirar o útero. ”
        },
        },
  "2.1 LEIOMIOMA DO ÚTERO OU MIOMA DO ÚTERO": [
                "Descritivo mínimo que o encaminhamento deve conter: • Sinais e sintomas (características do sangramento, tempo de evolução e infertilidade, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado para miomatose (medicamentos usados com posologia); • Hemograma completo, com data; • Ultrassonografia transvaginal ou pélvica, com data; • Descrição do exame de imagem, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).”
       ]
        },

        "criterios_classificacao_risco": {
            "Vermelho": "  A - Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero com mais de 250 cm³, em mulheres no menacme, com sangramento uterino anormal, causando anemia, com desejo de preservação do útero, com desejo reprodutivo",
            "Amarelo": " B - Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero com menos de 250 cm³, em mulheres no menacme, com sangramento uterino anormal, causando ou não anemia, refratário a tratamento clínico por 6 meses; com desejo de preservação do útero, com desejo reprodutivo, C - Mioma(s) submucoso maior 4 cm, intramural e/ou subseroso, em útero de qualquer tamanho, em mulheres no menacme, com dor pélvica ou dismenorréia moderada ou grave, refratário a tratamento clínico por 6 meses, com desejo de preservação do útero, com desejo reprodutivo D - Mioma(s) ) submucoso maior 4 cm, intramural e/ou subseroso, em útero de qualquer tamanho, em mulheres no menacme, assintomática, com desejo de preservação do útero, com desejo reprodutivo imediato ”,
"Verde ": " E - Mioma(s) de qualquer localização, em útero acima de 250 cm³ em mulheres no menacme, assintomáticas, com desejo de preservação do útero, sem desejo reprodutivo imediato",
        },
        },
  "3.1 ESPESSAMENTO ENDOMETRIAL, PÓLIPO ENDOMETRIAL (SUSPEITA DE PÓLIPO) ou SANGRAMENTO UTERINO ANORMAL": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (características do sangramento, tempo de evolução, outras informações relevantes); • Exame físico, abdominal e ginecológico completo com exame especular e toque vaginal; • Descrição da fase da mulher, se menacme, perimenopausa ou pós-menopausa; • Tratamento em uso ou já realizado para o sangramento uterino anormal (medicamentos utilizados e posologia; • Hemograma completo com data; • Ultrassonografia transvaginal ou pélvica, na primeira METADE da primeira fase do ciclo para as pacientes que ainda menstruam ou em qualquer momento para as menopausadas sem terapia hormonal ou após sangramento da supressão hormonal naquelas com terapia hormanal, com data.”
       ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": "  A - Espessamento endometrial na ultrassonografia transvaginal nas mulheres na pós-menopausa, assintomáticas: o Espessura ≥ 14 mm naquelas sem terapia hormonal; o Espessura ≥ 14 mm persistente na ultrassonografia de reavaliação após sangramento da supressão hormonal naquelas com terapia hormonal. B - Sangramento uterino anormal na presença de alteração estrutural ou não, em mulheres no menacme, COM anemia, sem resposta ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal; C - Sangramento pós-menopausa nas mulheres sem terapia hormonal com espessura ≥ 14 mm ou causando anemia independente da espessura; D - Sangramento uterino anormal e exame de imagem com lesão suspeita de neoplasia de endométrio; E - Pólipo endometrial em mulheres no menacme, com sangramento uterino anormal, causando anemia; F - Pólipo endometrial de qualquer tamanho, em mulheres na pós-menopausa, com sangramento uterino anormal, causando anemia ou não,",
            "Amarelo": " G - Espessamento endometrial na ultrassonografia transvaginal nas mulheres na pós-menopausa, assintomáticas: o Espessura ≥ 7 mm naquelas sem terapia hormonal; o Espessura ≥ 7 mm persistente na ultrassonografia de reavaliação após sangramento da supressão hormonal naquelas com terapia hormonal. H - Sangramento uterino anormal na presença de alteração estrutural ou não, em mulheres no menacme, SEM anemia, sem resposta ao tratamento clínico (AINE, hormonioterapia, pró-coagulante) por 6 meses ou com contraindicação para tal I - Sangramento pós-menopausa nas mulheres sem terapia hormonal com espessura ≥ 7 mm e < 14 mm, sem anemia J - Pólipo endometrial em mulheres na menacme, com sangramento uterino anormal, sem anemia, ou com dismenorreia; L - Pólipo endometrial de qualquer tamanho, em mulheres na pós-menopausa, assintomáticas, com fator de risco para câncer de endométrio como obesidade, hipertensão, diabetes ou usuária de Tamoxifeno”.,
"Verde ": " M - Sangramento pós-menopausa nas mulheres sem terapia hormonal e/ou com espessura > 4 mm e < 7 mm, sem anemia; N - Pólipo endometrial, em mulheres na pós-menopausa, assintomáticas O - Pólipo endometrial, em mulheres na menacme, assintomáticas",
        },
        },
  "4.1 TUMORES ANEXIAIS": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (tempo de evolução e infertilidade, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Ultrassonografia transvaginal ou pélvica, com data; • Descrição do exame de imagem, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).”
       ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": "  A - Neoplasias benignas do ovário, em mulheres no menacme, abaixo de 35 anos, maiores que 10 cm, com as outras características de benignidade pelo IOTA presentes: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâ",
            "Amarelo": " B - Neoplasias benignas do ovário, doenças das trompas, em mulheres de qualquer idade com características de benignidade pelo IOTA: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâmetro”.,
"Verde ": " C - Neoplasias benignas do ovário, doenças das trompas, em mulheres de qualquer idade com características de benignidade pelo IOTA: cisto unilocular, componente sólido < 7 mm, sombra acústica presente, multilocular liso com maior diâmetro < 10 cm, sem ascite ou sem fluxo ao doppler. Sem desejo reprodutivo imediato. D - Alterações funcionais dos ovários, cistos foliculares, cistos lúteos ou tecaluteínicos, em mulheres no menacme que persistem acima de 5 cm após 12 semanas com controle ultrasonografico",
        },
        },
  "5.1. CONTRACEPÇÃO CIRÚRGICA: [
                "Descritivo mínimo que o encaminhamento deve conter: • • Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Ultrassonografia transvaginal ou pélvica, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano) e CRITÉRIOS PARA SOLICITAÇÃO DE LAQUEADURA TUBÁRIA OU VASECTOMIA Mulheres ou homens com capacidade civil plena; Ser maior de 21 anos OU ter pelo menos dois filhos vivos (comprovados através de documentação probatória); Passar por atendimento individual ou em grupo de orientação e aconselhamento multidisciplinar; Respeitar o prazo mínimo de 60 (sessenta) dias entre o registro da manifestação da vontade e a realização do procedimento cirúrgico. Documentação mínima necessária, para regulação com inserção da paciente no SISREG III para esterilização cirúrgica definitiva, através da laqueadura tubária bilateral, atendendo os critérios definidos na Lei Nº 9.263, de 12 de janeiro de 1996, alterada pela Lei No 14.443, de 2 de setembro de 2022: • Comprovante de participação em palestra / reunião de aconselhamento sobre a importância do planejamento reprodutivo (Anexo I) preenchido, incluindo a data (sem rasura) e assinado, com “confere” do agente público que atender a paciente; • Termo de Consentimento Informado (TCI) (Anexo II) preenchido, incluindo a data (sem rasura) e assinado, com “confere” do agente público que atender a paciente; • ATA de Conferência (ATA) (Anexo III) preenchido incluindo a data (sem rasura) e assinado, com “confere” do agente público que atender a paciente.”
       ]
        },
        "criterios_classificacao_risco": {
            "Vermelho": " A - Mulheres no menacme com comorbidade de risco de vida elevado se engravidar, necessidade imediata de esterilização cirúrgica conforme relatório de especialidade médica, com desejo de esterilização cirúrgica definitiva, desde que atendidos os demais critérios definidos na Lei; B - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, com 04 (quatro) filhos OU mais, desde que atendidos os demais critérios definidos na Lei.",
            "Amarelo": " D - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, com 02 (dois) ou 03 (três), desde que atendidos os demais critérios definidos na Lei. E - Mulheres no menacme com necessidades especiais ou comorbidades que dificultem ou contraindiquem o uso dos métodos contraceptivos disponíveis na atenção primária, desde que atendidos os demais critérios definidos na Lei.”.,
"Verde ": " F - Mulheres no menacme com desejo de esterilização cirúrgica definitiva, laqueadura tubária, desde que atendidos os demais critérios definidos na Lei.,
        },
        },
  "6.1 CISTO VAGINAL e OUTRAS DOENÇAS DA GLÂNDULA DE BARTHOLIN": [
                "Descritivo mínimo que o encaminhamento deve conter: • • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Tratamento cirúrgico prévio realizado; • Ultrassonografia transvaginal ou pélvica, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano).”
       ]
        },

        "criterios_classificacao_risco": {
    
            "Amarelo": " A - Cisto da glândula de Bartholin;”,
"Verde ": " B - História de dois ou mais abcessos da glândula de Bartholin no mesmo lado drenados em pronto-socorro; C - Cisto embrionário vaginal",
        },
        },
 "7.1. HIPERTROFIA DE PEQUENOS LÁBIOS": [
                "Descritivo mínimo que o encaminhamento deve conter: •• Sinais e sintomas (tempo de evolução, outras informações relevantes); • Exame físico, abdominal e exame ginecológico completo; • Tratamento em uso ou já realizado (medicamentos usados com posologia); • Tratamento cirúrgico prévio realizado; • Ultrassonografia transvaginal ou pélvica, com data; • Colpocitologia Oncótica (CCO) preventivo recente (colhida há menos de 01 ano)”
       ]
        },

        "criterios_classificacao_risco": {
    
            "Amarelo": " A - Hipertrofia disfuncional dos pequenos lábios, maior que 8 cm de altura.”,
"Verde ": " B - Hipertrofia dos pequenos lábios, menor que 8 cm de altura",
        },
        },




# 2. Criar um seletor de fila
fila_selecionada = st.selectbox("Selecione a Fila:", list(criterios_filas.keys()))

# 3. Criar os campos de entrada para o regulador
descritivo = st.text_area("1. Descritivo do Caso Clínico:", "")

# 4. Criar as opções de análise final
st.write("### 3. Análise Final:")
apto = st.radio(
    "Selecione a opção:",
    ("Apto", "Não Apto", "Insuficiência de Informações"),
    index=2  # Define "Insuficiência de Informações" como padrão
)

# 5. Criar as opções de classificação de risco
st.write("### 4. Classificação de Risco:")
classificacao_risco = st.radio(
    "Selecione a opção:",
    ("Adequada", "Inadequada", "Dados Insuficientes"),
    index=2  # Define "Dados Insuficientes" como padrão
)

# 6. Exibir o laudo final
if st.button("Gerar Laudo"):
    # Obter os critérios da fila selecionada
    criterios = criterios_filas[fila_selecionada]

    # Gerar o texto da análise final
    if apto == "Apto":
        analise_final = f"Solicitação atende aos critérios da Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}. Aguarda vaga."
    elif apto == "Não Apto":
        analise_final = f"Solicitação não atende aos critérios da Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}. [Descrever objetivamente os critérios não atendidos]. Redirecionar para: [Fila adequada], conforme www.saude.df.gov.br"
    else:
        analise_final = "Solicito complementação do descritivo/laudos para avaliação."

    # Gerar o texto da classificação de risco
    if classificacao_risco == "Adequada":
        classificacao_final = f"Classificação de risco adequada, conforme Nota Técnica Nº {criterios['nota_num']} - {criterios['nota_nome']}."
    elif classificacao_risco == "Inadequada":
        classificacao_final = "Classificação de risco inadequada."
    else:
        classificacao_final = "Os dados apresentados não permitem determinar a classificação de risco adequada, pois faltam informações essenciais para a análise."

    # Exibir o laudo final
    st.write("### Laudo Final:")
    st.write(f"**1. Descritivo do Caso Clínico:**\n{descritivo}")
    st.write(f"**3. Análise Final:**\n{analise_final}")
    st.write(f"**4. Classificação de Risco:**\n{classificacao_final}")

    # Adicionar a nota para o regulador
    st.write("---")
    st.write("Observação: Registre a avaliação e a classificação de risco no sistema.")
