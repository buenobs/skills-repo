# Referência de sintaxe Markdown

Índice:
1. Cabeçalhos
2. Ênfase
3. Listas
4. Links e imagens
5. Código
6. Tabelas
7. Citações
8. Notas de rodapé
9. Listas de tarefas
10. Escape e caracteres especiais
11. HTML embutido
12. Quebras e separadores

## 1. Cabeçalhos

Use `#` a `######` para níveis 1 a 6. Deixe uma linha em branco antes e depois. Não pule níveis (não vá de `##` direto para `####`).

## 2. Ênfase

a. Itálico: `*texto*` ou `_texto_`.
b. Negrito: `**texto**`.
c. Negrito e itálico: `***texto***`.
d. Tachado: `~~texto~~`.

## 3. Listas

Listas ordenadas usam `1.`, `2.`. O renderizador renumera automaticamente, mas escreva os números corretos no fonte para legibilidade.

Para o padrão de letras (`a.`, `b.`) e romanos (`i.`, `ii.`), o Markdown padrão não os renumera nativamente; escreva-os como texto literal no início da linha. Isso mantém a preferência de estilo mesmo sem suporte nativo.

Subitens: recue quatro espaços (ou dois, conforme o renderizador) sob o item pai.

## 4. Links e imagens

a. Link inline: `[texto](https://exemplo.com)`.
b. Link com título: `[texto](https://exemplo.com "título")`.
c. Link de referência: `[texto][ref]` e, em outra linha, `[ref]: https://exemplo.com`.
d. Imagem: `![texto alternativo](caminho/imagem.png)`.

Nunca invente URLs. Use marcador `[preencher: url]` se desconhecida.

## 5. Código

Inline: use crase simples, `` `comando` ``.

Bloco: use três crases com o identificador da linguagem:

```python
def exemplo():
    return True
```

Linguagens comuns: `python`, `javascript`, `bash`, `sql`, `json`, `html`, `yaml`, `batch`.

## 6. Tabelas

```
| Coluna A | Coluna B | Coluna C |
|----------|----------|----------|
| valor 1  | valor 2  | valor 3  |
```

Alinhamento pela linha separadora: `:---` (esquerda), `:---:` (centro), `---:` (direita). Alinhe as colunas no fonte para facilitar edição.

## 7. Citações

Use `>` no início da linha. Aninhe com `>>`. Para transcrições longas, use um bloco por parágrafo com `>` em cada linha.

## 8. Notas de rodapé

```
Texto com referência.[^1]

[^1]: Conteúdo da nota de rodapé.
```

Útil para referências jurídicas, legislação e citações de acórdãos.

## 9. Listas de tarefas

```
- [ ] Tarefa pendente
- [x] Tarefa concluída
```

Esta é uma exceção legítima ao uso de bullets, pois a sintaxe de checkbox exige o marcador `-`.

## 10. Escape e caracteres especiais

Use `\` antes de caracteres que seriam interpretados como sintaxe: `\* \_ \# \` \[ \] \( \)`. Ex.: `\*` renderiza um asterisco literal.

## 11. HTML embutido

Markdown aceita HTML para casos que a sintaxe não cobre (ex.: `<sub>`, `<sup>`, `<br>`, `<details>`). Use com moderação e apenas quando necessário, pois reduz a portabilidade.

```
<details>
<summary>Clique para expandir</summary>

Conteúdo oculto.

</details>
```

## 12. Quebras e separadores

a. Quebra de linha simples: termine a linha com dois espaços ou use `<br>`.
b. Novo parágrafo: deixe uma linha em branco.
c. Linha horizontal: `---`, `***` ou `___` isolados em uma linha.
