
# 🔴 PokéLang - Documentação Oficial (Cinnabar Edition)

**Disciplina:** Paradigmas de Linguagens de Programação  
**Projeto:** Criação de Linguagem Esotérica  
**Extensão de Arquivo:** `.poke`  
**Linguagem Alvo:** Python 3  
**Equipe:** 
* ANNA ALICYA MAGALHAES CRUZ - 568323
* ANTONIO KILDERE SOUSA MENEZES - 567258
* DANIEL NECO SILVA - 568270
* HEVELLYN MEIRIANE NASCIMENTO DE MESQUITA - 565892
* JOSE ARTHUR GOMES AZEVEDO - 567419
* TAYNARA DE ARAUJO ALVES - 565040

---

## 1. Introdução

A **PokéLang** é uma **Linguagem Esotérica de Horror Cósmico**, simulando um *Memory Dump* corrompido da infame **Ilha Cinnabar** (local dos glitches originais de Pokémon Red/Blue).

O objetivo da linguagem é proporcionar uma experiência de programação imersiva e instável. O código fonte (`.poke`) é processado por um tradutor que injeta uma "Engine de Corrupção", resultando em saídas de texto com efeito de máquina de escrever, caracteres "sujos" (Zalgo text), sons de sistema e erros fatais temáticos (Bad Egg).

---

## 2. Estrutura do Programa

Todo programa em PokéLang simula a leitura de um encontro selvagem na memória do jogo. O código deve estar contido dentro deste bloco:

```text
Um pokémon selvagem apareceu
    ... (Seu código aqui) ...
O pokémon selvagem desmaiou
````

-----

## 3\. Guia de Sintaxe e Comandos

### 3.1. Saída de Dados (Print / Void Echo)

Exibe informações na tela com efeito de digitação lenta (lag) e chance de corrupção visual.

  * **Sintaxe:** `(Nome) Use cantar "Texto"`
  * **Exemplo:**
    ```text
    (MissingNo) Use cantar "A realidade está falhando..."
    ```

### 3.2. Declaração de Variáveis

Variáveis são tratadas como atributos de vida ou dados na memória.

  * **Sintaxe:** `(Variavel) tem [Valor] de vida`
  * **Exemplo:** `(HP) tem 128 de vida`

### 3.3. Entrada de Dados (Input / Void Inject)

Lê dados do usuário com um prompt estilizado (`0x??? >>`).

  * **Sintaxe:** `(Variavel) Use detectar`
  * **Exemplo:** `(Comando) Use detectar`

### 3.4. Estruturas de Controle (Condicionais)

  * **Sintaxe (IF):**
    ```text
    (Variavel) Escolha o movimento se (Condição)
        ... código ...
    (Variavel) Fim da escolha
    ```

### 3.5. Estruturas de Repetição (Loops)

**A. Loop Padrão (While):**

```text
(Contador) Equipou Faixa da escolha enquanto (Contador > 0)
    ... código ...
(Contador) Fim da faixa
```

**B. Modo Música (Loop Decrescente):**
Gera efeitos visuais a cada iteração.

```text
🎵 [Valor] ([Variavel]) na Mochila
    ... (corpo do loop) ...
```

### 3.6. Funções (Evolução / Memory Leak)

Funções são decoradas automaticamente para simular vazamento de memória.

  * **Declaração:**
    ```text
    [Pokemon] está evoluindo para [NomeDaFuncao]
        ... código ...
    [Pokemon] parou de evoluir
    ```
  * **Chamada:** `[Pokemon] use a habilidade [NomeDaFuncao]!`

### 3.7. Comandos Esotéricos (Glitches e Crashes)

Comandos exclusivos para manipular a instabilidade do sistema.

**A. Duplicação de Item (Glitch da Ilha Cinnabar):**
Multiplica o valor de uma variável numérica por **128** instantaneamente.

  * **Sintaxe:** `(Variavel) Usou item raro`

**B. Induzir Crash (Bad Egg):**
Força o encerramento do programa com um erro fatal, som de alerta e tela vermelha.

  * **Sintaxe:** `O jogo travou`

-----

## 4\. Implementação Técnica (Cinnabar Engine)

O projeto vai além de uma simples tradução de texto. Ele utiliza **Injeção de Runtime**.

### Arquitetura

1.  **`pokelang.py` (O Compilador):**

      * Lê o arquivo `.poke`.
      * Utiliza **Regex** para traduzir a sintaxe.
      * **Diferencial:** Injeta um cabeçalho Python robusto (aprox. 100 linhas) no início do arquivo gerado. Esse cabeçalho contém a *Cinnabar Island Memory Dump Engine*.

2.  **A Engine (Runtime Injetado):**

      * **Typewriter Effect:** Simula processador lento imprimindo caractere por caractere.
      * **Zalgo Text:** Algoritmo probabilístico que insere caracteres aleatórios (`#`, `?`, `ERROR`) no texto de saída.
      * **Bad Egg Handler:** Sobrescreve o `sys.excepthook` do Python. Qualquer erro (divisão por zero, sintaxe inválida ou o comando `O jogo travou`) aciona uma tela de "FATAL ERROR" personalizada e emite um som de *beep* (`\a`).
      * **ANSI Colors:** Todo o terminal é colorizado com tons de roxo (glitch), verde (código) e vermelho (erro).

3.  **`pokego.py` (O Executor):**

      * Gerencia o fluxo: Chama o compilador -\> Executa o Python gerado -\> Limpa os arquivos temporários.

-----

## 5\. Códigos Exemplo

### 5.1. Hello World (`ola_mundo.poke`)

```text
Um pokémon selvagem apareceu
(Pikachu) Use cantar "Hello World! A memória está instável..."
O pokémon selvagem desmaiou
```

### 5.2. Teste de Glitch (`crash_test.poke`)

Demonstra a duplicação de itens e o erro fatal proposital.

```text
Um pokémon selvagem apareceu

(Ash) Use cantar "Iniciando hack do sistema..."
(Dinheiro) tem 10 de vida

(Ash) Use cantar "Dinheiro antes do glitch: " + str(Dinheiro)
(Ash) Use cantar "Usando Item Raro no 6º slot..."

# Multiplica por 128
(Dinheiro) Usou item raro

(Ash) Use cantar "Dinheiro agora: " + str(Dinheiro)
(Ash) Use cantar "O sistema não vai aguentar..."

# Isso encerra o programa com tela da morte e som
O jogo travou

(Ash) Use cantar "Essa linha nunca será lida."
O pokémon selvagem desmaiou
```

-----

## 6\. Como Executar

⚠️ **Aviso:** Aumente o volume para ouvir os alertas de erro do sistema.

1.  Certifique-se de ter o Python 3 instalado.
2.  Coloque os arquivos `pokego.py`, `pokelang.py` e seu arquivo `.poke` na mesma pasta.
3.  Execute no terminal:

<!-- end list -->

```bash
python pokego.py crash_test.poke
```
