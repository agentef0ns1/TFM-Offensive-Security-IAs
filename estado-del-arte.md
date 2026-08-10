# 3. Estado del arte

## Índice {#indice}

  - [Paisaje de modelos (agosto 2026)](#paisaje-de-modelos-agosto-2026)
  - [Marcos normativos](#marcos-normativos)
  - [Líneas abiertas de investigación](#lineas-abiertas-de-investigacion)

---
En el curso del máster **2025–2026**, el panorama de modelos se divide de forma operativa en **open-weight** (pesos descargables) frente a **frontier / API de pago por tokens**. Cada compañía relevante publica familias y versiones; algunas mantienen ambas modalidades.

### Paisaje de modelos (agosto 2026)

El siguiente diagrama resume la visión global utilizada en la memoria: por compañía, familia de LLMs y versiones más conocidas.

![LLM Ecosystem Landscape — agosto 2026]({{ '/assets/images/docx/image1.png' | relative_url }})
<p class="figcap">Figura — Ecosistema LLM (open-weight vs. API de pago), agosto 2026. Fuente: memoria TFM v1.0.</p>

Detalle por modalidad (mapas de genealogía generados para el estado del arte):

![Open-weight LLMs — Company → Family → Models]({{ '/assets/images/estado-del-arte/map1_open_a3.png' | relative_url }})
<p class="figcap">Figura — Open-weight: compañía → familia → modelos (A3). Pesos descargables; las licencias no siempre son OSI open source.</p>

![Paid API / per-token LLMs — Company → Family → Models]({{ '/assets/images/estado-del-arte/map2_api_a3.png' | relative_url }})
<p class="figcap">Figura — API de pago / por token: compañía → familia → modelos (A3). Inferencia alojada por el proveedor.</p>

Vista combinada compacta (A4):

![Mapa combinado open-weight + API]({{ '/assets/images/estado-del-arte/map_combined_a4.png' | relative_url }})
<p class="figcap">Figura — Vista combinada A4: open-weight (arriba) y API de pago (abajo), nivel compañía → familia.</p>

La evolución es rápida: entre el desarrollo del TFM y su exposición pública el ecosistema habrá cambiado. Cuatro pilares resumen la tendencia:

| Pilar | Tendencia | Implicación ofensiva |
|-------|-----------|----------------------|
| **Modelos** | Más autonomía, razonamiento y capacidad ofensiva/defensiva (GPT-5.x, Qwen 3.2, Mythos…) | Mayor potencia del atacante y del defensor |
| **Arquitectura** | Del LLM aislado al **agente** (tool calling, memoria, orquestación multipaso) | Superficie de ataque multiplicada |
| **Protocolos** | **MCP** y **A2A** como ejes de integración | Tool poisoning, MitM, spoofing inter-agente |
| **Regulación** | Ley de IA UE (ago. 2026), Plan de Acción ciberseguridad e IA (jul. 2026) | Robustez, supervisión humana, obligaciones |

### Marcos normativos

| Estándar | Alcance |
|----------|---------|
| [**OWASP AISVS**](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/) | Requisitos verificables en el ciclo de vida de sistemas con IA |
| [**OWASP Top 10 for LLM Applications 2025**](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Diez riesgos en aplicaciones con LLMs |
| [**OWASP Top 10 for Agentic Applications 2026**](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Riesgos ASI01–ASI10 de sistemas autónomos |
| **Taxonomía B³** | Clasificación por Behavior, Bypass & Breach (detalle en [Caso 2](./caso-2-ataques-llms.md)) |

### Líneas abiertas de investigación

| Línea | Pregunta |
|-------|----------|
| Protocolos agénticos | ¿Cómo explotar y remediar MCP/A2A en entorno local? |
| Motores locales | ¿Cuál es la postura de seguridad por defecto de Ollama/LocalAI/vLLM? |
| Ataques sobre LLM | ¿Qué técnicas evaden guardrails actuales? |
| Ataques sobre agentes | ¿Qué técnicas explotan el funcionamiento de agentes locales? |
| Pentesting agéntico | ¿Hasta qué punto un agente local sustituye al auditor humano? ¿Qué riesgos implica? |
<p class="nav-footer"><a href="{{ '/objetivos.html' | relative_url }}">← Objetivos</a> · <a href="{{ '/' | relative_url }}">Índice</a> · <a href="{{ '/planificacion.html' | relative_url }}">Planificación →</a></p>
