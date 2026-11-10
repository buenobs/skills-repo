---
name: "mapa-mental-constructor"
description: "Converte conteúdo em mapa mental em texto simples (#, ##, ###, -) pronto para colar no XMind. Use quando pedirem mapa mental para XMind ou com títulos Markdown, em vez de tabulações."
---

# Mapa Mental Constructor (XMind)

Transforma o conteúdo fornecido pelo usuário em um mapa mental escrito em texto simples, pronto para copiar e colar no XMind.

## Quando usar

Use esta skill quando o usuário pedir um mapa mental para o XMind, ou um mapa mental em texto com hierarquia por títulos Markdown (#, ##, ###) e tópicos com hífen. Para mapas em outline com tabulações literais, use a skill mapa-mental-construtor.

## Processo

1. Leia e analise todo o conteúdo fornecido antes de escrever.
2. Identifique o tema central e os temas reais que organizam o conteúdo.
3. Escolha a melhor ordem dos ramos (lógica, cronológica, causal ou do geral para o específico, conforme o conteúdo).
4. Monte a hierarquia e entregue somente o mapa.

## Regras de estrutura

1. Use exatamente um título principal começando com `#`.
2. Use `##` para os ramos principais.
3. Use `###` para os sub-ramos.
4. Use `-` para os tópicos finais.
5. Use dois espaços antes de `-` para criar um nível adicional de subtópicos.
6. Mantenha uma hierarquia lógica e consistente.
7. Não use tabelas, colunas, caracteres gráficos, emojis ou desenhos.
8. Não use negrito, itálico, links ou formatação Markdown adicional.
9. Não numere os tópicos manualmente.
10. Não escreva introdução, conclusão ou explicações fora do mapa.
11. Cada tópico deve ser curto, claro e específico.
12. Organize as informações por temas reais, evitando categorias genéricas como "Outros", "Diversos" ou "Informações".
13. Coloque cada ideia em uma linha separada.
14. Preserve nomes próprios, datas, números, definições e relações importantes.
15. Não invente informações. Quando algo não estiver disponível, omita ou escreva "não informado".
16. Evite repetir a mesma informação em diferentes ramos.
17. Use o mesmo idioma do conteúdo fornecido.

## Formato obrigatório de saída

```
# Tema central
## Ramo principal
### Subtema
- Informação específica
- Outra informação específica
  - Detalhe complementar

## Outro ramo principal
- Informação específica
```

## Entrega

Entregue somente o mapa, em texto simples, preferencialmente dentro de um único bloco de código para facilitar a cópia, sem nenhum comentário antes ou depois.

## Verificação final

Antes de entregar, confira:

1. Há um único `#`.
2. Nenhuma linha usa negrito, itálico, link, emoji, tabela ou numeração manual.
3. Nenhum ramo se chama "Outros", "Diversos" ou "Informações".
4. Nenhuma informação foi inventada ou repetida entre ramos.
5. Não há texto fora do mapa.