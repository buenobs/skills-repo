## SEÇÃO III - MAPA DE GERENCIAMENTO DE RISCOS

### 1. IDENTIFICAÇÃO E ANÁLISE DOS PRINCIPAIS RISCOS

A tabela a seguir apresenta uma síntese dos riscos identificados e classificados:

| Id      | Risco                 | Relacionado ao(à): *              | P ** | I *** | Nível de Risco (P ⨯ I) **** |
| ------- | --------------------- | --------------------------------- | ---- | ----- | --------------------------- |
| **R01** | Descrição do Risco 01 | Gestão do Contrato                | 3    | 4     | 12                          |
| **R02** | Descrição do Risco 02 | Seleção do Fornecedor             | 3    | 3     | 9                           |
| **R03** | Descrição do Risco 03 | Gestão do Contrato                | 2    | 5     | 10                          |
| **R04** | Descrição do Risco 04 | Gestão do Contrato                | 3    | 3     | 9                           |
| **R05** | Descrição do Risco 05 | Planejamento / Gestão do Contrato | 4    | 3     | 12                          |
| **...** | ...                   |                                   | ...  | ...   | ...                         |

**Legenda: P = Probabilidade; I = Impacto.** * A qual natureza o risco está associado: fases do Processo de Contratação ou Solução Tecnológica: Planejamento, Seleção do Fornecedor, Gestão do Contrato. ** **Probabilidade**: chance de algo acontecer, não importando se definida, medida ou determinada objetiva ou subjetivamente, qualitativa ou quantitativamente, ou se descrita utilizando-se termos gerais ou matemáticos (ISO/IEC 31000). Usualmente usa-se uma escala de 1 a 5, sendo 1= muito baixo, 2= baixo, 3= médio, 4= alto, 5= muito alto. *** **Impacto**: resultado de um evento que afeta os objetivos (ISO/IEC 31000:2009). Usualmente usa-se uma escala de 1 a 5, sendo 1= muito baixo, 2= baixo, 3= médio, 4= alto, 5= muito alto. **** **Nível de Risco**: magnitude de um risco ou combinação de riscos, expressa em termos da combinação das consequências e de suas probabilidades (ISO/IEC 31000:2009). Obtido pelo produto da probabilidade pelo impacto.

{{... Lembrete: As probabilidades e Impactos são inicialmente definidos no item 3 – Avaliação e Tratamento dos Riscos Identificados e transferidos para a tabela acima para o cálculo dos níveis de risco}}.

{{... A seguir encontra-se um **exemplo** de relação de riscos, não exaustiva, de uma contratação de serviços de desenvolvimento e manutenção de software}}.

  

### 2. AVALIAÇÃO E TRATAMENTO DOS RISCOS IDENTIFICADOS

{{... _Riscos do processo de contratação (planejamento, seleção de fornecedores e gestão do contrato), ou qualquer outro risco relevante relacionado à solução de Tecnologia da Informação e Comunicação identificados_ }}.  
{{... _Para o tratamento de riscos, as seguintes opções podem ser selecionadas: evitar, reduzir ou mitigar, transferir ou compartilhar, e aceitar ou tolerar o risco_ }}.  
{{... _A seguir são apresentados alguns riscos meramente exemplificativos_}}.

#### Risco 01:
Ausência de recursos orçamentários ou financeiros para a prorrogação contratual ou para a contratação subsequente, ao término da vigência inicial de 12 (doze) meses.

Probabilidade: Média (3); Impacto: Alto (4).

**Dano(s):**  
  
1 - Interrupção do serviço ao final da vigência, com perda da eficiência obtida.  
2 - Retorno aos processos sem a utilização do motor de IA, impactando a capacidade das áreas que utilizam os sistemas integrados à IA.

**Tratamento:** Mitigar.

| Id     | Ação Preventiva                                                                                                                                                                                                                 | Responsável(is)    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **P1** | Incluir a previsão de renovação da despesa no Plano de Contratações de STIC do exercício subsequente.                                                                                                                           | STI, SAO           |
| **P2** | Iniciar o processo de prorrogação contratual ou de nova licitação com antecedência mínima de 180 (cento e oitenta) dias do término da vigência, nos termos do art. 33 da Resolução TRE-ES nº 63/2023.                           | SAO                |
| **Id** | **Ação de Contingência**                                                                                                                                                                                                        |                    |
| **C1** | Comunicar formalmente à Diretoria-Geral e à Presidência sobre o risco de descontinuidade e o impacto nas atividades dos servidores, buscando a alocação orçamentária necessária à prorrogação contratual ou à nova contratação. | Gestão do Contrato |

#### Risco 02:
Impugnações ou pedidos de esclarecimento durante o processo licitatório, decorrentes de especificação técnica que comprometa o caráter competitivo do certame, que causem atrasos ou suspensão. Probabilidade: Média (3); Impacto: Médio (3).  
  
**Dano(s):**  
  
1 - Atraso na disponibilização da plataforma para a STI.  
  
2 - Prejuízo na utilização da IA integrada aos sistemas do Tribunal.  
  
3 - Necessidade de fundamentação técnica adicional perante a Assessoria Jurídica, com potencial nova suspensão do certame.

**Tratamento:** Mitigar.

| Id     | Ação Preventiva                                                                                                                                                                                                                                                                                                                                             | Responsável(is)             |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **P1** | Assegurar consistência entre a classificação do objeto como Plataforma como Serviço (PaaS), o código CATSER 26069 e a dotação orçamentária correspondente, eliminando ambiguidades que possam fundamentar questionamento técnico.                                                                                                                           | Equipe de Planejamento, SAO |
| **P2** | Realizar ampla pesquisa de mercado, com múltiplos provedores e soluções de referência, para fundamentar o preço máximo aceitável.                                                                                                                                                                                                                           | SAO\COMAP\SECOM             |
| **P3** | Manter, no Termo de Referência, a fundamentação funcional dos requisitos de maior potencial restritivo, notadamente a janela de contexto igual ou superior a 1 (um) milhão de tokens, vinculada à análise integral de processos extensos dos sistemas APOIA e MIA-SEI, e o processamento multimodal nativo, vinculado a casos de uso concretos do Tribunal. | Equipe de Planejamento      |
| **P4** | Preservar a residência de dados em território nacional como requisito de execução contratual, e não como requisito eliminatório de habilitação, evitando restrição indevida à competitividade do certame.                                                                                                                                                   | Equipe de Planejamento      |
| **Id** | **Ação de Contingência**                                                                                                                                                                                                                                                                                                                                    |                             |
| **C1** | Manter a Equipe de Planejamento mobilizada para responder prontamente aos questionamentos e pedidos de esclarecimento, com o apoio da Assessoria Jurídica.                                                                                                                                                                                                  | Equipe de Planejamento      |
  

{{...}}
#### Risco N:

{{...}}

{{... inclusão de outros riscos e sua análise. O gerenciamento de riscos visa assegurar o sucesso da contratação, da execução do objeto e da gestão contratual por meio de ações contínuas de planejamento, organização e controle. O Mapa de Gerenciamento de Riscos deve identificar e analisar os principais riscos, determinando seu nível a partir da combinação de probabilidade e impacto, utilizando escala de 1 (Muito Baixo) a 5 (Muito Alto). Para cada risco, devem ser definidos: probabilidade de ocorrência, danos e impactos potenciais, ações preventivas e de contingência, responsáveis e mecanismos de acompanhamento. A classificação do nível de risco é obtida pelo produto entre probabilidade e impacto, posicionado na Matriz Probabilidade x Impacto, que orienta o tratamento adequado: riscos em nível baixo (região verde) admitem aceitação ou medidas preventivas; nível médio (região amarela) requerem atenção; níveis alto e muito alto (regiões vermelha e roxa) exigem adoção obrigatória de medidas preventivas. O gerenciamento de riscos deve ser conduzido em harmonia com a Política de Gestão de Riscos do órgão.}}

### 3. ACOMPANHAMENTO DAS AÇÕES DE TRATAMENTO DE RISCOS

{{ Espaço para registro e acompanhamento das ações de tratamento dos riscos, que poderá conter eventos relevantes relacionados ao gerenciamento de riscos, conforme exemplo abaixo }}.

| Data    | Id. Risco | Id. Ação | Registro e acompanhamento das ações de tratamento dos riscos |
| ------- | --------- | -------- | ------------------------------------------------------------ |
| {{...}} |           |          |                                                              |
| {{...}} |           |          |                                                              |
| {{...}} |           |          |                                                              |
| {{...}} |           |          |                                                              |


### 4. APROVAÇÃO E ASSINATURA

Este Mapa de Gerenciamento de Riscos foi elaborado em conformidade com o **art. 32 da Resolução TRE-ES nº 63/2023** e, após sua devida análise, é submetido para aprovação.
 
  
{{ A Análise de Riscos deve ser assinada pela Equipe de Planejamento da Contratação, nas fases de Planejamento da Contratação e de Seleção de Fornecedores, e pela Equipe de Gestão Contratual, na fase de Gestão do Contrato. O Mapa de Gerenciamento de Riscos é um documento vivo, atualizado ao longo das três fases da contratação. Na fase de Planejamento, é assinado pelos integrantes da equipe de planejamento ao término do mapeamento. Na fase de Seleção de Fornecedor, caso ocorram eventos não previstos ou sejam necessárias ações de tratamento, a equipe de planejamento gera documento atualizado a partir do anterior, registra as ações realizadas e assina. Na fase de Gestão do Contrato, o mesmo procedimento é adotado pela equipe de gestão — composta pelos três fiscais e pelo gestor do contrato —, sempre que houver necessidade de registro de novos eventos ou ações de tratamento. }}

  

EQUIPE DE PLANEJAMENTO DA CONTRATAÇÃO (Instituída pelo documento nº {{ número, referência SEI }})

Integrante Demandante: {{ Nome do titular }} (substituto: {{ Nome do substituto }})

Integrante Técnico: {{ Nome do titular }} (substituto: {{ Nome do substituto }})

Integrante Administrativo: {{ Nome do titular }} (substituto: {{ Nome do substituto }})

  

