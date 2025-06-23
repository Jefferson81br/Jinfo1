import streamlit as st
from datetime import datetime

st.title("Processador de Dados de Códigos de Barras para Alpha7")
st.markdown("---")

uploaded_file = st.file_uploader("Envie um arquivo .txt (formato: CODIGO,QUANTIDADE por linha)", type="txt")

if uploaded_file:
    lines = uploaded_file.read().decode("utf-8").splitlines()
    processed_data = []
    errors = []

    for line_num, line in enumerate(lines):
        stripped_line = line.strip()
        if not stripped_line:
            continue # Ignora linhas vazias

        parts = stripped_line.split(',')
        if len(parts) == 2:
            code = parts[0].strip()
            try:
                quantity = int(parts[1].strip())
                processed_data.append({"code": code, "quantity": quantity})
            except ValueError:
                errors.append(f"Linha {line_num + 1}: Quantidade '{parts[1].strip()}' não é um número válido.")
        else:
            errors.append(f"Linha {line_num + 1}: Formato inválido. Esperado 'CODIGO,QUANTIDADE'.")

    if errors:
        st.error("Foram encontrados os seguintes erros no arquivo:")
        for error in errors:
            st.write(f"- {error}")
        st.warning("Por favor, corrija o arquivo e tente novamente.")
    elif not processed_data:
        st.warning("O arquivo enviado não contém dados válidos no formato 'CODIGO,QUANTIDADE'.")
    else:
        # Ordena os dados pela quantidade (do menor para o maior)
        sorted_data = sorted(processed_data, key=lambda x: x['quantity'])

        now = datetime.now()
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%M%S")

        result_lines = []
        for item in sorted_data:
            result_lines.append(f"{date_str},{time_str},{item['code']},{item['quantity']}")

        result_text = "\n".join(result_lines)

        st.success("Dados processados com sucesso!")
        st.text_area("Resultado formatado:", result_text, height=300)

        st.download_button(
            label="Baixar resultado formatado",
            data=result_text,
            file_name="dados_formatados.txt",
            mime="text/plain"
        )
