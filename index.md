# Estudio de vulnerabilidades y protocolos de seguridad en sistemas de inteligencia artificial agénticos

**Trabajo Fin de Máster — MCAIS2**

**Autor:** Ildefonso González Sánchez

Documentación web del TFM del **Máster de Inteligencia Artificial orientado a Ciberseguridad (2.ª edición)**. Contiene la memoria segmentada para GitHub Pages, sincronizada con el documento Word de trabajo (~80 %).

El trabajo aborda la **ciberseguridad ofensiva** aplicada a sistemas de IA agénticos: vulnerabilidades, protocolos (MCP, A2A, tool calling), vectores de ataque y validación en laboratorio.

---

## Índice del TFM

### 1–2. Marco

* [**1. Introducción**](./introduccion.md) — contexto, motivación, alcance
* [**2. Objetivos**](./objetivos.md) — general, específicos, criterios de éxito

### 3–5. Fundamentos y laboratorio

* [**3. Estado del arte**](./estado-del-arte.md) — OWASP, MITRE ATLAS, MCP/A2A, pentesting agéntico
* [**4. Planificación**](./planificacion.md) — metodología DSR / sprints y fases
* [**5. Montaje del laboratorio**](./montaje-lab.md) — Proyecto-HW (externo) + capa lógica TFM

### 6. Casos de estudio

* [**6.1 Caso 1 — Arquitecturas agénticas**](./caso-1-arquitecturas-agenticas.md)
    * *6.1.1 Motores LLM (Ollama, LocalAI, vLLM) · rendimiento · superficie de ataque*
    * *6.1.2 MCP · 6.1.3 A2A · 6.1.4 Permisos, skills y tools*
* [**6.2 Caso 2 — Ataques sobre LLMs**](./caso-2-ataques-llms.md)
    * *Taxonomía B³ · Retos 0–10 · diseño · solución manual · Promptfoo*
* [**6.3 Caso 3 — Pentesting agéntico**](./caso-3-pentesting-agentico.md)
    * *Asistente (OpenWebUI, Cline, MVP) · auditorías autónomas (CAI, PortSwigger)*

### 7–8. Cierre

* [**7. Conclusiones**](./conclusiones.md)
* [**Bibliografía**](./bibliografia.md)
* [**Repositorio y vista previa local**](./repositorio.md)

### Tools, lab e informes

* [**Herramientas (catálogo)**](./herramientas.md)
* [Lab](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/lab) · [Tools](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/tools) · [Informes](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/informes)
* [Código en GitHub](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs)

---

*Fuente documental: `Entregable/TFM-Offensive-Security-IAs.docx` · última sync web: 2026-08-10*
