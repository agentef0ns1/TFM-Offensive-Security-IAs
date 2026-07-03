# Laboratorio TFM

Entorno reproducible y aislado para los casos de estudio del TFM.

## Estructura

| Directorio | Contenido |
|------------|-----------|
| [`ctf/`](ctf/) | Escenarios CTF (infraestructura agéntica, LLMs, etc.) |
| [`docs/`](docs/) | Guías de despliegue y configuración de red |
| `docker-compose.yml` | Orquestación de servicios del lab |

## Inicio rápido

```bash
cd lab
docker compose up -d
# Ver lab/docs/despliegue.md
```

## Requisitos

- Docker y Docker Compose
- Red aislada o máquina virtual dedicada
- **No ejecutar contra sistemas sin autorización explícita**
