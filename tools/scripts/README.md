# Scripts — índice de utilidades del TFM

Los scripts operativos viven junto a cada lab/tool. Este directorio del repo web actúa como **índice**; el generador de diagramas permanece en [`../../scripts/`](../../scripts/).

## Por dominio

### Motores LLM (§6.1.1)

`Caso-1-Arquitecturas-Agenticas/6.1.1-Motores-LLM-locales/scripts/`

| Script | Función |
|--------|---------|
| `install-ollama-ubuntu.sh` | Instalación Ollama |
| `install-localai-ubuntu.sh` | Instalación LocalAI |
| `install-vllm-ubuntu.sh` | Instalación vLLM |
| `install-textgen-webui-ubuntu.sh` | Instalación Text-Gen WebUI |
| `install-all-llm-motors.sh` | Orquestación multi-motor |
| `configure-ollama-intel-gpu.sh` / `diagnose-ollama.sh` | GPU / diagnóstico |
| `fix-ollama-*.sh` / `import-ollama-from-gguf.sh` | Operación diaria |

### MCP (§6.1.2)

`MASTER/Tools/MCP-labs/mcp-server/scripts/` — Inspector stdio/SSE/HTTP, arranque servidor.

### A2A (§6.1.3)

`MASTER/Tools/PoC-A2A/` — invoker, listeners, `lab_dos_spoof.py`.

### Permisos / skills (§6.1.4)

`MASTER/Tools/Agent-lab/scripts/agent-audit-cli.py` — Surface Auditor.

### Ataques LLM (§6.2)

Labs `Inferencia-Gandalf/Reto*` y `Guardrails-Jailbreaks/promptfoo/scripts/` (`run-eval.sh`, `run-redteam.sh`).

### Pentesting agéntico (§6.3)

| Origen | Scripts |
|--------|---------|
| `MVP-memory-context/scripts/` | install, inspector, auditoría |
| `MVP-burp-certification/scripts/` | orchestrator, supervisor |
| `MCP-Kali/scripts/` | lab Kali / LFI |
| `Open-webui/scripts/` | entorno asistente |

### Repo web

| Script | Función |
|--------|---------|
| [`../../scripts/generate_architecture_diagrams.py`](../../scripts/generate_architecture_diagrams.py) | Diagramas §6.1 |

[← Tools](../README.md)
