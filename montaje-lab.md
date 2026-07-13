# 2.1 Montaje del laboratorio (escenario)

Sincronizado con la memoria del TFM (§5). *Última actualización: 2026-07-13*

---

## Objetivo

Proporcionar un entorno **reproducible, aislado y de bajo coste** para ejecutar los casos de estudio: pentesting agéntico, explotación de superficie de ataque, ataques sobre LLMs y auditorías asistidas por IA.

---

## Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    LABORATORIO TFM                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐   ┌──────────────┐   ┌─────────────────┐  │
│  │ Agente local │   │ LLM local    │   │ MCP / Tools     │  │
│  │ (orquestador)│◄─►│ (Ollama/GGUF)│◄─►│ (pentest, etc.) │  │
│  └──────────────┘   └──────────────┘   └─────────────────┘  │
│         │                                    │              │
│         ▼                                    ▼              │
│  ┌──────────────┐                   ┌─────────────────┐   │
│  │ CTF targets  │                   │ Red aislada     │   │
│  │ (Docker/VM)  │                   │ (lab network)   │   │
│  └──────────────┘                   └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Componentes del repositorio

| Componente | Función | Ubicación |
|------------|---------|-----------|
| Host de laboratorio | Máquina base Linux | Físico, VM o Mini PC |
| Motor LLM local | Inferencia sin cloud | Ollama, LocalAI, Text-Gen, vLLM — ver [Caso 1](./caso-1-arquitecturas-agenticas.md) |
| Agente autónomo | Orquestación y tool calling | [`tools/agent/`](../tools/agent/) |
| Servidor MCP | Herramientas de pentesting | [`tools/mcp-server/`](../tools/mcp-server/) |
| Contenedores CTF | Objetivos vulnerables | [`lab/ctf/`](../lab/ctf/) |
| Monitorización | Logs, trazas, evidencias | Informes por caso |
| Guía de despliegue | Instrucciones paso a paso | [`lab/docs/`](../lab/docs/) |

---

## Hardware de referencia (opcional)

El directorio `Proyecto-HW/` del workspace documenta un laboratorio de alto rendimiento. **No es estrictamente necesario** para ejecutar las pruebas de los Casos 1–3:

| Componente | Modelo |
|------------|--------|
| Mini PC | Minisforum AtomMan X7 Ti |
| Dock eGPU | Minisforum DEG1 |
| GPU | AMD Radeon RX 7900 XTX (24 GB VRAM) |
| Fuente | Corsair SF850 SFX 850W |
| Conectividad | Cable OCuLink (SFF-8611) |
| Panel de estado | `screen.py` + `atomman.service` |

Las PoC de motores LLM pueden ejecutarse con un único motor (p. ej. Ollama en CPU/GPU integrada). Los escenarios de ataques a LLM y pentesting agéntico no dependen del hardware AtomMan.

---

## Despliegue

```bash
git clone https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git
cd TFM-Offensive-Security-IAs/lab
# Instrucciones detalladas en lab/docs/
docker compose up -d
```

---

## Seguridad del laboratorio

- Aislamiento de red respecto a entornos de producción.
- Datos sintéticos; sin información real de clientes.
- Alcance ético y legal documentado en cada caso de estudio.

---

[← Planificación](./planificacion.md) · [Índice](./index.md) · [Caso 1 →](./caso-1-arquitecturas-agenticas.md)
