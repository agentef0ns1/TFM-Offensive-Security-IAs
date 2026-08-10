# 5. Montaje del laboratorio (escenario)

### 5.1 Objetivo del laboratorio

Proporcionar un entorno **reproducible, aislado y de bajo coste** para ejecutar los casos de estudio del TFM: pentesting agéntico, explotación de superficie de ataque, ataques sobre LLMs y auditorías asistidas por IA.

El escenario se articula en **dos capas**:

1.  **Capa física — servidor de inferencia local** (`Proyecto-HW`): host Linux con GPU dedicada, ya montado y operativo.

2. **Capa lógica — laboratorio ofensivo TFM** (`TFM-Offensive-Security-IAs`): Código desarrollado de forma explicita pra el estudio y desarrollo del proyecto, instalación de software, tools de analisis, etc.

### 5.2 Escenario físico: `Proyecto-HW`

El **servidor de inferencia** del TFM está implementado y **funcionando.** Se trata de un sistema de IA local de alto rendimiento y bajo coste (1800 €), diseñado para ejecutar LLMs y cargas híbridas sin dependencia de APIs cloud.

#### Arquitectura hardware

Diseño modular en **dos unidades** unidas por **OCuLink** (PCIe 4.0 x4 nativo, ~64 GT/s), evitando el cuello de botella de Thunderbolt:

    ┌─────────────────────┐     OCuLink           ┌─────────────────────┐
    │  Minisforum AtomMan      │◄── PCIe 4.0 ──►│   Minisforum DEG1             │
    │      X7 Ti                        	 |		          │    (Dock eGPU)                      │
    │  • Core Ultra 9                	 |		          │  • RX 7900 XTX                     │
    │  • 32 GB DDR5                	 |		          │  • 24 GB VRAM                     │
    │  • 1 TB NVMe                        |     		          │  • Fuente ATX 850W           │
    │  • NPU AI Boost                    |      		          │                                                │
    └─────────────────────┘                                └─────────────────────┘

| Componente       | Modelo                              | Rol                                                         |
|------------------|-------------------------------------|-------------------------------------------------------------|
| **Mini PC**      | Minisforum AtomMan X7 Ti            | Host Linux: SO, orquestación, preprocesado, modelos ligeros |
| **Dock eGPU**    | Minisforum DEG1                     | Puente PCIe; aloja GPU y fuente                             |
| **GPU**          | AMD Radeon RX 7900 XTX (24 GB VRAM) | Inferencia principal (Ollama, ROCm, llama.cpp)              |
| **Fuente**       | Corsair SF850 SFX 850W              | Alimentación estable de GPU + dock                          |
| **Conectividad** | Cable OCuLink (SFF-8611)            | Enlace físico Mini PC ↔ dock                                |

#### Capacidad de inferencia

Con 24 GB de VRAM dedicados y 32 GB de RAM DDR5 (ampliable), el host soporta:

| Categoría          | Modelos                                         | Rendimiento orientativo                 |
|--------------------|-------------------------------------------------|-----------------------------------------|
| **GPU pura**       | Llama 3/3.1 8B, Mistral 7B, Gemma 2 9B, Phi-3/4 | 50–110+ tokens/seg                      |
| **Híbrido**        | Llama 3.1 70B (Q2/Q3), Mixtral, Command R 35B   | 5–15 tokens/seg (offloading VRAM + RAM) |
| **Límite teórico** | Llama 3.1 70B Q4, Qwen2.5 72B Q3                | 1–4 tokens/seg (swap NVMe)              |

La capacidad de inferencia se analiza en el 6.1.1-Motores-LLM-locales en si apartado benchmark, donse se comparan de forma explicaita las respuestas de un modelo en diferentes Motores de LLM

#### Software auxiliar en `Proyecto-HW`

| Elemento                             | Función                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `screen.py`                          | Panel de estado del Mini PC (GPU, red, fecha/hora, clima) vía pantalla serial AtomMan                            |
| `systemd/atomman.service`            | Servicio systemd del panel de monitorización                                                                     |
| `scripts/install-atomman-service.sh` | Instalación del servicio en el host                                                                              |
| Inference-Monitor                    | Docker con servicio web que monitoriza, el estado de HW y rendimiento en tiempo real del servidor de inferencia. |

> El panel AtomMan es **auxiliar de monitorización** del host, no interviene en la lógica agéntica ni en los casos de estudio ofensivos se enecarga de monitorizar y actualizar mediante scripts en el sistema operativo y llamdas a las APIs metorológicas los datos de la pantalla LCD del dispositivo:

El **monitor de del servidor de inferecncia**, se encarga de mostrar en tiempo real el estado del sistema, así como los Modelos de LLM disponibles y el manejo de los servicio de lso motores de LLM.

**Proyecto HW IA Local Bajo Coste — blog-hw-ias**

*visitar: <https://agentef0ns1.github.io/blog-hw-ias/>*

---

[← Planificación](./planificacion.md) · [Índice](./index.md) · [Caso 1 →](./caso-1-arquitecturas-agenticas.md)
