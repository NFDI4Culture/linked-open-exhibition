import xml.etree.ElementTree as ET

NS_MARC = "http://www.loc.gov/MARC21/slim"
NS_SRW  = "http://www.loc.gov/zing/srw/"

root = ET.parse("catalogues/sprengel_raw/page_001.xml").getroot()
records = root.findall(f".//{{{NS_SRW}}}recordData/{{{NS_MARC}}}record")

# Find every field containing Ausstellungskatalog
for rec in records:
    for df in rec.findall(f"{{{NS_MARC}}}datafield"):
        for sf in df.findall(f"{{{NS_MARC}}}subfield"):
            if sf.text and "Ausstellungskatalog" in sf.text:
                # get IDN
                cf001 = rec.find(f"{{{NS_MARC}}}controlfield")
                idn = cf001.text if cf001 is not None else "?"
                tag = df.get("tag")
                code = sf.get("code")
                t245 = rec.find(f".//{{{NS_MARC}}}datafield[@tag='245']/{{{NS_MARC}}}subfield[@code='a']")
                title = t245.text[:50] if t245 is not None else ""
                print(f"IDN={idn}  {tag}$${code}: {sf.text}  | {title}")
                break
