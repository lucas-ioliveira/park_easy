# Park Easy

Nesse repositório contém um projeto realizado o back-end com python, framework Django, Django Rest framework e Docker.

Desenvolvi esse projeto com o intuito de aplicar e aprimorar minhas habilidades em Django Rest framework e desenvolvimento em containers utilizando o Docker.

O Projeto consiste em uma Api para gereciamento de um estacionamento de carros. O usuário do sistema (Coloborador) consegue realizar login no sistema, cadastrar-se como novo usuário e todas as operaçoes de um CRUD para carros, clientes e vagas. A api conta com uma autenticação jwt com auxílio da biblioteca Simple JWT.

<br>

<h2>Pré-requisitos</h2>

- [Docker](https://www.docker.com/) 

<br>

<h2>Clone</h2>

```bash
git clone https://github.com/lucas-ioliveira/park_easy.git
```

<br>

<h2 id="started">🚀 Primeiros passos</h2>

<p>Basta entrar no diretório do projeto e no terminal rodar o comando:</p> 

```bash
make build
```

- ou

```bash
docker compose -f docker-compose.yaml up -d --build
```

<p>Isso fará com que todas as dependências sejam instaladas e um container docker seja executado.</p>

<br>

<p>Verifique se o container está em execução com o comando:</p>

```bash
docker ps -a
```

<br>

<p>Acessando o container:</p>

```bash
make enter container
```
- ou

```bash
docker exec -it park_easy_app bash
```

<p>Realize as migrações:</p>

```bash
python manage.py makemigrations && python manage.py migrate

```

<p>Crie um super usuario:</p>

```bash
python manage.py createsuperuser
```

<p>Com um usuário criado é possível acessar o painel administrativo e também gerar o token de acesso para consulir a api.</p>

<br>


<h2 id="routes">📍 API Endpoints</h2>

<p>Após rodar o projeto é possivel acessar a rota: (/swagger/) onde terá acesso ao swagger e uma documentação mais detalhada e também testar os endpoints.</p>

<br>

**Token**

<p>A validade do token está definida para 60 minutos.</p>
   
| <kbd>POST /api/v1/authentication/token/</kbd> | Obtendo o token de acesso para consumo da API.


**REQUEST**
```json
{
  "username": "Seu usuário",
  "password": "Sua senha"
}
```

**RESPONSE**
```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NDI5MTI1MSwiaWF0IjoxNzQ0MjA0ODUxLCJqdGkiOiI0YjFhN2NmNTkzNTI0OWM2ODI2NWVkZGUwYzZhMTBlNyIsInVzZXJfaWQiOjJ9.Bab-9HeBaEwqSqFn5y6IRz3fwas-PhqOQqQISL62GWE",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MjA1MTUxLCJpYXQiOjE3NDQyMDQ4NTEsImp0aSI6ImJiNjlkODJmNjUyMTRkMmViODhkNWEyMjBjOTQ0Yzk1IiwidXNlcl9pZCI6Mn0.90KP4KaRinC8vas0g4bVvCVynHWlCuPN1JoLcDR3eMA"
}
```

<br>

- A validade do  refresh token está definida para 7 dias.
   
| <kbd>POST /api/v1/authentication/token/refresh/</kbd> | Obtendo um novo token.


**REQUEST**
```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NDgxNjQ5MywiaWF0IjoxNzQ0MjExNjkzLCJqdGkiOiI2ODJiYTA2ZWFkOTc0OTQzOTUwZTAxMzM1NDNmZDE0NCIsInVzZXJfaWQiOjJ9.Tq9qd2tLeqfd0BSRMO4LibCLOSkh82kuS6FMcJDEXdU"
}
```

**RESPONSE**
```json
{
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MjE1MzA0LCJpYXQiOjE3NDQyMTE2OTMsImp0aSI6ImI1M2YxYTViNTRhYTQ1MDY5NWJiMzQzN2E0NTVjOGMwIiwidXNlcl9pZCI6Mn0.BntbNf0B4RzrI_Uc8lndtUXtbFhx3SG-4QQOf31Z-h0"
}
```

<br><br>


**Clients**

<p>Exemplo criação de cliente:</p>

| <kbd>POST /api/v1/clients/</kbd> | Endpoint para criação de cliente.


**REQUEST**
```json
{
	"first_name": "João",
    "last_name": "Legado",
    "email": "joao.legado@email.com",
    "phone": "11911111111",
    "address": "Rua exemplo",
    "city": "Cidade exemplo",
    "state": "Estado exemplo",
    "country": "Pais exemplo",
}
```

**RESPONSE**
```json
{
	"id": 1,
	"first_name": "João",
	"last_name": "Legado",
	"email": "joao.legado@email.com",
	"phone": "11911111111",
	"address": "Rua exemplo",
	"city": "Cidade exemplo",
	"state": "Estado exemplo",
	"country": "Pais exemplo",
	"is_active": true,
	"created_at": "2025-04-09T12:26:57.022438-03:00",
	"updated_at": "2025-04-09T12:26:57.022459-03:00"
}
```
```json
status  201 created
```

<br><br>


#### Rota para o admin (/admin/);

<p>Administração do sistema.</p>

![Rota do admin](docs/images/admin.png)







