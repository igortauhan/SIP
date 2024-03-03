import os


def list_files(directory):
    return os.listdir(directory)


def convert_pdf_to_text(directory, file):
    try:
        os.system(f'pdftotext -layout "{directory}/{file}"')
    except Exception as e:
        print(e)


def search_text(directory, file, text):
    try:
        return os.popen(f'cat "{directory}/{file}" | grep -i "{text}"').read()
    except Exception as e:
        print(e)


def delete_file(directory, file):
    os.remove(f'{directory}/{file}')
