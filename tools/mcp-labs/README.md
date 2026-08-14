# MCP-labs

Laboratorio de **Model Context Protocol** aplicado a pentesting: servidor de tools ofensivas, agente LLM y herramientas de interceptación (stdio / SSE / HTTP).

| Campo | Valor |
|-------|-------|
| **Caso TFM** | 6.1.2 — Arquitectura agéntica MCP |
| **Repo** | [github.com/agentef0ns1/MCP-security-lab](https://github.com/agentef0ns1/MCP-security-lab) |
| **Árbol local** | `MASTER/Tools/MCP-labs` |
| **Árbol Caso** | `Caso-1-Arquitecturas-Agenticas/6.1.2-MCP/mcp-lab/` |

## Componentes

| Directorio | Rol |
|------------|-----|
| `mcp-server/` | FastMCP: nmap, nuclei, searchsploit, CVE… |
| `mcp-agent/` | Cliente MCP + Ollama (`/assess`) |
| `MCP-hacking-tools/` | Sniffing / MitM del tráfico MCP por transporte |

## Escenarios

1. Depuración con **MCP Inspector** (tools, prompts, resources).
2. Interceptación **stdio** (pipes agente↔servidor).
3. Interceptación **SSE** / **HTTP** (streamable MCP).

```bash
cd MASTER/Tools/MCP-labs/mcp-server
./scripts/run-inspector.sh              # stdio
./scripts/run-inspector-sse.sh          # SSE
./scripts/run-inspector-http.sh         # HTTP
```

[← Tools](../README.md)
