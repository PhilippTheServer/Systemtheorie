#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

def convert_pdf(pdf_path: str, dpi: int, output_dir: str | None):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("Missing dependency. Install with: pip install pymupdf")
        sys.exit(1)

    pdf = Path(pdf_path)
    if not pdf.exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    out = Path(output_dir) if output_dir else pdf.parent / pdf.stem
    out.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        img_path = out / f"page_{i + 1:03d}.png"
        pix = page.get_pixmap(matrix=mat)
        pix.save(img_path)
        print(f"  {img_path}")

    page_count = len(doc)
    doc.close()
    print(f"\n{page_count} page(s) saved to {out}/")

def main():
    parser = argparse.ArgumentParser(description="Convert a PDF to PNG images.")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("--dpi", type=int, default=150, help="Resolution (default: 150)")
    parser.add_argument("--out", help="Output directory (default: <pdf-name>/)")
    args = parser.parse_args()
    convert_pdf(args.pdf, args.dpi, args.out)

if __name__ == "__main__":
    main()
