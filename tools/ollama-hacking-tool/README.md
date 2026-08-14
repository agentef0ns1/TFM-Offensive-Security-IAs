# Ollama-hacking-tool

Panel web de **auditoría ofensiva** de la API REST de [Ollama](https://ollama.com) sin autenticación: reconocimiento, escaneo CVE, inyección (generate/chat/embeddings), payloads (pull/push/create/delete) y streaming SSE.

| Campo | Valor |
|-------|-------|
| **Caso TFM** | 6.1.1 — Motores LLM locales (Ollama) |
| **Repo** | [github.com/agentef0ns1/ollama-hacking-tools](https://github.com/agentef0ns1/ollama-hacking-tools) |
| **Árbol local** | `MASTER/Tools/Ollama-hacking-tool` |
| **Árbol Caso** | `Caso-1-Arquitecturas-Agenticas/6.1.1-Motores-LLM-locales/Ollama/` |

## Componentes clave

- `app.py` — Flask UI + API
- `ollama_client.py` — cliente REST/SSE
- `cve_catalog.py` — CVEs conocidos de Ollama
- `modelfile_builder.py` — conversión Modelfile/YAML → `/api/create`

## Inicio rápido

```bash
cd MASTER/Tools/Ollama-hacking-tool
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py          # http://127.0.0.1:8080
```

Demo: [YouTube](https://www.youtube.com/watch?v=v46kJyIy9KQ)

[← Tools](../README.md)
