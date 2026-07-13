# 1.4 Planificación

Metodología iterativa por sprints. Sincronizado con la memoria del TFM (§4). *Última actualización: 2026-07-13*

---

## Metodología

El TFM combina **Design Science Research** (DSR) con **sprints iterativos**. Cada sprint produce un entregable verificable (informe, PoC, parche o documentación web).

**Ciclo de cada sprint:**

1. **Planificación** — objetivos del sprint, subtareas y criterios de aceptación.
2. **Estudio** — marco OWASP ASI / MITRE ATLAS, arquitectura y vectores del sub-apartado.
3. **Ejecución** — despliegue en laboratorio, pruebas ofensivas/defensivas y evidencias.
4. **Revisión** — resultados, remediación y actualización memoria + web.
5. **Cierre** — retrospectiva y planificación del sprint siguiente.

**Principios operativos:**

- Entorno controlado y autorizado.
- Reproducibilidad: scripts, Docker Compose y documentación en el repositorio.
- Sincronización diaria memoria ↔ web Jekyll.
- Cada sub-apartado de §6 sigue el par **estudio → ejecución**.

---

## Fases transversales

| Fase | Sprint(s) | Actividad | Entregable | Estado |
|------|-----------|-----------|------------|--------|
| **F1** | S0 | Revisión bibliográfica y alcance | Capítulos 1–3 | Completado |
| **F2** | S1 | Diseño del laboratorio | Arquitectura (§5) | Completado |
| **F3** | S1–S2 | Implementación lab y herramientas | `tools/`, `lab/` | En curso |
| **F7** | S11 | Remediación y bastionado | Contramedidas | Pendiente |
| **F8** | S12 | Memoria final y defensa | Memoria + web | Pendiente |

---

## Caso 1 — Arquitecturas agénticas

Workspace: `Caso-1-Arquitecturas-Agenticas/`

| Fase | Tipo | Subtarea | Directorio | Entregable | Sprint |
|------|------|----------|------------|------------|--------|
| F4.1 | Estudio | 6.1.1 MCP | `6.1.1-MCP/` | Informe arquitectura y amenazas | S2 |
| F4.1 | Ejecución | 6.1.1 MCP | `6.1.1-MCP/mcp-lab/` | PoC MCP + evidencias | S2 |
| F4.2 | Estudio | 6.1.2 Motores LLM | `6.1.2-Motores-LLM-locales/` | Matriz comparativa | S3 |
| F4.2 | Ejecución | 6.1.2.1 Ollama | `…/Ollama/` | Ficha técnica | S3 |
| F4.2 | Ejecución | 6.1.2.2 LocalAI | `…/LocalAI/` | Ficha técnica | S3 |
| F4.2 | Ejecución | 6.1.2.3 Text-Gen | `…/Text-Gen-WebUI/` | Ficha técnica | S3 |
| F4.2 | Ejecución | 6.1.2.4 vLLM | `…/vLLM/` | Ficha técnica | S3 |
| F4.3 | Estudio + Ejecución | 6.1.3 A2A | `6.1.3-A2A/` | PoC A2A + informe | S4 |
| F4.4 | Estudio + Ejecución | 6.1.4 Permisos | `6.1.4-Permisos-Skills-Tools/` | Cadena de ataque CTF | S5 |

---

## Caso 2 — Ataques sobre LLMs

Workspace: `Caso-2-Ataques-LLMs/`

| Fase | Tipo | Subtarea | Directorio | Entregable | Sprint |
|------|------|----------|------------|------------|--------|
| F5.1 | Estudio + Ejecución | 6.2.1 Prompt injection | `6.2.1-Prompt-Injection/` | Catálogo + informe CTF | S6 |
| F5.2 | Estudio + Ejecución | 6.2.2 Inferencia Gandalf | `6.2.2-Inferencia-Gandalf/` | Informe [Lakera Gandalf](https://gandalf.lakera.ai/) | S7 |
| F5.3 | Estudio + Ejecución | 6.2.3 Guardrails/Jailbreaks | `6.2.3-Guardrails-Jailbreaks/` | Matriz guardrail vs. jailbreak | S8 |

---

## Caso 3 — Pentesting agéntico

Workspace: `Caso-3-Pentesting-Agentico/`

| Fase | Tipo | Subtarea | Directorio | Entregable | Sprint |
|------|------|----------|------------|------------|--------|
| F6.1 | Estudio + Ejecución | 6.3.1 IA asistente | `6.3.1-IA-Asistente-Auditorias/` | Logs + informe copiloto | S9 |
| F6.2 | Estudio + Ejecución | 6.3.2 Auditorías autónomas | `6.3.2-Auditorias-Autonomas/` | Informe autónomo + métricas | S10 |

---

## Mapa de sprints

| Sprint | Fases | Foco principal |
|--------|-------|----------------|
| **S0** | F1 | Estado del arte, objetivos, alcance |
| **S1** | F2, F3 | Laboratorio base |
| **S2** | F4.1 | Caso 1 — MCP |
| **S3** | F4.2 | Caso 1 — Motores LLM |
| **S4** | F4.3 | Caso 1 — A2A |
| **S5** | F4.4 | Caso 1 — Permisos, skills y tools |
| **S6** | F5.1 | Caso 2 — Prompt injection |
| **S7** | F5.2 | Caso 2 — Inferencia (Gandalf) |
| **S8** | F5.3 | Caso 2 — Guardrails y jailbreaks |
| **S9** | F6.1 | Caso 3 — IA asistente |
| **S10** | F6.2 | Caso 3 — Auditorías autónomas |
| **S11** | F7 | Remediación y bastionado |
| **S12** | F8 | Memoria final y defensa |

---

## Planificación temporal

| Hito | Fecha | Estado |
|------|-------|--------|
| Título y alcance | 2026-07-03 | Completado |
| Estado del arte | 2026-07-13 | Completado |
| Planificación por sprints | 2026-07-13 | Completado |
| Laboratorio operativo (S1) | 2026-07-13 | Completado (host `Proyecto-HW/`) |
| Caso 1 (S2–S5) | — | Pendiente |
| Caso 2 (S6–S8) | — | Pendiente |
| Caso 3 (S9–S10) | — | Pendiente |
| Remediación (S11) | — | Pendiente |
| Memoria final (S12) | — | Pendiente |
| Defensa del TFM | — | Pendiente |

---

## Recursos necesarios

### Software (imprescindible)

- Host Linux (físico o VM), Docker, Docker Compose.
- Ollama (+ opcional LocalAI, Text-Gen WebUI, vLLM).
- Agente + servidor MCP ([`tools/agent/`](../tools/agent/), [`tools/mcp-server/`](../tools/mcp-server/)).
- nmap, nuclei, searchsploit.
- Repositorio GitHub y GitHub Pages.

### Hardware de referencia (`Proyecto-HW/`)

Laboratorio de alto rendimiento documentado por el autor. **No es estrictamente necesario** para las pruebas del TFM (reproducibles en hardware genérico o VM):

| Componente | Modelo |
|------------|--------|
| Mini PC | Minisforum AtomMan X7 Ti |
| Dock eGPU | Minisforum DEG1 |
| GPU | AMD Radeon RX 7900 XTX (24 GB VRAM) |
| Fuente | Corsair SF850 SFX 850W |
| Conectividad | Cable OCuLink (SFF-8611) |
| Panel de estado | `screen.py` + `atomman.service` (opcional) |

[← Estado del arte](./estado-del-arte.md) · [Índice](./index.md) · [Montaje lab →](./montaje-lab.md)
