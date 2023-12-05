# Equipe Dinossauros, Bancos de dados e Coisas Parecidas (DBDCP)
### Davi Gabriel Bandeira Coutinho (183710)
### Francisco Vinicius Sousa Guedes (260440)
### Márcio Levi Sales Prado (183680)



## `data`
Os dados foram extraídos de diretamente dos sites das pesquisas:
###External

[What we eat in America FCID ](https://fcid.foodrisk.org/dbc/)
[FoodDB](https://foodb.ca/)
[Food Consunption Data - Europa](https://www.efsa.europa.eu/en/data-report/food-consumption-data)


## `notebooks`
[Notebook com a criação das tabelas](notebooks/criando_tabelas_modelo_relacional.ipynb)

Implementamos as tabelas a partir dos arquivos CSVs. Para tabelas muito grandes como Contents e Intake 
### Página no Binder paraa execução do notebook 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/viniguedes29/mc536-DBDCP-Projeto-Final/HEAD)


## `src`

Fizemos a implementação em SQL e um script auxiliar em Python



## Motivação e Contexto

> Hoje em dia, com a acelação do dia a dia, muitas pessoas optam por opções de comida não muito saudáveis. Várias pesquisas estão preocupadas em mapear os hábitos alimentares das pessoas, no entanto, muitas delas, como a 'What we eat in America?' e a 'Food Consumption Data' da EFSA, não tem um detalhamento a nível de nutrientes dos itens consumidos.

> A partir disso, gostaríamos de fazer uma ligação em entre uma base que consiga classificar a comida a nível nutricional, como o FooDB, podendo assim entender como o consumo das pessoas está em nível de consumo de calorias e de nutrientes.

> Com isso, queremos desenvolver análises a nível de classificação das dietas, a partir do total consumido, sendo essa analise priorizada pelo modelo de relacional estruturado, enquanto queremos analises de agrupamento e clusterização a partir do modelo de grafos.

## Slides

### Apresentação Prévia
> Tivemos que mudar, pois fizemos com outra equipe que acabou desistindo da matéria, então tivemos que mudar o projeto
### Apresentação Final
> [Slide](assets/Apresentação%20-%20Projeto%20Final.pdf)

## Modelo Conceitual
![Modelo Conceitual](assets/Diagrama%20relacional.drawio.png)


## Modelos Lógicos

> Modelo Lógico Relacional:
~~~
FOOD_CONSUMPTION_DATA(_Country_, _Year_, _Population_Group_, Exposure_Hierarchy_1, _Exposure_Hierarchy_7_, Number_of_Subjects, Number_of_Consumers, Percent_of_Consumers, Mean_Consumers, Mean_Subjects, Mean_Consumers_BW, Mean_Subjects_BW)

FOODS_RELATION(_Food_Desc_FCID_, _Exposure_Hierarchy_7_)
  Food_Desc_FCID chave estrangeira -> FOODS(Food_Desc)
  Exposure_Hierarchy_7 chave estrangeira -> FOOD_CONSUMPTION_DATA(Exposure_Hierarchy_7)

FOODS(_Food_Code_, Food_Abbrev_Desc, Food_Desc)

RECIPES(_Food_Code_, Mod_Code, Ingredient_Num, _FCID_Code_, Cooked_Status, Food_Form, Cooking_Method, Commodity_Weight)

FCID_DESCRIPTION(_FCID_Code_, FCID_Desc, CGN, CG_Subgroup)

INTAKE(_SEQN_, _DAYCODE_, DRABF, FCID_Code, Cooked_Status, Food_Form, Cooking_Method, Intake_AVG, Intake_SUM, Intake_BW_AVG)
  FCID_Code chave estrangeira -> FCID_DESCRIPTION(FCID_Code)

CROP_GROUP(_CGN_, _CGL_, Crop_Group_Description)
  CGN chave estrangeira -> FCID_DESCRIPTION(CGN)

RELATE_COMMODITY(_name_foodb_, _FCID_Desc_)
  name_foodb chave estrangeira -> FOOD(name)
  FCID_Desc chave estrangeira -> FCID_DESCRIPTION(FCID_Desc)

FOOD(_id_, name, name_scientific, description, itis_id, food_group, food_subgroup, food_type, public_id)

NUTRIENT(_id_, legacy_id, public_id, description, calories_per_gram)

COMPOUNDS(_id_, public_id, name)

CONTENT(_id_, source_id, _food_id_, orig_food_id, orig_food_id_common_name, orig_food_id_scientific_name, orig_content, orig_min, orig_max, orig_unit)
  id chave estrangeira -> NUTRIENT(id)
  id chave estrangeira -> COMPOUNDS(id)
  food_id chave estrangeira -> FOOD(id)
~~~

> ![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final.png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(1).png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(2).png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(3).png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(4).png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(5).png)
![Modelo Lógico de Grafos](assets/Modelo%20Lógico%20de%20Grafos%20-%20Projeto%20Final%20(6).png)



## Dataset Publicado

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<food_FDB_e_FCID_matches.csv>` | `https://raw.githubusercontent.com/viniguedes29/mc536-DBDCP-Projeto-Final/main/bases/efsa/EFSA_Intake.csv` | `<Relacionamento entre os dados do FCID>`


## Bases de Dados
> 

título da base | link | breve descrição
----- | ----- | -----
`<EFSA_Intake>` | `<https://www.efsa.europa.eu/en/data-report/food-consumption-data>` | `<Base de consumo da pesquisa de consumo de comida da Europa>`
`<FoodDB>` | `<https://foodb.ca/>` | `<Base de alimentos>`
`<What We eat in America? - FICD>` | `<https://fcid.foodrisk.org/dbc/>` | `<Base de alimentos>`

## Detalhamento do Projeto
Detalhamento do Projeto:
O conjunto de bases de dados utilizado nas análises é composto de 3 bases de dados: FooDB, que traz informações nutricionais de diversos alimentos, detalhando inclusive suas composições. FCID (Food Commodity Intake Database), cujos dados da tabela de consumo foram obtidos por meio de pesquisas endereçadas a consumidores. Essa base também contém informações sobre a composição de diferentes receitas, que trazem uma análise diferente das demais bases, nos permitindo ver como um alimento interage com outros no aspecto culinário. EFSA (European Food Consumption Data), também obtida por meio de pesquisas, mas dessa vez trazendo informações sobre os consumidores e o consumo em relação a uma população, ou seja, algumas das tabelas dessa base não levam em conta apenas dados sobre as pessoas que de fato consumiram, mas de todas que foram entrevistadas, fornecendo dados mais robustos que nos permitem inferir hábitos alimentares sobre uma população em geral.

Nosso modelo conceitual conecta as 3 bases citadas acima, totalizando 12 tabelas. Essas conexões criam uma integralização entre as bases, que nos permite usar dados de uma base para conseguir informações sobre consumo ou a formação de receitas detalhadas em outras bases, possibilitando também a comparação do consumo em diferentes lugares. A conexão entre essas bases se dá por meio de uma entidade de relacionamento obtida com o algoritmo em NLP simples, TF-IDF, no qual fizemos a relção do nomes dos comodditys da tabela FCID com as comidas do FoodDB e do FCID que busca uma equivalência entre as descrições dos alimentos de cada par de bases, no nosso caso para simplificar só fizemos entre EFSA <-> FCID e FCID <-> FooDB, a relação entre EFSA <-> FooDB é obtida com a base FCID como intermediária.

Com base no modelo conceitual construímos o modelo relacional, onde cada entidade resultou em uma tabela, semelhantemente, cada atributo se tornou em uma coluna da respectiva tabela, inclusive as entidades intermediárias que realizavam a conexão entre as bases, as quais possuem 2 chaves estrangeiras e primárias, uma de cada base. Elas se tornaram tabelas intermediárias, responsáveis por registrar a equivalência entre um alimento de uma tabela e outro alimento da outra.

Para implementar o algoritimo de NLP, utilizamos a linguagem biblioteca Scikit-learn, que é utilizada para machine learning em geral, para tanto nós rodamos o código:
~~~
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar dados do FCID e do FoodDB (Configurar o ambiente para estar na raíz do repositório.)
fcid_data = pd.read_csv('bases/fcid/FCID_Code_Description.csv')
fooddb_data = pd.read_csv('bases/foodb/Food.csv')

# Pré-processamento: converter todos os nomes para minúsculas
fcid_data['processed'] = fcid_data['FCID_Desc'].str.lower()
fooddb_data['processed'] = fooddb_data['name'].str.lower()

# Usar TF-IDF para converter os nomes em vetores
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(fcid_data['processed'].tolist() + fooddb_data['processed'].tolist())

# Calcular a similaridade de cosseno
cosine_sim = cosine_similarity(tfidf_matrix[:len(fcid_data)], tfidf_matrix[len(fcid_data):])

# Encontrar a melhor correspondência para cada alimento do FCID
matches = []
for idx, row in enumerate(cosine_sim):
    best_match_idx = row.argmax()
    fcid_food = fcid_data.iloc[idx]['FCID_Desc']
    fooddb_food = fooddb_data.iloc[best_match_idx]['name']
    matches.append((fcid_food, fooddb_food))

# Criar um DataFrame com as correspondências
matches_df = pd.DataFrame(matches, columns=['FCID_Food', 'FoodDB_Food'])

# Salvar o DataFrame em um arquivo CSV
matches_df.to_csv('bases/relação/food_matches.csv', index=False)

~~~

A partir disso, conseguimos construir o relacionamento entre as tabelas FCID_Code_Description e Foods, ligando as tabelas e possibilitando a classificação quanto a nutrientes.
O modelo lógico de grafos procura ligar alimentos com dados sobre o seu consumo, ingredientes com as receitas que os usam, grupos e subgrupos com os alimentos que estão dentro deles e alimentos de diferentes bases para os quais encontramos correspondências entre suas descrições. Durante as consultas, que não foram implementadas, poderíamos também criar novas conexões entre vértices, inclusive tornando o grafo mais homogêneo.

Por fim, elaboramos perguntas que pudessem ser respondidas pelos nossos modelos, dando ênfase a integralização das bases de dados, comparando o consumo com diferentes parâmetros avaliativos, como ano da pesquisa, faixa etária e peso do consumidor, país em que foi feita a pesquisa e até mesmo diferentes pontos de vista sobre conceitos que trazem uma informação mais concreta sobre os dados disponíveis. Consideramos também os aspectos citados na motivação e contexto, como por exemplo a relação entre saúde e alimentação. Para as perguntas sobre grafos consideramos as ideias de análises de redes complexas, para encontrarmos relações entre grupos de ingredientes entre si e também com receitas.

## Evolução do Projeto
Evolução do Projeto:
Começamos escolhendo uma base de dados complementar que tivesse uma conexão com as bases de dados centrais, nos permitindo analisar dados de consumo e nutricionais por meio de hábitos alimentares.

Em seguida partimos para a construção do modelo conceitual a partir das bases de dados disponíveis. Durante a construção desse modelo, encontramos vários obstáculos: Como relacionar 2 bases de dados diferentes? A solução que encontramos era relacionar os tipos de alimentos entre si, por meio de correspondências entre alimentos que possuem uma descrição semelhante e para isso tivemos de recorrer a um algoritmo NLP que identificava semelhanças entre as descrições desses alimentos e fazia a relação de equivalência, indicada por uma entidade de relacionamento, no qual utilizamos um modelo simples de NLP, que usou a técnica de . Além disso, algumas tabelas se encontravam no formato de matrizes de adjacência, pois cada linha indicava a relação entre por exemplo, um ingrediente e uma receita que usava o mesmo, tornando a modelagem no modelo conceitual um pouco menos intuitiva do que no modelo de grafos. Também decidimos ocultar algumas tabelas/entidades que não contribuam para nossas análises.

Na modelagem relacional não encontramos muitos problemas, em geral traduzimos o modelo conceitual para o relacional seguindo as regras de cardinalidade de relacionamentos, adicionando novos atributos e criando tabelas intermediárias quando preciso. Na base de dados EFSA encontramos 4 tabelas, todas com informações úteis para possíveis análises, contudo elas possuem esquemas bem semelhantes, diferindo apenas de 1 ou 2 colunas, além de contar com informações pouco relevantes para nossas análises, referentes a curva gaussiana de consumo (exceto a média, que é nossa principal métrica). Para resolver isso, simplesmente removemos as colunas pouco relevantes e adicionamos novos atributos à tabela, referentes às outras tabelas, conseguindo assim unir todos os dados em uma só tabela, sem aumentar o número total de colunas e obtendo uma tabela bem propícia para as nossas análises. Um outro obstáculo encontrado foi durante a localização das chaves estrangeiras, já que a nomeação dos atributos tornava essa busca um pouco ambígua. Porém, observar as tabelas em um arquivo foi suficiente para identificar essas chaves. 

Utilizamos o binder para fazer a implementação das tabelas, vide o notebook.
Já no modelo lógico de grafos, a modelagem foi um pouco mais intuitiva, pois, como dito anteriormente, muitas tabelas do nosso conjunto de bases estavam já preparadas para o modelo de grafos, o maior desafio foi durante a implementação dos mesmos, que precisava do desenvolvimento de algumas linhas de código a mais para conectar os nós mediante as conexões impostas por uma terceira tabela.

Por fim, na seleção de perguntas tivemos um foco maior nas perguntas a serem respondidas pelo modelo lógico relacional. Conseguimos formular várias perguntas para esse modelo, levando em conta fatores que adicionavam um ponto de vista a mais para nossa análise, como por exemplo: o que caracteriza o ingrediente mais utilizado em um conjunto de receitas, a soma das quantidades que foram efetivamente utilizadas nessas receitas, ou em quantas receitas o ingrediente foi utilizado? Também pensamos em calcular métricas relacionadas à saúde dos consumidores, citamos aqui a ideia de um consumo médio de alimentos, que juntamente com as informações nutricionais da FooDB nos proporcionava uma estimativa média sobre o consumo de cada grupo populacional, em diferentes países e anos. Fomos evoluindo as nossas perguntas conforme criávamos o nosso modelo relacional e aprofundávamos nosso entendimento sobre a importância do tópico. Já no modelo lógico de grafos tentamos envolver conceitos de análise de rede complexas, ressaltamos aqui a seguinte pergunta: há algum conjunto de ingredientes que aparecem juntos em várias receitas diferentes? Que busca por meio dos conceitos de modularidade encontrar uma comunidade em meio ao grafo de ingredientes, evidenciando um conjunto de ingredientes que são comuns a várias receitas.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada


#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Quais os alimentos que cada grupo populacional mais consome? E qual o perfil 
>     calórico desses alimentos?
>   * Para responder essa pergunta podemos filtrar os consumos pelo grupo populacional 
>     e realizar uma soma sobre as médias de consumo, agrupando isso pela coluna de 
>     alimentos
>     SELECT MAX(consumo_total)
>     FROM(SELECT SUM(efsa.Mean_Subjects) consumo_total
>                 FROM EFSA_INTAKE efsa
>	       GROUP BY efsa.Population_Group, efsa.Exposure_Hierarchy_7);

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Quais os alimentos que cada grupo populacional mais consome? E qual o perfil 
>     calórico desses alimentos?
>   * Para responder essa pergunta podemos filtrar os consumos pelo grupo populacional 
>     e realizar uma soma sobre as médias de consumo, agrupando isso pela coluna de 
>     alimentos
>     SELECT MAX(consumo_total)
>     FROM(SELECT SUM(efsa.Mean_Subjects) consumo_total
>                 FROM EFSA_INTAKE efsa
>	       GROUP BY efsa.Population_Group, efsa.Exposure_Hierarchy_7);

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Para cada grupo de alimento, qual o alimento pertencente a este grupo que é
>     mais consumido?

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Qual o alimento mais consumido em cada país, levando em conta o peso do 
>     consumidor?

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Há algum conjunto de ingredientes que aparecem juntos em várias receitas 
>     diferentes?

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Que ingrediente combina mais com diferentes alimentos?

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * É possível prever a presença de pares de ingredientes em uma mesma receita?