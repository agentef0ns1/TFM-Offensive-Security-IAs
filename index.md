# Estudio de vulnerabilidades y protocolos de seguridad en sistemas de inteligencia artificial agénticos

**Trabajo Fin de Máster — MCAIS2**

**Autor:** Ildefonso González Sánchez

Bienvenido a la documentación web del TFM del **Máster de Inteligencia Artificial orientado a Ciberseguridad (2.ª edición)**.

El trabajo aborda la **ciberseguridad ofensiva** aplicada a sistemas de inteligencia artificial agénticos: análisis de vulnerabilidades, protocolos de interacción (tool calling, MCP), vectores de ataque y validación práctica en laboratorio.

---

## Introducción

La adopción masiva de **sistemas agénticos autónomos** en entornos corporativos ha generado una nueva superficie de ataque que los planes de estudio tradicionales aún no cubren de forma dedicada. Este TFM complementa la formación defensiva del máster con un enfoque operativo y práctico.

---

## Índice del TFM

### 1. Marco teórico y planificación

* [**1.1 Introducción**](./introduccion.md)
* [**1.2 Objetivos**](./objetivos.md)
* [**1.3 Estado del arte**](./estado-del-arte.md)
* [**1.4 Planificación**](./planificacion.md)

---

### 2. Laboratorio

* [**2.1 Montaje del laboratorio (escenario)**](./montaje-lab.md)
    * *Arquitectura, componentes y despliegue del entorno de pruebas.*

---

### 3. Casos de estudio

Tres casos principales con sub-apartados documentados en cada página.

* [**3.1 Caso 1 — Arquitecturas agénticas**](./caso-1-arquitecturas-agenticas.md)
    * *3.1.1 Arquitectura agéntica: MCP*
    * *3.1.2 Motores LLM locales — PoC por motor:*
        * *3.1.2.1 Ollama*
        * *3.1.2.2 LocalAI*
        * *3.1.2.3 Text Generation WebUI (Text-Gen)*
        * *3.1.2.4 vLLM*
    * *3.1.3 Arquitectura agéntica: Agent-to-Agent (A2A)*
    * *3.1.4 Agentes locales: permisos, skills y tools*
* [**3.2 Caso 2 — Ataques sobre LLMs**](./caso-2-ataques-llms.md)
    * *3.2.1 Prompt injection directa e indirecta*
    * *3.2.2 Inferencia de información (Lakera Gandalf)*
    * *3.2.3 Guardrails y Jailbreaks*
* [**3.3 Caso 3 — Pentesting agéntico**](./caso-3-pentesting-agentico.md)
    * *3.3.1 IA como asistente de auditorías*
    * *3.3.2 Auditorías autónomas*

---

### 4. Cierre

* [**4.1 Conclusiones**](./conclusiones.md)
* [**4.2 Bibliografía**](./bibliografia.md)

---

## Repositorio

* [Código fuente y herramientas](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/tools)
* [Laboratorio](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/lab)

---
