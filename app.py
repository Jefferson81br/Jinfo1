import streamlit as st
from collections import Counter
from datetime import datetime

st.title("Processador de Códigos de Barras")

uploaded_file = st.file_uploader("Envie um arquivo .txt com códigos EAN-13", type="txt")

if uploaded_file:
    lines = uploaded_file.read().decode("utf-8").splitlines()
    barcodes = [line.strip() for line in lines if line.strip()]
    counts = Counter(barcodes)

    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M%S")

    result_lines = [
        f"{date_str},{time_str},{code},{count}"
        for code, count in sorted(counts.items())
    ]
    result_text = "\n".join(result_lines)

    st.text_area("Resultado:", result_text, height=300)

    st.download_button(
        label="Baixar resultado",
        data=result_text,
        file_name="codigos_formatados.txt",
        mime="text/plain"
    )
