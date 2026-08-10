# Laboratorio TFM

Entorno **reproducible y aislado** para los casos §6. El hardware de inferencia (`Proyecto-HW`) es un repositorio independiente; aquí se documenta la **capa lógica** (labs, CTFs, tools).

## Estructura en este repo

| Ruta | Contenido |
|------|-----------|
| [`ctf/`](ctf/) | Mapa de escenarios CTF / retos → árbol real de Casos y Tools |
| [`docs/despliegue.md`](docs/despliegue.md) | Guía de despliegue por capa |
| `docker-compose.yml` | Orquestación (placeholder; labs viven en sus repos) |

---

## Labs reales (fuente de verdad)

| Lab | Ubicación | Caso | Tool / repo |
|-----|-----------|------|-------------|
| Motores LLM + monitor | `Caso-1/.../6.1.1-Motores-LLM-locales/` | §6.1.1 | Ollama / LocalAI / vLLM + `inference-monitor`, `benchmark` |
| MCP security lab | `MASTER/Tools/MCP-labs` · `Caso-1/.../6.1.2-MCP/mcp-lab/` | §6.1.2 | [MCP-security-lab](https://github.com/agentef0ns1/MCP-security-lab) |
| A2A PoC | `MASTER/Tools/PoC-A2A` · `Caso-1/.../6.1.3-A2A/` | §6.1.3 | [A2A-security-lab](https://github.com/agentef0ns1/A2A-security-lab) |
| Surface / Codex CTF | `MASTER/Tools/Agent-lab` · `Caso-1/.../6.1.4-*/codex/` | §6.1.4 | [agents-hacking-tool](https://github.com/agentef0ns1/agents-hacking-tool) |
| Inferencia Gandalf (Reto1–10 + Suelta-la-panoja) | `Caso-2-Ataques-LLMs/Inferencia-Gandalf/` | §6.2.2–6.2.3 | Labs locales Streamlit / niveles |
| Promptfoo + attacker-agent | `Caso-2/.../Guardrails-Jailbreaks/` | §6.2.4 | Automatización ASR / redteam |
| Open-webui + MVP análisis | `Caso-3/.../6.3.1-IA-Asistente-Auditorias/` | §6.3.1 | `MVP-memory-context` |
| MCP-Kali · MCP-Burp · CAI | `Caso-3/.../6.3.2-Auditorias-Autonomas/` | §6.3.2 | `MVP-burp-certification`, MCP-Kali |

Catálogo Tools: [`../tools/`](../tools/) · página web: [`../herramientas.md`](../herramientas.md)

---

## Capas del escenario

```
┌─────────────────────────────────────────────────────────────┐
│  Proyecto-HW (repo propio) — servidor de inferencia         │
│  https://agentef0ns1.github.io/blog-hw-ias/                 │
└────────────────────────────┬────────────────────────────────┘
                             │ API LLM local
┌────────────────────────────▼────────────────────────────────┐
│  Labs lógicos (Casos 1–3 + MASTER/Tools/*)                  │
│  MCP · A2A · Agent surface · Gandalf · Burp cert · Kali     │
└─────────────────────────────────────────────────────────────┘
```

## Requisitos

- Docker / Docker Compose donde aplique
- Python 3.10+ y motor LLM local
- Red aislada; **no** ejecutar contra sistemas sin autorización

[← Índice](../index.md)
