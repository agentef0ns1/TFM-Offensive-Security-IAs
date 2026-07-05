#!/usr/bin/env python3
"""Genera diagramas de arquitectura para los sub-casos 6.1.a, 6.1.b y 6.1.c."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "images"
W, H = 1200, 720

# Colores (estilo técnico legible en web y memoria)
BG = (248, 250, 252)
BORDER = (30, 41, 59)
BOX_FILL = (255, 255, 255)
BOX_BORDER = (14, 116, 144)
ACCENT = (8, 145, 178)
TEXT = (15, 23, 42)
SUBTEXT = (71, 85, 105)
ARROW = (51, 65, 85)
ENV_FILL = (236, 254, 255)
ENV_BORDER = (8, 145, 178)
EXTERNAL_FILL = (254, 243, 199)
EXTERNAL_BORDER = (217, 119, 6)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], label: str = "") -> None:
    draw.line([start, end], fill=ARROW, width=3)
    ex, ey = end
    sx, sy = start
    if abs(ex - sx) >= abs(ey - sy):
        tip = 12 if ex > sx else -12
        draw.polygon([(ex, ey), (ex - tip, ey - 7), (ex - tip, ey + 7)], fill=ARROW)
    else:
        tip = 12 if ey > sy else -12
        draw.polygon([(ex, ey), (ex - 7, ey - tip), (ex + 7, ey - tip)], fill=ARROW)
    if label:
        mx, my = (sx + ex) // 2, (sy + ey) // 2
        draw.text((mx - 40, my - 22), label, fill=SUBTEXT, font=font(16))


def draw_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    subtitle: str = "",
    fill: tuple[int, int, int] = BOX_FILL,
    border: tuple[int, int, int] = BOX_BORDER,
) -> None:
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=border, width=2)
    tw = draw.textlength(title, font=font(22, bold=True))
    draw.text(((x1 + x2 - tw) / 2, y1 + 18), title, fill=TEXT, font=font(22, bold=True))
    if subtitle:
        sw = draw.textlength(subtitle, font=font(16))
        draw.text(((x1 + x2 - sw) / 2, y1 + 52), subtitle, fill=SUBTEXT, font=font(16))


def draw_env(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], label: str) -> None:
    draw.rounded_rectangle(xy, radius=18, fill=ENV_FILL, outline=ENV_BORDER, width=2)
    draw.text((xy[0] + 16, xy[1] + 12), label, fill=ACCENT, font=font(18, bold=True))


def new_canvas(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.text((40, 28), title, fill=TEXT, font=font(28, bold=True))
    draw.text((40, 68), subtitle, fill=SUBTEXT, font=font(18))
    draw.line([(40, 100), (W - 40, 100)], fill=BORDER, width=1)
    return img, draw


def save(img: Image.Image, name: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    img.save(path, "PNG", optimize=True)
    return path


def diagram_mcp() -> Path:
    img, draw = new_canvas(
        "6.1.a — Arquitectura agéntica: Model Context Protocol (MCP)",
        "Entorno local: LLM, agente orquestador y servidor MCP (consultas a Internet)",
    )
    draw_env(draw, (60, 130, W - 60, H - 60), "Entorno local (host / laboratorio)")

    draw_box(draw, (120, 220, 340, 320), "Modelo LLM", "Ollama / GGUF")
    draw_box(draw, (480, 220, 720, 320), "Agente", "Orquestador + tool calling")
    draw_box(draw, (860, 220, 1100, 320), "Servidor MCP", "Tool: búsqueda web")

    draw_arrow(draw, (340, 270), (480, 270), "inferencia")
    draw_arrow(draw, (720, 270), (860, 270), "MCP / JSON-RPC")

    draw_box(draw, (860, 420, 1100, 500), "Internet", "Consultas externas", EXTERNAL_FILL, EXTERNAL_BORDER)
    draw_arrow(draw, (980, 320), (980, 420), "HTTP")

    draw.text((120, 560), "Flujo: el agente razona con el LLM local y delega consultas externas al servidor MCP.", fill=SUBTEXT, font=font(16))
    return save(img, "arquitectura-6-1a-mcp.png")


def diagram_llm_web() -> Path:
    img, draw = new_canvas(
        "6.1.b — Arquitectura agéntica: motor LLM local (Ollama / vLLM)",
        "Entorno local: motor de inferencia, agente y interfaz web",
    )
    draw_env(draw, (60, 130, W - 60, H - 60), "Entorno local (host / laboratorio)")

    draw_box(draw, (120, 260, 360, 360), "Motor LLM", "Ollama / vLLM + modelo")
    draw_box(draw, (470, 260, 730, 360), "Agente", "Lógica + memoria + tools")
    draw_box(draw, (840, 260, 1100, 360), "Web local", "Open WebUI / UI propia")

    draw_arrow(draw, (360, 310), (470, 310), "API local")
    draw_arrow(draw, (730, 310), (840, 310), "REST / WS")

    draw.text(
        (120, 520),
        "Flujo: la web local envía peticiones al agente; el agente invoca el motor LLM para generar respuestas.",
        fill=SUBTEXT,
        font=font(16),
    )
    return save(img, "arquitectura-6-1b-llm-web.png")


def diagram_a2a() -> Path:
    img, draw = new_canvas(
        "6.1.c — Arquitectura agéntica: Agent-to-Agent (A2A)",
        "Entorno local: dos agentes con LLMs distintos comunicados por protocolo A2A",
    )
    draw_env(draw, (60, 130, W - 60, H - 60), "Entorno local (host / laboratorio)")

    draw_box(draw, (100, 240, 320, 340), "LLM A", "Modelo local A")
    draw_box(draw, (100, 380, 320, 480), "Agente A", "Especialista / rol A")

    draw_box(draw, (880, 240, 1100, 340), "LLM B", "Modelo local B")
    draw_box(draw, (880, 380, 1100, 480), "Agente B", "Especialista / rol B")

    draw_arrow(draw, (210, 340), (210, 380))
    draw_arrow(draw, (990, 340), (990, 380))

    draw.rounded_rectangle((430, 390, 770, 470), radius=14, fill=(224, 242, 254), outline=ACCENT, width=2)
    draw.text((470, 408), "Comunicación A2A", fill=TEXT, font=font(22, bold=True))
    draw.text((455, 442), "Mensajes / tareas / delegación", fill=SUBTEXT, font=font(16))

    draw_arrow(draw, (320, 430), (430, 430), "A2A")
    draw_arrow(draw, (770, 430), (880, 430), "A2A")

    draw.text(
        (120, 560),
        "Flujo: cada agente usa su propio LLM; la coordinación multiagente se realiza mediante el protocolo A2A.",
        fill=SUBTEXT,
        font=font(16),
    )
    return save(img, "arquitectura-6-1c-a2a.png")


if __name__ == "__main__":
    paths = [diagram_mcp(), diagram_llm_web(), diagram_a2a()]
    for p in paths:
        print(p)
