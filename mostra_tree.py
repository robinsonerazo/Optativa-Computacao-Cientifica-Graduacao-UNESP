# -*- coding: cp1252 -*-
import os

def imprime_tree(caminho):

    """
    Imprime recursivamente a árvore de diretórios, subdiretórios e arquivos
    a partir de qualquer caminho.
    """

    a = os.walk(caminho)

    for dirpath, dirnames, filenames in a:
        print dirpath
        if dirnames:
            for dirname in dirnames:
                print '\t', dirname

        listnames = [name for name in filenames if filenames]
        for name in listnames:
            print '\t'*2, name

if __name__ == '__main__':

    imprime_tree('/')


