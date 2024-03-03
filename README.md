# SIP (Search in PDF)

## Motivação

Estudando para uma prova, onde o material previsto no edital chega a mais de 10.000 páginas, vi a necessidade de uma ferramenta que buscasse por textos nos PDFs e retornasse o nome do arquivo e o trecho onde a frase aparece.

## Requerimentos

- Python3
- [xpdf](https://www.xpdfreader.com/download.html)

Por enquanto, o script somente funciona em Linux.

## Modo de uso

O Script espera 2 argumentos: o diretório e a frase a ser buscada. O diretório será o primeiro argumento, e a frase o segundo. A frase não é *case sensitive*, ou seja, pode vir capitalizada ou não.

Exemplo:

``python3 main.py "/home/user/folder" "where"``

Onde *"/home/user/folder"* é o diretório, e *"where"* é a frase a ser procurada. Para evitar problemas com o grep, mantenha o diretório a frase entre aspas.

Saída:

```
Arquivo: asdf
Encontrado no(s) trecho(s):
Where does it come from?
Where can I get some?

Arquivo: asdf (3ª cópia)
Encontrado no(s) trecho(s):
Where does it come from?
Where can I get some?

Arquivo: asdf (cópia)
Encontrado no(s) trecho(s):
Where does it come from?
Where can I get some?
```
