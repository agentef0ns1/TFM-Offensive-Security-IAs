# MVP-burp-certification

MCP de **management** para la certificación PortSwigger Web Security Academy.  
La explotación la realiza **Cline + modelo local** con **MCP Burp**; este MVP orquesta cola, timeout 20 min, acceso al lab y continuidad (anti-paradas).

| Campo | Valor |
|-------|-------|
| **Caso TFM** | §6.3.2 — Auditorías autónomas |
| **Árbol local** | `MASTER/Tools/MVP-burp-certification` |
| **Árbol Caso** | `Caso-3-Pentesting-Agentico/6.3.2-Auditorias-Autonomas/MCP-Burp/` |

## Procesos

| Proceso | Script | Rol |
|---------|--------|-----|
| **A** — Lab Orchestrator | `scripts/run-cert-orchestrator.sh` | Cola de labs + reloj 20 min + `access_lab.py` |
| **S** — Continuity Supervisor | `scripts/run-agent-supervisor.sh` | Vigilancia IDE o spawn Cline CLI |
| **C** — Cline | plugin IDE o CLI | Explotación vía Burp MCP |

Estados: `cert_init → queued → running → completed | timed_out`.

Relacionado en Caso 3: `MCP-Kali/`, `CAI/`, `Autonomous-agent/`.

[← Tools](../README.md)
