# 2.1 Montaje del laboratorio (escenario)

## Objetivo

Entorno **reproducible, aislado y de bajo coste** para ejecutar los casos de estudio: pentesting agéntico, explotación de superficie de ataque, ataques sobre LLMs y auditorías asistidas por IA.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    LABORATORIO TFM                          │
├─────────────────────────────────────────────────────────────┤
│  Agente local ◄──► LLM local (Ollama/GGUF) ◄──► MCP/Tools   │
│       │                                              │      │
│       ▼                                              ▼      │
│  CTF targets (Docker)                    Red aislada (lab)  │
└─────────────────────────────────────────────────────────────┘
```

## Componentes

| Componente | Ubicación en el repo |
|------------|---------------------|
| Servidor MCP de pentesting | [`tools/mcp-server/`](../tools/mcp-server/) |
| Agente autónomo | [`tools/agent/`](../tools/agent/) |
| Escenarios CTF | [`lab/ctf/`](../lab/ctf/) |
| Guía de despliegue | [`lab/docs/`](../lab/docs/) |

## Despliegue

```bash
git clone https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git
cd TFM-Offensive-Security-IAs/lab
# Instrucciones detalladas en lab/docs/
docker compose up -d
```

---

*Instrucciones de despliegue en desarrollo.*

[← Planificación](./planificacion.md) · [Índice](./index.md) · [Caso 1 →](./caso-1-pentesting-agentico.md)
