import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# ==============================
# CONFIGURAÇÕES
# ==============================
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") 
MODELO = "gemini-1.5-flash"

# ==============================
# CLASSE DO ASSISTENTE 
# ==============================
class AssistenteIA:
    def __init__(self, api_key=API_KEY, modelo=MODELO):
        """Inicializa o assistente de IA."""
        if not api_key:
            raise ValueError("❌ API Key do Gemini não encontrada! Configure GEMINI_API_KEY no ambiente.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(modelo)
        self.historico = []

    def _eh_codigo(self, texto: str) -> bool:
        """Detecta se o input do usuário parece código."""
        # Padrões para detectar Python ou C/C++
        padroes = [r"int\s+main", r"#include", r"printf", r"scanf",  # C/C++
                   r"def\s+", r"print\(", r"import\s+"]          # Python
        return any(re.search(p, texto) for p in padroes)

    def _detectar_linguagem(self, codigo: str) -> str:
        """Detecta se é Python ou C/C++."""
        if re.search(r"int\s+main|#include", codigo):
            return "C/C++"
        return "Python"

    def _enviar_prompt(self, prompt_completo: str) -> str:
        """Envia um prompt completo para a IA e retorna a resposta formatada."""
        try:
            self.historico.append({"role": "user", "content": prompt_completo})
            
            resposta = self.model.generate_content(prompt_completo)
            conteudo = resposta.text.strip() if resposta and resposta.text else "⚠️ Não consegui gerar uma resposta."

            self.historico.append({"role": "assistant", "content": conteudo})
            return self._formatar_resposta(conteudo)
        except Exception as e:
            return f"❌ Erro ao processar: {str(e)}"

    def _formatar_resposta(self, texto: str) -> str:
        """Formata a resposta removendo warnings e padronizando blocos de código."""
        linhas = [linha for linha in texto.splitlines() if not linha.strip().startswith("WARNING:")]
        resposta = "\n".join(linhas).strip()
        resposta = re.sub(r"```(\s*python)?", "```python", resposta, flags=re.IGNORECASE)
        resposta = re.sub(r"```(\s*c(\+\+)?\s*)?", "```cpp", resposta, flags=re.IGNORECASE)
        return resposta

    def analisar_codigo(self, codigo: str, linguagem: str) -> str:
        """Cria um prompt para análise de código e o envia."""
        prompt = f"""
        Você é um revisor de código especialista.
        O usuário enviou um código em {linguagem}.

        Tarefas:
        1. Identifique erros de sintaxe ou lógicos e más práticas.
        2. Sugira melhorias de desempenho, clareza e boas práticas.
        3. Explique passo a passo o que o código faz.
        4. Forneça uma versão melhorada do código, se aplicável.

        Código enviado:
        ```{linguagem.lower()}
        {codigo}
        ```
        """
        return self._enviar_prompt(prompt)
    
    def responder_pergunta(self, pergunta: str) -> str:
        """Cria um prompt para responder a uma pergunta de programação e o envia."""
        prompt = f"""
        Você é um assistente de programação sênior e especialista.
        O usuário fez uma pergunta sobre programação.
        Responda de forma clara, objetiva e com exemplos em Python ou C/C++.
        
        Pergunta do usuário:
        {pergunta}
        """
        return self._enviar_prompt(prompt)

    def perguntar(self, entrada: str) -> str:
        """Ponto de entrada principal. Decide se a entrada é código ou pergunta."""
        if self._eh_codigo(entrada):
            linguagem = self._detectar_linguagem(entrada)
            return self.analisar_codigo(entrada, linguagem)
        else:
            return self.responder_pergunta(entrada)

# ==============================
# LOOP PRINCIPAL
# ==============================
if __name__ == "__main__":
    print("🤖 Code-Mentor iniciado! (digite 'sair' para encerrar)\n")

    ia = AssistenteIA()

    while True:
        try:
            entrada = input("Você: ").strip()
            if entrada.lower() in ["sair", "exit", "quit"]:
                print("👋 Encerrando o Code-Mentor. Até logo!")
                break

            resposta = ia.perguntar(entrada)
            print(f"\nAssistente:\n{resposta}\n")
        except KeyboardInterrupt:
            print("\n👋 Encerrando o Code-Mentor. Até logo!")
            break