from service.system_commands import list_files, convert_pdf_to_text, search_text, delete_file


def find_all_pdfs(directory):
    all_files = list_files(directory)
    pdf_files = []

    for file in all_files:
        if file.__contains__(".pdf"):
            pdf_files.append(file)

    return pdf_files


def convert(pdf_files):
    txt_files = []

    for file in pdf_files:
        convert_pdf_to_text(file)
        txt_files.append(f'{file.split(".")[0]}.txt')

    return txt_files


def search(txt_files, text):
    for file in txt_files:
        result = search_text(file, text)

        if result == "":
            print("Texto não encontrado em nenhum dos arquivos")
            return

        print(f'Arquivo: {file.split(".")[0]}\nEncontrado no(s) trecho(s):\n{result}')


def delete_txt_files(txt_files):
    for file in txt_files:
        delete_file(file)


def main():
    pdf_files = find_all_pdfs(".")
    txt_files = convert(pdf_files)
    search(txt_files, "")
    delete_txt_files(txt_files)


if __name__ == "__main__":
    main()
