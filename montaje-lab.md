# 2.1 Montaje del laboratorio (escenario)

Sincronizado con la memoria del TFM (§5). *Última actualización: 2026-07-13*

---

## Objetivo

Entorno **reproducible, aislado y de bajo coste** para los casos de estudio: pentesting agéntico, ataques sobre LLMs y auditorías asistidas por IA.

**Dos capas:**

1. **Capa física** — servidor de inferencia (`Proyecto-HW/`), **operativo**.
2. **Capa lógica** — laboratorio ofensivo TFM (agente, MCP, CTF) sobre el host.

---

## Escenario físico: Proyecto-HW

Sistema de IA local montado y funcionando en [`Proyecto-HW/`](https://github.com/agentef0ns1/blog-hw-ias). Arquitectura modular Mini PC + eGPU por OCuLink:

```
┌─────────────────────┐     OCuLink      ┌─────────────────────┐
│  AtomMan X7 Ti      │◄──── PCIe 4.0 ────►│   Minisforum DEG1   │
│  Core Ultra 9       │                    │  RX 7900 XTX 24GB   │
│  32 GB DDR5 · 1TB   │                    │  Fuente 850W        │
└─────────────────────┘                    └─────────────────────┘
```

| Componente | Modelo | Rol |
|------------|--------|-----|
| Mini PC | Minisforum AtomMan X7 Ti | Host Linux, orquestación |
| Dock eGPU | Minisforum DEG1 | Puente PCIe |
| GPU | AMD RX 7900 XTX (24 GB VRAM) | Inferencia (Ollama, ROCm) |
| Fuente | Corsair SF850 SFX 850W | Alimentación GPU + dock |
| Conectividad | Cable OCuLink (SFF-8611) | Enlace físico |

**Capacidad:** LLMs 7B–13B en GPU pura (50–110+ tok/s); modelos 70B cuantizados en modo híbrido.

### Documentación del montaje

El blog documenta **explícitamente** el diseño, compras, ensamblaje y puesta en marcha del servidor de inferencia:

### [**Proyecto HW IA Local Bajo Coste**](https://agentef0ns1.github.io/blog-hw-ias/)

Incluye objetivos, arquitectura, componentes, presupuesto, rendimiento estimado, galería y vídeos de funcionamiento.

Auxiliar en el host: `screen.py` + `atomman.service` (panel de monitorización; no requerido para los casos §6).

---

## Arquitectura lógica del laboratorio TFM

```
┌─────────────────────────────────────────────────────────────┐
│                    LABORATORIO TFM                          │
├─────────────────────────────────────────────────────────────┤
│  Agente local ◄──► LLM local (Ollama) ◄──► MCP / Tools      │
│       │                                              │      │
│       ▼                                              ▼      │
│  CTF targets (Docker)                    Red aislada (lab)  │
└─────────────────────────────────────────────────────────────┘
```

---

## Componentes software

| Componente | Ubicación |
|------------|-----------|
| Motor LLM | Ollama (+ LocalAI, Text-Gen, vLLM — [Caso 1](./caso-1-arquitecturas-agenticas.md)) |
| Agente | [`tools/agent/`](../tools/agent/) |
| Servidor MCP | [`tools/mcp-server/`](../tools/mcp-server/) |
| CTF | [`lab/ctf/`](../lab/ctf/) |
| Scripts motores LLM | `Caso-1-Arquitecturas-Agenticas/6.1.2-Motores-LLM-locales/scripts/` |

---

## Despliegue

```bash
# Host de inferencia configurado según:
# https://agentef0ns1.github.io/blog-hw-ias/

git clone https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git
cd TFM-Offensive-Security-IAs/lab
docker compose up -d
```

---

## Seguridad del laboratorio

- Red aislada; datos sintéticos; alcance ético documentado.
- Hardening del motor LLM (binding, sin exposición LAN) — ver §6.1.2.

---

[← Planificación](./planificacion.md) · [Índice](./index.md) · [Caso 1 →](./caso-1-arquitecturas-agenticas.md)
