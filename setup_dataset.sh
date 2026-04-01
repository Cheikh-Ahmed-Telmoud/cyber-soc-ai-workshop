#!/bin/bash
echo "🚀 Téléchargement et préparation du dataset CIC-IDS2017..."

mkdir -p data
cd data

# Version légère via Kaggle (recommandée pour workshop)
if [ ! -f "MachineLearningCSV.zip" ]; then
    echo "Téléchargement du dataset (environ 2Go)..."
    # Alternative : utilise wget si tu héberges un mirror, ou demande aux étudiants de télécharger manuellement
    echo "Veuillez télécharger MachineLearningCSV.zip depuis : https://www.unb.ca/cic/datasets/ids-2017.html"
    echo "Puis placez-le dans le dossier data/ et relancez le script."
else
    unzip -o MachineLearningCSV.zip
    echo "✅ Dataset prêt !"
fi