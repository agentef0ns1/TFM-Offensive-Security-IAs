# 3.3 Caso 3 — Ataques sobre LLMs

**Estado:** Pendiente

## Objetivo

Demostrar vectores de ataque sobre modelos de lenguaje: prompt injection directa e indirecta, inferencia de información y jailbreaking.

## Escenario

CTF de inyección de prompts con fuentes de datos externas comprometidas.

## Sub-casos de uso

### 3.3.a Prompt injection directa e indirecta

**Objetivo:** Ejecutar y documentar ataques de *Direct Prompt Injection* e *Indirect Prompt Injection* mediante fuentes de datos externas comprometidas.

**Referencias:** [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — LLM01 Prompt Injection.

**Estado:** Pendiente

### 3.3.b Inferencia de información (Lakera Gandalf)

**Objetivo:** Demostrar técnicas de extracción e inferencia de información confidencial oculta en el contexto o system prompt, usando el reto [Lakera Gandalf](https://gandalf.lakera.ai/) como laboratorio de referencia.

**Estado:** Pendiente

---

## Metodología

1. Ataques de prompt injection directa contra el agente/LLM.
2. Ataques indirectos mediante documentos/fuentes envenenadas en el contexto.
3. Intentos de extracción de información del system prompt o datos de sesión (Gandalf).
4. Evaluación de controles defensivos (filtros, sandboxing, guardrails).

## Entregables

- Catálogo de técnicas probadas en [`informes/`](../informes/)
- Tasa de éxito y recomendaciones de mitigación

[← Caso 2](./caso-2-superficie-ataque.md) · [Índice](./index.md) · [Caso 4 →](./caso-4-auditorias-ia.md)
