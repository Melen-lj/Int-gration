"""Module manipulant des fichiers texte."""
from filecmp import *
def diff(file_first, file_second):
    """Fonction retournant True si deux fichiers sont différents."""
    resultat=False
    with open(file_first) as file1_id:
		with open(file_second) as file2_id:
			resultat= file1.id.read()!=file_id.read()
	return resultat

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    return True
