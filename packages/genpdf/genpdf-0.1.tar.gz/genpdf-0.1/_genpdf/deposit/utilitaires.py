def split_path(chemin):
    """Retourne le chemin du dossier et le nom du fichier."""
    dossier, nom_fichier = chemin.rsplit('/', 1)
    return dossier, nom_fichier

def dossier_existe(dossier):
    """Vérifie si le dossier existe."""
    try:
        # Essayez d'ouvrir le dossier
        with open(dossier):
            return True
    except FileNotFoundError:
        return False

def creer_dossier(dossier):
    """Crée le dossier."""
    # Créez un fichier vide dans le dossier pour le créer
    with open(dossier, 'w'):
        pass
