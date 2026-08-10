# Guía de despliegue del laboratorio

*Última actualización: 2026-08-06*

## 1. Capas

| Capa | Qué despliega | Dónde |
|------|---------------|-------|
| Física / inferencia | Host + GPU, Ollama/LocalAI/vLLM | **Proyecto-HW** (repo propio) — [blog HW](https://agentef0ns1.github.io/blog-hw-ias/) |
| Lógica Caso 1 | Motores, MCP, A2A, surface agents | `Caso-1-Arquitecturas-Agenticas/` + `MASTER/Tools/{Ollama-hacking-tool,MCP-labs,PoC-A2A,Agent-lab}` |
| Lógica Caso 2 | Retos Gandalf, Promptfoo, attacker | `Caso-2-Ataques-LLMs/` |
| Lógica Caso 3 | Open-webui, MVP memoria, Kali, Burp cert | `Caso-3-Pentesting-Agentico/` + `MASTER/Tools/{MVP-memory-context,MVP-burp-certification}` |

## 2. Requisitos previos

- Linux con Docker 24+ (labs containerizados)
- Python 3.10+
- 16 GB RAM mínimo recomendado; GPU opcional (mejora §6.1.1 / §6.3)
- Red aislada del entorno de producción

## 3. Orden recomendado

1. **Inferencia** — seguir [Proyecto HW IA Local](https://agentef0ns1.github.io/blog-hw-ias/) o instalar solo Ollama/LocalAI vía `Caso-1/.../6.1.1-Motores-LLM-locales/scripts/`.
2. **§6.1.1** — verificar API del motor; opcionalmente `Ollama-hacking-tool` contra el target local.
3. **§6.1.2** — `MCP-labs`: servidor → Inspector → agente → hacking-tools.
4. **§6.1.3** — `PoC-A2A` (invoker + listener).
5. **§6.1.4** — `Agent-lab` CLI + CTF Docker Codex.
6. **§6.2** — levantar un Reto de `Inferencia-Gandalf/`; eval con Promptfoo.
7. **§6.3** — MVP-memory-context / Open-webui; luego MCP-Kali o MVP-burp-certification.

## 4. Verificación rápida

```bash
# Motor (ejemplo Ollama)
curl -s http://127.0.0.1:11434/api/tags | head

# MCP Inspector (desde MCP-labs)
cd MASTER/Tools/MCP-labs/mcp-server && ./scripts/run-inspector.sh

# Surface Auditor
cd MASTER/Tools/Agent-lab && python3 scripts/agent-audit-cli.py
```

Detalle por tool: [`../../tools/`](../../tools/).

## 5. Seguridad del lab

- Binding a localhost salvo necesidad documentada.
- Datos sintéticos; alcance ético en informes.
- No apuntar tools ofensivas a sistemas de terceros sin autorización.

[← Lab](../README.md)
