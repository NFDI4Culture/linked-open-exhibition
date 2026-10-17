import io
import os

import fitz
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

src = r"C:\git\linked-open-exhibition\CIDOC\cidoc_crm_version_7.1.3.pdf"
dst = r"C:\git\linked-open-exhibition\CIDOC\cidoc_crm_version_7.1.3_searchable.pdf"


def main():
    doc = fitz.open(src)
    ocr = RapidOCR()

    for page_index in range(doc.page_count):
        page = doc[page_index]
        pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), alpha=False)
        image = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
        arr = np.array(image)
        result, _ = ocr(arr)

        texts = []
        if result:
            for item in result:
                if isinstance(item, (list, tuple)) and len(item) >= 2 and isinstance(item[1], str):
                    text = item[1].strip()
                    if text:
                        texts.append(text)

        if texts:
            page_text = " ".join(texts)
            # Insert a very light, embedded text layer in the page margin so the PDF remains searchable
            # without significantly affecting the original page appearance.
            page.insert_text((5, 5), page_text, fontsize=6, fontname="helv", color=(0.98, 0.98, 0.98), overlay=True)

    doc.save(dst, garbage=4, deflate=True, clean=True)
    print(f"Saved searchable PDF to: {dst}")
    print(f"Pages processed: {doc.page_count}")
    print(f"Output size: {os.path.getsize(dst)} bytes")


if __name__ == "__main__":
    main()
