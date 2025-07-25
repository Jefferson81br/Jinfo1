import streamlit as st
from datetime import datetime
import pytz # Importa a biblioteca pytz

st.title("Processador de Dados de Códigos de Barras Para Alpha7 V1.1")
st.markdown("---")

uploaded_file = st.file_uploader("Envie um arquivo .txt (formato: CODIGO,QUANTIDADE por linha)", type="txt")

if uploaded_file:
    lines = uploaded_file.read().decode("utf-8").splitlines()
    processed_data = []
    errors = []

    # Define o fuso horário para UTC-3 (ex: 'America/Sao_Paulo')
    brazil_tz = pytz.timezone('America/Sao_Paulo') 

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

        # Obtém a data e hora atual no fuso horário UTC-3
        now_utc_minus_3 = datetime.now(brazil_tz)
        
        # String da data (para conteúdo e nome do arquivo)
        date_str = now_utc_minus_3.strftime("%Y%m%d")
        
        # String da hora COMPLETA (para o conteúdo do arquivo: HHMMSS)
        time_str_content = now_utc_minus_3.strftime("%H%M%S")
        
        # String da hora RESUMIDA (para o nome do arquivo: HHMM)
        time_str_filename = now_utc_minus_3.strftime("%H%M") 

        result_lines = []
        for item in sorted_data:
            # Usa a string da hora COMPLETA para o conteúdo do arquivo
            result_lines.append(f"{date_str},{time_str_content},{item['code']},{item['quantity']}")

        result_text = "\n".join(result_lines)

        st.success("Dados processados com sucesso!")
        st.text_area("Resultado formatado:", result_text, height=300)

        # Constrói o nome do arquivo dinamicamente usando a hora RESUMIDA
        download_file_name = f"Dados_formatados_{date_str}_{time_str_filename}.txt"

        st.download_button(
            label="Baixar resultado formatado",
            data=result_text,
            file_name=download_file_name,
            mime="text/plain"
        )
