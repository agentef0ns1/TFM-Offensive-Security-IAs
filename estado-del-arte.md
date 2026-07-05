# 1.3 Estado del arte

## 3.1 Seguridad en sistemas de IA y LLMs

### Marco OWASP

| Estándar | Descripción |
|----------|-------------|
| [**OWASP AISVS**](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/) | *Artificial Intelligence Security Verification Standard* — requisitos de seguridad verificables para sistemas con IA en todo su ciclo de vida. [Repositorio GitHub](https://github.com/OWASP/AISVS) |
| [**OWASP Top 10 for LLM Applications**](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Diez riesgos críticos en aplicaciones con LLMs (LLM01 Prompt Injection, filtrado de datos, supply chain, etc.) |
| [**OWASP Top 10 for Agentic Applications**](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Riesgos en sistemas agénticos autónomos (ASI01–ASI10: goal hijack, tool misuse, inter-agent comms, rogue agents…) |

### Vectores y ciclo de vida

- Prompt injection (directa e indirecta), jailbreaking, extracción de datos.
- Riesgos en el ciclo de vida del modelo: entrenamiento, despliegue, inferencia, fine-tuning.

---

## Arquitectura de sistemas agénticos

- Patrones: ReAct, Plan & Execute, sistemas multiagente.
- Protocolos: function calling, Model Context Protocol (MCP).
- Superficie de ataque: permisos excesivos, RCE, escalada de privilegios.

## Frameworks de pentesting agéntico

- CAI (Cyber Attack Agent)
- Bug-TraceAI
- Agentes autónomos con LLMs locales

## IA como asistente en auditorías

- Herramientas open source y comerciales.
- Desarrollo asistido por IA para automatización ofensiva.
- Riesgos: alucinaciones, filtrado de datos sensibles.

---

*Sección en desarrollo. Se ampliará con la revisión bibliográfica completa.*

[← Objetivos](./objetivos.md) · [Índice](./index.md) · [Planificación →](./planificacion.md)
