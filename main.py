from src.lexer import lex

def executar():
    try:
        # Lê o teu ficheiro Snakened
        with open("exemplo.s", "r", encoding="utf-8") as f:
            codigo = f.read()
        
        print("🐍 Snakened v0.1 - A analisar o código...\n")
        
        # Transforma o texto em Tokens usando o Lexer que criaste
        tokens = lex(codigo)
        
        # Mostra o que a linguagem "entendeu"
        for t in tokens:
            print(f"Token: {t[0]:<10} | Valor: {t[1]}")
            
    except FileNotFoundError:
        print("Erro: Ficheiro 'exemplo.s' não encontrado!")

if __name__ == "__main__":
    executar()
