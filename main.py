from pathlib import Path
from pdf_preprocessed import (
    extract_pdf_text,
    clean_brandstof_text,
    split_kentekens,
    text_to_csv
)

PDF_PATH = Path(__file__).parent.parent / "data" / "brandstof.pdf"
OUTPUT_FILE = "output"


def main() -> None:
    """
    Process PDF file and writes to CSV. 

    Args:
        None
    Returns: 
        None
    
    """
    pages = extract_pdf_text(PDF_PATH)
    text = clean_brandstof_text(pages)
    blocks = split_kentekens(text)
    text_to_csv(blocks, output_file=OUTPUT_FILE + '.csv')

if __name__ == "__main__":
    main()

