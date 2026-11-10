---
name: decora-norma-loop
description: Treino interativo de memorização de normas jurídicas (lacunas, certo/errado, múltipla escolha), uma questão por vez, com correção e feedback fundamentado. Use quando o usuário quiser memorizar, treinar ou fixar leis, artigos, súmulas ou prazos.
---

# Decora Norma Loop

Transforma textos normativos (leis, artigos, parágrafos, incisos, súmulas, resoluções) em um ciclo interativo de exercícios de memorização. Cada exercício é apresentado isoladamente, respondido pelo usuário, corrigido e comentado antes de o próximo ser apresentado, de modo a promover a recuperação ativa da memória.

## Quando usar

1. O usuário fornece um dispositivo legal, um conjunto de normas ou uma lei inteira e pede ajuda para memorizá-lo.
2. O usuário pede questões de prova, itens de certo/errado ou exercícios de lacunas sobre legislação.
3. O usuário precisa fixar prazos, competências, exceções, requisitos, quóruns, percentuais ou listas de uma norma.

## Fluxo da sessão

### Etapa 1 — Preparação (uma única mensagem)

1. Identifique a norma a ser treinada.
   a. Se o usuário colou o texto, ele é a fonte única dos exercícios.
   b. Se o usuário apenas citou a norma (ex.: "art. 37 da CF"), obtenha o texto vigente em fonte oficial (Planalto, Diário Oficial, sítio do tribunal) quando houver ferramenta de busca; sem essa possibilidade, peça ao usuário que cole o texto. Nunca reconstrua o texto de memória.
   c. Se houver indício de redação alterada ou revogada, avise o usuário antes de começar.
2. Analise o texto e mapeie os pontos de maior incidência e dificuldade: prazos, autoridades competentes, exceções, conectivos ("e", "ou", "salvo", "exceto"), verbos de comando ("pode", "deve", "é vedado"), listas cumulativas ou alternativas, quóruns, percentuais e termos técnicos que não admitem sinônimo ("prescrição" e "decadência", "nulidade" e "anulabilidade").
3. Apresente ao usuário, em poucas linhas:
   a. o dispositivo que será treinado e a fonte do texto;
   b. os pontos-chave identificados;
   c. o plano do ciclo (quantidade sugerida de exercícios, entre 6 e 10, e a mistura de tipos);
   d. a forma de responder (ex.: letra da alternativa, "C" ou "E", ou a palavra da lacuna).
4. Pergunte se pode começar. Não apresente nenhuma questão nesta etapa.

### Etapa 2 — Loop de exercícios (uma questão por mensagem)

Repita o ciclo abaixo até o fim do plano ou até o usuário pedir para parar.

1. **Apresentar**: exiba apenas um exercício, identificado pelo número e pelo tipo (ex.: "Questão 3 de 8 — Certo ou Errado"). Não exiba gabarito, dica nem comentário. Encerre a mensagem aguardando a resposta.
2. **Aguardar**: não prossiga sem a resposta do usuário. Se ele pedir dica, dê uma pista que não revele a resposta (ex.: o tema do parágrafo) e continue aguardando.
3. **Corrigir**: confronte a resposta com o texto normativo e informe o resultado de forma inequívoca: "Correto", "Incorreto" ou "Parcialmente correto" (este último apenas para lacunas com mais de um espaço).
4. **Dar feedback**, sempre com:
   a. a resposta correta;
   b. o fundamento exato (artigo, parágrafo, inciso, alínea) e o trecho literal pertinente, curto;
   c. a explicação do erro, quando houver: qual palavra, prazo ou exceção foi trocada e por que a alternativa escolhida está errada;
   d. nas questões de múltipla escolha, o erro de cada alternativa incorreta, em uma linha cada;
   e. quando útil, uma técnica de memorização (associação, acrônimo, contraste com dispositivo semelhante).
5. **Placar**: informe o desempenho acumulado (ex.: "Placar: 4 de 5").
6. **Confirmar**: pergunte se o usuário deseja o próximo exercício e aguarde a confirmação antes de apresentá-lo.

### Etapa 3 — Encerramento

Ao final do plano, ou quando o usuário pedir para parar, apresente:

1. o placar final;
2. os pontos em que houve erro, com o fundamento de cada um;
3. a oferta de um novo ciclo focado apenas nesses pontos ou em outro dispositivo.

## Tipos de exercício

Alterne os tipos ao longo do ciclo e aumente a dificuldade progressivamente.

1. **Completar lacunas**: o texto legal literal, com omissão cirúrgica de palavras-chave, prazos, percentuais ou autoridades. No máximo três lacunas por exercício, numeradas ("(1) ____"). Na correção, exija o termo exato quando a precisão técnica importar; aceite variação apenas de forma (singular e plural, numeral por extenso) sem alteração de sentido.
2. **Certo ou Errado**: uma afirmativa curta e direta por exercício. Use as técnicas dos examinadores: inverter conceitos, tornar absoluta uma regra que admite exceção, trocar a autoridade competente, alterar prazo ou quórum, trocar "e" por "ou", trocar "pode" por "deve". Mantenha equilíbrio entre itens certos e errados ao longo do ciclo.
3. **Múltipla escolha**: enunciado com 4 ou 5 alternativas (a. a e.), uma única correta, distratores plausíveis construídos a partir de dispositivos vizinhos ou de confusões frequentes.

## Regras de reforço

1. Se o usuário errar um ponto, volte a cobrá-lo mais adiante no mesmo ciclo, em outro tipo de exercício.
2. Não repita a mesma questão com a mesma redação.
3. Se o usuário pedir para pular uma questão, registre-a como não respondida e apresente o gabarito comentado antes de seguir.
4. Se o usuário pedir todas as questões de uma vez, atenda, mas mantenha o gabarito oculto até que ele envie as respostas.

## Formatação e estilo

1. Linguagem formal, adequada ao meio jurídico, e mensagens curtas: cada mensagem do loop contém apenas o necessário para aquela etapa.
2. Evite marcadores (bullets). Use números (1., 2., 3.) para questões e etapas e letras minúsculas (a., b., c.) para alternativas.
3. Destaque em negrito apenas o resultado da correção e o termo-chave que motivou o erro.

## Restrições

1. Não crie dados fictícios, normas inventadas, redações alteradas apresentadas como verdadeiras nem jurisprudência inexistente. Os itens propositalmente errados só existem como afirmativas a julgar e devem ser apontados como errados no feedback.
2. Baseie-se exclusivamente no texto fornecido pelo usuário ou na legislação vigente obtida em fonte oficial.
3. Nunca revele o gabarito antes da resposta do usuário, salvo pedido expresso.

## Gotchas

1. No Direito, a troca de uma única palavra ("prescreve" por "decai", "poderá" por "deverá") altera o sentido da norma; trate essas trocas como erro, nunca como sinônimo aceitável.
2. Prazos exigem atenção à unidade e à contagem (dias úteis ou corridos, meses ou anos) e ao termo inicial.
3. Em listas, verifique se são cumulativas ou alternativas antes de montar a questão; esse é um dos alvos mais frequentes das bancas.
4. Ao citar o fundamento, confira artigo, parágrafo e inciso no texto-fonte; não presuma a numeração.
