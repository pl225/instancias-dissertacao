# Satisfazendo demandas de conectividade em digrafos através de adição, complemento e reversão de arcos

Este repositório contém todas as informações que foram omitidas nas seções de resultados computacionais no texto da dissertação, além dos arquivos das instâncias que foram utilizadas nos experimentos computacionais.

Aqui o usuário encontrará a seguinte relação de pastas:

- 1-PRVV: contém todas as instâncias para o problema de Reversão de Arcos que concede a um digrafo, quando possível e com o menor custo, a arco-conectividade forte entre todos os seus vértices;
- k-PAVV: contém todas as instâncias para o problema de Adição de Arcos que concede a um digrafo, quando possível e com o menor custo, a arco-conectividade forte entre todos os seus vértices;
- 1-PR_1-PC: contém todas as instâncias para os problemas de Reversão e de Complemento de Arcos. As mesmas são utilizadas tanto para a versão de conectividade forte entre os vértices de um subconjunto S de V, quanto para a conectividade fraca de um vértice v para um subconjunto T de V e
- 1-PAsT_1-PASS: contém todas as instâncias para os problemas de Adição de Arcos. As mesmas são utilizadas tanto para a versão de conectividade forte entre os vértices de um subconjunto S de V, quanto para a conectividade fraca de um vértice v para um subconjunto T de V.

As pastas anteriores contém duas subpastas cada uma, a saber:

- BC: contém as instâncias derivadas das famílias B e C do Problema de Steiner, as quais foram mencionadas no texto da dissertação e
- PUC: contém as instâncias derivadas da família PUC do Problema de Steiner, as quais foram mencionadas no texto da dissertação. 

Cada arquivo de instância possui as seguintes características:

- Extensão _.dat_, um arquivo de texto comum;
- Cabeçalho formado por:
  - INSTANCE_NAME _{nome da instância}_;
  - NB_VERTICES _{número de vértices do digrafo}_;
  - NB_ARCS _{número de arcos do digrafo}_;
  - NB_REQUESTS _{0}_, dado não utilizado;
  - NB_BLOCKAGES _{número de arcos bloqueados}_: refere-se ao número de arcos que não poderão ser usados pelas operações sobre arcos;
  - NB_A' _{número de arcos que poderão ser adicionados ao digrafo}_: este dado existe apenas nas instâncias do problema de Adição de Arcos e
  - NB_TERMINALS _{número de vértices contidos no subconjunto de vértices S}_: este dado existe apenas nas instâncias dos problemas que não possuem o objetivo de conectar de maneira forte todos os vértices de um digrafo;
- Seção _VERTICES_: linhas no formato _IDENTIFICAÇÃO DO VÉRTICE 0 0_. Os números 0 e 0 funcionariam como as coordenadas de um vértice no plano cartesiano, os quais não foram utilizados na pesquisa;
- Seção _ARCS_: linhas no formato _IDENTIFICAÇÃO DO VÉRTICE IDENTIFICAÇÃO DO VÉRTICE CUSTO_ para qualificar um arco de um vértice a outro com um custo qualquer, o qual está atualmente no digrafo;
- Seção _REQUESTS_: sempre vazia;
- Seção _BLOCKAGES_: linhas no formato _IDENTIFICAÇÃO DO VÉRTICE _IDENTIFICAÇAO DO VÉRTICE_ para qualificar arcos que não poderão ser utilizados pelas operações sobre arcos;
- Seção _A'_: existe apenas nas instâncias para o problema de Adição de Arcos. Suas linhas possuem o formato _IDENTIFICAÇÃO DO VÉRTICE IDENTIFICAÇÃO DO VÉRTICE CUSTO_ para qualificar um arco de um vértice a outro com um custo qualquer, o qual não está atualmente no digrafo e que poderá ser adicionado a ele;
- Seção _TERMINALS_: existe apenas nas instâncias dos problemas que não possuem o objetivo de conectar de maneira forte todos os vértices de um digrafo. Contém linhas no formato _IDENTIFICAÇÃO DO VÉRTICE_ para caracterizar os vértices pertencentes ao subconjunto S de V e
- Seção _R_: não utilizado.

O formato acima descrito para os arquivos de instâncias utilizadas nos experimentos foi inspirado naquele utilizado por:  HUANG, Y., SANTOS, A. C., DUHAMEL, C.  “Model and methods toaddress urban road network problems with disruptions”,InternationalTransactions in Operational Research, v. 27, n. 6, pp. 2715–2739, 2020.doi:  https://doi.org/10.1111/itor.12641.  Disponível em:  <https://onlinelibrary.wiley.com/doi/abs/10.1111/itor.12641>