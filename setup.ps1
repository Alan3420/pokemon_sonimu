Write-Host "============================="
Write-Host " Inicializando entorno Python"
Write-Host "============================="

# 1. Crear entorno virtual
Write-Host "Creando entorno virtual .venv..."
python -m venv .venv

# 2. Activar el entorno virtual
Write-Host "Activando entorno virtual..."
. .\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "No se encontro requirements.txt. Instalando Flask..."
    pip install flask
}

# 4. Ver versiones instaladas
Write-Host "Paquetes instalados:"
pip freeze

# 5. Crea tabals
flask.exe --app app.main crear_tablas

# 5. Ejecutar la aplicación
Write-Host "Ejecutando la aplicación..."
python -m app.main

Write-Host "============================="
Write-Host "      Proceso completado"
Write-Host "============================="