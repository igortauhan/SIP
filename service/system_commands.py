import os


def list_files(directory):
    return os.listdir()


def convert_pdf_to_text(file):
    try:
        os.system(f'pdftotext -layout {file}')
    except Exception as e:
        print(e)


def search_text(file, text):
    try:
        return os.popen(f'cat {file} | grep -i {text}').read()
    except Exception as e:
        print(e)


def delete_file(file):
    os.remove(file)
