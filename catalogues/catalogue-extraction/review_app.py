"""
Review app for catalogue-ocr-llm-extraction.ipynb: the catalogue page with each
extracted value boxed on the left, the extracted entry on the right. Entries can be
edited, added and deleted, and the corrected CSV downloaded. No OCR or LLM runs here.

From the command line (needs: pip install gradio pandas pillow):

    python review_app.py path/to/<catalogue>-output             # a notebook output folder
    python review_app.py path/to/<catalogue>-output --pdf path/to/catalogue.pdf
    python review_app.py                                         # the Baldessari demo
    python review_app.py ... --share                             # also print a public link (72 h)

or from the last section of the notebook. Page images come from the output folder's
pages/ subfolder; if they aren't there, they are rendered from the PDF (needs pdftoppm).
Set REVIEW_APP_PASSWORD to require a login (user "demo").
"""
import argparse
import difflib
import html
import os
import re
import subprocess
import tempfile
from functools import lru_cache
from pathlib import Path

import gradio as gr
import pandas as pd
from PIL import Image

# The Baldessari demo, used when no output folder is given
DEMO = {
    "csv":   Path(__file__).parent / "demo" / "baldessari-sprengel-artworks.csv",
    "hocr":  Path.home() / "projects/datasets/stray_TIB/baldessari-sprengel.hocr",
    "pages": Path.home() / "projects/datasets/stray_TIB/baldessari-sprengel_pages",
    "pdf":   Path.home() / "projects/datasets/stray_TIB/baldessari-sprengel.pdf",
}
SRC = {}       # the catalogue being reviewed: csv, hocr, pages, pdf (set by configure)
HOCR = {}      # page number -> {"image", "size", "words"}

DISPLAY_WIDTH = 2200      # page images are scaled down to this width

# Fields located on the page, with their legend colours
FIELD_COLORS = {
    "artwork_title":     "#e6194b",
    "catalogue_no":      "#3cb44b",
    "artwork_inception": "#4363d8",
    "medium_material":   "#f58231",
    "height_cm":         "#911eb4",
    "width_cm":          "#911eb4",
    "depth_cm":          "#911eb4",
    "collection":        "#008080",
    "inventory_number":  "#9a6324",
    "artist_full_name":  "#808000",
}


# ── hOCR: words and their boxes per page ─────────────────────────────────────
def norm(s):
    return re.sub(r"[^0-9a-zà-ÿß.]+", "", str(s).lower().replace(",", "."))


def load_hocr(path):
    """{page number: {"image": file name, "size": (w, h), "words": [(text, norm, bbox)]}}"""
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    pages = {}
    for n, chunk in enumerate(re.split(r"<div class=.ocr_page.", text)[1:], start=1):
        image = re.search(r'image &quot;([^&]+)&quot;|image "([^"]+)"', chunk)
        size = re.search(r"bbox 0 0 (\d+) (\d+)", chunk)
        words = []
        for x0, y0, x1, y1, inner in re.findall(
                r"<span class=.ocrx_word.[^>]*?title=.bbox (\d+) (\d+) (\d+) (\d+)[^>]*>(.*?)</span>", chunk, re.S):
            w = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
            if w:
                words.append((w, norm(w), (int(x0), int(y0), int(x1), int(y1))))
        name = Path((image.group(1) or image.group(2))).name if image else f"page-{n:02d}.png"
        pages[n] = {"image": name, "size": (int(size.group(1)), int(size.group(2))) if size else None,
                    "words": words}
    return pages


def configure(output_dir=None, pdf=None):
    """Points the app at a notebook output folder (or the Baldessari demo if None)."""
    if output_dir is None:
        src = dict(DEMO)
    else:
        out = Path(output_dir).expanduser().resolve()
        csvs = [c for c in out.glob("*-artworks.csv") if not c.name.endswith("-reviewed.csv")]
        if len(csvs) != 1:
            raise FileNotFoundError(f"Expected one <name>-artworks.csv in {out}, found {len(csvs)}")
        stem = csvs[0].name[: -len("-artworks.csv")]
        src = {"csv": csvs[0], "hocr": out / f"{stem}.hocr", "pages": out / "pages", "pdf": None}
    if pdf:
        src["pdf"] = Path(pdf).expanduser().resolve()
    if not src["hocr"].exists():
        raise FileNotFoundError(f"hOCR file not found: {src['hocr']}")
    SRC.clear()
    SRC.update(src)
    HOCR.clear()
    HOCR.update(load_hocr(src["hocr"]))
    page_image.cache_clear()


def union(boxes):
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))


def centre(b):
    return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)


def candidates(value, words):
    """(score, bbox) for every place `value` could be printed on the page."""
    tokens = [norm(t) for t in str(value).split() if norm(t)]
    if not tokens:
        return []
    target = " ".join(tokens)
    out = []
    if len(tokens) == 1 and len(target) <= 6:          # short value (year, number): exact token match
        pat = re.compile(rf"(?<![0-9a-z]){re.escape(target)}(?![0-9a-z])")
        out = [(1.0, bbox) for _, wn, bbox in words if pat.search(wn)]
        return out
    n = len(tokens)
    for size in {max(1, n - 1), n, n + 1}:
        for i in range(len(words) - size + 1):
            window = words[i:i + size]
            score = difflib.SequenceMatcher(None, target, " ".join(w[1] for w in window)).ratio()
            if score >= 0.75:
                out.append((score, union([w[2] for w in window])))
    return out


def best(cands, anchor, page_w):
    """Best-scoring candidate, preferring ones near `anchor` (the title)."""
    if not cands:
        return None
    if anchor is None:
        return max(cands)[1]
    ax, ay = centre(anchor)
    def dist(b):
        x, y = centre(b)
        return ((x - ax) ** 2 + (y - ay) ** 2) ** 0.5
    near = [c for c in cands if dist(c[1]) < 0.3 * page_w]
    if not near:
        return None
    top = max(s for s, _ in near)
    return min((c for c in near if c[0] >= top - 0.05), key=lambda c: dist(c[1]))[1]


def locate(entry, page):
    """[(bbox, field)] for the fields of `entry` found on `page`."""
    words = HOCR[page]["words"]
    page_w = max((w[2][2] for w in words), default=1)
    found = []
    title_box = best(candidates(entry.get("artwork_title", ""), words), None, page_w)
    if title_box:
        found.append((title_box, "artwork_title"))
    for field in FIELD_COLORS:
        if field == "artwork_title":
            continue
        value = str(entry.get(field, "") or "").strip()
        if not value:
            continue
        parts = [p for p in re.split(r"\s*;\s*", value) if p] if field == "medium_material" else [value]
        used = {b for b, _ in found}
        for part in parts:   # skip boxes already taken (e.g. height and width are the same number)
            box = best([c for c in candidates(part, words) if c[1] not in used], title_box, page_w)
            if box:
                found.append((box, field))
    return found


def page_file(n):
    """Image file for PDF page n: from the pages folder, else rendered from the PDF."""
    pages = SRC["pages"]
    named = pages / HOCR[n]["image"]
    if named.exists():
        return named
    pattern = re.compile(rf"page-0*{n}\.png$")
    found = [f for f in pages.glob("page-*.png") if pattern.search(f.name)] if pages.exists() else []
    if found:
        return found[0]
    if SRC.get("pdf") and SRC["pdf"].exists():
        pages.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftoppm", "-f", str(n), "-l", str(n), "-r", "150", "-png", str(SRC["pdf"]),
                        str(pages / "page")], check=True)
        found = [f for f in pages.glob("page-*.png") if pattern.search(f.name)]
        if found:
            return found[0]
    return None


@lru_cache(maxsize=16)
def page_image(n):
    """(image, scale) with the image sized so that hOCR coordinates x scale = pixels."""
    path = page_file(n)
    if path is None:
        return None, 1.0
    im = Image.open(path).convert("RGB")
    w, h = HOCR[n]["size"] or im.size
    scale = min(1.0, DISPLAY_WIDTH / w)
    return im.resize((round(w * scale), round(h * scale))), scale


def annotated(entry):
    try:
        page = int(float(entry.get("source_page") or 0))
    except ValueError:
        page = 0
    if page not in HOCR:
        return None, "**Source page not found** for this entry: no page to show."
    im, scale = page_image(page)
    if im is None:
        return None, (f"PDF page {page}: **page image not found.** Put the page images in {SRC['pages']}, "
                      "or start the app with the catalogue PDF (--pdf) so they can be rendered.")
    boxes = [(tuple(round(c * scale) for c in b), f) for b, f in locate(entry, page)]
    if im.width > im.height and boxes:      # double-page spread: show only the half the entry is on
        title = next((b for b, f in boxes if f == "artwork_title"), boxes[0][0])
        x0 = 0 if centre(title)[0] < im.width / 2 else im.width // 2
        im = im.crop((x0, 0, x0 + im.width // 2, im.height))
        boxes = [((b[0] - x0, b[1], b[2] - x0, b[3]), f) for b, f in boxes if b[0] >= x0 and b[2] <= x0 + im.width]
    pad = 4
    boxes = [((b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad), f) for b, f in boxes]
    missing = [f for f in FIELD_COLORS if str(entry.get(f, "") or "").strip() and f not in {f for _, f in boxes}]
    note = f"PDF page {page}." + (f" Not found on the page: {', '.join(missing)}." if missing else "")
    return (im, boxes), note


# ── Data ─────────────────────────────────────────────────────────────────────
def load_csv():
    return pd.read_csv(SRC["csv"], dtype=str, keep_default_na=False)


def label(i, row):
    flag = " [?]" if row["notes"].startswith("[?]") else ""
    return f"{i + 1:>3}. p.{row['source_page'] or '?'} · {row['artwork_title'][:60]}{flag}"


def choices(df):
    return [(label(i, r), i) for i, r in df.iterrows()]


# Form layout: (section, heading, rows of (column, label, width))
SECTIONS = [
    ("ocr", "From the catalogue page", "OCR + LLM", [
        [("artwork_title", "Title", 1)],
        [("catalogue_no", "Cat. no.", 1), ("artwork_inception", "Date", 1),
         ("artwork_type", "Type", 1), ("artwork_title_lang", "Title lang.", 1)],
        [("medium_material", "Materials", 1)],
        [("height_cm", "Height cm", 1), ("width_cm", "Width cm", 1),
         ("depth_cm", "Depth cm", 1), ("inventory_number", "Inv. no.", 1)],
        [("collection", "Lender / collection", 1)],
    ]),
    ("pipeline", "Added by the notebook", "pipeline", [
        [("source_page", "PDF page", 1), ("notes", "Review notes", 4)],
    ]),
    ("wiki", "Artist details", "Wikidata", [
        [("artist_given_name", "Given name", 1), ("artist_family_name", "Family name", 1),
         ("artist_birth_year", "Born", 1), ("artist_death_year", "Died", 1)],
        [("artist_nationality", "Nationality", 1), ("artist_profession", "Profession", 2)],
        [("artist_gnd_id", "GND", 1), ("artist_ulan_id", "ULAN", 1)],
    ]),
    ("param", "Artist and exhibition (same on every row)", "notebook parameters", [
        [("artist_full_name", "Artist", 2), ("artist_wikidata_qid", "Artist QID", 1)],
        [("exhibition_title", "Exhibition", 1)],
        [("exhibition_location", "Venue", 2), ("exhibition_start", "Start", 1), ("exhibition_end", "End", 1)],
        [("exhibition_organizer", "Organiser", 2), ("exhibition_wikidata_qid", "Exhibition QID", 1)],
    ]),
]
FORM_FIELDS = [f for _, _, _, rows in SECTIONS for row in rows for f, _, _ in row]
SOURCE_COLORS = {"ocr": "#c2410c", "pipeline": "#6b7280", "wiki": "#2563eb", "param": "#6b7280"}


def show(df, i):
    i = int(i)
    image, note = annotated(df.loc[i].to_dict())
    return [image, note] + [df.at[i, f] if f in df.columns else "" for f in FORM_FIELDS]


def publish(df, i, changes, message):
    """Writes the CSV for download and refreshes the whole UI on entry i."""
    df = df.reset_index(drop=True)
    name = SRC["csv"].name.replace("-artworks.csv", "-artworks-reviewed.csv")
    out_file = Path(tempfile.mkdtemp()) / name   # a new file per save, so viewers never share one
    df.to_csv(out_file, index=False)
    changes = changes + [message]
    status = f"{message} · {len(changes)} change{'s' if len(changes) > 1 else ''} so far · {len(df)} entries"
    return [df, changes, gr.update(choices=choices(df), value=i), status, gr.update(value=str(out_file))] + show(df, i)


def save(df, i, changes, *values):
    i = int(i)
    df = df.copy()
    for field, value in zip(FORM_FIELDS, values):
        if field in df.columns:
            df.at[i, field] = "" if value is None else str(value)
    return publish(df, i, changes, f"Saved entry {i + 1}")


def add_entry(df, i, changes):
    """Inserts a blank entry after entry i, keeping its page, artist and exhibition fields."""
    i = int(i)
    new = {c: "" for c in df.columns}
    for c in df.columns:
        if c.startswith(("artist_", "exhibition_")) or c == "source_page":
            new[c] = df.at[i, c]
    new["notes"] = "added in review"
    df = pd.concat([df.iloc[:i + 1], pd.DataFrame([new]), df.iloc[i + 1:]], ignore_index=True)
    return publish(df, i + 1, changes, f"Added entry {i + 2}: fill it in, then Save entry")


def delete_entry(df, i, changes):
    i = int(i)
    if len(df) == 1:
        return publish(df, 0, changes, "Can't delete the last entry")
    title = df.at[i, "artwork_title"] or "(untitled)"
    df = df.drop(index=i)
    return publish(df, min(i, len(df) - 1), changes, f"Deleted entry {i + 1}: {title[:50]}")


def step(df, i, delta):
    return max(0, min(len(df) - 1, int(i) + delta))


# ── UI ───────────────────────────────────────────────────────────────────────
CSS = """
.gradio-container {max-width: 100% !important}
.fld {padding: 0 !important; min-width: 70px !important}
.fld textarea, .fld input {padding: 3px 7px !important; font-size: 0.88em !important; min-height: 0 !important}
.fld span[data-testid="block-info"] {font-size: 0.72em !important; margin-bottom: 1px !important}
.form-row {gap: 6px !important; margin-bottom: 2px !important}
.src-wiki textarea {background: #eff6ff !important}
.src-param textarea, .src-pipeline textarea {background: #f3f4f6 !important}
.section-head {margin: 4px 0 0 0 !important; padding: 0 !important}
.section-head p {font-size: 0.85em !important; margin: 0 !important}
""" + "\n".join(f".fld-{f} textarea {{border-left: 5px solid {c} !important}}" for f, c in FIELD_COLORS.items())


def badge(text, color):
    return (f"<span style='background:{color};color:white;padding:1px 7px;border-radius:9px;"
            f"font-size:0.85em;margin-left:6px'>{text}</span>")


def build_app():
    with gr.Blocks(title="Catalogue review") as demo:
        df0 = load_csv()
        data = gr.State(df0)
        changes = gr.State([])
        first = df0.iloc[0] if len(df0) else {}
        what = ", ".join(v for v in (first.get("exhibition_title", ""), first.get("exhibition_location", "")) if v)

        gr.Markdown(f"### Catalogue review: *{what or SRC['csv'].name}*  \n"
                    "<small>Coloured boxes on the page match the coloured edges of the fields. "
                    "Edit, <b>Save entry</b>, then download the CSV. [?] = flagged for review.</small>")
        with gr.Row(equal_height=True):
            prev_btn = gr.Button("◀", scale=0, min_width=50)
            picker = gr.Dropdown(choices=choices(df0), value=0, show_label=False, scale=6, container=False)
            next_btn = gr.Button("▶", scale=0, min_width=50)
            save_btn = gr.Button("Save entry", variant="primary", scale=1)
            add_btn = gr.Button("＋ Add entry", scale=1)
            delete_btn = gr.Button("✕ Delete entry", variant="stop", scale=1)
            download = gr.DownloadButton("Download CSV", value=None, scale=1)
        with gr.Row(visible=False) as confirm_row:
            gr.Markdown("**Delete this entry?** It is removed from the CSV.")
            confirm_btn = gr.Button("Yes, delete", variant="stop", scale=0, min_width=120)
            cancel_btn = gr.Button("Cancel", scale=0, min_width=100)
        status = gr.Markdown()

        boxes = {}
        with gr.Row():
            with gr.Column(scale=3):
                page = gr.AnnotatedImage(show_label=False, color_map=FIELD_COLORS, show_legend=False, height=800)
                page_note = gr.Markdown()
            with gr.Column(scale=2):
                for key, heading, source, rows in SECTIONS:
                    if key == "param":    # the same on every row: collapsed to save space
                        container = gr.Accordion(f"{heading} · from {source}", open=False)
                    else:
                        gr.HTML(f"<b>{heading}</b>{badge(source, SOURCE_COLORS[key])}", elem_classes=["section-head"])
                        container = gr.Group()
                    with container:
                        for row in rows:
                            with gr.Row(elem_classes=["form-row"]):
                                for field, lab, width in row:
                                    boxes[field] = gr.Textbox(
                                        label=lab, lines=1, max_lines=3, scale=width, min_width=70,
                                        elem_classes=["fld", f"fld-{field}", f"src-{key}"])

        form = [boxes[f] for f in FORM_FIELDS]
        picker.change(show, [data, picker], [page, page_note] + form)
        prev_btn.click(lambda d, i: step(d, i, -1), [data, picker], picker)
        next_btn.click(lambda d, i: step(d, i, 1), [data, picker], picker)
        outputs = [data, changes, picker, status, download, page, page_note] + form
        save_btn.click(save, [data, picker, changes] + form, outputs)
        add_btn.click(add_entry, [data, picker, changes], outputs)
        delete_btn.click(lambda: gr.update(visible=True), None, confirm_row)
        cancel_btn.click(lambda: gr.update(visible=False), None, confirm_row)
        confirm_btn.click(delete_entry, [data, picker, changes], outputs).then(
            lambda: gr.update(visible=False), None, confirm_row)
        demo.load(show, [data, picker], [page, page_note] + form)
    return demo


def launch(output_dir=None, pdf=None, share=False, **kwargs):
    """Builds and starts the app. In Jupyter it appears below the cell."""
    configure(output_dir, pdf)
    password = os.environ.get("REVIEW_APP_PASSWORD")
    return build_app().launch(share=share, auth=("demo", password) if password else None, css=CSS, **kwargs)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Review the output of catalogue-ocr-llm-extraction.ipynb")
    ap.add_argument("output_dir", nargs="?", help="notebook output folder (default: the Baldessari demo)")
    ap.add_argument("--pdf", help="catalogue PDF, used to render page images that aren't in pages/")
    ap.add_argument("--share", action="store_true", help="also create a public share link (72 h)")
    args = ap.parse_args()
    launch(args.output_dir, args.pdf, share=args.share)
