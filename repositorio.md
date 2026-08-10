# Repositorio GitHub asociado

## Índice {#indice}

  - [Vista previa Jekyll en local](#vista-previa-jekyll-en-local)
  - [Despliegue](#despliegue)

---
| Recurso | URL |
|---------|-----|
| **Repo** | <https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git> |
| **Web** | <https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/> |

### Vista previa Jekyll en local

```bash
cd Entregable/TFM-Offensive-Security-IAs
gem install bundler   # primera vez
bundle install
bundle exec jekyll serve --livereload
```

- Con baseurl: <http://127.0.0.1:4000/TFM-Offensive-Security-IAs/>
- Sin baseurl: `bundle exec jekyll serve --livereload --baseurl ""` → <http://127.0.0.1:4000/>

### Despliegue

GitHub Pages → branch `main` → folder `/ (root)`.

---
<p class="nav-footer"><a href="{{ '/bibliografia.html' | relative_url }}">← Bibliografía</a> · <a href="{{ '/' | relative_url }}">Índice</a></p>

