from pathlib import Path
from pypdf import PdfReader


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extrai todo o texto de um arquivo PDF.
    """
    reader = PdfReader(pdf_path)

    text = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            text.append(
                f"\n\n===== PÁGINA {page_number} =====\n\n"
            )
            text.append(page_text)

    return "".join(text)


def save_text(pdf_path: Path, text: str):
    """
    Salva o conteúdo extraído em um arquivo .txt.
    """
    output_file = PROCESSED_DIR / f"{pdf_path.stem}.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"Arquivo gerado: {output_file}")


def main():
    pdf_files = list(RAW_DIR.glob("*.pdf"))

    if not pdf_files:
        print("Nenhum PDF encontrado em data/raw")
        return

    for pdf_file in pdf_files:
        print(f"Processando: {pdf_file.name}")

        text = extract_text_from_pdf(pdf_file)

        save_text(pdf_file, text)

        print(f"Total de caracteres extraídos: {len(text)}")


if __name__ == "__main__":
    main()
