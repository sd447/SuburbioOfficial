Para executar a aplicação utilize os seguintes passos

Abra o terminal e execute os seguintes comandos

  # Para criar um ambiente virtual
  python3 -m venv .venv

  # Para instalar todas as dependencias do projeto
  pip install -r requirements.txt

  #Para realizar a migração
  python manage.py makemigrations

  #Para gerar o banco baseado nas migrações
  python manage.py migrate

  #Finalmente o comando para iniciar o servidor local com a aplicação web
  python manage.py runserver
