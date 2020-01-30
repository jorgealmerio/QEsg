# <a name="__RefHeading___Toc3816_1012792670"></a>![](images\figb6a402436fc68eb5.png)

[CLICK HERE FOR ENGLISH VERSION](https://github.com/jorgealmerio/QEsg/blob/master/README_en.md) 

# <a name="__RefHeading___Toc3818_1012792670"></a>1 APRESENTAÇÃO

<span lang="pt-BR">[QEsg](https://plugins.qgis.org/plugins/QEsg/) é um</span> <span lang="pt-BR">complemento</span> <span lang="pt-BR">desenvolvido para o software [Qgis](http://www.qgis.org/) com o objetivo de auxiliar no projeto de redes de esgotamento sanitário.</span>

<a name="__RefHeading___Toc3053_1012792670"></a><span lang="pt-BR">O plugin se utiliza das facilidades e recursos inerentes a um ambiente SIG (Sistema de Informações geográficas) para apoiar a</span> <span lang="pt-BR">organização,</span> <span lang="pt-BR">desenvolvimento,</span> <span lang="pt-BR">dimensionamento e apresentação final do projeto de uma rede de esgoto.</span>

# <a name="__RefHeading___Toc3912_1012792670"></a>2 SUMÁRIO

<div id="Sumario1" dir="ltr">

**[1 APRESENTAÇÃO](#__RefHeading___Toc3818_1012792670)**

**[2 SUMÁRIO](#__RefHeading___Toc3912_1012792670)**

**[3 SCREENSHOTS](#__RefHeading___Toc3057_1012792670)**

**[4 TUTORIAL](#__RefHeading___Toc3059_1012792670)**

<span style="background: transparent">[4.1 CONCEITUAÇÃO](#__RefHeading___Toc3061_1012792670)</span>

<span style="background: transparent">[4.2 ARQUIVOS UTILIZADOS NESSE TUTORIAL](#__RefHeading___Toc3063_1012792670)</span>

<span style="background: transparent">[4.3 EXEMPLO DE APLICAÇÃO](#__RefHeading___Toc3065_1012792670)</span>

<span style="background: transparent">[4.4 BOTÃO 00 CONFIGURAÇÃO](#__RefHeading___Toc3067_1012792670)</span>

<span style="background: transparent">[4.5 BOTÃO 01 VERIFICA/CRIA CAMPOS](#__RefHeading___Toc3069_1012792670)</span>

<span style="background: transparent">[4.6 BOTÃO 02 NUMERAR REDE](#__RefHeading___Toc3071_1012792670)</span>

<span style="background: transparent">[4.7 BOTÃO 03 CRIAR LAYER DE NÓS](#__RefHeading___Toc3073_1012792670)</span>

<span style="background: transparent">[4.8 BOTÃO 04 PREENCHE OS CAMPOS](#__RefHeading___Toc3075_1012792670)</span>

<span style="background: transparent">[4.9 PONTA SECA](#__RefHeading___Toc3077_1012792670)</span>

<span style="background: transparent">[4.10 BOTÃO 5 CALCULA VAZÃO](#__RefHeading___Toc3079_1012792670)</span>

<span style="background: transparent">[4.11 BOTÃO 6 DIMENSIONA](#__RefHeading___Toc3081_1012792670)</span>

<span style="background: transparent">[4.12 BOTÃO 7 DESENHA PERFIL](#__RefHeading___Toc3083_1012792670)</span>

**[5 TABELAS](#__RefHeading___Toc3085_1012792670)**

<span style="background: transparent">[5.1 SHAPE NÓS](#__RefHeading___Toc3087_1012792670)</span>

<span style="background: transparent">[5.2 SHAPE TRECHOS](#__RefHeading___Toc3089_1012792670)</span>

<span style="background: transparent">[5.3 SHAPE INTERFERÊNCIAS](#__RefHeading___Toc3091_1012792670)</span>

**[6 AUTOR](#__RefHeading___Toc3820_1012792670)**

**[7 COLABORADOR](#__RefHeading___Toc3822_1012792670)**

**[8 NOTA DE RESPONSABILIDADE DE USO](#__RefHeading___Toc3093_1012792670)**

**[9 DOAÇÃO](#__RefHeading___Toc3093_1012792670)**

</div>

# <a name="__RefHeading___Toc3057_1012792670"></a>3 SCREENSHOTS

<font style="font-size: 10pt" size="2">**Figura 1 - Tela típica de uma rede de esgoto com plugin QEsg.**</font>

![](images\figfe88cdc51ed7216e.png)

<font style="font-size: 10pt" size="2">**Figura 2 - Rede de esgoto com multiplas bacias em Ambiente Qgis.**</font>

![](images\figefc3987574fdab19.png)

<font style="font-size: 10pt" size="2">**Figura 3 - Resultado de um arquivo DXF exportado através do Plugin (a partir da versão 1.1) em ambiente CAD.**</font>

![](images\fig151e7a02dd465305.png)

<font style="font-size: 10pt" size="2">**Figura 4 - Detalhe do arquivo DXF exportado pelo Plugin (a partir da versão 1.1) em ambiente CAD.**</font>

![](images\fig55333ec8aaf3fe92.png)

# <a name="__RefHeading___Toc3059_1012792670"></a>4 TUTORIAL

## <a name="__RefHeading___Toc3061_1012792670"></a>4.1 CONCEITUAÇÃO

A estrutura da rede atende aos seguintes princípios.

*   O plugin considera a rede formada por um ou mais coletores.

*   O coletor principal possui o PV final da rede.

*   Os <span style="background: transparent">coletores</span> <span style="background: transparent"></span> são divididos em um ou mais trechos.

Outros detalhes básicos são apresentados no exemplo de aplicação a seguir.

## <a name="__RefHeading___Toc3063_1012792670"></a>4.2 ARQUIVOS UTILIZADOS NESSE TUTORIAL

<span lang="pt-BR">Arquivos</span> <span lang="pt-BR">utilizados no tutorial</span> <span lang="pt-BR">para download:</span>

*   [Arquivos brutos (inicial)](../master/core/sample/clean/shapes/Trechos.zip?raw=True), contém o shapefile da rede, composta por três coletores.

*   [Arquivo finalizados](../master/core/sample/finished/shapes/finished_shapes.zip?raw=True), contém os shapefile com os trechos da rede e e nós, calculados e dimensionados com a utilização do Plugin.

## <a name="__RefHeading___Toc3065_1012792670"></a>4.3 EXEMPLO DE APLICAÇÃO

*   Configure o projeto para as coordenadas UTM, conforme a faixa meridiana local.

*   Carregue um arquivo vetorial (shape) com a rede de esgoto. Como alternativa você pode criar um arquivo de linhas no formato shape e desenhar a rede de esgoto utilizando os recursos do QGIS, neste caso siga estritamente as recomendações seguintes para a criação de arquivo:

    *   Salve o arquivo <span style="background: transparent">(ex.:</span> **<span style="background: transparent">Trechos</span>****<span style="background: transparent">)</span>** utilizando um Sistema de Referência de Coordenadas (CRS) em Projeção UTM, para a faixa meridiana local.

    *   Desenhe sempre os trechos na direção do fluxo (de montante para jusante).

    *   Não é necessário criar nenhum campo específico no momento de salvar o shape **Trechos**.

*   Salve o projeto. Nesse momento a janela do projeto terá a aparência da **Figura 5**.

*   Abra a tabela de atributos do shape de rede, onde existirá uma linha para cada coletor traçado e somente um campo com valores nulos (vide **Figura 5**).

<font style="font-size: 10pt" size="2">**Figura 5 - Aparência inicial do projeto, após carregar ou traçar a rede de esgotos.**</font>

![](images\fig99e68e04b169121.png)

## <a name="__RefHeading___Toc3067_1012792670"></a>4.4 ![](images\figfef4e818bfc6bf06.png)BOTÃO 00 CONFIGURAÇÃO

Ao clicar abre uma janela apresentada na **Figura 6**.

<table width="100%" cellspacing="0" cellpadding="4"><colgroup><col width="128*"> <col width="128*"></colgroup>

<tbody>

<tr valign="top">

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="50%">

<font style="font-size: 10pt" size="2">**Figura 6 - Janela do Botão 00 – Configuração**</font>

![](images\fig7a42f593322f7f8d.png)

</td>

<td style="border: 1px solid #000000; padding: 0.1cm" width="50%">

<font style="font-size: 10pt" size="2">**Figura 7 - Janela do Botão 00 – Configuração após preenchimento dos dados básicos**</font>

![](images\fig3ae901ea0d41096a.png)

</td>

</tr>

</tbody>

</table>

Preencher as informações básicas na janela aberta.

*   No grupo Layers selecione o arquivo de linhas que você salvou com o nome **Trechos**, com o traçado da rede.

*   Neste exemplo, somente incluiremos dois parâmetros de entrada da aba **Dados** <span style="font-weight: normal">(atenção: não digite separador de milhar, o ponto é separador de decimais)</span>:

*   População inicial: (digite) 10000

*   População de saturação: (digite) 13000

*   Mantenha os parâmetros padrões das abas **Tubos** e **Opções de cálculo**. A janela terá a aparência da **Figura 7**.

*   Clique no botão **OK** para salvar os parâmetros gerais do projeto.

## <a name="__RefHeading___Toc3069_1012792670"></a>4.5 ![](images\fig4382197c198bdabe.png)BOTÃO 01 VERIFICA/CRIA CAMPOS

Ao pressionar neste botão o plugin verifica se o shape **Trechos** com o traçado da rede contém os campos padrões. Se não existe oferece a possibilidade de criá-los automaticamente, como mostra a **Figura 8**. Aceite essa opção.

Abra novamente a tabela de atributos do shape **Trechos** com a rede de esgoto (vide **Figura 9**). Você verá que foram criados um conjunto de campos para cada coletor traçado. Os valores contidos nesses campos serão nulos ou zeros (sem informação ainda).

<table width="100%" cellspacing="0" cellpadding="4"><colgroup><col width="128*"> <col width="128*"></colgroup>

<tbody>

<tr valign="top">

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="50%">

<font style="font-size: 10pt" size="2">**Figura 8 - Mensagem para criação dos campos padrões no shape da rede de esgotos.**</font>

![](images\fige9af7918483dbddc.png)

</td>

<td style="border: 1px solid #000000; padding: 0.1cm" width="50%">

<font style="font-size: 10pt" size="2">**Figura 9 - Tabela da rede de esgotos, após a criação dos campos padrões.**</font>

![](images\fig9a568b01d89ce8f3.png)

</td>

</tr>

</tbody>

</table>

## <a name="__RefHeading___Toc3071_1012792670"></a>4.6 ![](images\fig96a608ce40392369.png)BOTÃO 02 NUMERAR REDE

Ao clicar nesse botão é verificado se o traçado da rede de esgoto é composto por segmentos simples (segmentos de reta individuais entre vértices consecutivos). Caso exista algum elemento de rede com mais de dois vértices, será apresentada uma mensagem semelhante à da **Figura 10**.

<font style="font-size: 10pt" size="2">**Figura 10 - Mensagem subdivisão de coletores em trechos.**</font>

![](images\fige520154b13736a0b.png)

No nosso exemplo, antes de clicar pela primeira vez, o shape **Trechos** possui três coletores traçados de montante para jusante (vide **Figura 9**) definidos por poligonais abertas (um coletor com 5 vértices e dois coletores com 3). Na mensagem semelhante à da **Figura 10** <span style="font-weight: normal">clicar em</span> **Sim**.

Mensagem para subdivisão de coletores em trechos: Existem elementos com ( …). Deseja convertê-los para linhas simples? (vide **Figura 10**). Clique no botão **Sim**.

<font style="font-size: 10pt" size="2">**Figura 11 - Mensagem subdivisão de coletores em trechos.**</font>

![](images\fig497bb7c3ae5f5870.png)

Será aberta uma janela, semelhante à **Figura 11**, a qual será fixada na lateral direita no ambiente QGIS. Nos passos a seguir, proceda com atenção.

*   Verifique que a caixa <Coletor> esteja preenchido com o valor 1\. Senão digite o valor 1.

*   Verifique que a caixa <Número de dígitos> esteja preenchido com o valor 1\. Senão digite o valor 1.

*   Verifique que a opção <Somente trechos sem identificação> esteja selecionada.

*   Clique no botão <Selecionar Montante>.

*   Movimente o cursor e faça clique com o botão esquerdo (primário) no meio do trecho mais a montante do coletor principal da rede. Todos os trechos do coletor mudarão para a cor amarela (padrão de seleção do QGIS), como mostra a **Figura 12**.

<font style="font-size: 10pt" size="2">**Figura 12 - Seleção do trecho de montante do coletor principal.**</font>

![](images\figa0b8312aef0b4b0c.png)

*   Clique no botão <Renomear> da janela Renomear Rede. Na primeira vez, o estilo do shape **Trechos** é alterado, são representados os vértices e o sentido do fluxo, como ilustra a Figura 13\. Para o <span style="background: transparent">coletor</span> renomeado serão apresentadas as informações: nome do coletor-trecho e nomes dos PVs de montante e jusante.

<font style="font-size: 10pt" size="2">**Figura 13 - Coletor principal renumerado**</font>

![](images\figa9093071ca21db05.png)

*   <span style="background: transparent">Clique no botão <Novo Coletor>. O número da caixa Coletor mudará para 2 e o trecho anterior será deselecionado.</span>

*   <span style="background: transparent">Verifique que a opção <Soment</span>e trechos sem identificação> continue selecionada.

*   Selecione o trecho de montante do segundo coletor (no nosso exemplo, o coletor mais a jusante), como ilustra a Figura 14\. A cor do coletor mudará para amarelo até o PV de interligação com o coletor anterior.

<font style="font-size: 10pt" size="2">**Figura 14 - Seleção do trecho de montante do segundo coletor**</font>

![](images\fige462dd58418f2ff6.png)

*   Clique em renomear o coletor selecionado. O coletor selecionado será renomeado e numerado, de forma análoga ao primeiro coletor, como ilustra a Figura 15.

<font style="font-size: 10pt" size="2">**Figura 15 - Segundo coletor renumerado.**</font>

![](images\fige94a0e31ed3f3ca4.png)

*   Repita o processo para o terceiro coletor, que consiste em: clicar no botão Novo coletor, clicar sobre o trecho de montante do coletor (como mostra a Figura 16), clicar no botão Renomear (como mostra a Figura 17). O processo de nomeação de trechos da rede estará concluído.

<font style="font-size: 10pt" size="2">**Figura 16 - Clique no trecho de montante para a seleção do terceiro coletor.**</font>

![](images\figcf390edf76df8f0d.png)

<font style="font-size: 10pt" size="2">**Figura 17 - Todos os trechos dos três coletores renumerados**</font>

![](images\fig9984ce4666d03153.png)

*   Salve o shape **Trechos** e encerre o processo de edição.

No shape **Trechos** foram preenchidos os campos Coletor, Trecho, DC_ID, PVM e PVJ.

## <a name="__RefHeading___Toc3073_1012792670"></a>4.7 ![](images\fig30dc2cdc68e77050.png)BOTÃO 03 CRIAR LAYER DE NÓS

*   Ao clicar no botão é aberta a janela para atribuição do nome do shape de nós (formato de pontos). Selecione o local e nomes adequados a este shape, para este exemplo escolha como nome **Nos**. Clique no botão Salvar para concluir a gravação do layer. <u>Atenção</u>: quando elaborávamos este tutorial, no ambiente Linux, a biblioteca utilizada para salvar o shape de **Nos** apresentava um bug. Era necessário digitar a extensão “.shp” ao final do nome do arquivo para que ocorresse o carregamento automático do arquivo salvo.

*   Após fechar a janela o shape **Nos** é adicionado ao projeto.

*   Habilite o modo de edição do shape **Nos** e preencha todos os campos de cota do terreno de cada nó.

*   Salve o shape **Nos** e desabilite o modo de edição.

*   Salve o projeto.

## <a name="__RefHeading___Toc3075_1012792670"></a>4.8![](images\fig85a4f30f64038587.png)BOTÃO 04 PREENCHE OS CAMPOS

Ao clicar no botão:

*   Todos os campos nulos do shape **Trechos** são preenchidos;

*   São sobrescritos todos os campos de cota dos PVs de montante, jusante e comprimento do trecho (calculado como comprimento real do trecho desenhado) do shape **Trechos;**

*   São transferidos os valores do campo COTA_TN do shape **Nos** <span style="font-weight: normal">para os campos CTM e CTJ do shape</span> **Trechos**.

*   Salve o shape <span style="font-style: normal">**Trechos**</span> e saia do modo de edição.

## <a name="__RefHeading___Toc3077_1012792670"></a>4.9 PONTA SECA

Tem como objetivo identificar os trechos que não recebem contribuições através do PV de montante. Essa identificação é necessária em trechos cujos PVs de montante possam apresentar mais de uma saída, situação <font face="Calibri, sans-serif"><font style="font-size: 11pt" size="2">não</font></font> permitida segundo as normas brasileiras. A “ponta seca” é informada manualmente na tabela do shape **Trechos**, campo (coluna) PONTA_SECA, trocando a letra N (não) pela letra S (sim), como ilustra a **Figura 18**.

<font style="font-size: 10pt" size="2">**Figura 18 - Alteração da condição de montante para “ponta seca”**</font>

![](images\fig5acf898bdc82b29c.png)

<span lang="pt-BR">Após essa</span> alteração <span lang="pt-BR">a representação de montante dos trechos “</span>p<span lang="pt-BR">onta</span> s<span lang="pt-BR">eca” será modificada</span> <span lang="pt-BR">como ilustra a</span> <span lang="pt-BR">**Figura 19**</span><span lang="pt-BR">.</span>

<font style="font-size: 10pt" size="2">**Figura 19 - Alteração da condição hidráulica de montante dos trechos iniciais para “ponta seca”**</font>

![](images\fig87942741b4df8b51.png)

Salve as modificações introduzidas na tabela do shape **Trechos** <span style="font-weight: normal">e saia do modo de edição. Salve o</span> projeto.

## <a name="__RefHeading___Toc3079_1012792670"></a>4.10 ![](images\fig62bba675e061c761.png)BOTÃO 05 CALCULA VAZÃO

Ao clicar neste botão, são calculadas as vazões acumuladas ao longo de cada um dos trechos que formam os coletores, os resultados são gravados no shape **Trechos**. O formato de apresentação dos trechos muda para mostrar os dados: nome do trecho; comprimento, diâmetro e vazão de cada trecho.

<font style="font-size: 10pt" size="2">**Figura 20 - Todos os trechos dos três coletores com as vazões de projeto calculadas.**</font>

![](images\figa457ae216bd4057d.png)

## <a name="__RefHeading___Toc3081_1012792670"></a>4.11![](images\fige74254464005de07.png)BOTÃO 6 DIMENSIONA

Ao clicar neste botão, são dimensionados todos os trechos que formam os coletores da rede. O formato de apresentação dos trechos muda para mostrar os dados: nome do trecho; comprimento; diâmetro nominal e declividade, como mostra a **Figura 21**.

<font style="font-size: 10pt" size="2">**Figura 21 - Rede calculada.**</font>

![](images\figb238c0e89bad54f6.png)

Todos os dados do dimensionamento estão contidos na tabela do shape **Trechos**. Caso deseje, abra a tabela do shape **Trechos**<span style="font-weight: normal">, selecione todos os campos, copie e cole dentro de uma planilha eletrônica (MS-Excel, Libreoffice-Calc ou outra)</span>.

## <a name="__RefHeading___Toc3083_1012792670"></a>4.12![](images\figfe786608f4b2d9f7.png)BOTÃO 7 DESENHA PERFIL

Trata-se de uma ferramenta de conferência rápida que o projetista pode usar para análise dos coletores projetados. Ao clicar no botão é apresentado um menu flutuante como o da **Figura 22**. Selecione o coletor a desenhar e clique no botão **OK**.

<font style="font-size: 10pt" size="2">**Figura 22 - Menu flutuante para seleção do coletor a desenhar**</font>

![](images\figbe5d64e5199146fc.png)

Uma janela semelhante ao da **Figura 23** <span style="font-weight: normal"></span> será apresentada (neste exemplo foi selecionado o Coletor 1).

<font style="font-size: 10pt" size="2">**Figura 23 - Perfil do coletor selecionado**</font>

![](images\figb56f4bb5c449c1b9.png)

# <a name="__RefHeading___Toc3085_1012792670"></a>5 TABELAS

## <a name="__RefHeading___Toc3087_1012792670"></a>5.1 SHAPE NÓS

<table width="100%" cellspacing="0" cellpadding="4"><colgroup><col width="43*"> <col width="43*"> <col width="43*"> <col width="43*"> <col width="43*"> <col width="43*"></colgroup>

<tbody>

<tr valign="top">

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">**Ordem**</font>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">**Nome**</font>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">**Unidade**</font>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">**Tipo**</font>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.1cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">**Comprimento**</font>

</td>

<td style="border: 1px solid #000000; padding: 0.1cm" width="17%">

<font style="font-size: 10pt" size="2">**Precisão**</font>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">1</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">DC_ID</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">-</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">String</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">10</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0.1cm" width="17%">

<font style="font-size: 10pt" size="2">-</font>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">2</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">COTA_TN</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">m</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">Real</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0cm" width="17%">

<font style="font-size: 10pt" size="2">10</font>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding-top: 0cm; padding-bottom: 0.1cm; padding-left: 0.1cm; padding-right: 0.1cm" width="17%">

<font style="font-size: 10pt" size="2">3</font>

</td>

</tr>

</tbody>

</table>

## <a name="__RefHeading___Toc3089_1012792670"></a>5.2 SHAPE TRECHO

<table width="100%" cellspacing="0" cellpadding="4">

<tbody>

<tr valign="top">

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Ordem**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Nome**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Unidade**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Tipo**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Comprimento**</span>

</td>

<td style="border: 1px solid #000000; padding: 0.1cm;" width="17%">

<span style="font-size: small;">**Precisão**</span>

</td>

<td style="border: 1px solid #000000; padding: 0.1cm;" width="17%">

<span style="font-size: small;">**Descrição**</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">DC_ID</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Identificação do Trecho</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">PVM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Identificação do PV de Montante</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">PVJ</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Identificação do PV de Jusante</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">4</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">LENGTH</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Extensão do Trecho</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">5</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CTM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Cota do Terreno (Montante)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">6</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CTJ</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Cota do Terreno (Jusante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">7</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CCM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Cota do Coletor (Montante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">8</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CCJ</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Cota do Coletor (Jusante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">9</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">NA_MON</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Cota do Nivel de Água (Montante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">NA_JUS</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Cota do Nivel de Água (Jusante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">11</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">PRFM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Profundidade (Montante)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">12</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">PRFJ</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Profundidade (Jusante)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">13</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">DIAMETER</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">mm</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Diâmetro</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">14</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">DECL</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m/m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">5</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Declividade</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">15</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">MANNING</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Adimensional  
</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Coeficiente de rugosidade de Manning</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">16</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Q_CONC_INI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">L/s</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Vazão Concentrada (Inicio de Plano)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">17</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Q_CONC_FIM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">L/s</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Vazão Concentrada (Fim de Plano)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">18</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Q_INI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">L/s</span></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Vazão Total (Inicio de Plano)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">19</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Q_FIM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">L/s</span></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Vazão Total (Fim de Plano)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">20</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">VEL_INI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m/s</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Velocidade (Inicio de Plano)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">21</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">VEL_FIM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m/s</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Velocidade (Fim de Plano)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">22</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">VEL_CRI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m/s</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Velocidade Crítica</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">23</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">TRATIVA</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Pa</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Tensão Trativa</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">24</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">LAM_INI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">4</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Relação da lâmina/Diâmetro<span style="font-size: small;">(Inicio de Plano)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">25</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">LAM_FIM</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;"><span style="font-size: small;">Relação da lâmina /Diâmetro (Fim de Plano)</span></span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">26</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">LAM_MAX</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Adimensional</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Relação máxima entre altura da lâmina d'água e o Diâmetro</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">27</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">REC_MIN</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Recobrimento mínimo</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">28</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CONTR_LADO</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-<sup>(1)</sup></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Integer</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Contribuição lateral (0,1 ou 2)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">29</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">ETAPA</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-<sup>(2)</sup></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Integer</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Etapa</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">30</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">PONTA_SECA</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-<sup>(3)</sup></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Ponta Seca (S/N)</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">31</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">OBS</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">30</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Observações</span>

</td>

</tr>

</tbody>

</table>

<font style="font-size: 9pt" size="2">Valores permitidos</font>

<font style="font-size: 9pt" size="2"><sup>(1)</sup>: Trecho sem contribuição = 0, contribuição unilateral = 1 e contribuição bilateral = 2</font>

<font style="font-size: 9pt" size="2"><sup>(2)</sup>: Trecho existente = 0, a implantar na primeira etapa = 1, a implantar na segunda etapa = 2</font>

<font style="font-size: 9pt" size="2"><sup>(3)</sup>: É ponta seca = S, não é ponta seca = N</font>

## <a name="__RefHeading___Toc3091_1012792670"></a>5.3 SHAPE INTERFERÊNCIAS

<table width="100%" cellspacing="0" cellpadding="4">

<tbody>

<tr valign="top">

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Ordem**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Nome**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Unidade**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Tipo**</span>

</td>

<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0.1cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">**Comprimento**</span>

</td>

<td style="border: 1px solid #000000; padding: 0.1cm;" width="17%">

<span style="font-size: small;">**Precisão**</span>

</td>

<td style="border: 1px solid #000000; padding: 0.1cm;" width="17%">

<span style="font-size: small;">**Descrição**</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">1</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">DC_ID</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">31</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Identificação da Interferência</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">TIPO_INT</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-<sup>(1)</sup></span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">QString</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">2</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">-</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Tipo de Interferência</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CS</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Cota da Geratriz Superior da interferência</span>

</td>

</tr>

<tr valign="top">

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">4</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">CI</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">m</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Real</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding: 0cm 0cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">10</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">3</span>

</td>

<td style="border-top: none; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 0cm 0.1cm 0.1cm 0.1cm;" width="17%">

<span style="font-size: small;">Cota da Geratriz Inferior da interferência</span>

</td>

</tr>

</tbody>

</table>

<span style="font-size: small;">Valores permitidos</span>

<span style="font-size: small;"><sup>(1)</sup>: TN para terreno natural, qualquer outro valor (inclusive nulo) é considerada uma interferência.</span>

<span style="font-size: small;">Quando a interferência for do tipo 'TN' no campo 'CS' deve ser informada a cota do Terreno natural e no campo CI deve ser informada a cota da geratriz superior máxima desejada para a tubulação projetada.</span>

# <a name="__RefHeading___Toc3820_1012792670"></a>6 AUTOR

Plugin desenvolvido por Jorge Almério Sousa Moreira, Engenheiro Civil.

Dúvidas, críticas e sugestões são bem vindas.

Email: [jorgealmerio@yahoo.com.br](mailto:jorgealmerio@yahoo.com.br)

Plugin Site: [github.com/jorgealmerio/QEsg](https://github.com/jorgealmerio/QEsg/blob/master/README.md)

Bugs, Falhas e solicitações: [github.com/jorgealmerio/QEsg/issues](https://github.com/jorgealmerio/QEsg/issues)

# <a name="__RefHeading___Toc3822_1012792670"></a>7 COLABORADOR

Juan Santiago Ramseyer

# <a name="__RefHeading___Toc3093_1012792670"></a>8 NOTA DE RESPONSABILIDADE DE USO

Esse plugin está sujeito aos termos da licença “[_GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007_](https://www.gnu.org/licenses/gpl-3.0.html)”, portanto os danos ou consequências da utilização do plugin e/ou dos seus resultados, em qualquer ordem é de inteira responsabilidade do usuário final, ficando os desenvolvedores isentos de qualquer responsabilidade técnica ou jurídica inerente da utilização com ou sem inabilidade no uso do mesmo, inclusive no caso de eventual falha comprovada do plugin.

# <a name="__RefHeading___Toc3093_1012792670"></a>9 DOAÇÃO

Se o plugin for util para você, considere fazer uma doação para o autor.

[![Donate](https://www.paypalobjects.com/pt_BR/BR/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?button=donate&business=G5ERSTGG4U426&item_name=Jorge+Almerio/Qgis+QEsg+plugin&quantity=&amount=&currency_code=BRL&shipping=&tax=&notify_url=&cmd=_donations&bn=JavaScriptButton_donate&env=www)
