**Trabajo Fin de Máster — MCAIS2** · **Autor:** Ildefonso González Sánchez

<p><span class="pill">v1.0</span> <span class="pill">MCAIS2</span> <span class="pill">lab local</span> <span class="pill">ofensivo</span></p>

Ciberseguridad **ofensiva** aplicada a sistemas de IA agénticos: motores locales, MCP, A2A, superficie del agente, CTFs B³ y pentesting asistido/autónomo.

<div class="callout">

Fuente canónica: `TFM-Offensive-Security-IAs_v1.0.docx`. Esta web reproduce el contenido del documento con código, capturas, repositorios y demos en vídeo.

</div>

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

## Servidor de inferencia del laboratorio

Todo el contenido del laboratorio se ha realizado sobre el siguiente **servidor de inferencia**, montado de forma explícita e íntegra para el TFM (AtomMan X7 Ti + GPU AMD RX 7900 XTX vía OCuLink).

![Servidor de inferencia del TFM]({{ '/assets/images/docx/image3.png' | relative_url }})
<p class="figcap">Servidor de inferencia local del laboratorio — Minisforum AtomMan X7 Ti y eGPU AMD Radeon RX 7900 XTX. Detalle en <a href="{{ '/montaje-lab.html' | relative_url }}">§5 Montaje del laboratorio</a>.</p>

<div class="video-wrap">
<iframe src="https://www.youtube.com/embed/Op__mTqt7j0" title="Servidor de inferencia del TFM" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="figcap">Vídeo del servidor de inferencia — <a href="https://www.youtube.com/watch?v=Op__mTqt7j0">YouTube</a></p>
