from rag.pdf_to_text import pdf_to_text

pdf_path = "data/ASAP.pdf"

text = pdf_to_text(pdf_path)

print("----- EXTRACTED TEXT START -----")
print(text)
print("----- EXTRACTED TEXT END -----")