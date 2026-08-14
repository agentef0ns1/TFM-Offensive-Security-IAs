# 4. Planificación

## Índice {#indice}

  - [4.1 Metodología](#41-metodologia)
  - [4.2 Fases del proyecto](#42-fases-del-proyecto)
    - [4.2.1 Fases transversales](#421-fases-transversales)
    - [4.2.2 Caso 1 — Arquitecturas agénticas](#422-caso-1-arquitecturas-agenticas)
    - [4.2.3 Caso 2 — Ataques sobre LLMs](#423-caso-2-ataques-sobre-llms)
    - [4.2.4 Caso 3 — Pentesting agéntico](#424-caso-3-pentesting-agentico)

---
### 4.1 Metodología

El TFM combina **Design Science Research** (DSR) adaptado a ingeniería de seguridad con una **metodología iterativa por sprints**. Cada sprint produce un entregable verificable (informe, PoC, parche o documentación web) y alimenta el siguiente ciclo con retroalimentación de los hallazgos ofensivos y defensivos.

**Ciclo de cada sprint:**

1.  **Planificación** — objetivos del sprint, subtareas y criterios de aceptación.

2.  **Estudio** — revisión de marco (OWASP ASI, MITRE ATLAS), arquitectura y vectores de ataque del sub-apartado.
3.  **Ejecución** — despliegue en laboratorio, pruebas ofensivas/defensivas y recopilación de evidencias.
4.  **Revisión** — análisis de resultados, remediación documentada y actualización de memoria + web Jekyll.
5. **Cierre** — retrospectiva y planificación del sprint siguiente.

**Principios operativos:**

- Entorno controlado y autorizado; sin pruebas sobre sistemas de terceros.
- Reproducibilidad: scripts, Docker Compose y documentación de despliegue en el repositorio.
- Sincronización diaria memoria ↔ web (`TFM-Offensive-Security-IAs/`).
- Cada subapartado del capítulo 6 sigue el par **estudio → ejecución** antes de darse por cerrado.

### 4.2 Fases del proyecto

#### 4.2.1 Fases transversales

| Fase   | Sprint(s) | Actividad                                      | Entregable parcial                                   | Estado     |
|--------|-----------|------------------------------------------------|------------------------------------------------------|------------|
| **F1** | S0        | Revisión bibliográfica y definición de alcance | Capítulos 1–3 de la memoria                          | Completado |
| **F2** | S1        | Diseño del laboratorio                         | Arquitectura (apartado 5) y lista de componentes             | Completado |
| **F3** | S1–S2     | Implementación del lab y herramientas          | Repo GitHub: `tools/`, `lab/`, scripts de despliegue | Completado |
| **F8** | S12       | Redacción final y defensa                      | Memoria completa + web Jekyll                        | En Curso   |

#### 4.2.2 Caso 1 — Arquitecturas agénticas 

| Fase | Tipo | Subtarea | Actividades |
| --- | --- | --- | --- |
| F4.1 | Estudio + Ejecución | 6.1.2 Motores LLM | Comparativa Ollama, LocalAI, Text-Gen, vLLM; APIs, binding y postura de seguridad por defecto / Instalación, carga de modelo, prueba API, análisis de red y seguridad |
| F4.2 | Estudio + Ejecución | 6.1.1 MCP | Marco OWASP ASI02/ASI04; arquitectura agente–LLM–servidor MCP; superficie de ataque (tool poisoning, RCE STDIO) / Despliegue `mcp-server` + `mcp-agent`; pruebas de integración y vectores de ataque en lab |
| F4.3 | Estudio + Ejecución | 6.1.3 A2A | Protocolo A2A; ASI07; Agent Cards, TLS y delegación entre agentes / PoC comunicación entre dos agentes locales; vectores de suplantación |
| F4.4 | Estudio + Ejecución | 6.1.4 Permisos | Modelo de permisos, skills y tools; ASI01/ASI02/ASI05 / CTF infraestructura agéntica: reconocimiento, abuso de tools, RCE autorizado |


#### 4.2.3 Caso 2 — Ataques sobre LLMs 

| Fase | Tipo | Subtarea | Actividades |
| --- | --- | --- | --- |
| F5.1 | Estudio + Ejecución | 6.2.1 Taxonomia B³ | OWASP LLM01; inyección directa e indirecta; MITRE AML.T0051 / E integración con los conceptos de (Behavior, Bypass & Breach) |
| F5.2 | Estudio + Ejecución | 6.2.2 Definición de retos | Busqueda definición desarrollo y definición de retos del TFM |
| F5.3 | Estudio + Ejecución | 6.2.3 Seguridad en el diseño | Análisis de las cpas de seguridad implementadas en los retos a nievl modelos |
| F5.4 | Estudio + Ejecución | 6.2.3 Ejecución y solución manual | Ejecución de retos en entorno local y solución nivel por nivel |
| F5.5 | Estudio + Ejecución | 6.2.3 Ejecución y solución automatizada promptfoo | Pruebas de evasión; medición de bloqueo y falsos positivos, de forma automatizada mediante el uso de promptfoo |


#### 4.2.4 Caso 3 — Pentesting agéntico 

| Fase     | Tipo                | Subtarea                   | Actividades                                                              |
|----------|---------------------|----------------------------|--------------------------------------------------------------------------|
| **F6.1** | Estudio + Ejecución | 6.3.1 IA asistente         | OpenWebUI y MVP análisis de código                                       |
| **F6.2** | Estudio + Ejecución | 6.3.2 Auditorías autónomas | Estudios y desarrollo de pruebas aautónomas Challenge BSCP 24x7 Local-AI |
<p class="nav-footer"><a href="{{ '/estado-del-arte.html' | relative_url }}">← Estado del arte</a> · <a href="{{ '/' | relative_url }}">Índice</a> · <a href="{{ '/montaje-lab.html' | relative_url }}">Montaje lab →</a></p>


