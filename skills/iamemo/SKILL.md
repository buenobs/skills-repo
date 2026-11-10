---
name: iamemo
description: Carrega, atualiza e cria páginas de trabalho no IAMemo, a memória de trabalho portátil do usuário no Notion (página IAMemo, database Trabalhos), pelo conector do Notion. Use sempre que o usuário mencionar IAMemo, pedir "atualize o IAMemo", "carregue o trabalho X", "registre no IAMemo", "faça o checkpoint", ou quiser retomar, continuar ou recuperar um trabalho feito em outra máquina ou em outra IA, mesmo sem citar o Notion. Use também para listar trabalhos em andamento, ver o próximo passo de um trabalho e criar um trabalho novo. Não use para buscas gerais no Notion que não envolvam o IAMemo.
---

# IAMemo

O IAMemo é a memória de trabalho do usuário, compartilhada entre máquinas e entre IAs. Cada trabalho tem uma página no database Trabalhos: as IAs leem essa página ao começar e a atualizam ao terminar. Outras IAs dependem do que for escrito aqui, por isso o registro precisa ser fiel e cuidadoso.

## Endereços

a. Página raiz IAMemo (protocolo e modelo de contexto): `3fdb16276e8681bd80abc0370b2dfe23`
b. Database Trabalhos: `39d4ac1c14cf469d9bc3b0291b57f32e`
c. Fonte de dados de Trabalhos: `collection://d3aae1fe-d938-4a20-b1fc-f7f72185aa6c`

Use as ferramentas do conector do Notion (`notion-fetch`, `notion-search`, `notion-query-data-sources`, `notion-update-page`, `notion-create-pages`). Se o conector não estiver disponível, avise o usuário e pare: não tente acessar por outro caminho e não reconstrua o conteúdo de memória.

## Primeiro passo: ler o protocolo

Leia a página raiz antes de agir. O protocolo vive lá e o usuário pode alterá-lo; esta habilidade só resume como aplicá-lo com o conector. Se a página raiz divergir deste texto, siga a página raiz, com uma exceção: a regra do Google Drive, abaixo.

## Google Drive: só com pedido expresso

As regras 6, 7 e 8 da página raiz mandam manter o Google Drive sincronizado. Não faça isso por conta própria nem ofereça: o usuário decidiu atualizar só o Notion, porque outra instância cuida da sincronização com o Drive. Mexa no Drive apenas quando o usuário pedir nessa conversa.

## Ao carregar um trabalho

1. Localize a página na fonte de dados Trabalhos pelo nome. Consulte a fonte de dados em vez de buscar no workspace inteiro, porque a busca geral traz páginas de fora do IAMemo.
2. Se houver mais de uma página parecida, mostre as opções e pergunte qual é. Existem páginas de nome semelhante (por exemplo, duas sobre o conector do Notion), e escrever na errada espalha o contexto.
3. Se não houver nenhuma, pergunte se deve criar uma.
4. Leia a página inteira e apresente um resumo de até 5 linhas com o estado atual e o próximo passo. Aguarde a confirmação do usuário antes de produzir conteúdo.
5. Trate as Decisões tomadas como fechadas. Só as reabra se o usuário pedir expressamente.

Quando a página citar uma pasta ou um repositório, lembre que o trabalho pode estar em outra máquina: confira se o caminho existe aqui antes de presumir que os arquivos estão disponíveis.

## Ao atualizar

Atualize logo que concluir uma entrega relevante ou que o usuário aprovar uma decisão, sem esperar o fim da conversa. A conversa pode acabar sem aviso, e o que não foi registrado se perde.

Faça a menor edição possível:

| Alteração | Comando de `notion-update-page` |
|---|---|
| Status, Última IA, Próximo passo | `update_properties` |
| Trecho de uma seção | `update_content`, com `old_str` curto e exato |
| Nova linha no Registro de sessões, se a seção 8 for a última da página | `insert_content`, com `position` `end` |
| Novo item em Decisões tomadas | `update_content`, ancorado no último item da seção, repetindo-o no `new_str` e acrescentando o novo |

Evite `replace_content`, porque ele reescreve a página inteira e pode alterar seções que só aceitam acréscimos. O histórico de versões do plano gratuito dura só 7 dias, então um item apagado pode não ter volta.

Se já passou um tempo desde a última leitura, leia a página de novo antes de editar: outra IA pode tê-la atualizado.

## Ao encerrar (checkpoint)

Quando o usuário pedir "atualize o IAMemo" ou encerrar o trabalho:

1. Atualize as propriedades Status, Última IA e Próximo passo. Em Última IA, use `Claude`. Os valores de Status são: Não iniciado, Em andamento, Aguardando terceiros, Concluído.
2. Atualize as seções Estado dos documentos, Pendências e próximo passo, e Questões em aberto.
3. Acrescente ao Registro de sessões uma linha no formato `AAAA-MM-DD — Claude — resumo do que foi feito`.
4. Informe ao usuário, com o link da página, o que mudou.

## Ao criar um trabalho

Crie a página na fonte de dados Trabalhos, usando no corpo o Modelo de contexto da página raiz, e preencha só o que já se sabe. Deixe o restante como `[PREENCHER]` em vez de deduzir. Antes de criar, confirme com o usuário e verifique se já não existe página parecida.

## O que registrar

a. Apenas o que foi efetivamente decidido ou produzido. Marque como `[NÃO VERIFICADO]` o que for suposição.
b. Nada de dados pessoais, conteúdo de acesso restrito, tokens ou senhas. Essas páginas são lidas por várias IAs de diferentes provedores.
c. Arquivos pesados (PDF, .docx, planilhas) ficam fora do Notion. Na página, registre só o link ou o caminho, na propriedade Pasta no Drive.
d. Nas páginas, use letras (a., b.) para itens paralelos e números (1., 2.) para sequências. Evite marcadores.
