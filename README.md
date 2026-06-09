🎓 Sistema Inteligente de Previsão de Evasão Escolar
Este projeto foi desenvolvido como parte do Super Projeto de Estatística e Probabilidade. O objetivo central é utilizar técnicas de Ciência de Dados para identificar precocemente alunos em risco de evasão, permitindo intervenções pedagógicas assertivas.

🚀 O Projeto
O sistema integra uma análise exploratória visual (via Power BI) com um motor de classificação preditiva (via modelos de Machine Learning) para fornecer um diagnóstico probabilístico em tempo real sobre a trajetória acadêmica do estudante.

🛠 Tecnologias Utilizadas
Linguagem: Python 3.x

Framework Web: Streamlit

Modelagem Preditiva: Scikit-Learn (Bayesiano, Árvore de Decisão e KNN)

Visualização: Power BI (Embed)

Manipulação de Dados: Pandas & Pickle

📊 Funcionalidades
Dashboard Estratégico: Painel interativo com métricas de análise exploratória dos dados educacionais.

Simulador de Risco: Interface para entrada de características individuais (bolsista, turno, sexo, idade) com predição imediata.

Análise de Ensemble: O sistema compara 3 algoritmos distintos para entregar um parecer final baseado em consenso (Votação Majoritária).

💻 Como rodar localmente
Clone o repositório:

Bash
git clone https://github.com/juliaism/Superprojeto.git
cd Superprojeto
Instale as dependências:

Bash
pip install streamlit pandas scikit-learn
Execute a aplicação:

Bash
streamlit run app.py
🧠 Modelos de Classificação
O sistema utiliza os seguintes algoritmos para a predição:

Abordagem Bayesiana: Focada na probabilidade condicional do perfil.

Árvore de Decisão: Baseada em regras de ramificação de dados.

K-Nearest Neighbors (KNN): Baseado na similaridade com perfis de alunos anteriores.

Projeto desenvolvido por [Seu Nome/Equipe] para a disciplina de Estatística e Probabilidade.


