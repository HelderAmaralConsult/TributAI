from pypdf import PdfReader

arquivo = "data/raw/Emenda_Constitucional_132.pdf"

reader = PdfReader(arquivo)

print(f"Total de páginas: {len(reader.pages)}")

texto = reader.pages[0].extract_text()

print("\n--- PRIMEIRA PÁGINA ---\n")
print(texto[:3000])
