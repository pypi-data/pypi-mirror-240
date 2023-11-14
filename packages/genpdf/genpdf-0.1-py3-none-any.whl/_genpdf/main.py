from deposit.pdfgen import PDFGenerator

if __name__ == "__main__":
    # Chemin et nom fichier
    chemin_dossier = input("Entrez le chemin du dossier : ")
    nom_fichier = input("Entrez le nom du fichier (avec l'extension .pdf) : ")

    # Contenu principal
    contenu_principal = input("Entrez le contenu principal du PDF : ")

    # Contenu supplémentaire
    contenu_supplementaire = input("Entrez le contenu supplémentaire du PDF : ")

    # Génération du PDF 
    pdf_generator = PDFGenerator(chemin_dossier + '/' + nom_fichier)
    pdf_generator.ajouter_texte(contenu_principal)
    pdf_generator.ajouter_texte(contenu_supplementaire)
    pdf_generator.generer_pdf()
