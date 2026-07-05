# 3.2 Caso 2 — Ataques sobre LLMs

**Estado:** Pendiente

## Objetivo

Demostrar y documentar vectores de ataque sobre modelos de lenguaje y aplicaciones que los integran: **prompt injection**, **inferencia de información** y evasión de **guardrails** mediante **jailbreaks**.

## Escenario

CTF de inyección de prompts con fuentes de datos externas comprometidas; laboratorio con capas de moderación activas; reto [Lakera Gandalf](https://gandalf.lakera.ai/) como referencia externa controlada.

---

## 3.2.1 Prompt injection directa e indirecta

**Objetivo:** Ejecutar y documentar ataques de *Direct Prompt Injection* e *Indirect Prompt Injection* mediante fuentes de datos externas comprometidas (CTF Clase 3 del Módulo 10).

**Metodología:**

1. Inyección directa contra el agente/LLM (instrucciones adversarias en el prompt del usuario).
2. Inyección indirecta vía documentos, URLs o metadatos envenenados en el contexto.
3. Evaluación de controles defensivos (sandboxing, validación de entrada, hardening de prompts).

**Referencias:** [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — LLM01 Prompt Injection.

**Estado:** Pendiente

---

## 3.2.2 Inferencia de información (Lakera Gandalf)

**Objetivo:** Demostrar técnicas de extracción e inferencia de información confidencial oculta en el contexto o *system prompt*, usando el reto [Lakera Gandalf](https://gandalf.lakera.ai/) como laboratorio de referencia.

**Metodología:**

1. Enumeración de técnicas de extracción (role-play, traducción, codificación, multi-turno).
2. Replicación de vectores relevantes en LLM local del laboratorio.
3. Documentación de tasa de éxito y mitigaciones.

**Referencias:** OWASP LLM Top 10 — LLM07 System Prompt Leakage.

**Estado:** Pendiente

---

## 3.2.3 Guardrails y Jailbreaks

**Objetivo:** Evaluar la eficacia de **guardrails** (moderación de entrada/salida, filtros semánticos, Llama Guard, políticas de sistema) frente a técnicas de **jailbreak** (role-play, DAN, ofuscación, multi-turno, idioma alternativo, etc.).

**Metodología:**

1. Inventariar guardrails activos en el lab (pre/post-procesado, reglas, modelos auxiliares).
2. Ejecutar jailbreaks conocidos y variantes adaptadas al TFM.
3. Medir tasa de bloqueo, falsos positivos y respuestas parcialmente restringidas.
4. Documentar técnicas exitosas y recomendaciones de refuerzo (defensa en profundidad).

**Referencias:** OWASP LLM Top 10 — LLM01, LLM07; taxonomías de jailbreak (OWASP, MITRE ATLAS).

**Estado:** Pendiente

---

## Entregables

- Catálogo de técnicas en [`informes/caso-2-ataques-llms/`](../informes/)
- Matriz guardrail vs. jailbreak (tasa de éxito/bloqueo)
- Recomendaciones de mitigación

[← Caso 1](./caso-1-arquitecturas-agenticas.md) · [Índice](./index.md) · [Caso 3 →](./caso-3-pentesting-agentico.md)
