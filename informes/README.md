# Informes técnicos

Informes ejecutivos/técnicos de los casos de estudio.  
*Actualizado: 2026-08-06 — estructura alineada con directorios de Casos y Tools.*

## Estructura

```
informes/
├── caso-1-arquitecturas-agenticas/
│   ├── motores-llm/          # Ollama, LocalAI, vLLM (+ benchmark / monitor)
│   ├── mcp/                  # Arquitectura, Inspector, vectores stdio/SSE/HTTP
│   ├── a2a/                  # PoC A2A + lab ataque
│   └── permisos-skills/      # Surface Auditor, CTF Codex
├── caso-2-ataques-llms/
│   ├── taxonomia/            # B³, OWASP LLM, MITRE ATLAS
│   ├── retos/                # Definición + solución manual Reto1–10 / Suelta-la-panoja
│   └── automatizacion/       # Promptfoo results, agente atacante
└── caso-3-pentesting-agentico/
    ├── asistente/            # Open-webui, MVP-memory-context / análisis código
    └── autonomas/            # MCP-Kali, MCP-Burp / certificación, CAI
```

## Fuentes de evidencia (ya existentes en el workspace)

| Informe previsto | Evidencias actuales |
|------------------|---------------------|
| 6.1.1 Ollama | `Tools/Ollama-hacking-tool/docs/`, PoCs en `Caso-1/.../Ollama/` |
| 6.1.2 MCP | Capturas `MCP-labs/*.png`, `code_mcp-agent.md` |
| 6.1.3 A2A | `PoC-A2A/README_ATAQUE.md`, `capture_packets.pcapng` |
| 6.1.4 Surface | Informes exportados por Agent-lab CLI; `Agent-lab/*.png` |
| 6.2 Retos | `Caso-2/.../6.2.3 Solución manual/`, `promptfoo/results/` |
| 6.3.1 Memoria | `MVP-memory-context` diagrams + `.mvp-audit/` en repos auditados |
| 6.3.2 Burp cert | `MVP-burp-certification/docs/`, `MCP-Burp/Certification-global.md` |

Cada informe incluirá: alcance, metodología, hallazgos, evidencias y remediación.

**Estado:** estructura lista; consolidación de write-ups en curso desde labs operativos.

[← Índice](../index.md)
