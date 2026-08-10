# 3. Estado del arte

Revisión bibliográfica y de fuentes abiertas sobre seguridad ofensiva en sistemas de IA agénticos. Sincronizado con la memoria del TFM (§3) y el documento Word (2026-08). *Última actualización: 2026-08-10*

---

## Panorama del documento (2025–2026)

En el año en el que se cursa el Master 2025-2026, el siguiente diagrama cumple con una visión global de los modelos de inteligencia artificial disponibles. La división de que se raliza es simple modelos open-source vs modelos frontier, de APIs y pago por uso.

Por cada compañía relevante, se muestra la familia de LLMs, seguido de sus últimas y mas conocidas versiones.

En algunos casos, existen compañias que tienen dos modalidades, liberan un versión pública opne-source de sus modelos pero mantieen una o varias familias de modelos frontier, que es de donde realemnte se obtiene rentabilidad económica el pago por uso de APIs mediante el consumo de tokens.

La evoluciones importantes de la IA durante el último año, son muchas y muy relevantes, las noticias se generar a un ritmo vertiginoso y con total seguridad desde que se desarrolle el TFM, hasta que sea expueto el ecosistema habra evolucionado, por lo que requiere de una atención constante.  
En lineas generales la tendencia de evolución se peude definir en cuatro pilares princiaples:

- Modelos: tienden a un mayor autonomia, razonamiento y nivel de coberseguridad capacida ofensiva y defensiva, han salido modelos relevantes como GTP-5.x, Qwen 3.2, Mythos...

- Arquitectura: A nivel arquitectura los modelos han dejado de ser simplemente un LLM, sino que se mueven, en dirección al agente con capacidades de ejecución mediante tool calling, memoria de contexto propia y orquestación multipaso, lo que multiplica la superficie de ataque respecto a un LLM aislado.

- Protocolos: Los protocolos de comunicación entre las IA agenticas hen evolucionado en dos direcciones principales, servidores con protocolo MCP (Model Context Protocol) y comunicación A2A (Agent to Agent).

- Regulación: Esta evolución incipiente, obliga a una mayor robustez en la supervisión humana, de la ciberseguridad, a nivel regulatorio remarcar la Ley de IA de la Union Euoropea en (Agosto de 2026) y el plan de acción de la Union Europea de cibersguridad e IA en (Julio de 2026).

---

## Líneas abiertas de investigación

| Línea                            | Pregunta de investigación                                                                                                                  |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Protocolos agénticos             | Tras estudiar e investigar los protocolo de comunicación agenticos ¿Cómo explotar y remediar MCP/A2A en entorno local?                     |
| Motores locales                  | Tras entender e investigar los Motores locales ¿Cuál es la postura de seguridad por defecto de Ollama/LocalAI/vLLM?                        |
| Ataques sobre LLM                | Tras investigar el funcionamiento de los LLMs en la actualidad ¿Qué técnicas evaden guardrails actuales?                                   |
| Ataques sobre sistemas agénticos | Tras invesigar y entender los agentes locales ¿ Que técnicas se pueden utilizar para explotar, el funcionmianto de agentes locales ?       |
| Pentesting agéntico              | ¿Hasta qué punto un agente local puede sustituir al auditor humano? ¿Que riesgos corremos al permitir que un agente realice una auditoría? |

---

# 1.3 Estado del arte

Revisión bibliográfica y de fuentes abiertas sobre seguridad ofensiva en sistemas de IA agénticos. Sincronizado con la memoria del TFM (§3).

---

## 3.0 Panorama general (2025–2026)

En 2026 convergen cuatro dimensiones que condicionan el estudio de vulnerabilidades en sistemas agénticos:

| Dimensión | Tendencia relevante | Implicación para la seguridad |
|-----------|---------------------|-------------------------------|
| **Modelos** | GPT-5.x, Gemini 3.5, Qwen 3.5, Mythos Preview (ciberseguridad) | Mayor autonomía y capacidad ofensiva/defensiva |
| **Arquitectura** | Modelos «agentic» con tool calling, memoria y orquestación | Superficie de ataque ampliada respecto al LLM aislado |
| **Protocolos** | MCP (Anthropic/Linux Foundation) y A2A (Google/Linux Foundation) | Inyección de comandos, *tool poisoning*, comunicación inter-agente |
| **Regulación** | Ley de IA de la UE (agosto 2026), Plan de Acción UE ciberseguridad e IA | Obligaciones de robustez, ciberseguridad y supervisión humana |

El lanzamiento restringido de **Mythos Preview** (Anthropic, abril 2026) subraya el **doble uso** de la IA agéntica y la necesidad de marcos de evaluación ofensiva controlada.

---

## 3.1 Seguridad en sistemas de IA y LLMs

> Además de OWASP/MITRE, este TFM emplea la **taxonomía B³** (Behavior, Bypass & Breach) para clasificar ataques sobre LLMs y sistemas agénticos (detalle en [Caso 2](./caso-2-ataques-llms.md)).


### Marco OWASP

| Estándar | Alcance | Relevancia TFM |
|----------|---------|----------------|
| [**OWASP AISVS**](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/) | Requisitos verificables en el ciclo de vida de sistemas con IA | Auditorías y contramedidas (§6) |
| [**OWASP Top 10 LLM 2025**](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Diez riesgos en aplicaciones con LLMs | Caso 2 (§6.2) |
| [**OWASP Top 10 Agentic 2026**](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Diez riesgos en sistemas autónomos (ASI01–ASI10) | Casos 1 y 3 (§6.1, §6.3) |

### OWASP Top 10 LLM 2025

**LLM01: Prompt Injection** permanece como riesgo n.º 1. El modelo procesa instrucciones y datos en el mismo canal, sin separación nativa entre «comando» y «dato».

- **Inyección directa**: manipulación del prompt de entrada.
- **Inyección indirecta**: instrucciones maliciosas en documentos, webs o RAG.
- **Jailbreaking**: anulación completa de salvaguardas.

| Código | Riesgo | Caso TFM |
|--------|--------|----------|
| LLM02 | Filtrado de información sensible | §6.2.2 (Lakera Gandalf) |
| LLM06 | Exceso de agencia | §6.1.4 |
| LLM07 | Fuga del *system prompt* | §6.2.2 |
| LLM08 | Riesgos en vectorización/RAG | §6.2.1 |

### OWASP Top 10 Agentic 2026 (ASI01–ASI10)

| ID | Riesgo | Ejemplo documentado |
|----|--------|---------------------|
| **ASI01** | *Agent Goal Hijack* | EchoLeak |
| **ASI02** | *Tool Misuse and Exploitation* | Amazon Q |
| **ASI03** | *Identity and Privilege Abuse* | — |
| **ASI04** | *Agentic Supply Chain* | GitHub MCP exploit |
| **ASI05** | *Unexpected Code Execution* | AutoGPT RCE |
| **ASI06** | *Memory and Context Poisoning* | Gemini Memory Attack |
| **ASI07** | *Insecure Inter-Agent Communication* | — |
| **ASI08** | *Cascading Failures* | — |
| **ASI09** | *Human-Agent Trust Exploitation* | — |
| **ASI10** | *Rogue Agents* | Replit meltdown |

### MITRE ATLAS

[**MITRE ATLAS**](https://atlas.mitre.org/) adapta ATT&CK al ecosistema IA/ML. La actualización 2026 incorpora técnicas orientadas a agentes:

- **AML.T0051** — *LLM Prompt Injection*
- **AML.T0053** — *AI Agent Tool Invocation*
- **AML.T0054** — *LLM Jailbreak*
- **AML.T0056** — *Extract LLM System Prompt*
- **AML.T0070** — *RAG Poisoning*
- **AML.T0086** — *Exfiltration via AI Agent Tool Invocation*

### Guardrails y jailbreaks

Contramedidas frente a LLM01/ASI01:

1. Controles deterministas (validación, delimitadores, privilegio mínimo).
2. Guardrails basados en modelo: Llama Guard, ShieldGemma, NeMo Guardrails.
3. Arquitectura dual-LLM (Simon Willison): LLM privilegiado + LLM en cuarentena.

El Caso 2 (§6.2.3) evalúa la tensión guardrails vs. jailbreaks (*role-play*, DAN, ofuscación, multi-turno, *Best-of-N*).

---

## 3.2 Arquitectura de sistemas agénticos

### Patrones y componentes

- **Patrones**: ReAct, Plan & Execute, reflexión, sistemas multiagente.
- **Componentes**: planificador, selector de herramientas, memoria, entorno de ejecución.
- **Interfaces**: function/tool calling, MCP, A2A, APIs de orquestación.

### Model Context Protocol (MCP)

**MCP** estandariza la conexión agente–herramienta (JSON-RPC). Vector crítico del Caso 1 (§6.1.1).

| Categoría | Descripción |
|-----------|-------------|
| **RCE por diseño en STDIO** | Comandos del sistema sin validación en parámetros de configuración (CVE-2026-30623) |
| **Inyección de comandos** | 82 % de servidores alcanzan APIs de archivos (Endor Labs) |
| ***Tool poisoning*** | Modificación de tools tras aprobación inicial (ASI04) |
| **Autenticación opcional** | >1.800 instancias públicas sin auth |
| **CSRF Streamable HTTP** | CVE-2026-33252 en Go SDK |

Mitigaciones: `shell=False`, *allowlists*, *gateway* MCP, *sandboxing*, re-autorización de cambios.

### Agent-to-Agent (A2A)

**A2A** (Google/Linux Foundation) define interoperabilidad agente–agente sin exponer memoria ni tools internas.

| Aspecto | MCP | A2A |
|---------|-----|-----|
| Relación | Agente → herramienta | Agente → agente |
| Transporte | STDIO, Streamable HTTP | JSON-RPC sobre HTTPS |
| Seguridad | Auth opcional | OAuth 2.0, OIDC, TLS, firma JWS de Agent Cards |

Riesgos alineados con **ASI07** y **ASI03**. Subcaso §6.1.3.

### Motores LLM locales

| Motor | Riesgo por defecto | Mitigación |
|-------|-------------------|------------|
| **Ollama** | Sin auth; `OLLAMA_HOST=0.0.0.0` expone API; CVE-2024-37032 | Reverse proxy, aislamiento |
| **LocalAI** | API keys opcionales | Claves obligatorias |
| **Text-Gen WebUI** | Gradio sin auth | Autenticación, binding local |
| **vLLM** | Sin TLS/auth nativo | Reverse proxy |

PoC en §6.1.2 (Ollama, LocalAI, Text-Gen, vLLM).

---

## 3.3 Frameworks de pentesting agéntico

### CAI (Cybersecurity AI)

Framework open source ([arXiv:2504.06017](https://arxiv.org/abs/2504.06017v2)):

- Agentes especializados + HITL.
- Integración Nmap y herramientas estándar.
- Resultados: hasta 3.600× más rápido en CTFs; top-500 Hack The Box.

### BugTraceAI

Pipeline autónomo de 6 fases: Discovery → Analysis → Consolidation → Exploitation (14 agentes) → Validation → Reporting.

### Posicionamiento del TFM

| Criterio | CAI | BugTraceAI | Laboratorio TFM |
|----------|-----|------------|-----------------|
| Enfoque | CTF, bug bounty | Web apps | MCP + LLM local |
| Despliegue | Modular | Docker | Mini PC / VM |
| Autonomía | HITL | Pipeline autónomo | Asistido y autónomo (§6.3) |

---

## 3.4 IA como asistente en auditorías

### Copiloto humano (§6.3.1)

Reconocimiento asistido, generación de scripts, análisis de hallazgos, *vibe-coding*.

**Riesgos**: alucinaciones, falsa confianza (ASI09), filtrado de datos a APIs cloud, ampliación de superficie agéntica.

### Auditorías autónomas (§6.3.2)

Planificación → tool calling → observación → informe. Los sistemas actuales no sustituyen la validación humana en lógica de negocio compleja.

---

## 3.5 Brecha formativa del máster

Los 9 módulos del MCAIS2 cubren IA y **seguridad defensiva**, pero no **ciberseguridad ofensiva** en entornos agénticos. Este TFM propone el **Módulo 10** complementario.

| Área | Industria | Brecha formativa |
|------|-----------|------------------|
| Marcos | OWASP ASI, MITRE ATLAS, AISVS | Integración en laboratorio |
| Protocolos | MCP, A2A con CVEs activos | Evaluación ofensiva reproducible |
| Herramientas | CAI, BugTraceAI | Comparativa en hardware bajo coste |
| Regulación | Ley de IA UE | Puente normativa–práctica |

**Contribución del TFM**: enfoque agéntico, laboratorio reproducible, validación práctica ASI/ATLAS, material docente y herramientas open source.

---

## 3.6 Síntesis

| Línea | Pregunta | Caso TFM |
|-------|----------|----------|
| Protocolos | ¿Explotar y remediar MCP/A2A? | §6.1.1, §6.1.3 |
| Motores locales | ¿Seguridad por defecto? | §6.1.2 |
| Ataques LLM | ¿Evadir guardrails? | §6.2 |
| Pentesting agéntico | ¿Sustituir al auditor humano? | §6.3 |

*Última actualización: 2026-07-13*

[← Objetivos](./objetivos.md) · [Índice](./index.md) · [Planificación →](./planificacion.md)
