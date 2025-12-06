import re
import random

# --- FUNÇÕES AUXILIARES DO TRADUTOR ---

def limpar_var(nome):
    """Padroniza nomes de variáveis."""
    return nome.lower().replace(' ', '_')

def processar_codigo(expr):
    """Trata variáveis e funções."""
    expr = re.sub(r"(?<!\w)\((\w+)\)", lambda m: limpar_var(m.group(1)), expr)
    expr = re.sub(r"(?<=\w)\((\w+)\)", lambda m: f"({limpar_var(m.group(1))})", expr)
    
    def substituir_var_solta(m):
        palavra = m.group(1)
        keywords = ["True", "False", "None", "not", "and", "or", "input", "float", "int", "str"]
        if palavra in keywords: return palavra
        return palavra.lower()

    expr = re.sub(r"\b([A-Z][a-zA-Z0-9_]*)\b", substituir_var_solta, expr)
    expr = re.sub(r"\bfloat\(", "glitch_float(", expr)
    return expr

def processar_texto(expr):
    """Trata strings para print."""
    expr = re.sub(r"str\s*\(\s*([a-zA-Z_]\w*)\s*\)", lambda m: f"str({limpar_var(m.group(1))})", expr)
    expr = re.sub(r"(?<!str)\(([a-zA-Z_]\w*)\)", lambda m: f"str({limpar_var(m.group(1))})", expr)
    return expr

def processar_condicao(cond):
    return processar_codigo(cond)


# --- CÓDIGO INJETADO (Runtime Esotérico - Cinnabar Engine) ---
CABECALHO = r'''# Início
import sys
import time
import random
import atexit
import builtins

# Tenta importar som do Windows
try:
    import winsound
    SOM_HABILITADO = True
except ImportError:
    SOM_HABILITADO = False

# --- CONFIGURAÇÕES VISUAIS ---
COR_GLITCH = "\033[95m" # Roxo
COR_HEX = "\033[90m"    # Cinza
COR_ERR = "\033[91m"    # Vermelho
COR_CODE = "\033[92m"   # Verde
RESET = "\033[0m"
BOLD = "\033[1m"

# --- ENGINE GLITCH ---

def typewriter(texto, atraso=0.02):
    # Simula texto sendo digitado
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        if random.random() < 0.01: time.sleep(0.1)
        time.sleep(atraso)
    print("")

def gerar_ruido(texto):
    # Insere caracteres estranhos no texto
    if random.random() > 0.4: return texto
    chars_ruido = ['#', '?', '%', '&', '§', 'ERROR', '¿']
    lista = list(texto)
    for _ in range(random.randint(1, 2)):
        if lista:
            pos = random.randint(0, len(lista))
            lista.insert(pos, random.choice(chars_ruido))
    return "".join(lista)

def hexdump_simulado():
    print(f"{COR_HEX}LOADING TEXTURES... 0x8000{RESET}")
    time.sleep(0.2)

def inicializar_corrupcao():
    print(f"\n{COR_GLITCH}{BOLD}▒▒ CINNABAR ISLAND MEMORY DUMP v2.1 ▒▒{RESET}")
    hexdump_simulado()

def tocar_som_erro():
    # Toca um beep agudo se estiver no Windows
    if SOM_HABILITADO:
        try:
            winsound.Beep(2000, 800)
        except:
            pass
    else:
        print('\a')

# --- TRATAMENTO DE ERRO GLOBAL (BAD EGG) ---
def manipulador_de_excecao(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print(f"\n{COR_HEX}Processo interrompido.{RESET}")
        return
    
    # EFEITOS DE ERRO FATAL
    print(f"\n{COR_ERR}{BOLD}>> FATAL ERROR: BAD EGG DETECTED <<{RESET}")
    print(f"{COR_ERR}O jogo tentou acessar um endereço inválido.{RESET}")
    print(f"{COR_HEX}Dump: {value}{RESET}")
    
    tocar_som_erro()

sys.excepthook = manipulador_de_excecao

atexit.register(lambda: print(f"{COR_HEX}\n[CONNECTION TERMINATED]{RESET}"))
inicializar_corrupcao()

# --- FUNÇÕES PARA O USUÁRIO ---

def void_echo(*args, **kwargs):
    # Print com glitch visual
    texto = " ".join(map(str, args))
    texto_corrompido = gerar_ruido(texto)
    prefixo = f"{COR_CODE}▓▒░{RESET} "
    if texto != texto_corrompido: prefixo = f"{COR_ERR}⚠ {RESET}"
    sys.stdout.write(prefixo)
    typewriter(texto_corrompido)

def void_inject(prompt=""):
    # Input estilizado
    if prompt: void_echo(prompt)
    return builtins.input(f"{COR_GLITCH}0x??? >> {RESET}")

def glitch_float(valor):
    # Converte para float ou retorna 0.0 se falhar
    try:
        return float(valor)
    except:
        print(f"{COR_ERR}[GLITCH] Valor '{valor}' inválido. Convertido para NaN.{RESET}")
        return 0.0

def duplicar_item(valor):
    # Glitch de multiplicar por 128
    print(f"{COR_CODE}[GLITCH] Item duplicado no 6º slot!{RESET}")
    try:
        return valor * 128
    except:
        return valor
'''

# --- DICIONÁRIO DE REGRAS ---

REGRAS = {
    # 1. Início e Fim
    r"Um pokémon selvagem apareceu": CABECALHO, 
    r"O pokémon selvagem desmaiou": "\n# Fim",

    # 2. Funções (Evolução)
    r".*está evoluindo para\s+(.+)": "def {nome_func}():",
    r".*parou de evoluir": "pass",
    r".*use a habilidade\s+(.+)!": "{nome_func}()",

    # 3. Loops (Música)
    r"🎵\s+(\d+)\s+\((.+)\)\s+na [Mm]ochila": "{var} = {val}\nwhile {var} > 0:",
    r"(.*(pega|tira|lança|joga|assa) uma \((.+)\).*)": "void_echo(\"{frase}\")\n{var} -= 1",
    r"Nenhuma \((.+)\) na mochila.*": "void_echo(f\"Nenhuma {{{var}}} na mochila...\")",

    # 4. Comandos Especiais
    r"\((.+)\) Usou item raro": "{var} = duplicar_item({var})",
    r"O jogo travou": "raise Exception('MISSINGNO ENCOUNTER')",

    # 5. Input e Output
    r"\((.+)\) Use cantar\s+(.+)": "void_echo({expr})",
    r"\((.+)\) Use detectar": "{var} = void_inject()",

    # 6. Atribuição
    r"\((.+)\) tem\s+(.+)\s+de vida": "{var} = {val}",

    # 7. Condicionais
    r"\((.+)\) Equipou Faixa da escolha enquanto\s+\((.+)\)": "while {condicao}:",
    r"\((.+)\) Escolha o movimento se\s+\((.+)\)": "if {condicao}:",
    r".*Fim da (faixa|escolha)": "pass",
    
    r"^\s*$": "",

    # 8. Regra Genérica
    r"^\s*\(([^)]+)\)\s+(.+)": "void_echo(f\"{{{var}}} {texto}\")",
}

def traduzir_linha(linha):
    linha = linha.strip()
    for padrao, traducao in REGRAS.items():
        match = re.match(padrao, linha)
        if match:
            if "está evoluindo para" in padrao:
                return traducao.format(nome_func=limpar_var(match.group(1))), 1
            if "parou de evoluir" in padrao: return traducao, -1
            if "use a habilidade" in padrao:
                return traducao.format(nome_func=limpar_var(match.group(1))), 0
            if "🎵" in padrao:
                val, var = match.group(1), match.group(2)
                return traducao.format(var=limpar_var(var), val=val), 1
            if "uma" in padrao and ("pega" in padrao or "lança" in padrao):
                frase, var = match.group(1), match.group(3)
                return traducao.format(var=limpar_var(var), frase=frase), 0
            if "Nenhuma" in padrao:
                return traducao.format(var=limpar_var(match.group(1))), -1
            if "O jogo travou" in padrao:
                return traducao, 0
            if "Usou item raro" in padrao:
                return traducao.format(var=limpar_var(match.group(1))), 0
            if "Use cantar" in padrao:
                return traducao.format(expr=processar_texto(match.group(2))), 0
            if "Use detectar" in padrao:
                return traducao.format(var=limpar_var(match.group(1))), 0
            if "tem" in padrao and "de vida" in padrao:
                var = limpar_var(match.group(1))
                valor_bruto = match.group(2)
                val = processar_codigo(valor_bruto)
                return traducao.format(var=var, val=val), 0
            if "Equipou Faixa" in padrao or "Escolha o movimento" in padrao:
                cond = match.group(2)
                return traducao.format(condicao=processar_condicao(cond)), 1
            if "Fim da" in padrao: return "pass", -1
            if padrao.startswith(r"^\s*\(([^)]+)\)"):
                var = limpar_var(match.group(1))
                texto = match.group(2)
                return traducao.format(var=var, texto=texto), 0
            return traducao, 0

    if linha and not linha.startswith("#"): return f"# ERRO: {linha}", 0
    return "", 0

def converter_arquivo(arquivo_entrada):
    arquivo_saida = arquivo_entrada.rsplit('.', 1)[0] + ".py"
    linhas_py = []
    indent = 0
    lendo = False
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            for linha in f:
                linha_limpa = linha.strip()
                if re.match(r"Um pokémon selvagem apareceu", linha_limpa, re.IGNORECASE):
                    lendo = True
                    codigo, mudanca = traduzir_linha(linha_limpa)
                elif re.match(r"O pokémon selvagem desmaiou", linha_limpa, re.IGNORECASE):
                    codigo, mudanca = traduzir_linha(linha_limpa)
                    if codigo:
                        espacos = "    " * indent
                        linhas_py.append(espacos + codigo)
                    break 
                else:
                    if not lendo: continue
                    codigo, mudanca = traduzir_linha(linha_limpa)

                if mudanca < 0: indent += mudanca
                if indent < 0: indent = 0
                if codigo:
                    espacos = "    " * indent
                    linhas_py.append(espacos + codigo.replace("\n", "\n" + espacos))
                if mudanca > 0: indent += mudanca

        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write("\n".join(linhas_py))
        return arquivo_saida
    except Exception as e:
        print(f"ERRO: {e}")
        return None
