# FastAPI MLOps Satellite Image Classification

Proyecto para la clasificación de imágenes satelitales usando FastAPI y MLOps.

## Estructura del Proyecto

```
fastapi-mlops/
├── app/                 # Código principal de la aplicación
├── db/                  # Migraciones y configuración de base de datos
├── scripts/             # Scripts de utilidad
└── tests/              # Pruebas unitarias e integración
```

## Requisitos

- Python 3.9+
- Docker
- Poetry (gestor de dependencias)

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   poetry install
   ```
3. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   ```

## Uso

```bash
# Iniciar el servidor de desarrollo
poetry run uvicorn app.main:app --reload

# Iniciar con Docker
docker-compose up --build
```

## Endpoints

- `/api/v1/classify` - Clasificación de imágenes
- `/api/v1/models` - Gestión de modelos
- `/api/v1/health` - Estado del servicio
