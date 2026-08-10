# PoC-A2A

Prueba de concepto del protocolo **Agent-to-Agent (A2A)** con Ollama local: Invoker ↔ Weather-Tool-Agent, Agent Cards, JSON-RPC `message/send`, y laboratorio de vectores (DoS / spoof / listener falso).

| Campo | Valor |
|-------|-------|
| **Caso TFM** | §6.1.3 — Agent-to-Agent (A2A) |
| **Repo** | [github.com/agentef0ns1/A2A-security-lab](https://github.com/agentef0ns1/A2A-security-lab) |
| **Árbol local** | `MASTER/Tools/PoC-A2A` |
| **Árbol Caso** | `Caso-1-Arquitecturas-Agenticas/6.1.3-A2A/PoC-A2A/` |

## Scripts principales

| Script | Rol |
|--------|-----|
| `agent_invoker_improved.py` | Agente invocador (LLM + A2A) |
| `agent_listener_improved.py` | Weather agent legítimo |
| `agent_listener_fake.py` | Listener spoof |
| `lab_dos_spoof.py` / `dos_attack.py` | Lab DoS / spoof |
| `capture_packets.pcapng` | Evidencia de tráfico |

Ver también `README_ATAQUE.md` en el repo.

[← Tools](../README.md)
