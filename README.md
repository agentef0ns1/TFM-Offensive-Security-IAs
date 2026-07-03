# TFM — Offensive Security in AI Systems

**Título:** Estudio de vulnerabilidades y protocolos de seguridad en sistemas de inteligencia artificial agénticos

**Programa:** Máster de Inteligencia Artificial orientado a Ciberseguridad — 2.ª edición (MCAIS2)

**Autor:** Ildefonso González Sánchez

**Web publicada:** [https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/](https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/)

---

## Estructura del repositorio

| Directorio / raíz | Contenido |
|-------------------|-----------|
| Raíz (`*.md`, `_layouts/`, `assets/`) | **Web** — sitio Jekyll (GitHub Pages) con la memoria del TFM |
| [`tools/`](tools/) | **Tools** — código fuente: agente autónomo, servidor MCP, scripts |
| [`lab/`](lab/) | **Lab** — laboratorio reproducible: Docker, CTFs y guías de despliegue |
| [`informes/`](informes/) | Informes técnicos de los casos de estudio |

## GitHub Pages

1. Ir a **Settings → Pages**.
2. **Source:** Deploy from a branch.
3. **Branch:** `main` / **Folder:** `/ (root)`.
4. Guardar. La web quedará disponible en unos minutos.

## Desarrollo local de la web

```bash
bundle install
bundle exec jekyll serve
```

Abrir [http://localhost:4000/TFM-Offensive-Security-IAs/](http://localhost:4000/TFM-Offensive-Security-IAs/)

## Licencia

CC0 1.0 Universal — ver [LICENSE](LICENSE).
