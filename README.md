# pokemon_sonimu

## Integrantes del equipo

### Marcos Fernandez Garcia
### Alan Novas Mateo

## Descripcición
Proyecto dedicado a las batallas pokemon utillizando lenguajes como Python, HTML y CSS

## Instalacion de flask
1. utilizar el siguiente comando en la terminal de visual como en una terminal independiente:

        1.1 Instalacion del venv

    python -m venv nombreDelArchivo

    ``
    python -m venv .venv
    ``
    
2. Instalar flask buscando las carpetas dentro del .venv, ejemplo:

        ./.venv/Script/pip.exe install flask

Con este comando instalarás el flask.

Revisa las versiones que tienes que sean iguales al archivo ``requirements.txt``

    ./.venv/Script/pip.exe freeze 
Para ver las versiones que tienes.

3. Para ejecutar el proyecto python -m app.main

## Fase 0 ✅
El proyecto tiene la siguiente estructura:

    mi_proyecto/
    ├─ app.py
    ├─ templates/
    │   └─ index.html
    └─ static/
        ├─ css/
        │ └─ estilo.css
        ├─ js/
        │ └─ app.js
        └─ img/
        └─ logo.png
    └─ data/
        └─ pokemon.json


El fichero `requiements.txt` tiene las versiones de flask que se utilizaran en este proyecto

## Fase 1 ✅

### Pagina inicial ✅

### Listado de Pokemon ✅

    Creacion de un for donde se recorre cada tipo de pokemones, se añade una imagen dependiendo del tipo de pokemon que sea
    es decir si es tipo fuego tendra una imagen fire.png y asi sucesivamente.

        {% for tipo in poke.types %}
            <img src="{{ url_for('static', filename='img/Types_name/' + tipo + '.png') }}" alt="{{ tipo }}">
            {% endfor %}
        <h2>{{poke.name}}</h2>


### PokemonID (Datalles)

A parte del tipo de pokemon presentamos con mas detalles la altura su peso que se a considerado que si un pokemon pesa mas de
100 es ligero si es mayor que 500 es pesado y por ultimo si pesa menos de 100 es normal.

            <h2>{{pokemon.name}}</h2>
            <!-- Tipos -->
            {% for tipo in pokemon.types %}
                <img src="{{ url_for('static', filename='img/Types_name/' + tipo + '.png') }}" alt="{{ tipo }}">
            {% endfor %}

            <!-- Altura -->
            <p>Altura: {{ pokemon.height }}0 cm </p>

            <!-- Pesos -->
            {% if 100 > pokemon.weight %}
                <p>Peso: ligero</p>

            {% elif pokemon.weight > 500 %}
                <p>Peso: pesado</p>

            {% else %}
                <p>Peso: normal</p>
            {% endif %}


## Fase 2 ✅

Pagina princpal con formulario ✅

Listado de Pokémon (/pokemons) ✅

Página de batalla (/battle) ✅


## Comando para crear las tablas necesarias para el funcionamiento de la base de datos pokemons.db

`flask.exe --app app.main crear_tablas`

Recordar que este comando se ejecutará a nivel de la carpeta donde se encuentra nuestro proyecto.
