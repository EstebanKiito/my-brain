---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Instalar Ruby on Rails en Mac M1

Estos son los pasos que usé para instalar las herramientas del curso (Ruby 3.1.0 con RVM, Rails 7.0.4 y PostgreSQL) en un Mac con chip M1, y para crear un proyecto nuevo.

## Pasos para instalar los elementos del curso en Mac M1
```bash
brew install gnupg2
gpg --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
```

Utilizar **Rosetta** en caso de errores.

```bash
brew install postgresql
```

```bash
rvm install ruby-3.1.0 --reconfigure --enable-yjit --with-openssl-dir=$(brew --prefix openssl@3)
```

```bash
gem install rails -v 7.0.4
brew services start postgresql
```

## Crear un proyecto
```bash
rails new nombre-proyecto --database=postgresql
cd nombre-proyecto
bundle install
```

> [!tip] Complemento — qué hace cada paso
> | Comando | Para qué |
> |---|---|
> | `brew install gnupg2` + `gpg --recv-keys …` | instala GPG e importa las llaves para verificar el instalador de RVM |
> | `curl … get.rvm.io \| bash -s stable` | instala **RVM** (Ruby Version Manager), que permite tener varias versiones de Ruby |
> | `brew install postgresql` | instala la base de datos **PostgreSQL** |
> | `rvm install ruby-3.1.0 … --with-openssl-dir=…` | compila Ruby 3.1.0 enlazado al OpenSSL de Homebrew (en M1 es una fuente común de errores) |
> | `gem install rails -v 7.0.4` | instala la gema Rails en la versión del curso |
> | `brew services start postgresql` | deja PostgreSQL corriendo como servicio |
> | `rails new … --database=postgresql` | crea el proyecto configurado para PostgreSQL (por defecto usaría SQLite) |
> | `bundle install` | instala las gemas listadas en el `Gemfile` |
>
> - **Verificar la instalación** (slides "RoR - First API"): `ruby --version` y `rails --version`.
> - **Rosetta** permite correr en el M1 programas compilados para Intel; se recomienda si alguna compilación falla.
> - Las slides también pedían instalar **Postman**: https://www.postman.com/downloads/
> - Guía oficial: https://guides.rubyonrails.org/getting_started.html
> - Para crear un proyecto **solo API** (sin vistas): `rails new hello --api`.

## Preguntas de repaso

1. ¿Para qué sirve RVM?
> [!question]- Respuesta
> Para instalar y alternar entre varias versiones de Ruby en un mismo computador.

2. ¿Qué hace la opción `--database=postgresql` en `rails new`?
> [!question]- Respuesta
> Configura el proyecto para usar PostgreSQL como base de datos (`config/database.yml` y la gema `pg`) en vez de SQLite, que es el valor por defecto.

3. ¿Qué hace `bundle install`?
> [!question]- Respuesta
> Instala todas las gemas (dependencias) declaradas en el `Gemfile` del proyecto.
