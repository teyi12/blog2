# === Synchronise les variables Railway dans un fichier .env ===

Write-Host ""
Write-Host "==> Synchronisation des variables Railway vers .env"

# Vérifie si Railway CLI est installée
if (-not (Get-Command "railway" -ErrorAction SilentlyContinue)) {
    Write-Host "ERREUR : Railway CLI non trouvée. Installez-la avec : npm install -g @railway/cli"
    exit 1
}

# Définir le chemin du fichier .env
$envFilePath = ".env"

# Récupère les variables Railway au format JSON
$envVarsJson = railway variables --json | ConvertFrom-Json

# Vérifie s'il y a des données
if (-not $envVarsJson) {
    Write-Host "ERREUR : Aucune variable récupérée. Êtes-vous dans un projet Railway ?"
    exit 1
}

# Sauvegarde du fichier .env existant
if (Test-Path $envFilePath) {
    Copy-Item $envFilePath "$envFilePath.bak" -Force
    Write-Host "Backup existant sauvegardé sous .env.bak"
}

# Vide le fichier .env actuel
"" | Out-File -Encoding ASCII $envFilePath

# Écrit les variables dans le fichier .env
foreach ($var in $envVarsJson) {
    "$($var.key)=$($var.value)" | Out-File -Append -Encoding ASCII $envFilePath
}

Write-Host ""
Write-Host "Succès : Le fichier .env a été mis à jour avec les variables Railway."
