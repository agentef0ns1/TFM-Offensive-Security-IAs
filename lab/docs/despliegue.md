# Guía de despliegue del laboratorio

## 1. Requisitos previos

- Linux (recomendado) con Docker 24+ y Docker Compose v2
- 16 GB RAM mínimo recomendado
- Red aislada del entorno de producción

## 2. Clonar el repositorio

```bash
git clone https://github.com/agentef0ns1/TFM-Offensive-Security-IAs.git
cd TFM-Offensive-Security-IAs
```

## 3. Configurar variables de entorno

```bash
cp tools/mcp-server/.env.example tools/mcp-server/.env
# Editar según el entorno local
```

## 4. Levantar servicios

```bash
cd lab
docker compose up -d
```

## 5. Verificación

```bash
./tools/scripts/verify-lab.sh   # cuando esté disponible
```

---

*Guía en desarrollo. Se completará con la implementación del laboratorio.*

[← Lab](../README.md)
