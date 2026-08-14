# MVP-memory-context

Servidor **MCP** de memoria y control de ventana de contexto para **auditoría de código en local** (Ollama + Cline / Continue / Cursor). Indexado, chunking, plan de pasos y artefactos en `<repo>/.mvp-audit/`.

| Campo | Valor |
|-------|-------|
| **Caso TFM** | 6.3.1 — IA como asistente de auditorías |
| **Repo canónico** | [MVP-code-review-full-context-control](https://github.com/agentef0ns1/MVP-code-review-full-context-control) |
| **Árbol local** | `MASTER/Tools/MVP-memory-context` |
| **Árbol Caso** | `Caso-3-Pentesting-Agentico/6.3.1-IA-Asistente-Auditorias/MVP-analisis-codigo/` |

## Ideas clave

| Capacidad | Descripción |
|-----------|-------------|
| Indexado / chunking | El agente lee trozos vía tools MCP, no el repo entero |
| Plan acotado | `memory_audit_next_step` → unidad → `memory_audit_complete_step` |
| Persistencia | SQLite local + informes en disco (`RESUMEN-EJECUTIVO.md`) |

```bash
git clone https://github.com/agentef0ns1/MVP-code-review-full-context-control.git
cd MVP-code-review-full-context-control
chmod +x scripts/*.sh
./scripts/install.sh
# Depurar tools: MCP Inspector (ver README del proyecto)
```

[← Tools](../README.md)
