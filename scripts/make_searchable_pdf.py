import os
import fitz

src = r"C:\git\linked-open-exhibition\CIDOC\cidoc_crm_version_7.1.3.pdf"
dst = r"C:\git\linked-open-exhibition\CIDOC\cidoc_crm_version_7.1.3_searchable.pdf"


def main():
    doc = fitz.open(src)
    doc.save(dst, garbage=4, deflate=True, clean=True)
    print(f"Saved: {dst}")
    print(f"Pages: {doc.page_count}")
    out = fitz.open(dst)
    sample = out[0].get_text("text")
    print("sample_chars", len(sample))
    print(sample[:200].replace("\n", " | "))


if __name__ == "__main__":
    main()
