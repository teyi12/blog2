# Vérifier si Railway CLI est installé
if (-not (Get-Command "railway" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Railway CLI non installée. Installez-la avec : npm install -g @railway/cli" -ForegroundColor Red
    exit 1
}

# Définir le chemin du fichier .env de sortie
$envFilePath = ".env"
Write-Host "🔄 Récupération des variables Railway..."

# Exécuter la commande Railway pour récupérer les variables
$envVarsJson = railway variables | ConvertFrom-Json

# Si aucune variable n’est renvoyée
if (-not $envVarsJson) {
    Write-Host "❌ Aucune variable récupérée. Es-tu bien dans un dossier Railway ?"
    exit 1
}

# Sauvegarder l’ancienne version
if (Test-Path $envFilePath) {
    Copy-Item $envFilePath "$envFilePath.bak" -Force
    Write-Host "📦 Backup créée : .env.bak"
}

# Écrire les variables dans le fichier .env
Write-Host "`n📝 Écriture dans .env..."
"" | Out-File -Encoding utf8 $envFilePath  # vide le fichier

foreach ($var in $envVarsJson) {
    "$($var.key)=$($var.value)" | Out-File -Append -Encoding utf8 $envFilePath
}

Write-Host "`n✅ Synchronisation terminée. Fichier .env mis à jour." -ForegroundColor Green
