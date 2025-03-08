# Oráculo - Vetra

Este projeto é um assistente inteligente para o sistema **Vetra**, projetado para automatizar a busca e interpretação de dados armazenados em planilhas do Google Sheets. Ele permite que os usuários façam perguntas sobre os dados e recebam respostas relevantes de forma interativa.

## 📌 Funcionalidades

- **Busca Inteligente**: Permite que os usuários façam perguntas sobre os dados disponíveis.
- **Filtragem de Informações**: Identifica palavras-chave importantes para refinar os resultados.
- **Conexão com API do Google Sheets**: Obtém e processa os dados diretamente de uma planilha.
- **Exibição Organizada**: Exibe resumos e trechos detalhados das informações encontradas.
- **Histórico de Consultas**: Mantém um registro das perguntas feitas e suas respostas.
- **Interface Intuitiva**: Construída com Streamlit, garantindo uma experiência visual agradável.

## 🚀 Tecnologias Utilizadas

- **Python**
- **Streamlit** (Interface Web)
- **Requests** (Requisições HTTP para API do Google Sheets)
- **Regex** (Extração de palavras-chave)
- **Datetime** (Formatação de datas)

## 📖 Como Funciona

1. O usuário faz uma pergunta no chat.
2. O sistema extrai as palavras-chave relevantes da pergunta.
3. A API do Google Sheets é consultada para buscar os dados disponíveis.
4. Os dados são filtrados com base nas palavras-chave.
5. Um resumo dos resultados é exibido junto com trechos relevantes.
6. O histórico das interações é salvo na sessão.

## 🔧 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio/oraculo-vetra.git
   cd oraculo-vetra
   ```
2. Instale as dependências:
   ```bash
   pip install streamlit requests
   ```
3. Execute o projeto:
   ```bash
   streamlit run app.py
   ```

## 📂 Estrutura do Projeto

```
/
├── app.py              # Código principal
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## 🔄 Melhorias Futuras

- Implementação de aprendizado de máquina para respostas mais precisas.
- Suporte a múltiplas fontes de dados além do Google Sheets.
- Integração com IA para resumos mais avançados.

```

🛠️ **Desenvolvido por David Marques** para aprimorar o sistema **Vetra** 🚀

