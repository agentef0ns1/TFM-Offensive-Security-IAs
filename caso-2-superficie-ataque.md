# 3.2 Caso 2 — Superficie de ataque en infraestructura agéntica

**Estado:** Pendiente

## Objetivo

Explotar debilidades de diseño en un sistema agéntico: permisos excesivos, tool calling sin restricciones, escalada de privilegios y RCE.

## Escenario

CTF de infraestructura agéntica en [`lab/ctf/`](../lab/ctf/).

## Sub-casos de uso

### 3.2.a Agente local: permisos, skills y tools

**Objetivo:** Auditar y explotar la configuración del agente local: asignación de *skills*, permisos sobre el SO, políticas de tool calling y debilidades en la interacción agente–sistema operativo.

**Escenario:** CTF de infraestructura agéntica (Clase 2 del Módulo 10).

**Estado:** Pendiente

---

## Metodología

1. Reconocimiento de la arquitectura del agente (skills, permisos, memoria).
2. Identificación de vectores: inyección en prompts de sistema, abuso de herramientas, path traversal en ejecución.
3. Explotación hasta compromiso del host (RCE).
4. Documentación de la cadena de ataque.

## Entregables

- Write-up del CTF en [`informes/`](../informes/)
- Evidencias (capturas, logs) y diagrama de la cadena de explotación

[← Caso 1](./caso-1-pentesting-agentico.md) · [Índice](./index.md) · [Caso 3 →](./caso-3-ataques-llms.md)
