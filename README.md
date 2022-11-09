# Distribuidora Digital

Controle de estoque

## Como rodar o projeto?

- Clone este repositório
- Crie um virtualenv com Python 3.
- Ative o virtualenv
- Instale as dependências.
- Rode as migrações

```
git clone https://github.com/pedrolaraburu/distribuidora-digital.git
cd distribuidora-digital
python3 -m venv .venv
soruce .venv/bin/active
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```