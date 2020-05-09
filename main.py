#!/usr/bin/env python
# coding: utf-8

# # Desafio 4
# 
# Neste desafio, vamos praticar um pouco sobre testes de hipóteses. Utilizaremos o _data set_ [2016 Olympics in Rio de Janeiro](https://www.kaggle.com/rio2016/olympic-games/), que contém dados sobre os atletas das Olimpíadas de 2016 no Rio de Janeiro.
# 
# Esse _data set_ conta com informações gerais sobre 11538 atletas como nome, nacionalidade, altura, peso e esporte praticado. Estaremos especialmente interessados nas variáveis numéricas altura (`height`) e peso (`weight`). As análises feitas aqui são parte de uma Análise Exploratória de Dados (EDA).
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
import statsmodels.api as sm


# In[2]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# In[3]:


athletes = pd.read_csv("athletes.csv")


# In[4]:


def get_sample(df, col_name, n=100, seed=42):
    """Get a sample from a column of a dataframe.
    
    It drops any numpy.nan entries before sampling. The sampling
    is performed without replacement.
    
    Example of numpydoc for those who haven't seen yet.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Source dataframe.
    col_name : str
        Name of the column to be sampled.
    n : int
        Sample size. Default is 100.
    seed : int
        Random seed. Default is 42.
    
    Returns
    -------
    pandas.Series
        Sample of size n from dataframe's column.
    """
    np.random.seed(seed)
    
    random_idx = np.random.choice(df[col_name].dropna().index, size=n, replace=False)
    
    return df.loc[random_idx, col_name]


# ## Inicia sua análise a partir daqui

# In[102]:


# Sua análise começa aqui.


# ## Questão 1
# 
# Considerando uma amostra de tamanho 3000 da coluna `height` obtida com a função `get_sample()`, execute o teste de normalidade de Shapiro-Wilk com a função `scipy.stats.shapiro()`. Podemos afirmar que as alturas são normalmente distribuídas com base nesse teste (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[6]:


def q1():
    # Retorne aqui o resultado da questão 1.
    amostra = get_sample(athletes,"height",3000)
    resultado = list(sct.shapiro(amostra)) 
    #teste "verifica" se os dados vem de uma distribuiçao normal
    #Wcalculado < Wα
    #(W_Calculado, p-value)
    #pra porder ser considerado normal o p-value tem que ser menor do que 
    return bool(resultado[1]>0.05)
    #se deu falso é pq nao é uma distribuiçao normal
    #Quando o p-value for maior que 0,05 (p > 0.05) a hipótese nula (dos dados seguirem uma distribuição normal) é aceita.
    #sm.qqplot(amostra, fit=True, line="45");
    #sns.distplot(amostra, kde=False, bins=25, hist_kws={"density": True});

    pass


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que? **nao achei nada condizente, porque ele da um histograma no estilo de uma distribuiçao normal mas aparentemente o p-value é maior do que 0.05**
# * Plote o qq-plot para essa variável e a analise.**tbm nao entendo  pq q o qq-plot deu uma grande parte na linha **
# * Existe algum nível de significância razoável que nos dê outro resultado no teste? (Não faça isso na prática. Isso é chamado _p-value hacking_, e não é legal).**sim, se for 0.0000005**

# ## Questão 2
# 
# Repita o mesmo procedimento acima, mas agora utilizando o teste de normalidade de Jarque-Bera através da função `scipy.stats.jarque_bera()`. Agora podemos afirmar que as alturas são normalmente distribuídas (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[7]:


def q2():
    # Retorne aqui o resultado da questão 2.
    amostra = get_sample(athletes,"height",3000)
    resultado = sct.jarque_bera(amostra)
    return bool(resultado[1]>0.05)
    pass


# __Para refletir__:
# 
# * Esse resultado faz sentido? **ainda nao**

# ## Questão 3
# 
# Considerando agora uma amostra de tamanho 3000 da coluna `weight` obtida com a função `get_sample()`. Faça o teste de normalidade de D'Agostino-Pearson utilizando a função `scipy.stats.normaltest()`. Podemos afirmar que os pesos vêm de uma distribuição normal ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[68]:


def q3():
    # Retorne aqui o resultado da questão 3.
    amostra = get_sample(athletes,"weight",3000)
    resultado = sct.normaltest(amostra)
    #sns.distplot(amostra, kde=False, bins=25, hist_kws={"density": True});
    #sm.qqplot(amostra, fit=True, line="45");
    return bool(resultado[1]>0.05)
    #resultado
    pass


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que? **agora aparentemente a forma do grafio e o resultado do teste sao condizentes**
# * Um _box plot_ também poderia ajudar a entender a resposta.

# ## Questão 4
# 
# Realize uma transformação logarítmica em na amostra de `weight` da questão 3 e repita o mesmo procedimento. Podemos afirmar a normalidade da variável transformada ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[9]:


def q4():
    # Retorne aqui o resultado da questão 4.
    amostra = get_sample(athletes,"weight",3000)
    amostra_log = np.log(amostra)
    resultado_log = sct.normaltest(amostra_log)
    return bool(resultado_log[1]>0.05)
    #sns.distplot(amostra_log, kde=False, bins=25, hist_kws={"density": True});
    #sm.qqplot(amostra_log, fit=True, line="45");
    pass


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que? **se levar em consideraçao os resultado anteriores foi condizente com a tranformacao**
# * Você esperava um resultado diferente agora? **sim, esperava mas ainda nao aconteceu o q eu gostaria de ter visto**

# > __Para as questão 5 6 e 7 a seguir considere todos testes efetuados ao nível de significância de 5%__.

# ## Questão 5
# 
# Obtenha todos atletas brasileiros, norte-americanos e canadenses em `DataFrame`s chamados `bra`, `usa` e `can`,respectivamente. Realize um teste de hipóteses para comparação das médias das alturas (`height`) para amostras independentes e variâncias diferentes com a função `scipy.stats.ttest_ind()` entre `bra` e `usa`. Podemos afirmar que as médias são estatisticamente iguais? Responda com um boolean (`True` ou `False`).

# In[10]:


def q5():
    # Retorne aqui o resultado da questão 5.
    aux_bra = athletes['height'][athletes['nationality']=='BRA']
    aux_usa = athletes['height'][athletes['nationality']=='USA']

    bra_df = pd.DataFrame(aux_bra)
    usa_df = pd.DataFrame(aux_usa)
    #tive que tirar os nulos ...
    resultado = sct.ttest_ind(bra_df.dropna(), usa_df.dropna(),  equal_var = False)
    return bool(resultado[1]<0.05)
    #se a estatística t for superior ao valor crítico, a diferença será significativa. 
    #Se sua estatística t for menor, os dois números serão indistinguíveis em termos estatísticos.
    #fonte: https://pt.surveymonkey.com/mp/t-tests-explained/?program=7013A000000mweBQAQ&utm_bu=CR&utm_campaign=71700000064157503&utm_adgroup=58700005705977647&utm_content=39700052004881803&utm_medium=cpc&utm_source=adwords&utm_term=p52004881803&utm_kxconfid=s4bvpi0ju&gclid=Cj0KCQjwhtT1BRCiARIsAGlY51K60WcsH-w6g41awwB9u0CgL7k9qXVWaR_fce6sXXa4eksDpoXYR2UaAjqBEALw_wcB
    pass


# ## Questão 6
# 
# Repita o procedimento da questão 5, mas agora entre as alturas de `bra` e `can`. Podemos afimar agora que as médias são estatisticamente iguais? Reponda com um boolean (`True` ou `False`).

# In[11]:


def q6():
    # Retorne aqui o resultado da questão 6.
    aux_bra = athletes['height'][athletes['nationality']=='BRA']
    aux_can = athletes['height'][athletes['nationality']=='CAN']

    bra_df = pd.DataFrame(aux_bra)
    can_df = pd.DataFrame(aux_can)
    #tirando os nulos tbm...
    resultado = sct.ttest_ind(bra_df.dropna(), can_df.dropna(),  equal_var = False)
    #resultado
    return bool(resultado[1]<0.05)
    pass


# ## Questão 7
# 
# Repita o procedimento da questão 6, mas agora entre as alturas de `usa` e `can`. Qual o valor do p-valor retornado? Responda como um único escalar arredondado para oito casas decimais.

# In[12]:


def q7():
    # Retorne aqui o resultado da questão 7.
    aux_usa = athletes['height'][athletes['nationality']=='USA']
    aux_can = athletes['height'][athletes['nationality']=='CAN']

    usa_df = pd.DataFrame(aux_usa)
    can_df = pd.DataFrame(aux_can)
    # nulos ...
    resultado = sct.ttest_ind(usa_df.dropna(), can_df.dropna(),  equal_var = False)
    #resultado
    return round(float(resultado[1]),8)
    pass


# __Para refletir__:
# 
# * O resultado faz sentido?
# * Você consegue interpretar esse p-valor?
# * Você consegue chegar a esse valor de p-valor a partir da variável de estatística?
