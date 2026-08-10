# Escenarios CTF / retos

Mapa actualizado (2026-08-06) de escenarios prácticos del TFM.  
Los contenedores y código viven en **Casos** y **Tools**, no en este stub.

| Escenario | Caso | Ubicación | Estado |
|-----------|------|-----------|--------|
| Surface Auditor + CTF Codex (Docker) | §6.1.4 | `MASTER/Tools/Agent-lab` · `Caso-1/.../6.1.4-Permisos-Skills-Tools/codex/` | Operativo |
| MCP interceptación (stdio/SSE/HTTP) | §6.1.2 | `MASTER/Tools/MCP-labs` | Operativo |
| A2A DoS / spoof | §6.1.3 | `MASTER/Tools/PoC-A2A` (`lab_dos_spoof.py`, listener fake) | Operativo |
| Ollama API sin auth | §6.1.1 | `MASTER/Tools/Ollama-hacking-tool` | Operativo |
| Inferencia / secret leakage (Gandalf-like) | §6.2.2–6.2.3 | `Caso-2/.../Inferencia-Gandalf/{Reto1…Reto10,Suelta-la-panoja}/` | Labs cerrados por CLI |
| Jailbreak / guardrails (Promptfoo) | §6.2.4.1 | `Caso-2/.../Guardrails-Jailbreaks/promptfoo/` | Eval automatizada |
| Agente atacante autónomo | §6.2.4.2 | `Caso-2/.../6.2.4.2 Agente autónomo atacante/` · hub `attacker-agent/` | En curso |
| LFI / Kali vía MCP | §6.3.2 | `Caso-3/.../MCP-Kali/` (`LFI_lab.md`) | En curso |
| PortSwigger certification (cola 20 min) | §6.3.2 | `MASTER/Tools/MVP-burp-certification` · `MCP-Burp/` | En curso |

Cada lab incluye su propio `README.md`, scripts y evidencias. Informes consolidados: [`../../informes/`](../../informes/).

[← Lab](../README.md)
