# Projeto final do curso de testes

Projeto final do curso de teste de software, ministrado por **David Ferreira**, visa testar várias funcionalidades presentes no site [Udemy](https://www.udemy.com).

Os testes foram automatizados com o [framework Selenium](https://www.selenium.dev/), voltado para testes de aplicações web. Para o desenvolvimento dos scripts de automação, foi utilizado a linguagem Python.

### Indice
- [Testes implementados](#testes-implementados)
    - [Funcionalidade: Cadastro de usuário](#funcionalidade-cadastro-de-usuário)
- [Configurar o ambiente para testes](#configurar-o-ambiente-para-testes)
    - [Pré Requisitos](#pré-requisitos)
    - [Clonar Repositório](#clonar-repositório)
    - [Criar e ativar ambiente virtual python (venv)](#criar-e-ativar-ambiente-virtual-python-venv)
    - [Instalar dependencias do projeto](#instalar-dependencias-do-projeto)
    - [Definir navegador de execução dos testes](#definir-navegador-de-execução-dos-testes)
- [Executar testes](#executar-testes)
- [Equipe de Testers](#equipe-de-testers)

### Testes implementados
#### Funcionalidade: Cadastro de usuário
- Cadastrar novo usuário com sucesso (Automação bloqueada pela plataforma)
- Cadastrar um usuário que já existe (Automação bloqueada pela plataforma)
- Cadastrar usuário com e-mail fora de padrão
- Testar funcionalidade do botão exibir Senha

### Configurar o ambiente para testes

#### Pré Requisitos
- Driver Selenium
    - Para navegador Chrome: [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br)
    - Para navegador Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver)
- Python

#### Clonar Repositório
```shell
git clone git@github.com:FredericoFavaro/Projeto_final_curso_testes.git
```

#### Criar e ativar ambiente virtual python (venv)
Na raiz do projeto, execute o comando **para criar** a venv:
```shell
python -m venv .venv
```
**Obs:** Em `.venv` o `.` indica que diretório que será criado para armazenar o ambiente virtual é oculto.

**Para ativar** use o comando:
```shell
source .venv/bin/activate
```
#### Instalar dependencias do projeto
```python
pip install -r requirements.txt
```
#### Definir navegador de execução dos testes
Por padrão o projeto esta configurado para rodar no navegador **Chrome** e alguns de seus derivados.
Caso queira mudar para o Firefox, acesse o arquivo `features/environment.py` e edite a linha dentro da função `before_scenario` de:
```python
context.driver = webdriver.Chrome()
```
para:
```python
context.driver = webdriver.Firefox()
```
### Executar testes
No terminal e estando no diretorio do projeto, rode o comando:
```shell
behave
```
Esse comando irá executar todos os cenários de testes. Caso queira rodar algum cenário especifico, basta usar a flag `-n` e o título do cenário como informado no arquivo `.feature`:
```shell
behave -n "Testar funcionalidade do botão exibir Senha"
```

### Equipe de Testers
- [Frederico Fávaro Ribeiro](https://github.com/FredericoFavaro)
- [Ezequiel Leandro Jr.](https://github.com/Ezequiel-leandro-jr)
- [Arthur Alves](https://github.com/ArthurAlves1994)
- [Marcelo Mendonça](https://github.com/mclmendonca)
- Silas Oliveira
- [Advalker Souto Maior](https://github.com/Advalker)
