---
name: "artefatos-contratacao-tic"
description: "Orienta a elaboração, revisão e compatibilização dos artefatos de planejamento de contratações de TIC do TRE-ES — Estudo Técnico Preliminar (ETP), Termo de Referência (TR) e Mapa de Gerenciamento de Riscos (MGR) — segundo os modelos institucionais de 03/09/2026, a Lei nº 14.133/2021 e a Resolução TRE-ES nº 63/2023. Use SEMPRE que o usuário pedir para redigir, preencher, estruturar, revisar, atualizar ou conferir ETP, TR, Projeto Básico, MGR, mapa de riscos, análise de viabilidade, análise de sustentação e transição contratual, TCO, matriz probabilidade x impacto, ou qualquer peça da fase de planejamento de uma contratação de TIC (software, nuvem, IA, licenças, outsourcing, equipamentos, serviços continuados), inclusive prorrogações contratuais, mesmo que ele não cite os modelos ou a resolução."
---

# Artefatos de Planejamento de Contratações de TIC (ETP, TR e MGR)

Esta skill orienta a construção dos três artefatos centrais da fase de planejamento das contratações de TIC do TRE-ES. Eles formam um conjunto encadeado: o **ETP** demonstra que a contratação é viável e escolhe a solução; o **TR** transforma a solução escolhida em regras para a licitação e a execução; o **MGR** identifica e trata os riscos de todas as fases. Um erro em um deles costuma contaminar os outros, por isso a coerência entre os três é tão importante quanto a qualidade de cada um.

## 1. Arquivos da skill e quando lê-los

1. `references/etp.md` — orientação seção por seção do ETP (Seção I – Análise de Viabilidade; Seção II – Sustentação e Transição Contratual). Leia ao elaborar ou revisar um ETP.
2. `references/tr.md` — orientação seção por seção do TR, incluindo o que é reservado a outras unidades e as cláusulas obrigatórias. Leia ao elaborar ou revisar um TR.
3. `references/mgr.md` — orientação para identificação, avaliação, tratamento e acompanhamento dos riscos. Leia ao elaborar ou revisar um MGR.
4. `references/consistencia.md` — matriz de correspondência entre ETP, TR e MGR e checklist de conferência cruzada. Leia sempre que houver mais de um artefato em jogo ou quando o usuário pedir revisão.
5. `assets/modelo-etp.md`, `assets/modelo-tr.md`, `assets/modelo-mgr.md` — os modelos institucionais originais, com as orientações entre chaves `{{ }}`. Use-os como esqueleto literal da estrutura (títulos, numeração e textos fixos).

Se o pedido envolve só um artefato, leia a referência correspondente e o respectivo modelo. Se envolve dois ou três, leia também `consistencia.md`.

## 2. Fluxo de trabalho recomendado

1. **Identificar o cenário.** Verifique qual artefato é pedido, em que fase o processo está (planejamento, seleção do fornecedor, gestão do contrato) e se é contratação nova ou prorrogação. Na prorrogação de serviço contínuo, o art. 33 da Resolução TRE-ES nº 63/2023 dispensa novo DOD e novo ETP, mas exige atualização do TR (em minuta, sem estimativa de custos, para pesquisa de mercado) e revisão do MGR (art. 32).
2. **Reunir os insumos reais.** Procure no contexto, nos arquivos enviados, nos projetos e nos conectores disponíveis o DOD, atas do CGTIC, Plano de Contratações de TIC, PDTIC/PEI/ENTIC-JUD, contratos anteriores, pesquisas de mercado, portaria da equipe de planejamento e minutas anteriores. Liste o que falta antes de redigir.
3. **Partir do modelo.** Reproduza títulos, numeração e textos fixos do modelo. Substitua cada orientação `{{ }}` pelo conteúdo correspondente.
4. **Redigir na ordem lógica.** ETP primeiro (define necessidade, demanda, solução e custo), depois MGR (os riscos dependem da solução escolhida e da estratégia de transição) e por fim o TR (que herda do ETP e deve refletir as ações preventivas do MGR). Quando o usuário trouxer os três já prontos, revise nessa mesma ordem.
5. **Conferir a coerência cruzada** com `references/consistencia.md`.
6. **Entregar** o artefato e uma lista curta de pendências (dados ausentes, itens reservados a outras unidades, pontos que exigem decisão da equipe).

## 3. Regras transversais (valem para os três artefatos)

### 3.1. Nenhum dado fictício

Não invente números, valores, quantitativos, nomes de servidores, números de processo SEI, códigos CATMAT/CATSER, acórdãos, artigos de norma, datas ou preços. Contratações públicas são auditadas, e um dado plausível porém inventado é pior do que uma lacuna visível, porque pode passar despercebido até a publicação do edital. Quando faltar informação, mantenha um marcador explícito, como `{{ PENDENTE: quantitativo de licenças – fonte: DOD }}`, e registre-o na lista de pendências ao final. Só produza exemplos hipotéticos se o usuário pedir expressamente, e identifique-os como tal.

### 3.2. Orientações entre chaves não ficam no texto final

Os modelos trazem instruções entre `{{ }}`. Elas orientam o preenchimento e **devem ser removidas** do documento final. Os únicos marcadores `{{ }}` admitidos na versão entregue são os de pendência (item 3.1). Também devem ser removidos os exemplos meramente ilustrativos dos modelos que não se aplicam ao caso (por exemplo, riscos de exemplo no MGR ou a menção a "plataforma e pacote de SMS" na seção de sanções do TR).

### 3.3. Itens reservados a outras unidades

Alguns itens só são preenchidos quando o processo retorna da SAO: no TR, o 1.5 (estimativa de preço — SAO/COMAP/SECOM), o 3.2 (modalidade e tipo — SAO/COMAP/SL), o 3.4 (adequação orçamentária — SAO/COF/SEPLAN) e, dependendo desta manifestação, o 3.1 (forma de adjudicação). Na minuta, mantenha esses itens com a indicação de que estão reservados ao setor competente, sem preencher.

### 3.4. Fundamentação normativa

Cite apenas dispositivos que constam dos modelos, das referências desta skill ou de fonte verificada na conversa. As bases principais são a Lei nº 14.133/2021 (em especial art. 6º, XXIII, e art. 18), a Resolução TRE-ES nº 63/2023 (arts. 30, 32 e 33), a LGPD (Lei nº 13.709/2018), a Lei nº 10.522/2002 (CADIN) e os acórdãos do TCU já mencionados nos modelos. Quando o caso envolver IA, considere também a Resolução CNJ nº 615/2025. Se precisar de jurisprudência adicional, pesquise e confirme antes de citar.

### 3.5. Público de cada documento

O ETP é documento interno de fundamentação e pode ser analítico e extenso. O TR é distribuído a todos os licitantes: seja sucinto, não inclua informações sigilosas nem dados pessoais e lembre que qualquer afirmação pode ser objeto de impugnação ou pedido de esclarecimento. O MGR é documento vivo, atualizado nas três fases da contratação.

### 3.6. Competitividade

Toda especificação deve ser justificada pela necessidade do Tribunal, não pela preferência por um produto. Evite caracterização excessiva, detalhamento desnecessário, indicação de marca sem estudo técnico e econômico circunstanciado e requisitos que só um fornecedor atenda (Acórdãos 2.383/2014, 2.407/2006 e 488/2019 – TCU – Plenário). Quando um requisito for potencialmente restritivo, vincule-o expressamente a um caso de uso concreto e registre o risco correspondente no MGR.

### 3.7. Forma e redação

Produza os artefatos em Markdown, salvo pedido expresso de outro formato. Use a numeração decimal dos modelos (1., 1.1., 1.1.1.) e, para enumerações internas, alíneas em letras minúsculas (a), b), c)) e incisos em romanos quando houver hierarquia adicional, evitando marcadores do tipo bullet. Redija em linguagem técnica e impessoal, em português formal, com frases objetivas. Mantenha a mesma definição do objeto em todos os lugares em que ela aparece.

### 3.8. Assinaturas

Os três artefatos terminam com o bloco da Equipe de Planejamento da Contratação (Integrantes Demandante, Técnico e Administrativo, com titulares e substitutos, e o documento SEI que instituiu a equipe). Preencha apenas com nomes e referências informados; do contrário, deixe o marcador de pendência. No MGR, na fase de gestão, a assinatura passa à equipe de gestão contratual (gestor e fiscais).

### 3.9. Prazo de pagamento (padrão TRE-ES)

O prazo de pagamento adotado pelo TRE-ES é de **até o 10º (décimo) dia após a apresentação da nota fiscal** devidamente atestada, desde que não haja fator impeditivo provocado pela contratada. Esse padrão prevalece sobre a orientação do item 6.4 de `assets/modelo-tr.md`, que menciona "em até 5 dias úteis", e sobre a remissão ao "prazo de pagamento indicado no modelo" em `references/tr.md`; não reproduza o prazo de 5 dias úteis. No item 6.4 do TR (Critérios de Medição e de Pagamento), use redação equivalente a: "O pagamento será efetuado mediante depósito bancário na conta da contratada até o 10º (décimo) dia após a apresentação da nota fiscal ou fatura devidamente atestada, desde que não haja fator impeditivo provocado pela contratada." Ao revisar artefatos existentes, aponte como inconsistência qualquer outro prazo de pagamento (inclusive "5 dias úteis") e sugira a redação padrão. Prazo diverso só deve constar se o usuário o indicar expressamente para o caso concreto.

## 4. Entrega

Ao final de cada artefato produzido ou revisado, apresente fora do documento, em prosa ou lista enumerada breve:

a. as pendências de dados, com a fonte provável de cada uma;
b. os itens reservados a outras unidades;
c. as inconsistências encontradas entre os artefatos (quando houver mais de um);
d. as decisões que cabem à equipe de planejamento e não podem ser tomadas pelo assistente (por exemplo, vigência, parcelamento, critérios de qualificação técnica).

Em revisões, aponte o problema, o item afetado e a redação sugerida, sem reescrever o documento inteiro quando o usuário pedir apenas ajustes pontuais.