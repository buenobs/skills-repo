---
name: markdown-docs
description: Use esta skill sempre que o usuário quiser criar, estruturar, redigir ou revisar documentos em Markdown (.md) — relatórios, notas técnicas, resumos, guias, documentação, artigos, README, atas, pareceres ou qualquer entregável textual em formato Markdown. Acione mesmo que o usuário não diga "markdown" explicitamente, desde que peça um documento de texto sem exigir outro formato (docx, pdf, pptx). Também acione quando pedir para converter um rascunho ou conteúdo solto em um documento .md bem estruturado, ou para revisar/melhorar a formatação de um arquivo Markdown existente. NÃO acione quando o usuário exigir explicitamente Word (.docx), PDF, apresentação (.pptx) ou planilha (.xlsx) — nesses casos use a skill correspondente.
---

# Markdown Docs

Skill para criação e revisão de documentos em Markdown bem estruturados, legíveis e prontos para uso ou publicação. Markdown é o formato padrão de entrega para documentos textuais.

## Quando usar

Use esta skill para produzir qualquer documento textual em `.md`: relatórios, notas técnicas, resumos executivos, guias, documentação, artigos, README, atas, pareceres, checklists estruturados. Não use quando o usuário exigir outro formato (docx, pdf, pptx, xlsx).

## Regras invioláveis

1. Nunca invente dados, números, nomes, datas ou citações. Se faltar informação, deixe um marcador explícito de preenchimento (ex.: `[preencher: valor do contrato]`) e sinalize ao usuário o que precisa ser completado.
2. Não use bullets (`-`, `*`, `•`) como padrão. Use enumeração conforme a seção "Estilo de listas" abaixo.
3. Entregue sempre um arquivo `.md` salvo, não apenas texto no chat, quando o pedido for um documento (relatório, guia, parecer etc.). Para respostas conversacionais curtas, mantenha no chat.
4. Preserve o conteúdo do usuário; melhore estrutura e formatação sem alterar o sentido.

## Estilo de listas

Ordem de preferência para enumerações:

a. Letras minúsculas com ponto (`a.`, `b.`, `c.`) — para opções, alternativas ou itens paralelos no mesmo nível.
b. Números com ponto (`1.`, `2.`, `3.`) — para sequências, etapas, prioridades ou rankings onde a ordem importa.
c. Algarismos romanos minúsculos (`i.`, `ii.`, `iii.`) — para subitens dentro de uma lista numerada ou enumerações formais/hierárquicas.

Reserve bullets apenas quando a ordem é irrelevante, os itens são muito curtos (uma ou duas palavras) e não precisarão ser referenciados depois.

Sempre que o fluxo permitir, incorpore listas curtas na prosa (ex.: "há três fatores: primeiro, a; segundo, b; terceiro, c") em vez de quebrar em marcadores.

Mantenha consistência: iniciada uma enumeração com letras, não alterne para números no mesmo nível sem justificativa.

## Estrutura do documento

Um documento bem formado geralmente tem:

1. Título nível 1 (`#`) único, no topo, claro e específico.
2. Linha de metadados quando fizer sentido (autor, data, versão, referência de processo) — sem inventar valores.
3. Sumário/introdução curto quando o documento for longo (acima de ~2 páginas).
4. Seções com hierarquia coerente de headings (`##`, `###`), sem pular níveis.
5. Conclusão, próximos passos ou referências, quando aplicável.

Não crie sumário automático (TOC) com âncoras a menos que solicitado.

## Elementos de formatação

a. Ênfase: use negrito (`**`) com parcimônia, apenas para termos-chave; itálico (`*`) para destaques leves ou títulos de obras.
b. Tabelas: use tabelas Markdown para dados comparativos ou estruturados; alinhe visualmente as colunas no fonte para legibilidade.
c. Código: use crases triplas com identificador de linguagem para blocos; crase simples para termos inline (comandos, nomes de arquivo, variáveis).
d. Citações: use `>` para transcrições ou destaques; nunca reproduza material protegido por direitos autorais além do permitido.
e. Links: use a sintaxe `[texto](url)`; não invente URLs.
f. Separadores: use `---` para dividir seções maiores apenas quando agregar clareza.
g. Notas de rodapé: use a sintaxe `[^1]` quando o documento exigir referências acadêmicas ou jurídicas.

## Boas práticas de escrita

1. Prefira prosa clara a listas fragmentadas; nem tudo precisa virar lista.
2. Uma ideia por parágrafo; parágrafos curtos.
3. Frases na ordem direta e voz ativa.
4. Consistência terminológica ao longo do documento.
5. Quando o documento tiver caráter técnico-jurídico ou institucional, mantenha tom formal e impessoal.

## Fluxo de trabalho

1. Entenda o tipo de documento, o público e o objetivo. Se ambíguo, pergunte antes de redigir.
2. Se houver conteúdo de origem (rascunho, notas, arquivo), leia-o integralmente antes de estruturar.
3. Monte a estrutura de headings antes de preencher o texto de documentos longos.
4. Redija respeitando as regras de estilo de listas e formatação.
5. Salve em `/mnt/user-data/outputs/` com nome descritivo e apresente o arquivo ao usuário.
6. Sinalize marcadores de preenchimento pendentes, se houver.

## Referências

Consulte `references/sintaxe.md` para referência completa da sintaxe Markdown quando precisar de elementos menos comuns (tabelas complexas, notas de rodapé, listas de tarefas, HTML embutido, escape de caracteres).
