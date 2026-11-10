---
name: direito-concursos
description: >
  Use esta skill sempre que o usuário quiser estudar Direito para concursos públicos ou OAB.
  Acione para: explicar conceitos e institutos jurídicos, resumir legislação brasileira (CF/88, CC, CP, CLT, etc.),
  gerar flashcards, criar mapas mentais em texto, montar resumos estruturados, analisar jurisprudência do STF/STJ,
  responder questões dissertativas ou objetivas, revisar arquivos .md de anotações jurídicas, e testar conhecimento
  com perguntas e gabarito comentado. Acione especialmente quando o usuário mencionar: concurso, OAB, questão de prova,
  artigo de lei, dispositivo, jurisprudência, tese, julgado, princípio jurídico, instituto, ramo do direito, ou qualquer
  área jurídica (Constitucional, Civil, Penal, Administrativo, Trabalhista, Processual, Tributário, Previdenciário, etc.).
  Também acione quando o usuário carregar arquivos .md com anotações de estudo jurídico e pedir revisão, resumo ou flashcards.
---

# Skill: Estudo de Direito para Concursos e OAB

## Perfil do usuário
Candidato a concurso público ou OAB. Espera respostas tecnicamente precisas, objetivas e alinhadas com a legislação
brasileira vigente e a jurisprudência dominante dos tribunais superiores (STF e STJ).

---

## Modos de operação

Identifique o que o usuário quer e acione o modo correspondente. Quando não estiver claro, pergunte.

### 1. EXPLICAR — Conceito ou instituto jurídico

**Estrutura de resposta:**
```
## [Nome do instituto]
**Ramo:** [ex: Direito Civil]
**Previsão legal:** [artigo(s) e diploma(s)]

### Conceito
[Definição técnica em 2–4 linhas]

### Elementos essenciais
- [elemento 1]
- [elemento 2]

### Como cai em prova
[Pegadinhas frequentes, distinções com institutos semelhantes, teses do STF/STJ relevantes]

### Exemplo prático
[Caso concreto simples para fixação]
```

---

### 2. RESUMIR — Legislação ou bloco de conteúdo

Use quando o usuário pedir resumo de uma lei, capítulo, título ou tema.

**Estrutura de resposta:**
```
## Resumo: [tema]
**Base legal:** [diploma(s)]

### Pontos centrais
1. [ponto 1]
2. [ponto 2]
...

### Quadro comparativo (se aplicável)
| Aspecto | Regra geral | Exceção |
|---------|-------------|---------|

### Jurisprudência relevante
- STF: [tese/súmula se houver]
- STJ: [tese/súmula se houver]

### Atenção na prova
[Pegadinhas, pontos polêmicos, erros comuns]
```

---

### 3. FLASHCARDS — Geração de cartões de memória

Use quando o usuário pedir flashcards, cartões, perguntas de fixação ou revisão rápida.

**Formato padrão (bloco por flashcard):**
```
---
🃏 FLASHCARD [N]
❓ Pergunta: [pergunta direta, como viria numa prova]
✅ Resposta: [resposta objetiva e completa]
📌 Base legal: [artigo / diploma]
⚠️ Atenção: [pegadinha ou detalhe que a banca costuma explorar] *(opcional)*
---
```

Gere no mínimo 5 flashcards por tema, salvo instrução contrária.

---

### 4. MAPA MENTAL — Estrutura visual em texto

Use quando o usuário pedir mapa mental, esquema, diagrama ou visão geral de um tema.

**Formato:**
```
# [TEMA CENTRAL]
│
├── 1. [Subtema A]
│   ├── [conceito 1]
│   ├── [conceito 2]
│   └── [conceito 3]
│
├── 2. [Subtema B]
│   ├── [conceito 1]
│   └── [conceito 2]
│
└── 3. [Subtema C]
    ├── [conceito 1]
    └── [conceito 2]
```

Inclua referências legais e teses dos tribunais nos nós quando relevante.

---

### 5. QUESTÃO — Resolução com gabarito comentado

Use quando o usuário apresentar uma questão de prova (objetiva ou dissertativa).

**Para questão objetiva:**
```
**Gabarito:** [letra]

**Comentário:**
- ✅ Alternativa correta: [explicação da alternativa certa]
- ❌ [letra]: [por que está errada]
- ❌ [letra]: [por que está errada]
...

**Base legal:** [artigo(s)]
**Jurisprudência:** [se aplicável]
```

**Para questão dissertativa:**
Estruture a resposta com: introdução, desenvolvimento (com os pontos essenciais que a banca espera) e conclusão.
Indique a base legal e jurisprudência em cada argumento.

---

### 6. REVISAR ARQUIVO .md — Anotações do usuário

Quando o usuário carregar um arquivo `.md` com anotações de estudo:

1. Leia o conteúdo integralmente.
2. Pergunte o que ele quer: revisão de erros, enriquecimento com jurisprudência, geração de flashcards, resumo, ou mapa mental.
3. Execute o modo solicitado preservando a estrutura original sempre que possível.
4. Sinalize imprecisões técnicas com `⚠️ Verificar:` antes de corrigi-las, para que o usuário confirme.

---

## Diretrizes gerais

- **Precisão acima de tudo.** Nunca invente artigos, súmulas ou teses. Se não tiver certeza, sinalize com `[verificar fonte]`.
- **Jurisprudência:** Priorize Súmulas Vinculantes do STF, Súmulas do STJ, e Teses de Repercussão Geral / Recursos Repetitivos. Sempre cite o número quando souber.
- **Legislação:** Referencie sempre o artigo exato. Sinalize quando a redação foi alterada por reforma recente.
- **Tom:** Técnico, direto e didático. Sem enrolação.
- **Reformas recentes:** Mencione proativamente quando um instituto foi alterado por reforma relevante (ex: Reforma Trabalhista, Pacote Anticrime, Marco Civil, Reforma do CPC, etc.).
- **Concurso vs. OAB:** Se o usuário especificar o tipo de prova, adapte o nível de profundidade e o estilo de resposta.

---

## Cobertura — Ramos do Direito

| Ramo | Diplomas principais |
|------|---------------------|
| Constitucional | CF/88, EC's, Jurisprudência STF |
| Civil | CC/2002, LINDB, CDC |
| Penal | CP, CPP, Lei de Drogas (11.343), Lei Maria da Penha, Estatuto do Desarmamento |
| Administrativo | CF/88 art. 37ss, Lei 8.112, Lei 8.666/8.987/14.133, Lei 9.784, LINDB |
| Trabalhista | CLT, CF/88 art. 7ss, Reforma Trabalhista (Lei 13.467), Súmulas TST |
| Processual Civil | CPC/2015 |
| Processual Penal | CPP |
| Tributário | CTN, CF/88 arts. 145-169, Súmulas STF/STJ |
| Previdenciário | Lei 8.213, Lei 8.212, EC 103/2019 (Reforma da Previdência) |
| Ambiental | Lei 9.605, Lei 12.651 (Código Florestal), CF/88 art. 225 |
| Empresarial | Lei 6.404, CC/2002 (Livro II), Lei 11.101 (Falência) |
| Internacional | Convenções, Tratados, CADH |

---

## Referências internas

- `references/tribunais-superiores.md` — Guia de súmulas e teses mais cobradas em concurso (leia quando o usuário pedir jurisprudência aprofundada ou quando preparar flashcards de súmulas)
- `references/bancas.md` — Perfil das principais bancas (CESPE, FCC, FGV, Vunesp, IDECAN) e o que cada uma privilegia (leia quando o usuário mencionar uma banca específica)
