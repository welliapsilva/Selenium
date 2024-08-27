import sys
import os
from cx_Freeze import setup, Executable
#requisitos, ter o arqguivo com o codigo e criar este arquivo como nome setup na mesma pasta
##junto na pasta do arquivo, cria as pastas necessaris, com porexemplo a pata musicas citada abaixo
#a pata criada ira ir pra dentro do executavel
##criar também um arquivo com o nome setup, que é este que estavamo configurando neste codito atual

# Definir o que deve ser incluído na pasta final
arquivos = ['dados.txt', 'musicas/'] #incluindo pasta de musica e arquivo de dados se necessário
# Saida de arquivos
configuracao = Executable(
    script='app.py', #arquivo com o codigo da aplicação
    icon='rede.ico' #incluir um icone, basta pegar um arqivo png e colocar no google "png to ico" pra transformar tipo .ico
)
# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatizar o login deste site',
    author='Jhonatan de Souza',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True #isso faz o codigo executar sem precisa instalar o pthon no pc
    }},
    executables=[configuracao]
)