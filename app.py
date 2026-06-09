import streamlit as st
import pandas as pd
import pickle
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURAÇÃO E LAYOUT
# ==========================================
st.set_page_config(page_title="Dashboard | Previsão de Evasão", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 2. CSS AVANÇADO (ESTILO PREMIUM)
# ==========================================
st.markdown("""
<style>
    /* Tipografia mais moderna e limpa */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Título Customizado com Gradiente */
    .titulo-premium {
        background: -webkit-linear-gradient(45deg, #1E3A8A, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8em;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        padding-top: 20px;
    }
    .sub-titulo {
        text-align: center;
        color: #64748b;
        font-size: 1.1em;
        font-weight: 400;
        margin-bottom: 40px;
    }

    /* Cards de Métrica com efeito Glass e Hover */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 5px solid #3B82F6;
        border-radius: 12px;
        padding: 20px 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-top: 5px solid #1E3A8A;
    }
    
    /* Centralizando textos das métricas */
    div[data-testid="stMetricValue"] {
        font-size: 1.4em !important;
        justify-content: center;
    }
    div[data-testid="stMetricLabel"] {
        justify-content: center;
        font-size: 1em !important;
        color: #475569 !important;
        font-weight: 600;
    }

    /* Botão Premium no Sidebar */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: 600;
        width: 100%;
        height: 50px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3);
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(59, 130, 246, 0.5);
        color: white;
    }

    /* Banners de Resultado */
    .banner-sucesso {
        background-color: #ecfdf5;
        border-left: 6px solid #10b981;
        color: #065f46;
        padding: 20px;
        border-radius: 8px;
        font-size: 1.2em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .banner-alerta {
        background-color: #fef2f2;
        border-left: 6px solid #ef4444;
        color: #991b1b;
        padding: 20px;
        border-radius: 8px;
        font-size: 1.2em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        gap: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABEÇALHO CUSTOMIZADO
# ==========================================
st.markdown('<p class="titulo-premium">Sistema de Inteligência Educacional</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-titulo">Plataforma integrada de Análise Exploratória e Modelagem Preditiva de Evasão</p>', unsafe_allow_html=True)

# ==========================================
# 4. SEÇÃO 1 - ANÁLISE DOS DADOS (POWER BI)
# ==========================================
st.markdown("### 📊 Visão Geral dos Dados (Power BI)")
st.info("Explore interativamente o painel abaixo para identificar padrões demográficos e acadêmicos.")

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMGNjZmYzNzUtMmU4Ny00NmRjLWFiODAtZTdmNmVmYjJlMjZkIiwidCI6ImM5YTlmNzRkLWViMjUtNDg4OS05ZGJhLTE2NDA2NjQxNDFiMCJ9"

with st.container():
    components.iframe(power_bi_url, width=1200, height=620, scrolling=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ==========================================
# 5. SEÇÃO 2 - CLASSIFICAÇÃO PROBABILÍSTICA
# ==========================================
st.markdown("### 🧠 Simulador Preditivo de Evasão")
st.write("Utilize os parâmetros na barra lateral esquerda para processar o perfil de um novo aluno pelos algoritmos.")

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

# ==========================================
# 6. MENU LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='80' style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    st.markdown("### 📋 Configurar Perfil")
    
    bolsista_selecao = st.selectbox("Status de Bolsa:", ["Sim", "Não"], help="O aluno recebe algum tipo de auxílio financeiro?")
    turno_selecao = st.selectbox("Turno Matriculado:", ["Diurno", "Noturno"])
    sexo_selecao = st.selectbox("Gênero:", ["Masculino", "Feminino"])
    idade_ingresso = st.slider("Idade ao Ingressar:", 17, 34, 21)

    botao_executar = st.button("Executar Algoritmos ⚡")

# ==========================================
# 7. PROCESSAMENTO E RESULTADOS
# ==========================================
bolsista_num = 1 if bolsista_selecao == "Sim" else 0
turno_num = 1 if turno_selecao == "Diurno" else 0
sexo_num = 1 if sexo_selecao == "Masculino" else 0

dados_novo_aluno = pd.DataFrame([{
    'bolsista_num': bolsista_num,
    'turno_num': turno_num,
    'sexo_num': sexo_num,
    'idade_ingresso': idade_ingresso
}])

resultado_container = st.container()

if botao_executar:
    with st.spinner("Processando dados e consultando modelos matemáticos..."):
        
        pred_bayes = modelo_bayes.predict(dados_novo_aluno)[0]
        pred_arvore = modelo_arvore.predict(dados_novo_aluno)[0]
        pred_knn = modelo_knn.predict(dados_novo_aluno)[0]
        
        tradutor = {0: "Formação Prevista", 1: "Alto Risco"}
        soma_riscos = pred_bayes + pred_arvore + pred_knn
        
        with resultado_container:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Renderiza o Banner Customizado
            if soma_riscos >= 2:
                st.markdown("""
                    <div class="banner-alerta">
                        <span style='font-size: 1.8em;'>🚨</span>
                        <div>
                            <strong>ALERTA DE EVASÃO DETECTADO</strong><br>
                            <span style='font-size: 0.9em; font-weight: 400;'>A maioria dos modelos aponta que este aluno tem grande probabilidade de abandonar o curso.</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="banner-sucesso">
                        <span style='font-size: 1.8em;'>🎓</span>
                        <div>
                            <strong>TENDÊNCIA POSITIVA DETECTADA</strong><br>
                            <span style='font-size: 0.9em; font-weight: 400;'>A maioria dos modelos aponta que este aluno possui perfil para concluir o curso com sucesso.</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br><br>", unsafe_allow_html=True)
            
            # Exibição dos cards customizados
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Teorema de Bayes (Núcleo)", value=tradutor[pred_bayes], delta="Acurácia: 70.80%", delta_color="off")
            with col2:
                st.metric(label="Árvore de Decisão", value=tradutor[pred_arvore], delta="Acurácia: 70.11%", delta_color="off")
            with col3:
                st.metric(label="KNN (K-Vizinhos)", value=tradutor[pred_knn], delta="Acurácia: 67.49%", delta_color="off")