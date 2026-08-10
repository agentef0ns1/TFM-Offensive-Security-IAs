# TFM — Offensive Security in AI Systems

**Título:** Estudio de vulnerabilidades y protocolos de seguridad en sistemas de inteligencia artificial agénticos

**Programa:** Máster de Inteligencia Artificial orientado a Ciberseguridad — 2.ª edición (MCAIS2)

**Autor:** Ildefonso González Sánchez

**Web:** [https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/](https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/)

---

## Contenido

Sitio Jekyll (tema `jekyll-theme-hacker`) con la memoria del TFM **segmentada por capítulos**, lista para GitHub Pages.

| Página | Contenido |
|--------|-----------|
| [`index.md`](index.md) | Portada e índice |
| [`introduccion.md`](introduccion.md) … [`bibliografia.md`](bibliografia.md) | Capítulos 1–7 + bibliografía |
| [`caso-1|2|3-*.md`](caso-1-arquitecturas-agenticas.md) | Casos de estudio (§6) |
| [`herramientas.md`](herramientas.md) | Catálogo de tools |
| [`tools/`](tools/), [`lab/`](lab/), [`informes/`](informes/) | Fichas e índices (visibles en GitHub; excluidos del build Jekyll) |
| [`assets/images/docx/`](assets/images/docx/) | Figuras exportadas del Word |

**Fuente de sincronización:** `../TFM-Offensive-Security-IAs.docx`

## Despliegue (GitHub Pages)

1. **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main` · **Folder:** `/ (root)`

Push a `main` publica en `https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/`.

## Vista previa local

```bash
bundle install
bundle exec jekyll serve --livereload
# → http://127.0.0.1:4000/TFM-Offensive-Security-IAs/
```

Sin baseurl:

```bash
bundle exec jekyll serve --livereload --baseurl ""
```

## Licencia

CC0 1.0 Universal — ver [LICENSE](LICENSE).
