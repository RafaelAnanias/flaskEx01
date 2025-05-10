# Projeto Flask01 - Configuração de Ambiente e Git

Para realizar essa atividade eu precisei remover o arquivo remover o diretório `.venv` do controle do Git


## Como o arquivo já tinha sido adiconado anteriormente, segui esse passo a passo para remover:

1º comando: git rm -r --cached .venv

Esse comando remove o diretório .venv do Git, mas mantém o ambiente virtual no seu computador.

Para criar o arquivo gitignore e adiconar o .venv digitei esse código:

echo ".venv/" >> .gitignore

Para gerar gerar o arquivo de dependências digitei esse código no terminal:

pip freeze > requirements.txt

Após seguir essas instruções a atividade foi concluída com sucesso!