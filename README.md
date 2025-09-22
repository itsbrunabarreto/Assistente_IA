# Code-Mentor: Assistente de Programação com IA Gemini

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 O que é o Code-Mentor?

O Code-Mentor é uma ferramenta projetada para auxiliar desenvolvedores, estudantes e entusiastas da programação. Ele atua como um mentor virtual, especialista nas linguagens **Python** e **C/C++**, capaz de:

* **Responder a perguntas de programação:** Desde conceitos básicos a tópicos complexos, o assistente fornece explicações claras com exemplos de código.
* **Analisar e revisar código:** Ao receber um trecho de código, a IA o analisa em busca de erros, más práticas e oportunidades de melhoria, fornecendo uma explicação detalhada e uma versão corrigida.

O projeto utiliza uma lógica de programação própria com expressões regulares para diferenciar entre perguntas e códigos, montando um prompt dinâmico e contextual para a API Gemini, garantindo respostas precisas para cada situação.

## ✨ Features

* **IA Especialista:** Assistência focada em Python e C/C++.
* **Detecção Inteligente:** Diferenciação automática entre perguntas e códigos.
* **Análise de Código:** Identificação de erros, sugestão de boas práticas e otimizações.
* **Interface Gráfica Moderna:** UI amigável e intuitiva construída com CustomTkinter.
* **Segurança:** Gestão segura da chave da API através de variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **IA Generativa:** API do Google Gemini (`gemini-1.5-flash`)
* **Bibliotecas Principais:**
    * `google-generativeai`: Para comunicação com a API Gemini.
    * `customtkinter`: Para a construção da interface gráfica.
    * `python-dotenv`: Para carregar a chave da API com segurança.
    * `re` (Expressões Regulares): Para a lógica de detecção de código.

---

## 🚀 Como Utilizar no seu PC

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/) instalado e configurado no PATH.
* [Git](https://git-scm.com/downloads) instalado.

### 1. Clonar o Repositório

    Abra seu terminal ou Git Bash e clone este repositório:

    git clone https://github.com/itsbrunabarreto/Assistente_IA
    cd [NOME_DA_PASTA_DO_PROJETO]

### 2. Criar e Ativar o Ambiente Virtual

    Cria o ambiente virtual na pasta .venv
    python -m venv .venv

    Ativa o ambiente virtual
    No Windows:
    .\.venv\Scripts\Activate.ps1

    No macOS/Linux:
    source .venv/bin/activate

### 3. Instalar Dependências

    pip install -r requirements.txt

### 4. Configurar a Chave da API

    Na pasta raiz do projeto, crie um arquivo chamado .env.

    Dentro deste arquivo, adicione a seguinte linha, substituindo "SUA_CHAVE..." pela sua chave de API real obtida no Google AI Studio:

    GEMINI_API_KEY=SUA_CHAVE_DE_API_REAL_AQUI

    Salve e feche o arquivo.

### 5. Executar a Aplicação

    python assistente_gui.py