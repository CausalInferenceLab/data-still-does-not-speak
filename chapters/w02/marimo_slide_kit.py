"""Small helpers for the marimo slide theme (theme/marimo-slides.css).

Only needed for: cover, 2-column layout, footer/page number, figures, tables, code blocks.
Plain `mo.md("# Title ...")` cells are styled by the CSS alone, no import required.

Depends on `marimo` only. Every sample number you pass in is your responsibility;
`fake_badge()` marks synthetic data on a slide.

Note: this is a local module, so `import marimo_slide_kit` works with
`marimo edit/run/export` from this folder but NOT in the WASM/Pyodide HTML export
(see docs/COMPATIBILITY.md).
"""
from __future__ import annotations

from html import escape
from typing import Iterable, Sequence

import marimo as mo

_footer_text = ""


def configure(footer: str = "") -> None:
    """Set the footer text used by slide() (call once in the setup cell)."""
    global _footer_text
    _footer_text = footer


def _html(part) -> str:
    """str -> markdown, marimo object -> its html, mo.Html -> as is."""
    if isinstance(part, str):
        return mo.md(part).text
    return mo.as_html(part).text


def _footer(page) -> str:
    if not _footer_text and page is None:
        return ""
    page_html = f'<span class="mt-page">{escape(str(page))}</span>' if page is not None else "<span></span>"
    return f'<div class="mt-footer"><span>{escape(_footer_text)}</span>{page_html}</div>'


def slide(*parts, page=None) -> mo.Html:
    """Body slide: markdown strings and/or marimo objects, plus footer and page number."""
    return mo.Html("".join(_html(p) for p in parts) + _footer(page))


def cover(title: str, subtitle: str = "", presenter: str = "", note: str = "") -> mo.Html:
    """Cover slide (peach/blue bands). `note` is a small line above the bottom band."""
    parts = [f'<h1 class="mt-cover-title">{escape(title)}</h1>']
    if subtitle:
        parts.append(f'<p class="mt-cover-sub">{escape(subtitle)}</p>')
    if presenter:
        parts.append(f'<p class="mt-cover-by">{escape(presenter)}</p>')
    if note:
        parts.append(f'<p class="mt-cover-note">{escape(note)}</p>')
    return mo.Html(f'<div class="mt-cover">{"".join(parts)}</div>')


def cols(*parts, ratio: Sequence[float] = (1, 1)) -> mo.Html:
    """Side-by-side columns; `ratio` like (1.2, 1). One part per ratio entry."""
    if len(parts) != len(ratio):
        raise ValueError(f"cols(): {len(parts)} parts but ratio has {len(ratio)} entries")
    tracks = " ".join(f"{r}fr" for r in ratio)
    body = "".join(f"<div>{_html(p)}</div>" for p in parts)
    return mo.Html(f'<div class="mt-cols" style="--mt-cols:{tracks}">{body}</div>')


def fake_badge(text: str = "가상 데이터 · 실제 분석 결과 아님") -> mo.Html:
    """Badge; put it above any synthetic figure/table."""
    return mo.Html(f'<div><span class="mt-fake">{escape(text)}</span></div>')


def note(text: str) -> mo.Html:
    return mo.Html(f'<p class="mt-note">{escape(text)}</p>')


def widget(element) -> mo.Html:
    """Wrap a mo.ui element so it keeps the slide's widget size."""
    return mo.Html(f'<div class="mt-widget">{mo.as_html(element).text}</div>')


def html_table(headers: Sequence[str], rows: Iterable[Sequence], numeric_cols: Sequence[int] = ()) -> mo.Html:
    """Static table (no pandas/polars). Numeric columns are right-aligned."""
    num = set(numeric_cols)
    head = "".join(f'<th class="{"mt-num" if i in num else ""}">{escape(str(h))}</th>' for i, h in enumerate(headers))
    body = "".join(
        "<tr>" + "".join(f'<td class="{"mt-num" if i in num else ""}">{escape(str(c))}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    return mo.Html(f'<table class="mt-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>')


def code_block(source: str) -> mo.Html:
    """Plain (not syntax-highlighted) code block; scrolls inside the block when long."""
    return mo.Html(f'<pre class="mt-code"><code>{escape(source.strip(chr(10)))}</code></pre>')


def bar_figure(labels: Sequence[str], values: Sequence[float], *, vmax: float | None = None,
               width: int = 560, bar_h: int = 44, highlight: int | None = None, unit: str = "") -> mo.Html:
    """Horizontal bar chart as inline SVG (no plotting library).

    `width` is in 1280-canvas px (the whole slide scales together). For Altair/Vega charts do the same:
    give an explicit pixel `.properties(width=..., height=...)`, never width="container".
    """
    vmax = vmax or max(values) or 1
    label_w, val_w, gap = 90, 70, 14
    track = width - label_w - val_w
    h = len(values) * (bar_h + gap)
    rows = []
    for i, (lab, v) in enumerate(zip(labels, values)):
        y = i * (bar_h + gap)
        w = max(0.0, min(1.0, v / vmax)) * track
        cls = "mt-bar-b" if (highlight == i) else "mt-bar-a"
        rows.append(
            f'<text class="mt-svg-text" x="0" y="{y + bar_h * 0.68:.1f}" font-size="22" font-weight="700">{escape(str(lab))}</text>'
            f'<rect class="mt-bar-track" x="{label_w}" y="{y}" width="{track}" height="{bar_h}"/>'
            f'<rect class="{cls}" x="{label_w}" y="{y}" width="{w:.1f}" height="{bar_h}"/>'
            f'<text class="mt-svg-text" x="{label_w + track + 10}" y="{y + bar_h * 0.68:.1f}" font-size="22">{escape(f"{v:g}{unit}")}</text>'
        )
    svg = f'<svg viewBox="0 0 {width} {h}" width="{width}" height="{h}" role="img">{"".join(rows)}</svg>'
    return mo.Html(f'<div class="mt-figure">{svg}</div>')
