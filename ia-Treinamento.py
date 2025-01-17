import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Configura a API do Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def ler_arquivo():
    """Lê o conteúdo do arquivo de texto"""
    try:
        with open('arquivo.csv', 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"

def fazer_busca(texto, pergunta):
    """Realiza uma busca no texto usando o Gemini"""
    try:
        # Inicializa o modelo
        modelo = genai.GenerativeModel('gemini-pro')
        
        # Cria o prompt combinando o texto e a pergunta
        prompt = f"""
        Com base no seguinte texto:
        
        {texto}
        
        Por favor, responda: {pergunta}
        """
        
        # Gera a resposta
        resposta = modelo.generate_content(prompt)
        return resposta.text
    
    except Exception as e:
        return f"Erro ao processar a busca: {str(e)}"

def main():
    # Lê o conteúdo do arquivo
    conteudo = ler_arquivo()
    
    while True:
            # Solicita a pergunta ao usuário
            pergunta = input("\nDigite sua pergunta sobre o texto (ou 'sair' para encerrar): ")
            
            if pergunta.lower() == 'sair':
                break
                
            # Realiza a busca
            resposta = fazer_busca(conteudo, pergunta)
            print("\nResposta:", resposta)
            print("\n" + "-"*50)

if __name__ == "__main__":
    main()
