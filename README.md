# Projeto Info4V

Aplicação web desenvolvida em Python com Flask, SQLAlchemy e SQLite.

## Pré-requisitos

- Python 3.12 ou superior;
- Git (opcional, caso o projeto seja obtido de um repositório);
- Chromium, instalado pelo Playwright para a execução dos testes de interface.

## Instalação

### 1. Obtenha o projeto

Clone o repositório ou copie os arquivos para a máquina e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd info4v-prog-int
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 4. Configure o banco de dados

Por padrão, a aplicação utiliza SQLite no arquivo `instance/app.sqlite3`. O diretório e o banco são criados automaticamente. Para criar as tabelas, execute:

```bash
flask --app run:app db upgrade
```

A configuração de conexão com MySQL foi mantida. Para utilizá-la, defina `DATABASE_DRIVER=mysql` e configure o banco `2026-info4v` e as credenciais correspondentes.

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e substitua os valores de exemplo pelas configurações da sua máquina:

```bash
cp .env.example .env
```

O arquivo `.env` não deve ser versionado, pois pode conter credenciais e chaves secretas. Para a configuração padrão, defina o driver SQLite e a chave da aplicação antes de executá-la. Exemplo no Linux/macOS:

```bash
export DATABASE_DRIVER="sqlite"
export SECRET_KEY="uma-chave-secreta-forte"
```

No Windows (PowerShell):

```powershell
$env:DATABASE_DRIVER = "sqlite"
$env:SECRET_KEY = "uma-chave-secreta-forte"
```

Como o carregamento automático do `.env` não está configurado no ponto de entrada atual, exporte as variáveis no terminal ou carregue o arquivo manualmente antes da execução. No Linux/macOS, é possível carregá-lo com:

```bash
set -a
source .env
set +a
```

No Windows, configure as variáveis individualmente usando o PowerShell conforme o exemplo acima. Nunca compartilhe a `SECRET_KEY` nem versione o arquivo `.env` com valores reais.

## Execução

Com o ambiente virtual ativado e as variáveis configuradas:

```bash
python run.py
```

Abra [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

## Testes

Inicie a aplicação em um terminal e, em outro terminal com o ambiente virtual ativado, execute:

```bash
python -m unittest discover -s tests
```

Os testes usam um navegador Chromium em modo visível (`headless=False`). Portanto, mantenha o ambiente gráfico disponível durante a execução.

## Estrutura principal

```text
app/
├── forms/       # Formulários Flask-WTF
├── models/      # Modelos do banco de dados
├── services/    # Regras de negócio
├── static/      # CSS, JavaScript e imagens
├── templates/   # Templates Jinja2
└── routes.py    # Rotas da aplicação
config.py        # Configuração do Flask e do banco
run.py           # Ponto de entrada
requirements.txt # Dependências Python
tests/           # Testes automatizados
```

## Solução de problemas

- **Erro de conexão com o MySQL:** confirme se `DATABASE_DRIVER=mysql`, o serviço e o banco `2026-info4v` estão disponíveis, e se `DB_USERNAME` e `DB_PASSWORD` estão corretos.
- **Erro ao instalar ou executar os testes:** execute novamente `python -m playwright install chromium` dentro do ambiente virtual.
- **Porta 5000 ocupada:** encerre o processo que a utiliza antes de iniciar a aplicação.
