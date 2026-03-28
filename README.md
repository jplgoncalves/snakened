<p align="center">
  <img width="1408" height="768" alt="logo_snakened (2)" src="https://github.com/user-attachments/assets/cb199465-bf12-4fa2-bb31-e900f873f089" />
</p>

# 🐍 Snakened

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Version: 0.1.0](https://img.shields.io/badge/version-0.1.0--alpha-blue.svg)

**Inspirada na simplicidade de Python. Forjada para a performance de C.**

Snakened é uma "Linguagem em S" desenhada para ser intuitiva, mas com uma execução ultra-rápida através de compilação nativa. Ela combina o melhor dos dois mundos: a legibilidade que os desenvolvedores amam com a velocidade bruta que os sistemas de próxima geração exigem.

[🌐 Visite o Site Oficial](https://jplgoncalves.github.io/snakened)

---

## ✨ Diferenciais Técnicos

* 🚀 **Performance Nativa:** Compilação otimizada que rivaliza com linguagens de baixo nível.
* 🧠 **Sintaxe Limpa:** Estilo Python para máxima produtividade.
* 🛡️ **Extensão de Ficheiro:** `.s`
* 🔧 **Focada em Sistemas:** Ideal para quem precisa de controle e velocidade.

## 💻 Exemplo de Código (.s)

```s
func principal() {
    escrever("Olá mundo da Snakened!")
}

func calcular_fibonacci(n: int) -> int {
    if (n <= 1) {
        return n
    }
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)
}
