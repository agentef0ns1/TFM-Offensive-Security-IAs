# Agent-lab

Laboratorio y CLI **Agent Hacking Tools — Surface Auditor** para inventariar permisos, skills, `execpolicy` y procesos de **OpenAI Codex CLI**, con CTF Docker aislado.

| Campo | Valor |
|-------|-------|
| **Caso TFM** | 6.1.4 — Permisos, skills y tools |
| **Repo** | [github.com/agentef0ns1/agents-hacking-tool](https://github.com/agentef0ns1/agents-hacking-tool) |
| **Árbol local** | `MASTER/Tools/Agent-lab` |
| **Árbol Caso** | `Caso-1-Arquitecturas-Agenticas/6.1.4-Permisos-Skills-Tools/` |

## Capacidades

- Auditoría de `$HOME/.codex` y workspaces `.codex`
- Análisis de `approval_policy`, `sandbox_mode`, skills y `execpolicy`
- Escaneo de procesos Codex en `/proc`
- Demostración de escalada (PoC con backup) si config/skills son escribibles
- Exportación de informes JSON / texto

```bash
cd MASTER/Tools/Agent-lab
python3 scripts/agent-audit-cli.py
```

Demo: [YouTube](https://youtu.be/k7eNc1mPccc) · CTF: directorio `codex/` (Docker)

[← Tools](../README.md)
