import streamlit as st
import requests
import re
from datetime import datetime

URL_API = "https://script.google.com/macros/s/AKfycbz--aEmwL96WoJ5cmjWqvlBwUyWLd45Jx-r4d6TAMX-Oo7ZFp7TBbFRZzsxDLwG6cnj/exec"

st.set_page_config(page_title="Oráculo", page_icon="🔍", layout="wide")
st.title("📊🔍 Oráculo - Vetra")

palavras_comuns = {"o", "é", "de", "do", "da", "um", "uma", "os", "as", "em", "para", "por", "com", "sobre", "tem", "que"}

def extrair_palavras_importantes(pergunta):
    palavras = re.findall(r'\b\w+\b', pergunta.lower())
    return [p for p in palavras if p not in palavras_comuns]

def buscar_dados_planilha():
    try:
        resposta = requests.get(URL_API)
        if resposta.status_code == 200:
            return resposta.json()
    except Exception:
        return None

def formatar_data(data):
    if isinstance(data, str) and 'T' in data:
        try:
            return datetime.fromisoformat(data.replace("Z", "")).strftime("%d/%m/%Y %H:%M")
        except ValueError:
            return data
    return data

def encontrar_informacoes(dados, pergunta):
    palavras_chave = extrair_palavras_importantes(pergunta)
    resultados = []
    
    for nome_aba, linhas in dados.items():
        for linha in linhas:
            # Apenas verifica os valores, não as chaves (cabeçalhos)
            texto_formatado = "\n".join([f"**{campo}:** {formatar_data(valor) if 'T' in str(valor) else valor}" for campo, valor in linha.items()])
            
            # Verifica se qualquer valor contém as palavras-chave
            if any(palavra in str(valor).lower() for palavra in palavras_chave for valor in linha.values()):
                resultados.append(f"📌 **{nome_aba.upper()}**\n{texto_formatado}")
    
    return resultados

def gerar_resumo(resultados):
    if not resultados:
        return "Parece que não encontrei informações relevantes com base na sua consulta. Que tal tentar outra pergunta?"

    narrativa = "Aqui estão algumas informações que encontrei relacionadas à sua consulta:\n\n"
    
    for resultado in resultados[:3]:  # Mostra os 3 primeiros resultados
        aba, dados = resultado.split("\n", 1)
        narrativa += f"🔹 **{aba}**: \n"
        narrativa += f"- {dados}\n\n"
    
    return narrativa

def salvar_historico(historico):
    st.session_state["historico"] = historico

def carregar_historico():
    return st.session_state.get("historico", [])

def limpar_historico():
    st.session_state["historico"] = []

def formatar_negrito_em_linha_abaixo(texto):
    return re.sub(r'(\*\*[^*]+\*\*)', r'\n\1', texto)

if st.sidebar.button("🗑️ Limpar Conversa"):
    limpar_historico()
    st.toast("🔄 Conversa limpa!", icon="✅")
    st.rerun()

historico = carregar_historico()

for item in historico:
    with st.chat_message("user"):
        st.write(f"💬 **Pergunta:** {item['pergunta']}")
    with st.chat_message("assistant"):
        st.write(f"🤖 **Resumo:** {item['resumo']}")
        for trecho in item["resultados"]:
            with st.expander(f"🔍 Detalhes da {item['pergunta']}"):
                st.write(formatar_negrito_em_linha_abaixo(trecho))

pergunta = st.chat_input("Digite sua pergunta sobre os dados das planilhas...")

if pergunta:
    dados_planilha = buscar_dados_planilha()
    if dados_planilha:
        resultados = encontrar_informacoes(dados_planilha, pergunta)
        resumo = gerar_resumo(resultados)
        
        with st.chat_message("user"):
            st.write(f"💬 **Pergunta:** {pergunta}")
        
        with st.chat_message("assistant"):
            st.success("✅ **Resumo das informações encontradas:**")
            st.write(resumo)
            if resultados:
                st.success("🔎 **Trechos Relevantes:**")
                for trecho in resultados:
                    with st.expander(f"🔍 Detalhes do resultado"):
                        st.write(formatar_negrito_em_linha_abaixo(trecho))
            else:
                st.warning("❌ Nenhuma informação relevante encontrada.")
        
        historico.append({"pergunta": pergunta, "resumo": resumo, "resultados": resultados})
        salvar_historico(historico)
    else:
        with st.chat_message("assistant"):
            st.error("⚠️ Erro ao acessar os dados das planilhas.")
