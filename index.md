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

Cuatro casos principales con sub-casos de uso documentados en cada página.

* [**3.1 Caso 1 — Pentesting agéntico**](./caso-1-pentesting-agentico.md)
    * *3.1.a Arquitectura agéntica: MCP*
    * *3.1.b Arquitectura agéntica: motor LLM local (Ollama / vLLM)*
    * *3.1.c Arquitectura agéntica: Agent-to-Agent (A2A)*
* [**3.2 Caso 2 — Superficie de ataque en infraestructura agéntica**](./caso-2-superficie-ataque.md)
    * *3.2.a Agente local: permisos, skills y tools*
* [**3.3 Caso 3 — Ataques sobre LLMs**](./caso-3-ataques-llms.md)
    * *3.3.a Prompt injection directa e indirecta*
    * *3.3.b Inferencia de información (Lakera Gandalf)*
* [**3.4 Caso 4 — IA como asistente en auditorías**](./caso-4-auditorias-ia.md) *(por confirmar)*

---

### 4. Cierre

* [**4.1 Conclusiones**](./conclusiones.md)
* [**4.2 Bibliografía**](./bibliografia.md)

---

## Repositorio

* [Código fuente y herramientas](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/tools)
* [Laboratorio](https://github.com/agentef0ns1/TFM-Offensive-Security-IAs/tree/main/lab)

---
