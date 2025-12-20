# blango

Starting point for the Advanced Django course. This is the equivalent of the following command:

```bash
$ django-admin.py startproject blango
```

## Configurações com django-configurations

- `settings.py` foi refatorado para classes usando `django-configurations`:
	- `Common`: base compartilhada
	- `Development`: para desenvolvimento local (`DEBUG=True`)
	- `Production`: endurecida para produção (SSL, HSTS, cookies seguros e `SECRET_KEY` via env)

- Variáveis de ambiente relevantes:
	- `DJANGO_CONFIGURATION`: seleciona a classe (`Development` ou `Production`)
	- `SECRET_KEY`: obrigatório em `Production`
	- `DATABASE_URL`: opcional (ex.: `postgres://...`), senão usa SQLite por padrão
	- `CSRF_TRUSTED_ORIGINS`: opcional em produção (lista de origens)

- Executar comandos com paths contendo espaços (use aspas):

```bash
"/home/suporte6/Área de Trabalho/blango/.venv/bin/python" \
	"/home/suporte6/Área de Trabalho/blango/manage.py" check

export DJANGO_CONFIGURATION=Development
"/home/suporte6/Área de Trabalho/blango/.venv/bin/python" \
	"/home/suporte6/Área de Trabalho/blango/manage.py" runserver

# Produção (exemplo)
export DJANGO_CONFIGURATION=Production
export SECRET_KEY="coloque-uma-chave-secreta-aqui"
export DATABASE_URL="postgres://usuario:senha@host:5432/db"
"/home/suporte6/Área de Trabalho/blango/.venv/bin/python" \
	"/home/suporte6/Área de Trabalho/blango/manage.py" migrate
"/home/suporte6/Área de Trabalho/blango/.venv/bin/python" \
	"/home/suporte6/Área de Trabalho/blango/manage.py" runserver 0.0.0.0:8000
```

## Crispy Forms

- Pacotes: `django-crispy-forms` + `crispy-bootstrap4` instalados.
- Em `INSTALLED_APPS`: adicionar `crispy_forms`.
- Em `settings.py`: `CRISPY_TEMPLATE_PACK = "bootstrap4"`.
- Renderização de formulário: `{{ form|crispy }}` e `{% load crispy_forms_tags %}`.
