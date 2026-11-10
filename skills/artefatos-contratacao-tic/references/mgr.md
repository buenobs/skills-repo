# Mapa de Gerenciamento de Riscos (MGR) — Orientação por Seção

Modelo de base: `assets/modelo-mgr.md` (Seção III do conjunto de artefatos).

## Sumário

1. Função do MGR
2. Conceitos e escala
3. Orientação por seção (itens 1 a 4)
4. Como identificar riscos
5. Erros frequentes

## 1. Função do MGR

O MGR (art. 32 da Resolução TRE-ES nº 63/2023) identifica, avalia e trata os riscos que ameaçam o sucesso da contratação, da execução do objeto e da gestão contratual. É um **documento vivo**: elaborado no planejamento, atualizado na seleção do fornecedor e na gestão do contrato sempre que surgirem eventos não previstos ou ações de tratamento a registrar. Deve seguir a Política de Gestão de Riscos do órgão. Em prorrogações de serviço contínuo, sua revisão é obrigatória (art. 33 c/c art. 32).

## 2. Conceitos e escala

Os conceitos seguem a ISO/IEC 31000, conforme a legenda do modelo:

a) **Probabilidade (P)** — chance de o evento ocorrer, em escala de 1 a 5 (1 muito baixa; 2 baixa; 3 média; 4 alta; 5 muito alta).
b) **Impacto (I)** — efeito do evento sobre os objetivos, na mesma escala de 1 a 5.
c) **Nível de risco** — produto P × I, posicionado na Matriz Probabilidade × Impacto.

O modelo indica o tratamento por região da matriz: nível baixo (verde) admite aceitação ou medidas preventivas; médio (amarelo) requer atenção; alto e muito alto (vermelho e roxo) exigem medidas preventivas obrigatórias. Os limites numéricos de cada região devem ser os da Política de Gestão de Riscos do TRE-ES; se o usuário não os fornecer, não os invente — deixe pendência ou classifique apenas pelo produto P × I.

Opções de tratamento: **evitar**, **mitigar (reduzir)**, **transferir (compartilhar)** e **aceitar (tolerar)**.

## 3. Orientação por seção

### 1. Identificação e análise dos principais riscos

Tabela-síntese com as colunas do modelo: Id (R01, R02...), Risco, Relacionado ao(à) (Planejamento, Seleção do Fornecedor, Gestão do Contrato ou combinações), P, I e Nível (P × I). Mantenha a legenda do modelo. Os valores de P e I são definidos primeiro no item 2 (Avaliação e Tratamento) e depois transferidos para esta tabela; confira se o produto está correto e se os números coincidem com os do item 2. Observação: o lembrete do modelo remete a "item 3", mas a avaliação está no item 2.

Remova os riscos de exemplo do modelo (R01 a R05 genéricos) e os textos entre chaves.

### 2. Avaliação e tratamento dos riscos identificados

Para cada risco, use o bloco:

```
#### Risco NN:
[Descrição do evento de risco, com causa e consequência.]

Probabilidade: [Nível] ([n]); Impacto: [Nível] ([n]).

**Dano(s):**
1 - ...
2 - ...

**Tratamento:** [Evitar | Mitigar | Transferir | Aceitar].

| Id     | Ação Preventiva | Responsável(is) |
| ------ | --------------- | --------------- |
| **P1** | ...             | ...             |
| **Id** | **Ação de Contingência** |        |
| **C1** | ...             | ...             |
```

Orientações:

a) Descreva o risco como evento incerto com causa e efeito ("atraso na entrega decorrente de..."), não como problema já ocorrido nem como mera ausência de algo.
b) Danos concretos e ligados aos objetivos da contratação.
c) Ações preventivas (P) atuam sobre a probabilidade; ações de contingência (C) atuam depois que o risco se materializa, reduzindo o impacto.
d) Cada ação com responsável identificado por unidade ou papel (STI, SAO, SAO/COMAP/SECOM, Equipe de Planejamento, Gestão do Contrato etc.).
e) Ações preventivas que dependem de cláusula devem aparecer efetivamente no TR (por exemplo, residência de dados, ANS, transferência de conhecimento).
f) Os dois riscos do modelo (descontinuidade orçamentária e impugnações por especificação restritiva) são exemplos reais de uma contratação de IA; só reaproveite se o risco existir no caso concreto, adaptando descrição, notas e ações.

### 3. Acompanhamento das ações de tratamento

Tabela com Data, Id. Risco, Id. Ação e Registro. Na fase de planejamento, pode ficar vazia (com linhas em branco) ou registrar ações já executadas. Nas fases seguintes, registre eventos e ações efetivamente realizados, com datas reais informadas pelo usuário.

### 4. Aprovação e assinatura

Texto fixo com referência ao art. 32 da Resolução TRE-ES nº 63/2023 e bloco de assinaturas. Planejamento e seleção do fornecedor: equipe de planejamento. Gestão do contrato: equipe de gestão (gestor e três fiscais), gerando nova versão a partir da anterior sempre que houver novos registros.

## 4. Como identificar riscos

Percorra o ETP e o TR e pergunte, para cada fase, o que pode impedir o resultado. Categorias que costumam render riscos relevantes em contratações de TIC:

1. **Planejamento** — demanda mal estimada; especificação restritiva ou insuficiente; pesquisa de preços frágil; ausência de recursos orçamentários; atraso na instrução processual.
2. **Seleção do fornecedor** — impugnações e pedidos de esclarecimento; certame deserto ou fracassado; proposta inexequível; recursos que suspendam o certame.
3. **Gestão do contrato** — atraso na implantação; descumprimento de níveis de serviço; indisponibilidade da solução; falhas de segurança ou incidentes com dados pessoais; dependência tecnológica e aprisionamento ao fornecedor; descontinuidade no fim da vigência; falta de capacitação dos usuários ou fiscais; variação cambial ou de consumo em modelos sob demanda.

Esses itens são pontos de partida para a análise, não uma lista a ser copiada: inclua apenas os riscos que se aplicam ao objeto, com P e I justificados pelo contexto. Os riscos de dependência tecnológica apontados no item 7.1 do ETP e as estratégias da Seção II do ETP devem ter correspondência no MGR.

## 5. Erros frequentes

1. P × I calculado errado ou divergente entre as tabelas dos itens 1 e 2.
2. Riscos genéricos copiados do modelo sem relação com o objeto.
3. Risco de nível alto sem ação preventiva.
4. Ações sem responsável ou com responsável genérico ("Tribunal").
5. Confundir ação preventiva com ação de contingência.
6. Ação preventiva que exige cláusula ausente no TR.
7. Datas e registros de acompanhamento inventados.
