---
name: notebooklmskill
description: Acesso ao Google NotebookLM pelo servidor local gemini-notebook — listar cadernos pelo número, consultar fontes, perguntar com citações, criar cadernos, adicionar fontes (sites, YouTube, PDF, texto), pesquisar na web, gerar podcast, vídeo, apresentação, infográfico, relatório, quiz, flashcards, tabela e mapa mental, e baixar os resultados. Use quando o usuário citar NotebookLM, caderno ou notebook do NotebookLM, "caderno 5", "nb", ou pedir "crie um podcast sobre X", "gere um quiz", "faça um mapa mental", "resuma estas fontes", "adicione estas fontes", "pesquise sobre X no NotebookLM", "liste meus cadernos".
---

# NotebookLM pelo gemini-notebook

Todo acesso ao NotebookLM passa pelo **gemini-notebook**, um servidor local que usa a conta Google do usuário (repositório privado buenobs/gemini-notebook, pasta `D:\MDOCS\DEV\gemini-notebook`, porta 8788).

Não instale nem use a CLI `notebooklm` nem a biblioteca `notebooklm-py` diretamente, e não faça login por outro caminho. O servidor mantém uma única sessão Google e renova os cookies sozinho. Uma segunda sessão com os mesmos cookies derruba a primeira.

Os cadernos têm **número fixo** (1, 2, 3...), e o usuário se refere a eles pelo número. Em qualquer comando, no lugar do número também serve um trecho único do título.

## 1. Antes de começar

1. Confira se o servidor está no ar:

```powershell
D:\MDOCS\DEV\gemini-notebook\nb.bat lista
```

2. Se aparecer "O servidor não está rodando", peça ao usuário para abrir `D:\MDOCS\DEV\gemini-notebook\iniciar.bat` e deixar a janela aberta. Também é possível abri-lo numa aba de terminal visível ao usuário. Não suba o servidor escondido em segundo plano.
3. Se aparecer erro de login (401, "login inválido ou vencido"), peça ao usuário para rodar `login.bat` na mesma pasta, fazer o login na janela do Chrome e depois reiniciar o `iniciar.bat`. A senha é sempre digitada pelo usuário, nunca pela IA.
4. Em outra máquina, se a pasta não existir: clonar buenobs/gemini-notebook, criar a venv (`python -m venv .venv` e `.venv\Scripts\python.exe -m pip install -r requirements.txt`) e seguir o README.

Nos exemplos abaixo, `nb` é `D:\MDOCS\DEV\gemini-notebook\nb.bat`. Dentro da pasta, no PowerShell, use `.\nb.bat`.

## 2. Comandos

### 2.1 Consultar (executar sem pedir confirmação)

| Tarefa | Comando |
|---|---|
| Listar cadernos numerados | `nb lista` |
| Fontes de um caderno, numeradas | `nb fontes 5` |
| Perguntar ao caderno (com citações) | `nb pergunta 5 "pergunta"` |
| Perguntar só a algumas fontes | `nb pergunta 5 -f 1,3 "pergunta"` |
| Artefatos (áudio, vídeo, quiz...) e status | `nb artefatos 5` |
| Andamento de uma geração | `nb status 5 <task_id>` |
| Tipos de geração e opções | `nb tipos` |

### 2.2 Criar e alimentar (executar quando o usuário pedir; não precisa confirmar de novo)

| Tarefa | Comando |
|---|---|
| Criar caderno (mostra o número novo) | `nb criar "Título"` |
| Adicionar sites, YouTube ou arquivos | `nb adicionar 5 https://... C:\pasta\doc.pdf` |
| Adicionar texto colado | `nb texto 5 "Título" "conteúdo"` |
| Pesquisa na web, rápida, importando as fontes | `nb pesquisa 5 "consulta"` |
| Pesquisa profunda | `nb pesquisa 5 "consulta" --profunda` |
| Pesquisar sem importar | `nb pesquisa 5 "consulta" --sem-importar` |

Fontes recém-adicionadas levam alguns minutos para ficar prontas. Confira com `nb fontes 5`: as que ainda não estão prontas aparecem com `[processing]`, e as recusadas com `[error]`.

### 2.3 Gerar e baixar (confirmar com o usuário antes)

Gerar é demorado e pode falhar por limite do Google. Baixar grava arquivo no disco.

```powershell
nb gerar 5 audio "instruções" --idioma pt-BR
nb gerar 5 quiz "foco em prazos" -f 1,2 --idioma pt-BR --opcao quantity=fewer --opcao difficulty=easy
nb gerar 5 slide-deck --opcao deck_format=detailed --esperar
nb status 5 <task_id>
nb baixar 5 audio C:\saida\podcast.mp3
nb baixar 5 slide-deck C:\saida\slides.pptx --formato pptx
nb baixar 5 quiz C:\saida\quiz.md --formato markdown
```

| Tipo | Opções (`--opcao chave=valor`) | Baixa como |
|---|---|---|
| `audio` (podcast) | `audio_format=deep-dive\|brief\|critique\|debate`, `audio_length=short\|default\|long` | .mp3 |
| `video` | `video_format=explainer\|brief`, `style=auto\|classic\|whiteboard\|kawaii\|anime\|watercolor\|...` | .mp4 |
| `cinematic-video` | — | .mp4 |
| `slide-deck` | `deck_format=detailed\|presenter`, `deck_length=default\|short` | .pdf ou .pptx (`--formato pptx`) |
| `infographic` | `orientation=landscape\|portrait\|square`, `detail=concise\|standard\|detailed` | .png |
| `report` | `report_format=briefing-doc\|study-guide\|blog-post\|custom` | .md |
| `quiz` | `difficulty=easy\|medium\|hard`, `quantity=fewer\|standard\|more` | .json, ou `--formato markdown\|html` |
| `flashcards` | iguais às do quiz | .json, ou `--formato markdown\|html` |
| `data-table` | a descrição vai nas instruções | .csv |
| `mind-map` | sai na hora, sem espera | .json |

a. Use sempre `--idioma pt-BR` para conteúdo em português (o padrão é inglês).
b. Tempos aproximados: áudio de 10 a 20 min, vídeo de 15 a 45 min, quiz e flashcards de 5 a 15 min.
c. `--esperar` acompanha até terminar (máximo de 60 min). Sem ele, o comando devolve o `task_id`; acompanhe com `nb status`.
d. `nb baixar` baixa o artefato mais recente daquele tipo no caderno.

### 2.4 Destrutivo ou fora do comum (sempre confirmar antes)

O que não tem comando próprio sai pela chamada livre à API completa (`/nlm/v1`). Nela, `{5}` vira o id do caderno 5:

```powershell
nb api GET "notebooks/{5}/notes"
nb api POST "notebooks/{5}/notes" title=Resumo "content=texto da nota"
nb api POST "notebooks/{5}/chat/configure" chat_mode=learning_guide
nb api DELETE "notebooks/{5}/sources/<id_da_fonte>"
nb api DELETE "notebooks/{5}"
```

O corpo vai como pares `chave=valor` ou como `@arquivo.json`. Não passe JSON entre aspas: o PowerShell tira as aspas internas ao chamar o `.bat`. `true`, `false`, números e listas como `[1,2]` viram JSON.

Apagar caderno, fonte, nota ou artefato não tem volta: confirme com o usuário dizendo o que será apagado.

## 3. Acesso por HTTP (quando não houver terminal)

Todas as rotas exigem o cabeçalho `Authorization: Bearer <GEMINI_NOTEBOOK_KEY>`. A chave está no `.env` da pasta do gemini-notebook; nunca a escreva em respostas, notas ou arquivos compartilhados.

a. `GET /cadernos` — lista `[{n, titulo, fontes, id}]`.<br>
b. `GET /cadernos/{ref}`, `/cadernos/{ref}/fontes` e `/cadernos/{ref}/artefatos`.<br>
c. `POST /cadernos/{ref}/perguntar` com `{"pergunta": "...", "fontes": [1, 3]}`.<br>
d. `GET /v1/models` e `POST /v1/chat/completions` — formato OpenAI, com o caderno como modelo (`"5"` ou `"5. Título"`).<br>
e. `/nlm/v1/notebooks/{id}/...` — API completa: `sources/url`, `sources/text`, `sources/file`, `research`, `artifacts`, `artifacts/download`, `notes`, `chat`.

Exemplo no PowerShell:

```powershell
$k = ((Get-Content D:\MDOCS\DEV\gemini-notebook\.env | Select-String '^GEMINI_NOTEBOOK_KEY=').Line -split '=',2)[1]
$h = @{Authorization="Bearer $k"}
(Invoke-RestMethod http://127.0.0.1:8788/cadernos -Headers $h).cadernos
```

## 4. Fluxos comuns

1. **Pesquisa até podcast:** `nb criar "Pesquisa: tema"` → `nb pesquisa N "tema"` (ou `nb adicionar N url1 url2`) → `nb fontes N` até todas ficarem prontas → confirmar com o usuário → `nb gerar N audio "ângulo" --idioma pt-BR` → `nb status N <task_id>` → `nb baixar N audio podcast.mp3`.
2. **Análise de documentos:** `nb criar "Análise: projeto"` → `nb adicionar N doc1.pdf doc2.docx` → `nb pergunta N "resuma os pontos-chave"`.
3. **Estudo:** `nb gerar N flashcards --idioma pt-BR` e `nb gerar N quiz --idioma pt-BR` → `nb baixar N quiz quiz.md --formato markdown`.
4. **Apresentação:** `nb gerar N slide-deck --opcao deck_format=detailed --idioma pt-BR --esperar` → `nb baixar N slide-deck slides.pptx --formato pptx`.

## 5. Numeração

a. O número de cada caderno é fixo. Caderno novo recebe o próximo número livre. Caderno excluído deixa um buraco, sem renumerar os outros.<br>
b. `nb renumera` fecha os buracos (1..N). Só use se o usuário pedir, porque muda os números que ele já conhece.<br>
c. As fontes são numeradas por ordem de inclusão no caderno.

## 6. Erros

| Mensagem | Causa | O que fazer |
|---|---|---|
| "O servidor não está rodando" | `iniciar.bat` fechado | Pedir para abrir o `iniciar.bat` |
| 401 / 503 "login" | Sessão Google vencida | `login.bat` e reiniciar o servidor |
| "corresponde a mais de um caderno" | Trecho de título ambíguo | Usar o número |
| 502 "Failed to add source" | Site inacessível, com login ou vazio | Tentar outra URL ou baixar e enviar o arquivo |
| 400 "Unsupported language" | Código de idioma inválido | Usar `pt-BR`, `en`, `es`... |
| 429 ou falha na geração | Limite do Google | Esperar de 5 a 10 min e tentar de novo |

## 7. Cuidados

a. Uso não oficial (engenharia reversa do site): pode quebrar quando o Google mudar o NotebookLM.<br>
b. Não envie ao NotebookLM conteúdo sigiloso ou institucional restrito sem autorização do usuário.<br>
c. As respostas do NotebookLM são material de trabalho: confira as citações antes de usar.
