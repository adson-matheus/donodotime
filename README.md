# donodotime
http://donodotime.herokuapp.com

Site para notícias de NBA e NFL em Python/Django

<h3>Acessando o site</h3>
Para uma melhor experiência, é altamente recomendado você fazer login utilizando uma conta do Google para visualizar as notícias completas.

<h3>Instalar localmente</h3>
É aconselhado você ter alguma experiência com Python, Django, comandos de terminal e saiba utilizar ambientes virtuais para que entenda este tutorial completamente.
<br>

Se você deseja instalar localmente e fazer mudanças no projeto, precisará primeiro realizar algumas instalações, além de clonar o repositório.
<br>

É necessário ter o <a href="https://pypi.org/project/pip/" target="_blank">pip</a> instalado em sua máquina, visite o site oficial e siga as instruções para instalá-lo. Crie um ambiente virtual com <a href="https://pypi.org/project/virtualenv/" target="_blank">virtualenv</a> na pasta do projeto clonado (não dentro da raíz do projeto!) usando <code>pip install virtualenv</code> e, em seguida, crie um novo ambiente com o comando <code>virtualenv nome-do-ambiente</code> e o ative usando <code>source nome-do-ambiente/bin/activate</code>. Para desativar, basta escrever <code>deactivate</code> no terminal.
<br>

Para baixar os pacotes requeridos, ative o seu virtualenv e vá até a pasta raiz do projeto, onde está o arquivo 'requirements.txt' e use o comando:
<code>pip install -r requirements.txt</code>
ou, dependendo da versão do Python instalada:
<code>pip3 install -r requirements.txt</code>
<br>

<h3>Oauth2</h3>
Se deseja utilizar o login com oauth2, a partir do Google, é necessário realizar o próximo procedimento.<br>
Visitar este <a href="https://console.developers.google.com/" target="_blank">site</a> de developers e logar com sua conta Google. Após isso, siga este <a href="https://dev.to/codetricity/how-to-set-up-django-with-central-oauth2-login-1co/" target="_blank">tutorial de Craig Oda</a>, ele serve para que você consiga realizar login utilizando contas do Google.

ps: Não se esqueça de criar o arquivo 'local_settings.py' e adicionar suas credenciais do Google, como mostrado no tutorial, e lembre-se de importar esse arquivo a partir do 'settings.py'.
<br>

<h3>Settings.py</h3>
Diversas configurações do 'settings.py' estão em modo de produção, se você deixá-las no arquivo, provavelmente não retornará erro pois os pacotes já foram instalados (é aconselhado que você exclua ou, pelo menos, deixe comentado para não causar conflitos); algumas variáveis de ambiente devem ser mudadas para modo de desenvolvimento:
<br>

Encontre <code>SECRET_KEY</code> e defina = 'sua-chave-secreta'.<br>
#existem diversos geradores de SECRET_KEY para o Django na internet.


Encontre <code>DEBUG</code> e defina = True.<br>
#modo de desevolvimento


Encontre <code>ALLOWED_HOSTS</code> e defina = ['localhost',].<br>
#para rodar em sua máquina

<h3>Banco de dados</h3>
Faça a migração do banco de dados, a partir da linha de comando da raíz do projeto, onde está o arquivo 'manage.py' <code>python3 manage.py makemigrations</code>
e depois:
<code>python3 manage.py migrate</code>
<br>

<h3>Rodando o projeto localmente</h3>
Crie um admin:
<code>python3 manage.py createsuperuser</code>
e inicie o servidor:
<code>python3 manage.py runserver</code>
agora vá até http://localhost:8000 e o projeto estará rodando localmente.
Para acesso total das funcionalidades como admin, faça login com suas credenciais de superuser em http://localhost:8000/admin/ e volte ao index. A partir de então, você poderá controlar tudo através do front-end.
