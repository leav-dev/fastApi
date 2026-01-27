# Proyecto FastAPI

Este proyecto es una aplicación web desarrollada con FastAPI que puede ejecutarse tanto con Docker como sin Docker.

## 📋 Requisitos

### Para ejecución sin Docker:
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Para ejecución con Docker:
- Docker
- Docker Compose

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución sin Docker

#### 1. Clonar el repositorio
```bash
git clone https://github.com/leav-dev/fastApi
cd fastApi
```

#### 2. Crear entorno virtual
```bash
python3 -m venv .venv
```

#### 3. Activar entorno virtual
**En Linux/macOS:**
```bash
source .venv/bin/activate
```

**En Windows:**
```bash
.venv\Scripts\activate
```

#### 4. Instalar dependencias
```bash
pip install -r complements/requirements.txt
```

#### 5. Ejecutar el servidor
```bash
cd main
uvicorn core.main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en: `http://localhost:8000`

#### 6. Desactivar entorno virtual (cuando termines)
```bash
deactivate
```

### Opción 2: Ejecución con Docker

#### 1. Clonar el repositorio
```bash
git clone https://github.com/leav-dev/fastApi
cd fastApi
```

#### 2. Construir y ejecutar con Docker Compose
```bash
docker-compose up --build
```

El servidor estará disponible en: `http://localhost:3000`

#### 3. Ejecutar en segundo plano (opcional)
```bash
docker-compose up -d --build
```

#### 4. Ver logs del contenedor
```bash
docker-compose logs -f proyecto_fast_api
```

#### 5. Detener el contenedor
```bash
docker-compose down
```

## 📁 Estructura del Proyecto

```
.
├── main/
│   └── core/
│       └── main.py          # Aplicación principal FastAPI
├── complements/
│   └── requirements.txt     # Dependencias del proyecto
├── Dockerfile              # Configuración Docker
├── Docker-compose.yml      # Configuración Docker Compose
└── README.md               # Este archivo
```

## 🔧 Configuración

### Puertos
- **Sin Docker**: El servidor se ejecuta en el puerto `8000`
- **Con Docker**: El servidor se mapea al puerto `3000` del host (puerto interno `1998`)

### Variables de entorno
Actualmente no se requieren variables de entorno adicionales.

## 📚 API Endpoints

### GET /
- **Descripción**: Endpoint de prueba que retorna un saludo
- **Respuesta**: 
```json
{
  "greeting": "Hello world"
}
```

## 🛠️ Desarrollo

### Agregar nuevas dependencias
1. Agregar la dependencia a `complements/requirements.txt`
2. Si usas Docker, reconstruir la imagen:
   ```bash
   docker-compose up --build
   ```
3. Si no usas Docker, instalar la nueva dependencia:
   ```bash
   pip install -r complements/requirements.txt
   ```

### Hot Reload
- **Sin Docker**: El servidor se reinicia automáticamente con `--reload`
- **Con Docker**: Los cambios en el código se reflejan automáticamente gracias al volumen montado

## 🐛 Solución de Problemas

### Error de permisos en Docker
Si encuentras errores de permisos, asegúrate de que Docker tenga los permisos necesarios para acceder a los archivos del proyecto.

### Puerto ocupado
Si el puerto está ocupado, puedes cambiar el puerto en:
- **Sin Docker**: Modificar el parámetro `--port` en el comando uvicorn
- **Con Docker**: Modificar el mapeo de puertos en `Docker-compose.yml`

### Dependencias faltantes
Asegúrate de que todas las dependencias estén instaladas ejecutando:
```bash
pip install -r complements/requirements.txt
```

## 📝 Notas Adicionales

- El proyecto utiliza FastAPI con Uvicorn como servidor ASGI
- La configuración de Docker incluye un entorno virtual dentro del contenedor
- Los archivos de código están montados como volumen para facilitar el desarrollo
