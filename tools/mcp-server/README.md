# Servidor MCP de pentesting

Servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) que expone herramientas ofensivas al agente de IA.

## Herramientas previstas

- Reconocimiento: nmap (discovery, port scan, NSE)
- Vulnerabilidades: nuclei, búsqueda CVE, searchsploit
- Assessment: pipelines de auditoría automatizada

## Estado

En desarrollo. La base de código se integrará desde el proyecto local `MCPs/linux-portable/mcp-hacking-tool`.

## Instalación (borrador)

```bash
cd tools/mcp-server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución (borrador)

```bash
./scripts/run-mcp-hacking-web.sh   # interfaz web opcional
# o modo stdio MCP para el agente
```

[← Tools](../README.md)
