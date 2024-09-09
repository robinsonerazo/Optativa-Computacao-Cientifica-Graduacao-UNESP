# -*- coding: cp1252 -*-

# Defini��o da classe Cachorros
class Cachorros(object):
    """Classe de cachorros pra registro.
Instancie o c�o com nome, idade e ra�a.
    """
    def __init__(self,nome,
                 idade = 'desconhecida',
                 kind = 'SRD'):
        
    #Atributos da classe 
        self.nome = nome      
        self.idade = idade
        self.kind = kind
        self.food = self._come(idade)

    # M�todos da classe

    def late(self):   
        print '%s: "AU AU AU" ' %self.nome

    def _come(self,idade):
        if idade != 'desconhecida':
            if idade <= 1 :
                food = 'ra��o_junior'
            elif idade >1:
                food = 'ra��o_senior'

        else:
            food = 'ra��o_gen�rica'

        print '%s come %s'%(self.nome,food)
        return food

    def __repr__(self):
        return 'Oi! Eu sou o %s' %self.nome

if __name__ == '__main__':
    
    c1 = Cachorros('Fido',1,'pastor')
    c2 = Cachorros('Uzi',2,'poodle')
    c3 = Cachorros('Vagau')

    c1.late()
    c2.late()
    c3.late()

    
