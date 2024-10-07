# Django first project

## Description
L'idée du site est de permettre aux petites entreprises, ainsi que les auto entrepeneurs d'avoir un espace où stocker ses factures. Chaque utilisateur pourra enregistrer ses factures avec des informations tel que la date de facturation, la nom du client, ainsi que la date de relance. Il y aura une fonctionnalité de notification pour les factures arrivées à échéance, ainsi l'utilisateur n'oubliera pas d'envoyer un mail ou d'appeler son client pour réclamer son paiement.

## Installation
1. **Cloner le Repo**
   ```bash
   git clone https://github.com/Macacul-accel/Gestion_facture.git
   cd Gestion_facture
   ```

2. **Activer l'environnement virtuel (Optionnel)**
   ```bash
   python -m venv .env
   source .env/bin/activate  # Sur Windows: `venv\Scripts\activate`
   ```

3. **Installer les packages nécessaires**
   ```bash
   pip install -r requirements.txt
   ```

4. **Activer la base de données**
   ```bash
   python manage.py migrate
   ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

6. **Accès au site**
   Open your browser and go to `http://127.0.0.1:8000/`.
