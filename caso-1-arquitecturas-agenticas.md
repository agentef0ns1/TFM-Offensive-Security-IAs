# 6.1 Caso 1 — Arquitecturas agénticas

<p><span class="pill">motores LLM</span> <span class="pill">MCP</span> <span class="pill">A2A</span> <span class="pill">surface</span></p>

## Índice {#indice}

- [6.1.1 Motores LLM locales](#611-motores-llm-locales)
  - [Ollama](#ollama)
  - [LocalAI](#localai)
  - [vLLM](#vllm)
  - [Pruebas de rendimiento](#pruebas-de-rendimiento)
  - [Superficie de ataque en motores LLM](#superficie-de-ataque-en-motores-llm)
    - [Compromiso del servidor agéntico (lab)](#compromiso-del-servidor-agentico-lab)
- [6.1.2 Model Context Protocol (MCP)](#612-model-context-protocol-mcp)
- [6.1.3 Agent-to-Agent (A2A)](#613-agent-to-agent-a2a)
- [6.1.4 Permisos, skills y tools](#614-permisos-skills-y-tools)

---
**Objetivo:** documentar y analizar las **arquitecturas agénticas locales**: motores de inferencia, protocolos de integración (tools, MCP, A2A) y el modelo operativo del agente (permisos, *skills*, *tools*).

**Alcance:** todo lo desplegado y evaluado en el laboratorio del apartado 5.


<div class="card"><h4>6.1.2 MCP</h4><p>stdio / SSE / HTTP · Inspector · MitM</p></div>
<div class="card"><h4>6.1.3 A2A</h4><p>Agent Cards · spoofing · DoS + prompt injection</p></div>
<div class="card"><h4>6.1.4 Permisos</h4><p>Codex · Cline · Claude Code · OpenCode · Surface Auditor</p></div>
</div>

---


## 6.1.1 Motores LLM locales

Instalar y comparar motores de inferencia local como backend de un agente. Motores evaluados: **Ollama**, **LocalAI**, **vLLM**.

Por cada uno: PoC de instalación en Ubuntu Server, pruebas mínimas y análisis de la **configuración por defecto**. Complementos de rendimiento:

1. Web de monitorización del servidor de inferencia  
2. Scripts de benchmark comparativo  

### Ollama

Herramienta open-source para administrar y ejecutar LLMs en local (CLI o app de escritorio). En el host del lab se usa **solo CLI**.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Servicio systemd en el arranque (`ollama.service`), con drop-in de configuración del TFM:

![Ollama — systemctl status]({{ '/assets/images/docx/image6.png' | relative_url }})
<p class="figcap">Ollama — <code>systemctl status ollama.service</code> y unidad systemd</p>

Configuración orientada a cargar modelos en GPU (AMD RX 7900 XTX / OCuLink):

![Ollama — variables / drop-in GPU]({{ '/assets/images/docx/image7.png' | relative_url }})
<p class="figcap">Ollama — configuración básica / entorno para inferencia en GPU</p>

### LocalAI

Motor open-source con API compatible OpenAI / Anthropic / ElevenLabs. A diferencia de Ollama, expone una **WebUI** de administración e interacción.

![LocalAI — WebUI]({{ '/assets/images/docx/image8.png' | relative_url }})
<p class="figcap">LocalAI — interfaz web de administración e interacción</p>

Despliegue vía **imagen Docker** + servicio systemd de usuario:

![LocalAI — docker compose]({{ '/assets/images/docx/image9.png' | relative_url }})
<p class="figcap">LocalAI — <code>docker-compose</code> del servicio</p>

![LocalAI — systemd user service]({{ '/assets/images/docx/image10.png' | relative_url }})
<p class="figcap">LocalAI — unidad systemd (<code>~/.config/systemd/user/localai.service</code>, backend ROCm/AMD)</p>

Modelos en directorio local compartido:

![LocalAI — directorio de modelos]({{ '/assets/images/docx/image11.png' | relative_url }})
<p class="figcap">LocalAI — almacenamiento local de modelos</p>

![LocalAI — detalle configuración]({{ '/assets/images/docx/image12.png' | relative_url }})
<p class="figcap">LocalAI — detalle adicional de configuración / volúmenes</p>

### vLLM

Motor orientado a inferencia de producción: mínima latencia, alto throughput. Docker en Ubuntu Server, **un modelo** con ROCm explícito sobre la 7900 XTX (24 GB VRAM), compartiendo el store de modelos con LocalAI.

![vLLM — servicio / configuración]({{ '/assets/images/docx/image13.png' | relative_url }})
<p class="figcap">vLLM — configuración del servicio en el host</p>

![vLLM — imagen Docker ROCm]({{ '/assets/images/docx/image14.png' | relative_url }})
<p class="figcap">vLLM — imagen <code>vllm/vllm-openai-rocm:latest</code></p>

### Pruebas de rendimiento

**Inference-Monitor** — web Docker que, vía API del SO, monitoriza recursos y administra Ollama / LocalAI / vLLM.

![Inference-Monitor]({{ '/assets/images/docx/image15.png' | relative_url }})
<p class="figcap">Inference-Monitor — panel de monitorización del servidor de inferencia</p>

<div class="card"><h4>📦 Inference-monitor</h4><p><a href="https://github.com/agentef0ns1/Inference-monitor">github.com/agentef0ns1/Inference-monitor</a></p></div>

**Benchmark** — mismo hardware, modelo comparable **Qwen3-14B** (~16 GB VRAM). Objetivo: qué motor responde mejor para los ejercicios del TFM.

![Benchmark]({{ '/assets/images/docx/image16.png' | relative_url }})
<p class="figcap">Benchmark comparativo entre motores</p>

<div class="card"><h4>📦 benchmark-inference-monitor</h4><p><a href="https://github.com/agentef0ns1/benchmark-inference-monitor">github.com/agentef0ns1/benchmark-inference-monitor</a></p></div>

### Superficie de ataque en motores LLM

La superficie no difiere de otro software con exposición externa: **interna** (ficheros, permisos, usuario del proceso) y **externa** (APIs HTTP de admin e inferencia).

Vulnerabilidades por defecto frecuentes:

- HTTP sin TLS  
- APIs **sin autenticación**  
- Binding a `0.0.0.0`  

![Análisis configuración interna]({{ '/assets/images/docx/image17.png' | relative_url }})
<p class="figcap">Script / análisis de configuración interna y privilegios</p>

![Exposición API]({{ '/assets/images/docx/image18.png' | relative_url }})
<p class="figcap">Superficie externa — APIs expuestas</p>

![Ollama hacking tool]({{ '/assets/images/docx/image19.png' | relative_url }})
<p class="figcap">Herramienta Ollama-hacking-tools frente a API sin autenticación</p>  

#### Compromiso del servidor agéntico (lab)

Escenario: web en tiempo real alimentada por un agente → LLM. Vector de entrada: **Ollama expuesto sin auth**. Herramienta:

<div class="card"><h4>📦 ollama-hacking-tools</h4><p><a href="https://github.com/agentef0ns1/ollama-hacking-tools">github.com/agentef0ns1/ollama-hacking-tools</a></p></div>

Intrusión con **RCE vía modelos maliciosos**:

<div class="video-wrap">
<iframe src="https://www.youtube.com/embed/v46kJyIy9KQ" title="Ollama hacking / RCE" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="figcap">Demo RCE sobre Ollama — <a href="https://www.youtube.com/watch?v=v46kJyIy9KQ&t=3s">YouTube</a></p>

---

## 6.1.2 Model Context Protocol (MCP)

Estudio del MCP como capa agente↔herramientas y de su superficie (descubrimiento de tools, *poisoning*, abuso de recursos).

<div class="card"><h4>📦 MCP-security-lab</h4><p><a href="https://github.com/agentef0ns1/MCP-security-lab">github.com/agentef0ns1/MCP-security-lab</a></p></div>

Servidor MCP de ejemplo + tres transportes: **stdio**, **SSE**, **HTTP**. Herramienta de laboratorio para interceptar y manipular cada uno:

![]({{ '/assets/images/docx/image20.png' | relative_url }})
<p class="figcap">Interceptación MCP por transporte (stdio / SSE / HTTP)</p>

![]({{ '/assets/images/docx/image21.png' | relative_url }})
<p class="figcap">Arquitectura del laboratorio MCP y flujos de comunicación</p>

Capacidades formativas de la tool: sniffing, **MitM**, manipulación del JSON-RPC y redirección a proxy externo para auditorías HTTP/SSE.

---

## 6.1.3 Agent-to-Agent (A2A)

Análisis del protocolo A2A y vectores si los agentes **no están autenticados**.

<div class="card"><h4>📦 A2A-security-lab</h4><p><a href="https://github.com/agentef0ns1/A2A-security-lab">github.com/agentef0ns1/A2A-security-lab</a></p></div>

**Flujo legítimo**

1. Usuario pide el clima de una ciudad al **Invoker**.  
2. El Invoker usa el LLM para extraer ubicación/acción.  
3. Lee el **Agent Card** del Weather Agent.  
4. `message/send` por A2A → resultado → LLM redacta la respuesta.

**Cadena de ataque (spoofing)**

```
Atacante ──DoS──► Weather Agent (cae)
Atacante ──spoof──► Fake Agent (mismo Agent Card)
Invoker ──A2A──► Fake Agent
Fake Agent ──clima + prompt injection──► Invoker/LLM
LLM ──system prompt leak──► Usuario
```

<div class="video-wrap">
<iframe src="https://www.youtube.com/embed/ldbxnRV__Ns" title="A2A agent spoofing" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="figcap">DoS → spoofing → prompt injection → leak — <a href="https://www.youtube.com/watch?v=ldbxnRV__Ns">YouTube</a></p>

---

## 6.1.4 Permisos, skills y tools

Auditoría de la configuración del agente local: skills, permisos SO, políticas de tool calling y debilidades agente–SO.

Agentes estudiados: **Codex**, **Cline**, **Claude Code**, **OpenCode**.

CLI de auditoría / explotación local:

- Inventario de directorios donde el agente escribe config y datos  
- PoCs: skill maliciosa · sandbox `auto-approval` · reglas `exec *` · alias `ls=rm -fr`  

<div class="video-wrap">
<iframe src="https://www.youtube.com/embed/k7eNc1mPccc" title="Agent Surface Auditor" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="figcap">Surface Auditor — auditoría y explotación — <a href="https://www.youtube.com/watch?v=k7eNc1mPccc">YouTube</a></p>

<div class="callout warn">

Uso exclusivo en entornos controlados con autorización. Las PoCs modifican config/skills del agente.

</div>

---
<p class="nav-footer"><a href="{{ '/montaje-lab.html' | relative_url }}">← Montaje lab</a> · <a href="{{ '/' | relative_url }}">Índice</a> · <a href="{{ '/caso-2-ataques-llms.html' | relative_url }}">Caso 2 →</a></p>


