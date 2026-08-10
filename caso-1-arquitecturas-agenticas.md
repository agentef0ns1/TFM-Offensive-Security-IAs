# 6.1 Caso 1 — Arquitecturas agénticas

**Objetivo:** Documentar y analizar las **arquitecturas agénticas locales** estudiadas en el TFM: motores de inferencia LLM en la IA Local, protocolos de integración (tools, MCP, comunicación A2A), y el modelo operativo del agente local (permisos, *skills* y *tools*).

**Alcance:** Todo lo relacionado con las arquitecturas locales desplegadas y evaluadas en el laboratorio.

### 6.1.1 Arquitectura agéntica: motores LLM locales

El objetivo principal del estudio de los motores de LLM lcoales, es instalar y comparar diferentes motores de inferencia local como backend de un LLM para un agente de IA.

Los motores, seleccionados con los que se han realizado pruebas han sido:

- Ollama

- LocalAI

- vLLM

Para cada uno de ellos, se proporcionará una PoC de instalación en el sistema operativo Ubuntu-server anfitrions del servidor para la realización de pruebas mínimas, y se realizarán purebas/analisis de seguridad de la configuración por defecto.

Para las pruebas de rendimiento se han abordado dos soluciones, principales:

- Desarrollo de una web de monitorización sobre el servidor de inferencia:

- Generación de script de benchmark para comparación del rendimiento de los motores locales.

#### 6.1.1.1 Ollama

Ollama se trata de una herramienta de código abierto, diseñada para administrar y ejecutar modelos de lenguaje largo o LLMs completamente en local con tus propios componetes de hardware, puede ser administrada con interfaz gráfica desde una aplicación de escritorio, o por linea de comandos.  
Debido al sistema operativo seleccionado en el sistema anfitrion, se ha decidido realizar la instalación y administración por la segunda vía.

Instalación en linux-server:  
curl -fsSL https://ollama.com/install.sh \| sh

Servición instalado que se ejecuta en el arranque:

Con la siguiente configuración básica:

necesaria para que los modelos LlMss carguen en la targeta gráfica AMD 7900 XTX conectada al Mini-pc por ocunlink.

#### 6.1.1.2 LocalAI

LocalAI se trata de un motor de inteligencia artifical de código abierto, diseñado para ejecutar en local. Su configuración a nivel API e interación con agentes, modelos y MCPs es un remplazo directo de API de OpenAI, Anthorpic y ElevenLabs.

A diferencia de Ollama, la interacción con este motor se realiza desde una Web que levanta en local el propio servicio.

La web de LocalAI, permite tanto administrar como interectuar con los modelos de lenguaje larg o LLMs.  
La instalación directa en el entorno del servidor se ha realiza mediante el uso de una imagen docker, conectada a un servicio del sistema operativo que lo arranca en el inicio.

La configuración específica del servicio:  
  
Asi como el docker compose procio del servicio:

Todos los modelos están almcenados en un directorio local:

#### 6.1.1.3 vLLM

VLLM es un motor de Lenguajes de modelos largos LLMs, orientado a servidor de inferencia local de cara a entornos productivos, que requieren míma velicidad y baja latencia.

La instalción por simplicidad se ha relizado desde una imagen docker en el sistema operativo anfitrion Ubuntu-Server, configurado como un servicio en local que comparte los modelos a utilizar en un directorio común con LocalAI.  
El servicio instalado local, con una configuración más compleja a nivel variables de entrono, orientado a la ejecución de un solo modelo con el uso explicito de la GPU de rocm de la gráfica AMD 7900 XTX de 24GB de VRAM:

La imagen docker:

#### 6.1.1.4 Pruebas de rendimiento

**Web de inferencia:**

Para evaluar el rendimeitno y consumo de rcursos en tiempo real, se ha desarrollado la siguiente Web montada en un docker que se despliega como servicio en el sistema operativo del servidor de Inferencia, dicha web se levanta en el arranque asociada al servicio docker.

Sus funcionalidades principales por medio de una API al sistema operativo, son las de, evaluar el consumo de recursos monitoricación y administración básica mediante el usao de los servicios de lso 3 motores de LMMs, Ollama, LocalAI y VLLM.  
  
El contenido del mismo se pue encontrar en mi repositorio personal:

<https://github.com/agentef0ns1/Inference-monitor>  
  
**Benchmark de Motores:**

El objetivo del proyecto de benchamrk, es comprobar con las mismas capcidades de hardware en el servidor de inferencia, con un modelo standard equiparable en los tres entornos,  Qwen3-14B con el que el sistema funciona de una modo olgado, de forma aproxima 16GB de VRAM de la tarjeta gráfica

Que modelo responderá mejor y por lo tanto será máscómodo de usar durante el uso de los ejerecicios del TFM, los resultados obtenidos han sido los siguientes de forma gráfica:**  
  
  
**El código completo se encuentra en el siguiente repositorio:  
<https://github.com/agentef0ns1/benchmark-inference-monitor>

#### 6.1.1.5 Superficie de ataque en motores LLM

La superficie de ataque orientada a los motores de LLMs locales debido a su arquitectura no difiere de cualquier otro software tradicional que se conecta con el exterios y por lo tanto puede ser interna, o externa.

La superficie interna viane dada por cada uno de sus ficheros de configuración, permisos y privilegios definidos con los que ejecutan los modelos, así como el usuario del sistema operativo con el que ejecutan sus procesos del sistema.

La superficie externa viene dada por sus APIs webs, que puede tener múltiples usos, tanto para la administración del propio LLM como para la comunicación de este con otros sistemas como puedan ser software de comunicación don un humano o software de comunicación con un agente. Es por esto que no difiere de una auitoría de seguridad sobre APIs o Web.

Script de analisis de configuración interna, que valida escalada de privilegios

Comunicación con el exterior vulnerabilidades por defecto:

- Uso de HTTP

- APIs expuestas sin autenticación

**Compromiso de un servidor completo de un sistema agentico :**

El compromiso completo del servidor agentico por un atacante, remoto se centra en un ejericio sobre un entrorno de laboratorio, que contiene diferentes instlaciónes por defecto y por lo tanto vulnerabilidades que pueden hacer que un atacante externo acceda el servidor de inferencia desde el exterior.

La arquitectura expuesta en el ataque será la siguiente y estara compuesta por una Web que se actualiza en tiempo real por un agente de IA conectado a un LLM al que realiza consultas:

El vector de entrada será el motor de LLM Ollama expueto en su web por la interfaz 0.0.0.0, sin autenticar. Para eto se utilizará la herramienta desarrollada de Ollama-Hacking-tool:

Disponible en mi respositorio de GitHub:

**<https://github.com/agentef0ns1/ollama-hacking-tools>  
  
**El ejericio de intrusión con RCE mediante modelos de LLM maliciosos explicado en el siguiente video:

**<https://www.youtube.com/watch?v=v46kJyIy9KQ&t=3s>**

### 6.1.2 Arquitectura agéntica: Model Context Protocol (MCP)

El Objetivo es estudiar el protocolo MCP como capa de integración entre agente y herramientas, a nievel funcionamientoasí como su superficied e ataque (descubrimiento de tools, *poisoning* de servidores, abuso de recursos).  
Pero esto se ha desarrollado un Laboratorio específico pra interactuar entre agentes locales y servidores MCP:  
  
<https://github.com/agentef0ns1/MCP-security-lab>  
  
Se monta un servidor MCP local de ejemplo y se estudian los diferentes tipos de comunicaiones con los que un agente puede interactuar con un servidor MCP.

Los tipos de protocolos de comunicaión son los siguientes: Stdio, SSE y HTTP en el laboratorio se ha desarrollado una herramieta que se encarga de interceptar y manipular estos protocolos:



![](./assets/images/docx/image20.png)



La arquitectura del laboratorio y comunicaciones, se puede ver a continucaicón:



![](./assets/images/docx/image21.png)



La herramienta, trata de ser formativo y puede snifar el tráfico, realizar un ataque de MiTM , para controlar o manipular el cntenido qeu viaja en la comunicación entre el agente y el sevridor MCP. Así como desviar el tráfico a un proxy externo que con el cual, será posible reslizar auditorías de tipo HTTP y SSE:

### 6.1.3 Arquitectura agéntica: Agent-to-Agent (A2A)

El Objetivo será analizar el protocolo Agent-to-Agent (A2A) entre diferentes agentes, asi como estudiar sus posibles vulnerabilidades o vectores de ataque si estos no, se encunetran correctamente securizados.

Para este punto se ha desarrollado tanto un PoC de auditoria de comunicación entre dos agentes y un LLM, como una explicación completa del ataque realizado agent spoofing en video, ideado por el alumno para la ocasión:

El código completo se encunetra en el respositorio github:  
<https://github.com/agentef0ns1/A2A-security-lab>

La arquitectura será la siguiente:

**  
**

- Usuario: mediante un prompt se comunicará con el agente1 o agente invocador indicando que quiere conocer el clima en una cidudad

- Agente invocador, interactua con LLM para extración concreta de la ubicación y acción a realizar.

- Mediante el AgentCard, el agente invocador entiend que el agente a la escucha proprociona el servicio de conocer el clima en una ubicación determinada.

- Se comunica con el mediante el protocolo A2A, y obtiene el resultado que es procesado finalmente por el LLM y devuelto el usuario final.

En el laboratorio se estudian los vectores de ataque de lo que puede ocurrir si los Agentes no están autenticados entre ellos.  
El laboratorio reproduce un ataque de agente spoofing donde un usaurio malicioso realiza un **ataque de DOS sobre el Agente2** que tiene la capacidad de conectarse a internet y obtner el tiempo.

Cuando este se cae por el número elevdo de solicitudes recibidas, se levante un Agente3 malicioso que lo suplanta. Cuando el Agente3 es invocado, devuelve un resultado del clima **seguido de un prompt injection** que será procesado por el Agente1, he inyectado en el LLM que devolvera un **Leak de información** al usuario final, con el prmpot del sistema.

Explicado y ejecutado en el siguiente video:

<https://www.youtube.com/watch?v=ldbxnRV__Ns>

### 6.1.4 Agentes locales: permisos, skills y tools

El Objetivo del módulo es el de Auditar y explotar la configuración del agente local, asignación de *skills*, permisos sobre el sistema operativo, políticas de tool calling y debilidades en la interacción agente–SO.  
Para esto se han estudiado el funcionamiento y las capacidades de los siguientes agentes lcoales:

- Codex

- Cline

- Caude-code

- Open-code

Se ha desarrollado una tool de linea de comandos quese puede utilizar par estudiar o evaluar los permisos de un agente en local para realizar un ataque sobre el sistema o usuario que lo esta utilizando.

Tiene dos funcionalidades principales, la primera es la de auditar todos los directorios locales donde los agnetes escroben sus datos y configuraciones y la segunda, es la de generar PoC de explotcaciones en local, como son:

- Inyectar skill maliciosa

- Modificar las propiedades del sandbox auto-approval all

- Añadir reglas de ejecución em la configuración exec \*

- Inyectar un alias de comando malicioso ejemplo ls=rm -fr

Video demo del uso del agente del código auditor y explotación desde el agente:  
<https://www.youtube.com/watch?v=k7eNc1mPccc>

---

[← Montaje lab](./montaje-lab.md) · [Índice](./index.md) · [Caso 2 →](./caso-2-ataques-llms.md)
