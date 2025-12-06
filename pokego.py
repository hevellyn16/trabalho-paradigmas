import sys          
import os           
import subprocess   
import pokelang     

def main():
    # 1. VERIFICAÇÃO DE ARGUMENTOS
    # sys.argv é uma lista. [0] é o nome do script, [1] é o primeiro argumento.
    if len(sys.argv) < 2:
        print("ERRO: Faltou informar o arquivo .poke")
        print("Uso correto: python pokego.py <arquivo.poke>")
        return

    arquivo_poke = sys.argv[1]

    # 2. CHAMADA DA TRADUÇÃO
    print(f"--> Traduzindo {arquivo_poke}...")

    arquivo_py = pokelang.converter_arquivo(arquivo_poke)

    if arquivo_py is None:
        print("--> Falha na tradução.")
        return

    # 3. EXECUÇÃO DO CÓDIGO GERADO
    print("--------------------------------")
    print("--> Executando...")

    try:
        # subprocess.run cria um processo filho para rodar o arquivo Python
        # sys.executable garante que usamos o mesmo interpretador Python atual
        subprocess.run([sys.executable, arquivo_py], check=True)
    except subprocess.CalledProcessError:
        print("--> Ocorreu um erro durante a execução do programa.")
    except Exception as e:
        print(f"--> Erro inesperado: {e}")

    print("--------------------------------")

    # 4. LIMPEZA
    # Se o usuário digitou "debug" no comando, a gente NÃO apaga
    if "debug" in sys.argv:
        print(f"--> MODO DEBUG: Arquivo '{arquivo_py}' mantido.")
    else:
        # Se não tem "debug", apaga normalmente
        if os.path.exists(arquivo_py):
            os.remove(arquivo_py)

if __name__ == "__main__":
    main()
