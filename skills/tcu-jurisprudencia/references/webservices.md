# Webservices oficiais do TCU — referência de campos e endpoints

Fonte: https://sites.tcu.gov.br/dados-abertos/webservices-tcu/ (página oficial
de dados abertos do TCU). Todos os endpoints abaixo são públicos, não exigem
autenticação e devem ser acessados com a ferramenta de fetch de URL do
ambiente (não via `curl`/bash — bloqueado pelo proxy de sandbox em testes).

Observação: "Pode ser que alguns serviços fiquem indisponíveis das 20h às 21h"
(manutenção diária informada pelo próprio TCU).

## 1. Acórdãos (o principal para "inteiro teor")

```
GET https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos?inicio={inicio}&quantidade={quantidade}
```

- `inicio`: índice de referência (0-based) na lista de acórdãos disponíveis.
- `quantidade`: quantos acórdãos retornar a partir de `inicio`.
- A lista vem ordenada dos acórdãos mais recentes para os mais antigos (testado
  em 2026-07-05: os primeiros itens eram acórdãos de junho/2026). Não há
  parâmetro de busca por palavra-chave, ano específico ou relator — é preciso
  paginar e filtrar do lado do cliente.

Campos de cada item retornado:
- `key`: chave do acórdão no banco (ex.: `ACORDAO-COMPLETO-2768308`)
- `tipo`: tipo do acórdão
- `anoAcordao`: ano de expedição
- `titulo`: título (ex.: "ACÓRDÃO 1519/2026 ATA 22/2026 - PLENÁRIO")
- `numeroAcordao`: número do acórdão
- `numeroAta`: número da ata da sessão
- `colegiado`: colegiado (Plenário, 1ª Câmara, 2ª Câmara)
- `dataSessao`: data da sessão (DD/MM/AAAA)
- `relator`: nome do relator
- `situacao`: situação (ex.: "OFICIALIZADO")
- `sumario`: sumário/ementa da decisão — bom proxy para filtrar por tema
- `urlArquivo`: URL para o arquivo em formato DOC (retorna texto ao ser
  buscado com a ferramenta de fetch)
- `urlArquivoPdf`: URL para o arquivo em formato PDF — **ao buscar essa URL
  com a ferramenta de fetch, o conteúdo já vem extraído como texto puro,
  contendo relatório, voto e acórdão na íntegra**. Esta é a forma mais direta
  de obter o inteiro teor de uma decisão.
- `urlAcordao`: link para a página do acórdão no sistema de pesquisa
  integrada (`pesquisa.apps.tcu.gov.br`) — útil para citar/compartilhar um
  link "oficial", mas essa página em si é uma SPA em JavaScript (não dá para
  extrair texto dela via fetch simples).

### Exemplo real (testado)
```json
{
  "key": "ACORDAO-COMPLETO-2768308",
  "tipo": "ACÓRDÃO",
  "anoAcordao": "2026",
  "titulo": "ACÓRDÃO 1519/2026 ATA 22/2026 - PLENÁRIO",
  "numeroAcordao": "1519",
  "numeroAta": "22/2026",
  "colegiado": "Plenário",
  "dataSessao": "10/06/2026",
  "relator": "MARCOS BEMQUERER",
  "situacao": "OFICIALIZADO",
  "sumario": "MONITORAMENTO. ESTRUTURA E PRÁTICAS DE GOVERNANÇA NA ÁREA DE TECNOLOGIA E SEGURANÇA DA INFORMAÇÃO DO INSTITUTO NACIONAL DE COLONIZAÇÃO E REFORMA AGRÁRIA - INCRA...",
  "urlArquivo": "https://contas.tcu.gov.br/sagas/SvlVisualizarRelVotoAcRtf?codFiltro=SAGAS-SESSAO-ENCERRADA&seOcultaPagina=S&item0=910704",
  "urlArquivoPdf": "https://contas.tcu.gov.br/sagas/SvlVisualizarRelVotoAc?codFiltro=SAGAS-SESSAO-ENCERRADA&seOcultaPagina=S&item0=910704",
  "urlAcordao": "https://contas.tcu.gov.br/pesquisaJurisprudencia/#/detalhamento/11/*/KEY:%22ACORDAO-COMPLETO-2768308%22/DTRELEVANCIA%2520desc%252C%2520NUMACORDAOINT%2520desc/false/1/false"
}
```

## 2. Atos normativos (Instruções Normativas, Portarias, Decisões Normativas, Resoluções, Resoluções Administrativas)

```
GET https://dados-abertos.apps.tcu.gov.br/api/atonormativo/recupera-atos-normativos
```

Campos principais: `tipo`, `anoAtoNormativo`, `colegiado`, `dataSessao`,
`dataExpedicao`, `dataDou`, `ementa`, `numeroAto`, `situacao` (revogado ou
não), `alteradoPelaNorma`/`normasAlteradasPorEsta`/`revogadaPelaNorma`/
`normasRevogadasPorEsta` (listas de relacionamentos entre normas),
`urlArquivo` (DOC) e `textoDocumento` (link para o texto no sistema de
pesquisa integrada).

## 3. Consulta consolidada de Pessoa Jurídica (certidões)

```
GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/tipos-certidoes
GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/{cnpj}?seEmitirPDF=(true|false)
```
Retorna certidões consolidadas de uma pessoa jurídica (CNPJ), incluindo as
emitidas pelo TCU.

## 4. Sanções e condenações (idoneidade)

### Responsáveis inabilitados (impedidos de cargo em comissão/função de confiança)
```
POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-inabilitados
Body: {"parteNome": "...", "cpf": "...", "uf": "...", "municipio": "..."}
```

### Licitantes inidôneos (impedidos de licitar)
```
POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-inidoneos
Body: {"parteNome": "...", "cpf": "...", "cnpj": "...", "uf": "...", "municipio": "..."}
```

### Contas julgadas irregulares — CADIRREG
```
POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-contas-irregulares
Body: {"parteNome": "...", "cpf": "...", "cnpj": "...", "uf": "...", "municipio": "..."}
```

### Contas julgadas irregulares com possível implicação eleitoral
```
POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-fins-eleitorais
Body: {"parteNome": "...", "cpf": "...", "uf": "...", "municipio": "..."}
```

Todos retornam uma lista com `numeroProcessoFormatado`, `nome`,
`numeroAcordaoFormatado`, `dataAcordao`, `dataTransitoEmJulgado`,
`dataFinalSancao`, `linkDeliberacoesProcesso` (link direto ao processo na
pesquisa integrada) e `linkAcompanhamentoProcesso`.

Envie apenas os campos de filtro que você realmente tem — o body aceita um
subconjunto dos campos.

## 5. Solicitações do Congresso Nacional

```
GET https://contas.tcu.gov.br/ords/api/publica/scn/pedidos_congresso
GET https://contas.tcu.gov.br/ords/api/publica/scn/pedidos_congresso/{numero_processo_sem_pontuacao}
```
Retorna pedidos do Congresso Nacional ao TCU (tipo, número, data de
aprovação, assunto, autor, processo no TCU, link para a proposição).
A listagem geral é paginada; a chave `next` no retorno indica a próxima
página.

## 6. Pautas das sessões

```
GET http://dados-abertos.apps.tcu.gov.br/api/pautassessao
```
Lista de processos pautados para julgamento nas sessões colegiadas.

## 7. Cálculo de débito (Selic + juros)

```
POST https://divida.apps.tcu.gov.br/api/publico/calculadora/calcular-saldos-debito
```
Recebe uma lista de parcelas (data, valor, indicativo débito/crédito) e
devolve saldo de débito, variação Selic, juros e saldo total. Datas no
formato `DD/MM/AAAA`.

## 8. Downloads em massa (CSV) de jurisprudência

O TCU também disponibiliza a jurisprudência completa (Acórdãos, Jurisprudência
Selecionada, Publicações, Súmulas, Respostas a Consultas) em arquivos CSV para
download em `https://sites.tcu.gov.br/dados-abertos/jurisprudencia/`. Essa
página é renderizada via JavaScript e os links de download variam por ano —
se o usuário quiser um dump completo em vez de consultar via API, considere
usar o Claude in Chrome para navegar até essa página e capturar os links de
download reais, em vez de tentar adivinhar a URL do arquivo CSV.

## O que NÃO existe (não tente adivinhar)

- Não há endpoint oficial documentado de **busca textual completa por
  palavra-chave** entre relatório/voto/acórdão de todos os acórdãos — isso só
  existe na interface `pesquisa.apps.tcu.gov.br`, que é uma aplicação
  JavaScript (SPA) e não responde a fetch simples de URL (retorna apenas o
  esqueleto HTML pedindo JavaScript). Para uma busca desse tipo, a alternativa
  recomendada é WebSearch restrita aos domínios do TCU, ou navegação via
  Claude in Chrome quando disponível.
- Não invente parâmetros de busca (ex.: `?relator=` ou `?assunto=`) para o
  endpoint `recupera-acordaos` — eles não existem na documentação oficial e
  não têm efeito.
