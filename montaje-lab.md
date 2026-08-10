# 5. Montaje del laboratorio (escenario)

### 5.1 Objetivo del laboratorio

Entorno **reproducible, aislado y de bajo coste** para pentesting agéntico, superficie de ataque, ataques sobre LLMs y auditorías asistidas por IA.

Dos capas:

1. **Capa física — servidor de inferencia** (`Proyecto-HW`): host Linux con GPU dedicada, operativo.
2. **Capa lógica — laboratorio ofensivo TFM**: código, tools de análisis e instalaciones específicas del estudio.

### 5.2 Escenario físico: Proyecto-HW

Servidor de inferencia local de alto rendimiento y bajo coste (**~1.800 €**), sin dependencia de APIs cloud.

#### Arquitectura hardware

Diseño modular en dos unidades unidas por **OCuLink** (PCIe 4.0 x4):

```
┌─────────────────────┐     OCuLink      ┌─────────────────────┐
│  AtomMan X7 Ti      │◄── PCIe 4.0 ───►│  Minisforum DEG1    │
│  Core Ultra 9       │                  │  RX 7900 XTX 24GB   │
│  32 GB DDR5 · 1TB   │                  │  Fuente 850W        │
│  NPU AI Boost       │                  │                     │
└─────────────────────┘                  └─────────────────────┘
```

| Componente | Modelo | Rol |
|------------|--------|-----|
| Mini PC | Minisforum AtomMan X7 Ti | Host Linux, orquestación, modelos ligeros |
| Dock eGPU | Minisforum DEG1 | Puente PCIe; GPU + fuente |
| GPU | AMD Radeon RX 7900 XTX (24 GB) | Inferencia (Ollama, ROCm, llama.cpp) |
| Fuente | Corsair SF850 SFX 850W | Alimentación estable |
| Conectividad | Cable OCuLink (SFF-8611) | Enlace físico |

#### Capacidad de inferencia

| Categoría | Modelos | Rendimiento orientativo |
|-----------|---------|-------------------------|
| GPU pura | Llama 3/3.1 8B, Mistral 7B, Gemma 2 9B, Phi-3/4 | 50–110+ tok/s |
| Híbrido | Llama 3.1 70B (Q2/Q3), Mixtral, Command R 35B | 5–15 tok/s |
| Límite | Llama 3.1 70B Q4, Qwen2.5 72B Q3 | 1–4 tok/s |

La comparación entre motores se detalla en [§6.1](./caso-1-arquitecturas-agenticas.md) (benchmark).

#### Software auxiliar

| Elemento | Función |
|----------|---------|
| `screen.py` | Panel LCD AtomMan (GPU, red, clima…) |
| `systemd/atomman.service` | Servicio del panel |
| `scripts/install-atomman-service.sh` | Instalación |
| Inference-Monitor | Web Docker de monitorización HW + motores LLM |

<div class="callout">

Blog del montaje físico: [Proyecto HW IA Local Bajo Coste](https://agentef0ns1.github.io/blog-hw-ias/)

</div>



<div class="nav-footer">

[← Planificación](./planificacion.md) · [Índice](./index.md) · [Caso 1 →](./caso-1-arquitecturas-agenticas.md)

</div>
