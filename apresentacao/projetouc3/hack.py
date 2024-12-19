import os

# Função para substituir o texto dentro dos arquivos .py e .html
def substituir_texto(pasta, texto_antigo, texto_novo):
    # Percorrer todos os arquivos da pasta e subpastas
    for root, dirs, files in os.walk(pasta):
        print(f"Verificando a pasta: {root}")  # Mostra qual pasta está sendo verificada
        for file in files:
            # Verificar se o arquivo é .py ou .html
            if file.endswith(('.py', '.html')):  # Agora verificamos tanto arquivos .py quanto .html
                caminho_arquivo = os.path.join(root, file)
                print(f"Processando o arquivo: {caminho_arquivo}")  # Mostra o arquivo que está sendo processado
                
                try:
                    # Abrir o arquivo e ler seu conteúdo
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                    
                    # Verificar se o texto a ser substituído está presente no conteúdo
                    if texto_antigo in conteudo:
                        print(f"Texto encontrado no arquivo: {caminho_arquivo}")  # Texto foi encontrado
                        
                        # Substituir o texto antigo pelo novo
                        conteudo_novo = conteudo.replace(texto_antigo, texto_novo)

                        # Reescrever o arquivo com o conteúdo atualizado
                        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                            f.write(conteudo_novo)
                        
                        print(f"Texto substituído no arquivo {caminho_arquivo}")
                    else:
                        print(f"Texto não encontrado no arquivo: {caminho_arquivo}")  # Texto não encontrado no arquivo
                except Exception as e:
                    print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")

# Caminho da pasta onde estão os arquivos .py e .html
pasta = r'C:\Users\169129532024.2\Documents\GitHub\HTPY03\apresentacao\projetouc3'  # Caminho com prefixo 'r' para string raw
texto_antigo = 'src="/static/global/images'  # Texto que você deseja substituir
texto_novo = 'src="/static/global/images'  # Texto que substituirá o antigo

# Chamar a função
substituir_texto(pasta, texto_antigo, texto_novo)