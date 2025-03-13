import pdfplumber
from tqdm import tqdm

def pdf_to_text(pdf_path, output_txt):
    with pdfplumber.open(pdf_path) as pdf, open(output_txt, "w", encoding="utf-8") as out_file:
        total_pages = len(pdf.pages)
        
        # Use tqdm to show progress
        for i in tqdm(range(total_pages), total=total_pages, desc="Extracting PDF", unit="page"):
            try:
                page = pdf.pages[i]  # Load only one page at a time
                text = page.extract_text()
                if text:
                    out_file.write(text + "\n\n")
            except Exception as e:
                print(f"Error processing page {i}: {e}")

if __name__ == "__main__":
    pdf_path = "FULL PDF FILE PATH HERE"
    output_txt = "output.txt"
    pdf_to_text(pdf_path, output_txt)
    print(f"Text extracted and saved to {output_txt}")
