import csv, xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path

CSV = Path("catalogues/scan-2/output-plan-b-readable.csv")
XML = Path("catalogues/scan-2/catalogue-items.xml")

def sub(parent, tag, text=""):
    el = ET.SubElement(parent, tag)
    el.text = (text or "").strip()
    return el

root = ET.Element("catalogue")

meta = ET.SubElement(root, "meta")
sub(meta, "exhibition_title", "John Baldessari at Sprengel Museum Hannover")
sub(meta, "venue",            "Sprengel Museum Hannover")
sub(meta, "venue_qid",        "Q510144")
sub(meta, "creator_name",     "John Baldessari")
sub(meta, "creator_qid",      "Q312793")
sub(meta, "source_file",      CSV.name)

items_el = ET.SubElement(root, "items")

with open(CSV, newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        item = ET.SubElement(items_el, "item")
        sub(item, "title",           row.get("title",""))
        sub(item, "creator",         row.get("creator",""))
        sub(item, "creator_qid",     row.get("creator_qid",""))
        sub(item, "date",            row.get("date",""))
        sub(item, "object_type",     row.get("object_type",""))
        sub(item, "object_type_qid", row.get("object_type_qid",""))
        sub(item, "materials",       row.get("materials",""))
        sub(item, "materials_qids",  row.get("materials_qids",""))
        dim = ET.SubElement(item, "dimensions")
        sub(dim, "height_cm", row.get("height_cm",""))
        sub(dim, "width_cm",  row.get("width_cm",""))
        sub(dim, "depth_cm",  row.get("depth_cm",""))
        sub(item, "inventory_number", row.get("inventory_number",""))
        sub(item, "catalog_number",   row.get("catalog_number",""))
        sub(item, "location",         row.get("location",""))
        # CSV "exhibited_at" column holds the QID; use "location" column for the label
        exhibited_label = row.get("location","").strip()
        exhibited_qid   = row.get("exhibited_at","").strip()
        sub(item, "exhibited_at",     exhibited_label)
        sub(item, "exhibited_at_qid", exhibited_qid)
        sub(item, "notes",            row.get("notes",""))

xml_str = minidom.parseString(ET.tostring(root, encoding="unicode")).toprettyxml(indent="  ")
body = "\n".join(xml_str.split("\n")[1:])
header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE catalogue SYSTEM "catalogue-items.dtd">\n'
XML.write_text(header + body, encoding="utf-8")

count = len(list(items_el))
print(f"Written {count} items to {XML}")
