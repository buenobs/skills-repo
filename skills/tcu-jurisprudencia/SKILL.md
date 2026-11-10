---
name: tcu-jurisprudencia
description: >-
  Consulta a base de dados oficial do Tribunal de Contas da União (TCU) —
  acórdãos, jurisprudência, inteiro teor de decisões, atos normativos,
  súmulas e cadastros de sanções (inidôneos, inabilitados, contas
  irregulares). Use esta habilidade sempre que o usuário pedir para buscar,
  localizar, resumir ou citar um acórdão do TCU, pesquisar jurisprudência do
  TCU sobre um tema (ex.: parcelamento de objeto, sobrepreço,
  terceirização), obter o inteiro teor (relatório, voto e acórdão) de uma
  decisão, verificar se uma empresa ou CPF está na lista de inidôneos ou
  inabilitados do TCU, ou consultar normativos (instruções normativas,
  resoluções, decisões normativas) do TCU. Acione mesmo que o usuário não
  mencione API ou webservice — basta citar TCU, Tribunal de Contas da
  União, acórdão, jurisprudência de controle externo, ou pedir para
  verificar sanções/idoneidade de uma empresa perante o TCU.
---

# Consulta à base do TCU (acórdãos e jurisprudência)

## Por que isso não é uma busca comum na internet

O TCU expõe webservices públicos e oficiais (sem autenticação) que devolvem
metadados estruturados e o **inteiro teor** de acórdãos diretamente em JSON/texto.
Isso é muito mais confiável do que tentar adivinhar o conteúdo de uma decisão a
partir de resumos de terceiros ou memória — e evita qualquer risco de citar um
número, data ou trecho errado. Sempre prefira consultar a base oficial a
responder de memória.

**Nunca invente número de acórdão, relator, data, sumário ou trecho de voto.**
Se a busca não encontrar nada, diga isso claramente ao usuário em vez de
preencher a lacuna com um palpite. Isso vale também para resumos/snippets que
vêm de resultados de WebSearch: eles às vezes parafraseiam ou "completam"
detalhes de forma plausível mas imprecisa. Trate snippets de busca como pistas
para achar o acórdão certo, não como fonte final — sempre confirme o
conteúdo lendo o inteiro teor real (passo 4) antes de citar algo como fato.

## Regra técnica importante: use a ferramenta de fetch de URL, não `curl`/bash

Em ambientes de sandbox (como o Cowork), chamadas diretas via `curl`/`requests`
dentro do shell costumam ser bloqueadas pelo proxy de rede para os domínios do
TCU (`dados-abertos.apps.tcu.gov.br`, `contas.tcu.gov.br` etc.), retornando erro
403 do proxy. Isso já foi testado e confirmado. A ferramenta de fetch de URL
disponível no ambiente (`web_fetch`/`WebFetch`), porém, acessa esses mesmos
endereços normalmente. **Sempre use essa ferramenta para chamar os endpoints
abaixo — nunca tente `curl`/`wget`/`requests` via bash.**

## Fluxo de trabalho

1. **Entenda o que o usuário quer**: um acórdão específico (número/ano/processo
   conhecido), uma busca por tema/palavra-chave, verificação de sanção
   (idoneidade/inabilitação) de uma pessoa/empresa, ou um normativo do TCU.

2. **Busca por tema/palavra-chave (o caso mais comum)**:
   O webservice oficial de acórdãos (passo 3) **não filtra por palavra-chave** —
   ele apenas pagina uma lista ordenada. Por isso, para descobrir *quais*
   acórdãos tratam de um tema, primeiro use a ferramenta de busca na web
   (WebSearch) restringindo aos domínios oficiais, por exemplo:
   `allowed_domains: ["tcu.gov.br", "pesquisa.apps.tcu.gov.br"]` com a query do
   tema do usuário. Isso aproveita a indexação do Google sobre o site do TCU
   para achar números de acórdão/processo candidatos. Depois, confirme os
   dados e obtenha o inteiro teor pelos passos 3 e 4.
   Se a busca na web não trouxer nada útil e o tema for muito amplo, informe ao
   usuário que a busca textual completa por tema exige o site
   `pesquisa.apps.tcu.gov.br` (aplicação em JavaScript) e que, se ele tiver a
   extensão Claude in Chrome conectada, você pode navegar até lá para uma busca
   mais completa — mas isso é um passo opcional, não o padrão.

3. **Consultar/confirmar metadados de acórdãos (webservice oficial)**:
   ```
   GET https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos?inicio={N}&quantidade={M}
   ```
   Busque com a ferramenta de fetch de URL. Retorna uma lista JSON (mais
   recentes primeiro) com campos como `key`, `tipo`, `anoAcordao`, `titulo`,
   `numeroAcordao`, `colegiado`, `dataSessao`, `relator`, `situacao`,
   `sumario`, `urlArquivo` (DOC), `urlArquivoPdf` (PDF/inteiro teor) e
   `urlAcordao` (link para o sistema de pesquisa integrada). Pagine ajustando
   `inicio`/`quantidade` (ex.: 50 a 100 por chamada) e filtre pelo `titulo`/
   `sumario` quando precisar localizar algo por aproximação. Detalhes completos
   de todos os webservices (atos normativos, sanções, pautas, etc.) estão em
   `references/webservices.md` — leia esse arquivo quando precisar de um campo
   ou endpoint que não esteja resumido aqui.

4. **Obter o inteiro teor (relatório + voto + acórdão)**:
   Busque a URL de `urlArquivoPdf` (ou `urlArquivo`) com a ferramenta de fetch
   de URL. Apesar do nome, a ferramenta extrai e devolve o **texto completo**
   do documento (confirmado em testes) — relatório, voto e acórdão na
   íntegra. É essa chamada que responde perguntas como "o que diz o acórdão
   X" ou permite citar trechos literais.

   Se você já sabe o número/ano/colegiado do acórdão (ex.: "Acórdão 1519/2026
   - Plenário") e paginar o webservice desde o índice 0 seria caro (acórdãos
   antigos podem exigir dezenas de chamadas), **e** você tiver a extensão
   Claude in Chrome conectada, um atalho testado é navegar diretamente para
   `https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/{numero}/{ano}/{colegiado}`
   — essa página é uma SPA em JavaScript (não funciona com fetch simples de
   URL), mas o Chrome consegue renderizá-la e você lê o texto oficial
   (sumário, acórdão, relatório, voto) direto na página. Use isso só como
   atalho complementar; a via padrão continua sendo o webservice oficial.

5. **Cite sempre a fonte**: número do acórdão, colegiado, data da sessão,
   relator, e o link (`urlAcordao` e/ou `urlArquivoPdf`). Isso vale tanto para
   respostas no chat quanto para documentos gerados.

6. **Outras consultas da base do TCU** (ver `references/webservices.md` para
   parâmetros exatos):
   - Atos normativos (instruções normativas, resoluções, decisões normativas):
     `GET https://dados-abertos.apps.tcu.gov.br/api/atonormativo/recupera-atos-normativos`
   - Empresas/pessoas inidôneas: `POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-inidoneos`
   - Responsáveis inabilitados: `POST https://certidoes.apps.tcu.gov.br/api/publico/responsaveis-inabilitados`
   - Contas julgadas irregulares (CADIRREG): `POST http