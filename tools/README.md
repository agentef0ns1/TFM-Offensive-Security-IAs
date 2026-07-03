# Tools — Herramientas del TFM

Código fuente asociado al Trabajo Fin de Máster.

## Estructura

| Directorio | Descripción | Estado |
|------------|-------------|--------|
| [`agent/`](agent/) | Agente autónomo personalizado con LLM local | En desarrollo |
| [`mcp-server/`](mcp-server/) | Servidor MCP de pentesting (nmap, nuclei, CVE, etc.) | En desarrollo |
| [`scripts/`](scripts/) | Utilidades de automatización y despliegue | En desarrollo |

## Requisitos generales

- Python 3.10+
- Docker (para servicios del laboratorio)
- Ollama o motor LLM local compatible (opcional según el caso)

## Uso

Cada subdirectorio incluye su propio `README.md` con instrucciones de instalación y ejecución.
