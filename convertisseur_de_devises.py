class ConvertisseurDeDevises:
    def __init__(self):
        self.taux_de_change = {
            'EUR': 1,
            'YEN': 160.5,
            'LIVRE': 0.85,
            'WON': 1451.41,
            'USD': 1.09
        }

    def convertir(self, montant, devise_depart, devise_arrivee):
        if devise_depart not in self.taux_de_change or devise_arrivee not in self.taux_de_change:
            raise ValueError("Une des devises n'est pas prise en charge.")

        if devise_depart != 'EUR':
            montant_en_usd = montant / self.taux_de_change[devise_depart]
        else:
            montant_en_usd = montant

        montant_converti = montant_en_usd * self.taux_de_change[devise_arrivee]
        return montant_converti

def demander_utilisateur():
    convertisseur = ConvertisseurDeDevises()
    
    while True:
        devise_depart = input("Entrez la devise de départ (USD, EUR, YEN, LIVRE, WON) ou 'exit' pour quitter : ")
        if devise_depart.lower() == 'exit':
            break

        devise_arrivee = input("Entrez la devise d'arrivée (USD, EUR, YEN, LIVRE, WON) : ")
        montant = float(input("Entrez le montant à convertir : "))

        try:
            montant_converti = convertisseur.convertir(montant, devise_depart, devise_arrivee)
            print(f"{montant} {devise_depart} = {montant_converti:.2f} {devise_arrivee}")
        except ValueError as e:
            print(e)

demander_utilisateur()
