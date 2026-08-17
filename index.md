**Trabajo Fin de Máster — MCAIS2** · **Autor:** Ildefonso González Sánchez

<p><span class="pill">v1.0</span> <span class="pill">MCAIS2</span> <span class="pill">lab local</span> <span class="pill">ofensivo</span></p>

Ciberseguridad **ofensiva** aplicada a sistemas de IA agénticos: motores locales, MCP, A2A, superficie del agente, CTFs B³ y pentesting asistido/autónomo.

## Índice

1. [Introducción]({{ '/introduccion.html' | relative_url }})
   - [1.1 Contexto]({{ '/introduccion.html' | relative_url }}#11-contexto)
   - [1.2 Motivación]({{ '/introduccion.html' | relative_url }}#12-motivacion)
   - [1.3 Alcance y limitaciones]({{ '/introduccion.html' | relative_url }}#13-alcance-y-limitaciones)
2. [Objetivos]({{ '/objetivos.html' | relative_url }})
   - [2.1 Objetivo general]({{ '/objetivos.html' | relative_url }}#21-objetivo-general)
   - [2.2 Objetivos específicos]({{ '/objetivos.html' | relative_url }}#22-objetivos-especificos)
   - [2.3 Criterios de éxito]({{ '/objetivos.html' | relative_url }}#23-criterios-de-exito)
3. [Estado del arte]({{ '/estado-del-arte.html' | relative_url }})
   - [Marcos normativos]({{ '/estado-del-arte.html' | relative_url }}#marcos-normativos)
   - [Líneas abiertas de investigación]({{ '/estado-del-arte.html' | relative_url }}#lineas-abiertas-de-investigacion)
4. [Planificación]({{ '/planificacion.html' | relative_url }})
   - [4.1 Metodología]({{ '/planificacion.html' | relative_url }}#41-metodologia)
   - [4.2 Fases del proyecto]({{ '/planificacion.html' | relative_url }}#42-fases-del-proyecto)
5. [Montaje del laboratorio]({{ '/montaje-lab.html' | relative_url }})
   - [5.1 Objetivo]({{ '/montaje-lab.html' | relative_url }}#51-objetivo-del-laboratorio)
   - [5.2 Proyecto-HW]({{ '/montaje-lab.html' | relative_url }}#52-escenario-fisico-proyecto-hw)
6. Casos de estudio
   - [6.1 Arquitecturas agénticas]({{ '/caso-1-arquitecturas-agenticas.html' | relative_url }})
   - [6.2 Ataques sobre LLMs]({{ '/caso-2-ataques-llms.html' | relative_url }})
   - [6.3 Pentesting agéntico]({{ '/caso-3-pentesting-agentico.html' | relative_url }})
7. [Conclusiones]({{ '/conclusiones.html' | relative_url }})
8. [Bibliografía]({{ '/bibliografia.html' | relative_url }})
9. [Repositorio]({{ '/repositorio.html' | relative_url }})
10. [Vídeos del TFM](#videos)

## Servidor de inferencia del laboratorio

Todo el contenido del laboratorio se ha realizado sobre el siguiente **servidor de inferencia**, montado de forma explícita e íntegra para el TFM (AtomMan X7 Ti + GPU AMD RX 7900 XTX vía OCuLink).

![Servidor de inferencia del TFM]({{ '/assets/images/docx/image3.png' | relative_url }})
<p class="figcap">Servidor de inferencia local del laboratorio — Minisforum AtomMan X7 Ti y eGPU AMD Radeon RX 7900 XTX. Detalle en <a href="{{ '/montaje-lab.html' | relative_url }}">5. Montaje del laboratorio</a>.</p>

<div class="video-wrap">
<iframe src="https://www.youtube.com/embed/Op__mTqt7j0" title="Servidor de inferencia del TFM" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="figcap">Vídeo del servidor de inferencia — <a href="https://www.youtube.com/watch?v=Op__mTqt7j0">YouTube</a></p>

## Vídeos del TFM {#videos}

| Sección | Qué explica | Vídeo |
|---------|-------------|-------|
| Lab / HW | Presentación del servidor de inferencia local (AtomMan X7 Ti + RX 7900 XTX) | [YouTube](https://www.youtube.com/watch?v=Op__mTqt7j0) |
| 6.1.1 | Demo RCE / hacking sobre API de Ollama | [YouTube](https://www.youtube.com/watch?v=v46kJyIy9KQ) |
| 6.1.3 | A2A: DoS → spoofing → prompt injection → leak | [YouTube](https://www.youtube.com/watch?v=ldbxnRV__Ns) |
| 6.1.4 | Surface Auditor — auditoría y explotación de superficie agéntica | [YouTube](https://www.youtube.com/watch?v=k7eNc1mPccc) |
| 6.2 Reto 0 | Solución manual — Suelta la panoja (extracción de keyword / DCE) | [YouTube](https://youtu.be/MVx4puzXeXQ) |
| 6.2 Reto 1 | Solución manual — Solace AI (Direct Instruction Override) | [YouTube](https://youtu.be/S8NRqlIOBLo) |
| 6.2 Reto 2 | Solución manual — CorpConnect (Direct Tool Injection) | [YouTube](https://youtu.be/Xg3LWBjN3XU) |
| 6.2 Reto 3 | Solución manual — Trippy Planner (IIO / web envenenada) | [YouTube](https://youtu.be/1BitTyvV8ok) |
| 6.2 Reto 4 | Solución manual — Curs-ed CodeReview (IIO / `review.rules`) | [YouTube](https://youtu.be/6LPOqTywBEQ) |
| 6.2 Reto 5 | Solución manual — Clause AI (ITI / RAG + email) | [YouTube](https://youtu.be/cJQWC0yfsPE) |
| 6.2 Reto 6 | Solución manual — PortfolioIQ (IIO / PDF envenenado) | [YouTube](https://youtu.be/fq-UzqMJYxw) |
| 6.2 Reto 7 | Solución manual — MindfulChat (DAIS / memory poisoning) | [YouTube](https://youtu.be/hciiFZgGcoY) |
| 6.2 Reto 8 | Solución manual — Thingularity (DCE / tools y schema) | [YouTube](https://youtu.be/ODC4UNCrwSI) |
| 6.2 Reto 9 | Solución manual — OmniChat Desktop (ITI / MCP `notes`) | [YouTube](https://youtu.be/QhUsU6RxMNE) |
| 6.2 Reto 10 | Solución manual — Cycling Coach (DCE / system prompt) | [YouTube](https://youtu.be/h3hcaymoWDM) |
| 6.2.4 | Promptfoo — automatización / red team de los retos | [YouTube](https://youtu.be/WGViOPk3BY4) |
| 6.3.1 | MCP Kali Cline — wrapper Kali Linux vía MCP | [YouTube](https://www.youtube.com/watch?v=WqCFbNn0XlE) |
| 6.3.2 | Auditoría autónoma con CAI + LLM local | [YouTube](https://www.youtube.com/watch?v=iKfAk7cQ7o8) |
| 6.3.2 | Challenge PoC 24×7 BSCP PortSwigger — inicio de la orquestación | [YouTube](https://www.youtube.com/watch?v=RgUM4ZRogNE) |
