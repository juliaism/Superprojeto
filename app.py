import streamlit as st
import pandas as pd
import pickle


st.set_page_config(page_title="Preditor de Evasão Escolar", layout="wide")

st.title("🔮 Sistema Inteligente de Previsão de Abandono Escolar")
st.markdown("Insira as características do estudante para receber o diagnóstico dos 3 modelos de Machine Learning em tempo real.")


@st.cache_resource 
def carregar_modelos():
    with open('modelo_bayes.pkl', 'rb') as f:
        bayes = pickle.load(f)
    with open('modelo_arvore.pkl', 'rb') as f:
        arvore = pickle.load(f)
    with open('modelo_knn.pkl', 'rb') as f:
        knn = pickle.load(f)
    return bayes, arvore, knn

modelo_bayes, modelo_arvore, modelo_knn = carregar_modelos()


st.sidebar.header("📋 Perfil do Novo Estudante")

bolsista_selecao = st.sidebar.selectbox("O aluno é Bolsista?", ["Sim", "Não"])
turno_selecao = st.sidebar.selectbox("Qual o turno das aulas?", ["Diurno", "Noturno"])
sexo_selecao = st.sidebar.selectbox("Qual o sexo biológico?", ["Masculino", "Feminino"])
idade_ingresso = st.sidebar.slider("Idade ao ingressar no curso:", 17, 34, 21)


bolsista_num = 1 if bolsista_selecao == "Sim" else 0
turno_num = 1 if turno_selecao == "Diurno" else 0
sexo_num = 1 if sexo_selecao == "Masculino" else 0


dados_novo_aluno = pd.DataFrame([{
    'bolsista_num': bolsista_num,
    'turno_num': turno_num,
    'sexo_num': sexo_num,
    'idade_ingresso': idade_ingresso
}])


if st.sidebar.button("🧠 Executar Modelos de Previsão"):
    
    
    pred_bayes = modelo_bayes.predict(dados_novo_aluno)[0]
    pred_arvore = modelo_arvore.predict(dados_novo_aluno)[0]
    pred_knn = modelo_knn.predict(dados_novo_aluno)[0]
    
   
    tradutor = {0: "🎉 Sucesso (Se Formará)", 1: "⚠️ Alerta de Abandono"}
    
    
    st.subheader("📊 Comparativo de Diagnósticos dos Modelos")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Abordagem Bayesiana (Núcleo)", value=tradutor[pred_bayes])
        st.caption("Acurácia do Modelo: 70.80%")
        
    with col2:
        st.metric(label="Árvore de Decisão", value=tradutor[pred_arvore])
        st.caption("Acurácia do Modelo: 70.11%")
        
    with col3:
        st.metric(label="KNN (K-Vizinhos)", value=tradutor[pred_knn])
        st.caption("Acurácia do Modelo: 67.49%")