# Exercícios Práticos Baseados em Atividades Reais do Tribunal

> Estes exercícios foram elaborados a partir de levantamentos realizados com as
> unidades COPE/STI, CTPS, UAI, SDO e relato do servidor Felipe Pezzin (SGP).
> Cada exercício reflete uma atividade já praticada ou desejada pelo próprio Tribunal.
> **Não inventar dados. Onde valores reais não estiverem disponíveis, usar [A DEFINIR].**

---

## MÓDULO 1 — FUNDAMENTOS: O QUE É IA E COMO ELA FUNCIONA NO NOSSO TRABALHO

### Exercício 1.1 — Identificando IA no Seu Dia a Dia (Discussão em grupo)

**Contexto:** Servidores de diversas unidades do Tribunal já usam IA — alguns sem
perceber, outros de forma deliberada. O primeiro passo é reconhecer onde ela já está.

**Atividade:**
Em grupos de 3 a 4 pessoas, discutam e listem:
1. Quais ferramentas de IA vocês já usaram (ou viram colegas usar) no trabalho?
2. Para qual tarefa foram usadas?
3. A IA ajudou? Qual foi o resultado?

**Exemplos reais que podem surgir na discussão:**
- Uso do ChatGPT Plus para auditar processos licitatórios (UAI — Marquinhos)
- Uso do NotebookLM para tabelar respostas de questionários de cartórios (UAI — Priscilla)
- Uso de IA para redigir minutas de pareceres sobre aposentadoria (CTPS)
- Uso de IA para refinamento de textos em pareceres da SDO

**Pergunta de fechamento:** Qual foi o maior ganho? Qual foi o maior risco percebido?

---

## MÓDULO 2 — FERRAMENTAS DE IA: COMO USAR NO TRABALHO PÚBLICO

### Exercício 2.1 — Triagem de Requerimento com IA (Hands-on)

**Caso real:** A SDO recebe petições extensas e precisa identificar rapidamente o
pedido principal antes de instruir o processo.

**Situação:** Você recebeu um requerimento de 4 páginas pedindo licença para
capacitação. O texto mistura justificativas pessoais, histórico funcional, datas e
o pedido formal.

**Sua tarefa:**
1. Abra a ferramenta de IA disponível (ChatGPT / Gemini / Claude)
2. Cole o texto do requerimento (use o modelo fornecido pelo instrutor)
3. Use o prompt abaixo e observe o resultado:

```
Você é um assistente de triagem administrativa de um tribunal.
Leia o requerimento a seguir e extraia, de forma estruturada:
1. O que está sendo pedido (o objeto do requerimento)
2. A data de início e fim solicitadas (se mencionadas)
3. A fundamentação legal citada pelo servidor (se houver)
4. Documentos que o servidor afirma ter anexado

Requerimento:
[COLAR O TEXTO AQUI]
```

4. Avalie: a IA identificou corretamente todos os pontos?
5. O que precisou ser corrigido?

**Reflexão:** Quanto tempo você levaria para fazer essa triagem manualmente?
Quanto tempo levou com IA? O que ainda depende do seu julgamento?

---

### Exercício 2.2 — Refinamento de Minuta com IA (Hands-on)

**Caso real:** A SDO e a CTPS usam IA para melhorar a clareza e corrigir a redação
de pareceres técnicos antes de encaminhar ao SEI.

**Situação:** Você redigiu o parágrafo abaixo às pressas. Precisa melhorar a clareza,
adequar ao padrão de redação oficial e corrigir eventuais erros.

**Texto para refinar:**
> "O servidor em questão não cumpriu o prazo determinado pela norma aplicável
> ao caso, tendo em vista que ele não entregou os documentos que foram solicitados
> anteriormente pela chefia imediata, portanto não pode ter seu pedido deferido
> nesta oportunidade, devendo ser instado a regularizar sua situação."

**Prompt sugerido:**
```
Você é especialista em redação oficial conforme o Manual de Redação da
Presidência da República (4ª edição). Reescreva o parágrafo abaixo para
o contexto de um despacho administrativo de tribunal, tornando o texto:
- Mais claro e objetivo
- Com linguagem impessoal
- Sem repetições ou termos vagos
- Mantendo o mesmo sentido jurídico

Texto original:
[COLAR O PARÁGRAFO]
```

**Discussão em grupo:** Compare as versões produzidas por diferentes participantes.
Quais diferenças surgiram? A IA manteve o sentido jurídico correto?

---

### Exercício 2.3 — Pesquisa Legislativa com IA (Hands-on)

**Caso real:** A CTPS usa IA para buscar legislação e jurisprudência do TCU, STF e STJ
sobre temas previdenciários, superando as limitações das buscas manuais em portais.

**Situação:** Um servidor solicitou licença por motivo de doença em pessoa da família.
Você precisa verificar qual é o prazo máximo remunerado previsto em lei/regulamento.

**Prompt sugerido:**
```
No contexto do Poder Judiciário brasileiro e da legislação federal de pessoal,
qual é o prazo máximo de licença remunerada por motivo de doença em pessoa da
família para servidores públicos federais?

Por favor:
1. Cite o dispositivo legal ou regulamentar aplicável (lei, decreto ou resolução)
2. Informe se há limite de período de referência (ex.: dentro de 12 meses)
3. Indique se há diferença de tratamento para cônjuges, filhos e pais
4. Sinalize se há jurisprudência relevante do STJ ou TCU sobre o tema

IMPORTANTE: Se não tiver certeza sobre algum dado, diga explicitamente.
Não invente artigos ou acórdãos.
```

**Verificação obrigatória:** Após receber a resposta, acesse o portal do Planalto
(planalto.gov.br) e verifique se os dispositivos citados existem e dizem o que
a IA afirmou. Anote qualquer divergência.

**Reflexão:** A IA "alucionou" algum artigo ou jurisprudência? Por que isso é perigoso
em um parecer que vai fundamentar uma decisão administrativa?

---

### Exercício 2.4 — Agente de Carreira: Simulação de Progressão Funcional (Demonstração)

**Caso real:** Felipe Pezzin (SGP) implementou um agente customizado no ChatGPT
que guia servidores no processo de progressão e promoção funcional, aplicando
as regras das Resoluções do TRE-ES e TSE.

**Situação simulada:** Um servidor ocupa atualmente a classe A, padrão 5 (A5).
Quer saber se pode progredir para B6 e quais providências precisa tomar.

**Prompt demonstrativo (instructor-led):**
```
Você é um assistente especializado nas normas de progressão e promoção
funcional do Tribunal Regional Eleitoral. Com base nas regras de movimento
funcional entre classes e padrões:

1. Quais são os requisitos para progressão do padrão A5 para B1?
   (interstício, avaliação de desempenho, frequência)
2. Qual é o fluxo do processo no SEI? Quais unidades precisam assinar?
3. Qual é o documento gerado ao final?

[INSERIR AQUI AS NORMAS INTERNAS DO TRIBUNAL APÓS CONTRATAÇÃO CORPORATIVA]
```

**Discussão:** Como esse tipo de agente muda a capacidade de atendimento
da SGP? Quais riscos existem se as normas internas não forem atualizadas?

---

## MÓDULO 3 — IA APLICADA À GESTÃO: CASOS DO TRIBUNAL

### Exercício 3.1 — Análise de Processo Licitatório com IA (UAI)

**Caso real:** Marquinhos (UAI) carrega processos completos em PDF no NotebookLM
(DOD, DFD, ETP, TR e Edital) e usa IA para verificar coerência interna e divergências
de valores — por exemplo, em contratações de veículos e materiais eleitorais.

**Situação:** Você recebeu um Termo de Referência de 12 páginas para auditar.
Precisa verificar se os critérios de aceitação e as sanções administrativas estão
coerentes com o objeto contratado.

**Parte A — Preparação do documento (LGPD e segurança):**
Antes de usar qualquer IA, responda:
- O TR contém dados pessoais de servidores ou fornecedores? (Nome, CPF, endereço?)
- O processo está em sigilo?
- Qual ferramenta institucional está autorizada para este uso?

**Parte B — Prompt de auditoria:**
```
Você é um auditor interno de um tribunal. Analise o Termo de Referência abaixo
e identifique:

1. COERÊNCIA INTERNA: O objeto descrito está alinhado com os critérios de
   aceitação e os níveis de serviço (SLA) exigidos?

2. DIVERGÊNCIAS: Há contradições entre seções (ex.: prazo de entrega
   incompatível com escopo técnico)?

3. LACUNAS: Há obrigações da contratada que ficaram indefinidas ou vagas?

4. SANÇÕES: As sanções previstas são proporcionais ao descumprimento descrito?

Responda em formato de tabela: | Item | Análise | Recomendação |

Termo de Referência:
[COLAR O DOCUMENTO — COM DADOS PESSOAIS REMOVIDOS]
```

**Parte C — Verificação humana:**
Após a análise da IA, você como auditor deve:
1. Confirmar cada divergência apontada no documento original
2. Verificar se a IA "inventou" problemas que não existem
3. Assinar o parecer final assumindo responsabilidade integral

---

### Exercício 3.2 — Convocação de Candidatos: Lógica de Alternância (Demonstração)

**Caso real:** Felipe Pezzin usa o NotebookLM para gerenciar a lógica de alternância
entre lista geral e lista de cotistas, controlando desistências e pulos de fila
em processos de convocação de servidores para as Zonas Eleitorais 52 e 59.

**Situação:** Você tem uma lista de 20 classificados (15 geral + 5 cotistas).
O 3º colocado da lista geral desistiu. O 2º cotista também desistiu.
Qual é a ordem correta de convocação agora?

**Atividade (discussão antes de usar IA):**
1. Qual é a regra legal de alternância em seu órgão?
2. Sem IA: resolva manualmente para os 5 primeiros convocados
3. Com IA: alimente a ferramenta com a lista e as regras do edital e compare

**Ponto de atenção:** A IA deve ser alimentada com o edital real.
Sem o edital, ela pode inventar regras de alternância incorretas.
Isso poderia anular uma convocação? Quais são as consequências?

---

### Exercício 3.3 — Triagem de Reembolsos: Validação de Despesas (COPE/SPAUT)

**Caso real:** A SPAUT usa IA com OCR para validar despesas de reembolso:
cruza dados de nota fiscal com o SGRH, verifica CNPJ e CNAE do prestador,
compara com o rol de procedimentos autorizados e verifica assinaturas e datas.

**Situação simulada:** Você recebeu um pedido de reembolso com:
- Nota fiscal de R$ 850,00
- Prestador: "Clínica Bem Estar Ltda"
- Serviço descrito: "Consulta e avaliação nutricional"
- Beneficiário declarado: cônjuge do servidor

**Checklist manual (fazer antes de usar IA):**
- [ ] O beneficiário está cadastrado no SGRH?
- [ ] O CNPJ do prestador está ativo? O CNAE é de saúde?
- [ ] O serviço descrito está no rol de procedimentos autorizados?
- [ ] A nota fiscal é contemporânea ao pedido?
- [ ] A declaração do servidor está completa?

**Prompt de triagem:**
```
Você é um assistente de triagem de reembolsos de saúde de um tribunal público.
Com base nas informações abaixo, identifique se há pendências ou inconsistências
que devem ser verificadas por um analista humano.

Responda apenas: SIM (há pendência) ou NÃO (documento parece regular)
Para cada item abaixo, seguido de uma justificativa de 1 linha.

Dados do pedido:
- Tipo de despesa: [consulta nutricional]
- CNAE do prestador: [verificar no CNPJ.ws]
- Beneficiário: [cônjuge]
- Valor: [R$ 850,00]
- Data da nota: [data]
- Procedimento consta no rol? [informar]
```

**Reflexão crítica:** A IA pode errar nessa triagem? Que tipo de erro seria
mais grave: negar um reembolso legítimo ou aprovar um indevido?

---

## MÓDULO 4 — COMPLIANCE: RESOLUÇÃO 615/2025 E LGPD NA PRÁTICA

### Exercício 4.1 — Classificando Situações: Permitido, Restrito ou Vedado?

**Baseado nos casos reais levantados nas reuniões técnicas do Tribunal.**

Analise cada situação e classifique: **PERMITIDO | RESTRITO (com condições) | VEDADO**

| # | Situação | Classificação | Justificativa |
|---|---|---|---|
| 1 | Marquinhos carrega um processo licitatório completo em PDF no NotebookLM pessoal (conta gratuita) para análise de auditoria | | |
| 2 | Felipe usa o ChatGPT Plus para calcular progressão funcional de A5 para B6, sem inserir CPF do servidor | | |
| 3 | Priscilla insere 30 questionários de cartórios (com nomes e endereços) no NotebookLM para tabelar respostas | | |
| 4 | Um analista usa IA para gerar uma minuta de portaria de nomeação e assina sem revisar o conteúdo | | |
| 5 | A CTPS usa IA para buscar jurisprudência do STJ sobre aposentadoria e usa o resultado como base para fundamentar um parecer (com revisão humana) | | |
| 6 | Um servidor usa IA gratuita (conta pessoal) para analisar um processo em segredo de justiça | | |
| 7 | A SPAUT usa IA com OCR para triagem inicial de notas fiscais de reembolso, com revisão humana de 100% dos casos sinalizados | | |
| 8 | Um juiz delega à IA a decisão final sobre um pedido de liminar, sem revisar | | |

**Gabarito esperado e discussão:**
1. RESTRITO — conta gratuita não tem proteção contratual; dados do processo podem ir para treinamento
2. PERMITIDO — sem dado pessoal identificável; uso auxiliar com revisão humana
3. RESTRITO — dados nominais exigem conta corporativa; verificar se há segredo
4. VEDADO — supervisão humana é obrigatória; servidor assinou sem revisar
5. PERMITIDO — uso auxiliar com revisão humana; boa prática de verificação de fontes
6. VEDADO — processo sigiloso não pode ser carregado em IA de mercado
7. PERMITIDO — triagem auxiliar com revisão humana integral
8. VEDADO — vedação absoluta do art. 13 da Resolução 615/2025

---

### Exercício 4.2 — Quando Anonimizar? Quando Não É Possível?

**Baseado no debate real registrado no relatório de Felipe Pezzin (SGP).**

O servidor identificou um dilema real: em algumas atividades (como gerar uma portaria
individualizada de nomeação), a anonimização torna a ferramenta inútil para
a finalidade pública. Em outras (como analisar fluxos gerais), é perfeitamente possível.

**Atividade em duplas:** Para cada situação abaixo, decida:
- É possível anonimizar sem perder a utilidade? (SIM / NÃO)
- Se sim, como fazer?
- Se não, qual é a base legal que autoriza o uso do dado identificado?

| Situação | Anon. possível? | Como? / Base legal |
|---|---|---|
| Testar o fluxo de convocação usando candidatos fictícios | | |
| Gerar portaria de promoção com nome e matrícula do servidor | | |
| Resumir um processo de aposentadoria para orientar o analista | | |
| Verificar se um CNPJ de prestador de saúde tem CNAE ativo | | |
| Analisar a coerência interna de um Edital de licitação | | |

---

### Exercício 4.3 — Elaborando a Declaração de Uso de IA

**Caso real:** A Resolução CNJ 615/2025, art. 19, § 3º, exige que servidores
declarem o uso de IA em atos processuais e administrativos.

**Situação:** Você usou o ChatGPT Plus para redigir a fundamentação de um despacho
determinando a citação de um réu em processo administrativo disciplinar.
O prompt que você usou foi: "Elabore um despacho de citação para processo
administrativo disciplinar com base no art. 161 da Lei 8.112/90".

Você revisou integralmente e assinou o despacho. Agora, escreva a declaração
de uso de IA conforme o modelo da Resolução 615/2025:

```
DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL GENERATIVA
(Resolução CNJ nº 615/2025, art. 19, § 3º)

(1) Ferramenta utilizada: _______________
(2) Finalidade: _______________
(3) Prompt principal: _______________
(4) Fontes consultadas/mencionadas: _______________
(5) Revisão: O conteúdo foi integralmente revisado e é de responsabilidade
    do signatário. [ ] Confirmo
```

---

## MÓDULO 5 — AUTOMAÇÃO E EFICIÊNCIA

### Exercício 5.1 — Análise de Receituário com OCR (Demonstração — COPE/SPAUT)

**Caso real:** A SPAUT enfrenta o desafio de receitas médicas ilegíveis.
A COPE propôs usar modelos de reconhecimento de escrita manual (HWR)
para extrair nomes de medicamentos e validar contra a base da Anvisa.

**Demonstração (instructor-led):**
1. O instrutor mostra uma imagem de receita médica (simulada, sem dados reais)
2. Demonstra o uso de IA com visão computacional para extrair o texto
3. Mostra como um prompt pode cruzar o medicamento extraído com critérios de cobertura

**Discussão:**
- Que tipo de erro a IA pode cometer ao ler caligrafia médica?
- Quais seriam as consequências de um erro de interpretação de medicamento?
- Por que a revisão humana é obrigatória neste caso?

---

### Exercício 5.2 — Saneamento de Dados Históricos: O Desafio das Fichas Legadas (COPE/SPSERV)

**Caso real:** A SPSERV precisa processar fichas financeiras digitalizadas anteriores a 2006,
quando os sistemas de folha não eram integrados, para reconstruir vínculos
e calcular proporcionalidade de funções comissionadas (FCs).

**Situação simulada:** Você tem uma ficha financeira digitalizada de 1998
com valores de rubricas em colunas manuscritas. Precisa extrair e organizar
os dados em planilha.

**Prompt de extração estruturada:**
```
Você receberá a descrição de uma ficha financeira de servidor público.
Extraia as informações e organize em formato de tabela com as colunas:
| Mês/Ano | Rubrica | Valor (R$) | Observação |

Importante:
- Se algum valor estiver ilegível, escreva [ILEGÍVEL] na célula
- Não invente valores; apenas registre o que está descrito
- Se houver rasura ou correção, registre as duas versões

Conteúdo da ficha:
[DESCRIÇÃO DO DOCUMENTO]
```

**Reflexão:** Por que é crítico que a IA não "complete" valores ilegíveis?
Qual é o impacto financeiro e jurídico de um erro em um cálculo previdenciário?

---

### Exercício 5.3 — Saídas Estruturadas: JSON e Tabelas para Sistemas (COPE/STI)

**Caso real:** A COPE/STI estabeleceu o protocolo de "Fracionamento e Estruturação":
a IA deve entregar resultados em JSON ou tabelas para importação automática
por outros sistemas — não apenas texto livre.

**Situação:** Você precisa que a IA valide uma lista de pedidos de reembolso
e entregue o resultado em formato que possa ser importado para planilha de controle.

**Prompt com saída estruturada:**
```
Analise os pedidos de reembolso abaixo e para cada um responda
EXCLUSIVAMENTE no formato JSON a seguir, sem texto adicional:

{
  "id_pedido": "",
  "status": "APROVADO" | "PENDENTE" | "GLOSADO",
  "motivo": "descrição em 1 linha",
  "acao_requerida": "o que o servidor deve fazer"
}

Pedidos:
[LISTA DE PEDIDOS]
```

**Atividade:** Tente importar o resultado JSON para o Excel usando
Dados > Obter Dados > De JSON. Funcionou? O que facilitaria a integração?

---

## AVALIAÇÕES

### Avaliação Diagnóstica (Pré-Curso)

1. Você já usou alguma ferramenta de IA no seu trabalho? Qual?
2. Você sabe o que é a Resolução CNJ 615/2025? Marque: [ ] Sim [ ] Não [ ] Ouvi falar
3. O que você faria se precisasse resumir um processo judicial usando IA?
4. Na sua opinião, qual é o maior risco do uso de IA no trabalho do Tribunal?

---

### Avaliação Final — Questões Objetivas

**1.** Um colega usa o ChatGPT gratuito para analisar um processo que contém
CPF e endereço de uma parte. Isso é:
- (A) Permitido, pois é só para consulta interna
- (B) Vedado, pois dados pessoais não podem ser inseridos em contas sem proteção contratual ✓
- (C) Permitido, pois o ChatGPT não armazena dados
- (D) Indiferente, pois a LGPD não se aplica ao Judiciário

**2.** Você usou IA para gerar a fundamentação de um despacho. Antes de assinar,
o que é obrigatório conforme a Resolução CNJ 615/2025?
- (A) Nada; a IA já é confiável o suficiente
- (B) Revisão humana integral do conteúdo ✓
- (C) Aprovação do Comitê Nacional de IA (CNIAJ)
- (D) Só é necessário revisar se o processo for de alto risco

**3.** Marquinhos (UAI) precisa auditar um Edital de licitação usando IA.
O primeiro passo correto é:
- (A) Colar o edital completo na ferramenta e pedir análise
- (B) Verificar se o documento contém dados pessoais e se a ferramenta é autorizada ✓
- (C) Pedir autorização do CNJ antes de usar qualquer IA
- (D) Usar apenas ferramentas gratuitas para economizar recursos

**4.** A IA gerou a seguinte fundamentação: "Conforme o art. 45-B da Lei 8.112/90...".
O que você deve fazer?
- (A) Usar diretamente; a IA raramente erra em legislação
- (B) Verificar no portal do Planalto se o artigo existe e diz o que a IA afirmou ✓
- (C) Substituir por outro artigo que você conheça
- (D) Apagar a fundamentação; IA não pode ser usada para isso

**5.** A Resolução CNJ 615/2025 VEDA expressamente qual das seguintes situações?
- (A) Usar IA para redigir minutas de atos com revisão humana
- (B) Usar IA para pesquisar jurisprudência do STJ
- (C) Usar sistema de IA que classifica pessoas por comportamento para avaliar seus direitos judiciais ✓
- (D) Usar IA para sumarizar processos administrativos

---

### Avaliação Final — Questão Dissertativa

**Situação:** Você é servidor da CTPS e recebeu um requerimento de aposentadoria.
Descreva como usaria IA de forma segura e conforme para:
1. Pesquisar a legislação aplicável
2. Estruturar o parecer
3. Verificar cálculos de tempo de serviço
4. Finalizar e assinar o documento

Inclua: quais dados podem e não podem ser inseridos na ferramenta,
qual ferramenta usaria, e o que você faria antes de assinar.

**Critérios de avaliação:**
- Mencionou a necessidade de revisão humana integral (obrigatório)
- Identificou restrição ao uso de dados pessoais em ferramentas sem contrato corporativo
- Reconheceu que IA não é determinística para cálculos previdenciários (exige conferência)
- Demonstrou compreensão do princípio da responsabilidade do servidor signatário
