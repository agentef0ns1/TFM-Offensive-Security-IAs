# Tools — Herramientas del TFM

Catálogo de **herramientas y laboratorios de código** desarrollados o integrados en el TFM.  
Cada entrada apunta al repositorio (o árbol de trabajo) canónico; este directorio documenta el mapeo con los casos §6.

> **Aviso:** uso exclusivo en entornos controlados con autorización explícita.

---

## Catálogo (repos canónicos)

| Tool | Repositorio / ruta | Caso TFM | Rol |
|------|--------------------|----------|-----|
| **Ollama-hacking-tool** | [ollama-hacking-tools](https://github.com/agentef0ns1/ollama-hacking-tools) · `MASTER/Tools/Ollama-hacking-tool` | [§6.1.1](../caso-1-arquitecturas-agenticas.md#611-motores-llm-locales) | Auditoría ofensiva de la API REST de Ollama (recon, CVE, inyección, payloads) |
| **MCP-labs** | [MCP-security-lab](https://github.com/agentef0ns1/MCP-security-lab) · `MASTER/Tools/MCP-labs` | [§6.1.2](../caso-1-arquitecturas-agenticas.md#612-arquitectura-agéntica-mcp) | Lab MCP: `mcp-server`, `mcp-agent`, `MCP-hacking-tools` (stdio/SSE/HTTP) |
| **PoC-A2A** | [A2A-security-lab](https://github.com/agentef0ns1/A2A-security-lab) · `MASTER/Tools/PoC-A2A` | [§6.1.3](../caso-1-arquitecturas-agenticas.md#613-arquitectura-agéntica-agent-to-agent-a2a) | PoC Agent-to-Agent + vectores DoS/spoof |
| **Agent-lab** | [agents-hacking-tool](https://github.com/agentef0ns1/agents-hacking-tool) · `MASTER/Tools/Agent-lab` | [§6.1.4](../caso-1-arquitecturas-agenticas.md#614-permisos-skills-y-tools) | Surface Auditor (Codex) + CTF Docker de superficie agéntica |
| **MVP-memory-context** | `MASTER/Tools/MVP-memory-context` | [§6.3.1](../caso-3-pentesting-agentico.md#631-ia-como-asistente-de-auditorías) | MCP de memoria/contexto para auditoría de código con LLM local |
| **MVP-burp-certification** | `MASTER/Tools/MVP-burp-certification` | [§6.3.2](../caso-3-pentesting-agentico.md#632-auditorías-autónomas) | Orquestación de certificación PortSwigger + Cline + MCP Burp |

Fichas locales (este repo):

| Directorio | Tool |
|------------|------|
| [`ollama-hacking-tool/`](ollama-hacking-tool/) | Ollama-hacking-tool |
| [`mcp-labs/`](mcp-labs/) | MCP-labs |
| [`poc-a2a/`](poc-a2a/) | PoC-A2A |
| [`agent-lab/`](agent-lab/) | Agent-lab |
| [`mvp-memory-context/`](mvp-memory-context/) | MVP-memory-context |
| [`mvp-burp-certification/`](mvp-burp-certification/) | MVP-burp-certification |
| [`scripts/`](scripts/) | Scripts de despliegue / utilidades (índice) |

---

## Mapa Tools ↔ Casos ↔ árbol de trabajo

```
MASTER/Tools/                         TFM/Caso-*
├── Ollama-hacking-tool  ──────────►  Caso-1/.../6.1.1-Motores-LLM-locales/Ollama/
├── MCP-labs             ──────────►  Caso-1/.../6.1.2-MCP/mcp-lab/
├── PoC-A2A              ──────────►  Caso-1/.../6.1.3-A2A/PoC-A2A/
├── Agent-lab            ──────────►  Caso-1/.../6.1.4-Permisos-Skills-Tools/
├── MVP-memory-context   ──────────►  Caso-3/.../6.3.1-*/MVP-analisis-codigo/
└── MVP-burp-certification ────────►  Caso-3/.../6.3.2-*/MCP-Burp/
```

**Fuera de alcance de este catálogo:** `Proyecto-HW` (servidor de inferencia — [blog-hw-ias](https://agentef0ns1.github.io/blog-hw-ias/), repo propio).

---

## Requisitos generales

- Python 3.10+ (3.11+ recomendado en A2A / MVP)
- Docker (Agent-lab CTF, MCP-Kali, labs Gandalf)
- Motor LLM local (Ollama / LocalAI / vLLM) según el caso
- Red aislada; sin pruebas contra terceros sin autorización

---

## Relacionado

- Laboratorio: [`../lab/`](../lab/)
- Informes: [`../informes/`](../informes/)
- Página web (índice Tools): [`../herramientas.md`](../herramientas.md)
