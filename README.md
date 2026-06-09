# 🎓 Sistema Inteligente de Previsão de Evasão Escolar

Este projeto foi desenvolvido como parte do Super Projeto de Estatística e Probabilidade. O objetivo central é utilizar técnicas de Ciência de Dados para identificar precocemente alunos em risco de evasão, permitindo intervenções pedagógicas assertivas.

---

## 🚀 Sobre o Projeto
O sistema integra uma análise exploratória visual (via Power BI) com um motor de classificação preditiva (via modelos de Machine Learning) para fornecer um diagnóstico probabilístico em tempo real sobre a trajetória acadêmica do estudante.

## 🛠 Tecnologias Utilizadas
* Linguagem: Python 3.x
* Framework Web: Streamlit
* Modelagem Preditiva: Scikit-Learn (Bayesiano, Árvore de Decisão e KNN)
* Visualização: Power BI (Embed)
* Manipulação de Dados: Pandas & Pickle

## 📊 Funcionalidades
1. Dashboard Estratégico: Painel interativo com métricas de análise exploratória dos dados educacionais.
2. Simulador de Risco: Interface para entrada de características individuais com predição imediata.
3. Análise de Ensemble: O sistema compara 3 algoritmos distintos para entregar um parecer final baseado em consenso.

## 💻 Como rodar localmente

1. Clone o repositório:
git clone https://github.com/juliaism/Superprojeto.git
cd Superprojeto

2. Instale as dependências:
pip install streamlit pandas scikit-learn

3. Execute a aplicação:
streamlit run app.py

## 🧠 Modelos de Classificação

O sistema utiliza os seguintes algoritmos para a predição:

* Abordagem Bayesiana: Focada na probabilidade condicional do perfil.
* Árvore de Decisão: Baseada em regras de ramificação de dados.
* K-Nearest Neighbors (KNN): Baseado na similaridade com perfis de alunos anteriores.

---
*Projeto desenvolvido para a disciplina de Estatística e Probabilidade por Luan Piedade de Oliveira, Júlia Labad Jatene e João Paulo Oliveira*
