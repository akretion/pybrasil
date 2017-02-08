#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright 2016 Taŭga Tecnologia
#   Aristides Caldeira <aristides.caldeira@tauga.com.br>
# License AGPL-3 or later (http://www.gnu.org/licenses/agpl)
#


from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from pyparsing import Word, quotedString, pythonStyleComment, QuotedString, \
    alphanums, alphas8bit, Combine, Literal, unicodeString
from pybrasil.base import tira_acentos


PALAVRAS_BRASIL = {}

_PALAVRAS_PADRAO = {
    #
    #  Lógica
    #
    'e': 'and',
    'ou': 'or',
    'não': 'not',
    'nao': 'not',
    'Sim': 'True',
    'Não': 'False',
    'Nao': 'False',
    'Verdadeiro': 'True',
    'Falso': 'False',
    'Nada': 'None',

    #
    # Métodos, classes etc.
    #
    'defina': 'def',
    'classe': 'class',
    'eu': 'self',
    'global': 'global',

    #
    # Import
    #
    'de': 'from',
    'da': 'from',
    'do': 'from',
    'das': 'from',
    'dos': 'from',
    'importe': 'import',
    'como': 'as',

    #
    # Fluxo
    #
    'retorne': 'return',
    'passe': 'pass',
    'suba': 'raise',
    'continue': 'continue',

    #
    # Controle
    #
    'se': 'if',
    'ou_se': 'elif',
    'ouse': 'elif',
    'se_não': 'else',
    'se_nao': 'else',
    'senão': 'else',
    'senao': 'else',

    #
    # Laço for
    #
    'para': 'for',
    'para cada': 'for',
    'em': 'in',
    'no': 'in',
    'na': 'in',
    'nos': 'in',
    'nas': 'in',
    'fora': 'not in',
    'fora do': 'not in',
    'fora da': 'not in',
    'fora dos': 'not in',
    'fora das': 'not in',

    #
    # Laço while
    #
    'enquanto': 'while',
    'pare': 'break',

    #
    # try
    #
    'tente': 'try',
    'exceto': 'except',
    'por_fim': 'finally',
    'por fim': 'finally',
    'porfim': 'finally',
    'certifique': 'assert',

    #
    # Métodos built-in
    #
    'execute': 'exec',
    'função': 'lambda',
    'funcao': 'lambda',
    'mostre': 'print',
    'com': 'with',
    'produza': 'yield',

    'entrada_pura': 'raw_input',
    # build-in types
    'qualquertexto': 'basestring',
    'qualquer_texto': 'basestring',
    'texto': 'str',
    'lógico': 'bool',
    'logico': 'bool',
    'buleano': 'bool',
    'lista': 'list',
    'dic': 'dict',
    'dicionário': 'dict',
    'dicionario': 'dict',
    'tupla': 'tuple',
    'conjunto': 'set',
    'conjunto_imutável': 'frozenset',
    'conjunto_imutavel': 'frozenset',
    'chr': 'chr',
    'ordem': 'ord',
    'arquivo': 'file',
    # number methods
    'inteiro': 'int',
    'decimal': 'float',
    'complexo': 'complex',
    'hexadecimal': 'hex',
    'abs': 'abs',
    'compare': 'cmp',
    # string methods
    'começa_com': 'startswith',
    'comeca_com': 'startswith',
    'começacom': 'startswith',
    'comecacom': 'startswith',
    'termina_com': 'endswith',
    'terminacom': 'endswith',
    'junte': 'join',
    'separe': 'split',
    'troque': 'replace',
    'substitua': 'replace',
    'codificação': 'encoding',
    'codificacão': 'encoding',
    'codificaçao': 'encoding',
    'codificacao': 'encoding',
    'decodificação': 'decoding',
    'decodificacão': 'decoding',
    'decodificaçao': 'decoding',
    'decodificacao': 'decoding',
    'codifique': 'encode',
    'decodifique': 'decode',
    # list methods
    'anexe': 'append',
    'acrescente': 'append',
    'extenda': 'extend',
    'insira': 'insert',
    '彈出': 'pop',
    'próximo': 'next',
    'proximo': 'next',
    'remova': 'remove',
    'inverta': 'reverse',
    'conte': 'count',
    'índice': 'index',
    'indice': 'index',
    'ordene': 'sort',
    # dict methods
    'chaves': 'keys',
    'valores': 'values',
    'itens': 'items',
    'atualize': 'update',
    'copie': 'copy',
    # set methods
    'limpe': 'clear',
    'adicione': 'add',
    'descarte': 'discard',
    'união': 'union',
    'uniao': 'union',
    'intesecção': 'intersection',
    'intesecçao': 'intersection',
    'inteseccão': 'intersection',
    'inteseccao': 'intersection',
    'inteseção': 'intersection',
    'inteseçao': 'intersection',
    'intesecão': 'intersection',
    'intesecao': 'intersection',
    'diferença': 'difference',
    'diferenca': 'difference',
    'diferença_simétrica': 'symmetric_difference',
    'diferenca_simétrica': 'symmetric_difference',
    'diferença_simetrica': 'symmetric_difference',
    'diferenca_simetrica': 'symmetric_difference',
    # file methods
    'abra': 'open',
    'leia': 'read',
    'grave': 'write',
    'leia_linha': 'readline',
    'leialinha': 'readline',
    'leia_linhas': 'readlines',
    'leialinhas': 'readlines',
    'feche': 'close',
    # OO
    '可調用': 'callable',
    '列出屬性': 'dir',
    '取屬性': 'getattr',
    '有屬性': 'hasattr',
    '設定屬性': 'setattr',
    'propriedade': 'property',
    # build in functions
    'tam': 'len',
    'tamanho': 'len',
    'máximo': 'max',
    'maximo': 'max',
    'máx': 'max',
    'mínimo': 'min',
    'minimo': 'min',
    'mín': 'min',
    # build in methods
    '列舉': 'enumerate',
    '評估': 'eval',
    '過濾': 'filter',
    'mapeie': 'map',
    'intervalo': 'range',
    'intervalo_x': 'xrange',
    'intervalox': 'xrange',
    'some': 'sum',
    'tipo': 'type',
    'objeto': 'object',
    'zip': 'zip',
    'ajuda': 'help',
    'locais': 'locals',
    'globais': 'globals',
    'método_de_classe': 'classmethod',
    'metodo_de_classe': 'classmethod',
    'método_classe': 'classmethod',
    'metodo_classe': 'classmethod',

    '__nome__': '__name__',
}


def _converte_ingles(original, posicao, tokens):
    palavra = tokens[0]

    if palavra in PALAVRAS_BRASIL:
        palavra = PALAVRAS_BRASIL[palavra]

    elif palavra in _PALAVRAS_PADRAO:
        palavra = _PALAVRAS_PADRAO[palavra]

    else:
        palavra = tira_acentos(palavra)

    return palavra


palavras_pt_BR = Word(alphanums + alphas8bit + '_=!')
palavras_pt_BR.setParseAction(_converte_ingles)

tripleQuote = QuotedString('"""', multiline=True, unquoteResults=False) | \
            QuotedString("'''", multiline=True, unquoteResults=False)

unicodeTripleQuote = Combine(Literal('u') + tripleQuote.copy()).setName("unicode string triple quoted")

python_brasil = unicodeTripleQuote | tripleQuote | unicodeString | \
    quotedString | pythonStyleComment | \
    palavras_pt_BR


def python_pt_BR(texto, dicionario={}):
    global PALAVRAS_BRASIL
    PALAVRAS_BRASIL.update(dicionario)

    if type(texto) != unicode:
        texto = unicode(texto)

    return python_brasil.transformString(texto)


if __name__ == '__main__':
    texto = u'''# -*- coding: utf-8 -*-
#
# Este é um exemplo de código Python escrito em pt_BR
#

#
# Variáveis, nomes de funções e métodos, pode ter acentos ou não, e são
# considerados equivalentes (sem acento == com acento)
#
variável = u'Isto é uma variável'

def função_qualquer(parâmetro_1, parâmetro_2):
    se tipo(parametro_1) == qualquer_texto:
        mostre(u'Este foi o parâmetro 1', parâmetro_1)
    senão:
        mostre(u'O tipo do parâmetro 1 é', tipo(parâmetro_1))

    se tipo(parâmetro_2) == lógico:
        mostre(u'O 2º parâmetro foi', u'sim' se parametro_2 == Verdadeiro senão u'não')

se __nome__ == '__main__':
    função_qualquer(123.4, Falso)

'''
    #print(texto)
    ingles = python_brasil.transformString(texto)
    print(ingles.encode('utf-8'))
