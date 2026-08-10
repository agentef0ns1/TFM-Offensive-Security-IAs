# Repositorio GitHub asociado

| Recurso | URL |
|---------|-----|
| **Repo** | <https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git> |
| **Web (GitHub Pages)** | <https://agentef0ns1.github.io/TFM-Offensive-Security-IAs/> |

### Vista previa web Jekyll en local

```bash
cd Entregable/TFM-Offensive-Security-IAs

# Primera vez
gem install bundler
bundle install

# Servidor con recarga automática
bundle exec jekyll serve --livereload
```

Abrir en el navegador:

- **Con baseurl de GitHub Pages:** <http://127.0.0.1:4000/TFM-Offensive-Security-IAs/>
- **Sin baseurl:** `bundle exec jekyll serve --livereload --baseurl ""` → <http://127.0.0.1:4000/>

### Despliegue

Push a la rama `main` con Pages configurado como **Deploy from a branch** → carpeta `/ (root)`.

---

[← Conclusiones](./conclusiones.md) · [Índice](./index.md) · [Bibliografía →](./bibliografia.md)
