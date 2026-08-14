# 7. Conclusiones

## Índice {#indice}

  - [7.1 Cumplimiento de objetivos](#cumplimiento-objetivos)
  - [7.2 Hallazgos principales](#hallazgos-principales)
  - [7.3 Limitaciones del estudio](#limitaciones-estudio)
  - [7.4 Trabajo futuro](#trabajo-futuro)
  - [7.5 Contribución al máster](#contribucion-master)

---

### 7.1 Cumplimiento de objetivos {#cumplimiento-objetivos}

El TFM ha permitido **ampliar de forma práctica** lo aprendido en el máster MCAIS2, pasando del marco teórico-defensivo a un laboratorio ofensivo operativo sobre sistemas de IA.

En concreto, como alumno se han cumplido los siguientes logros:

- **Ampliación de conocimientos** en ciberseguridad aplicada a IA: taxonomía B³, prompt injection (directa/indirecta), tool calling, memoria, guardrails y evaluación automatizada (Promptfoo).
- **Dominio de IA local y hardware de inferencia**: despliegue y comparación de motores (Ollama, LocalAI, vLLM), monitorización y un escenario físico propio ([Proyecto-HW]({{ '/montaje-lab.html' | relative_url }})) con GPU dedicada para workloads ofensivos y de auditoría.
- **Creación de retos y casos de uso ofensivos no existentes** en el plan de estudios: implementación propia (inspirada en Gandalf / Agent Breaker de Lakera) de un CTF local con niveles progresivos de defensa, write-ups y demos en vídeo ([Caso 2]({{ '/caso-2-ataques-llms.html' | relative_url }})).
- **Wrapper MCP Kali** ([MCP-kali-cline](https://github.com/agentef0ns1/MCP-kali-cline)): integración de Kali Linux con Cline/Cursor vía MCP (Docker, API, noVNC), de modo que el agente pueda orquestar herramientas de pentesting en laboratorio autorizado.
- **Wrapper de análisis de código con control de contexto** ([MVP-code-review-full-context-control](https://github.com/agentef0ns1/MVP-code-review-full-context-control)): servidor MCP de memoria/contexto (chunking, plan acotado, SQLite e informes en `.mvp-audit/`) para auditar repos grandes con LLM local sin saturar la ventana de contexto.
- **Pentesting agéntico sostenido**: PoC 24×7 sobre Web Security Academy / BSCP con orquestación vía MCP Burp, alcanzando **154 labs** resueltos ([Caso 3]({{ '/caso-3-pentesting-agentico.html' | relative_url }}#challenge-poc-247-bscp-portswigger)).



### 7.2 Hallazgos principales {#hallazgos-principales}

- **Es necesario ampliar el contenido del máster** con material ofensivo sobre IA agéntica: MCP, A2A, superficie del agente, jailbreaks, pre/post-check, juez LLM y automatización de red teaming. La formación actual cubre bien el enfoque defensivo; este TFM muestra que falta la contraparte operativa.
- Los **ataques sobre agentes** no se limitan al prompt del usuario: el contenido externo (HTML, PDF, `review.rules`, schemas MCP, memoria) es un vector crítico (IIO/ITI/DAIS).
- La **defensa en profundidad** (pre-check, post-check RegEx, juez LLM) es efectiva a nivel de laboratorio, pero cada capa introduce nuevos puntos de bypass; los retos demuestran que un único control no basta.
- La **IA local + MCP** habilita copiloto y autonomía real en auditoría (Kali, Burp, análisis de código), siempre que se controle el contexto, el scope y la autorización del objetivo.
- Publicar **herramientas y CTFs propios** acelera el aprendizaje: obliga a diseñar escenarios, medir éxito del ataque y documentar evidencias, no solo consumir demos ajenas.

### 7.3 Limitaciones del estudio {#limitaciones-estudio}

- **Tiempo disponible**: el TFM se ha desarrollado en paralelo a trabajo y al resto del máster. El tiempo invertible ha sido limitado frente a la amplitud del tema (HW, tres casos, CTFs, wrappers MCP, automatización y PoC 24×7). Priorizar entrega reproducible ha obligado a acotar profundidad en algunas líneas (p. ej. más niveles de reto, más motores o evaluación longitudinal de frameworks).
- **Alcance de laboratorio**: las pruebas se restringen a entornos controlados y autorizados; no se extrapolan a sistemas de terceros ni a producción real.
- **Cadena de herramientas en evolución**: MCP, clientes IDE, Promptfoo y APIs de agentes cambian con rapidez; resultados y scripts pueden requerir ajustes en versiones futuras.
- **Cobertura incompleta del espacio de ataque**: la taxonomía B³ y los retos ilustran familias representativas, no un inventario exhaustivo de vulnerabilidades en IA.

### 7.4 Trabajo futuro {#trabajo-futuro}

- Ampliación de casos de estudio y CTFs (nuevos vectores IIO/ITI, niveles adicionales de defensa).
- Integración con masterclass y material docente del Módulo 10.
- Evaluación longitudinal de frameworks emergentes de pentesting agéntico.
- Endurecimiento y empaquetado de los wrappers (MCP Kali, MVP de contexto) para reutilización por otros alumnos.
- Continuar la cola BSCP / certificación y documentar playbooks de orquestación MCP-Burp.

### 7.5 Contribución al máster {#contribucion-master}

Este TFM pretende **complementar** la formación defensiva del MCAIS2 con competencias **ofensivas operativas** en entornos de IA: laboratorio local, retos propios, wrappers MCP y evidencia de auditoría asistida/autónoma.

Más allá del entregable, me gustaría **aportar un granito de arena** a los alumnos del próximo curso: compartir la experiencia personal ofensiva montaje de HW/inferencia local, diseño de retos, bypass de guardrails, uso de MCP con Kali y Burp, control de contexto en auditorías de código, incluso **impartiendo alguna clase o sesión práctica** preparada en profundidad, alineada con el Módulo 10 o una masterclass dedicada.

El material ya publicado (web, repos, vídeos y write-ups) puede servir de base docente inmediata: pero seguro que la evolución en la materia requiere nuevos cambios antes de ser impartida.

---
<p class="nav-footer"><a href="{{ '/caso-3-pentesting-agentico.html' | relative_url }}">← Caso 3</a> · <a href="{{ '/' | relative_url }}">Índice</a> · <a href="{{ '/bibliografia.html' | relative_url }}">Bibliografía →</a></p>
