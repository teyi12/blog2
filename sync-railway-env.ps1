# === sync-env-railway.ps1 ===
Write-Host "🔁 Synchronisation bi-directionnelle Railway ↔ .env" -ForegroundColor Cyan

# 0. Vérification de la CLI Railway
if (-not (Get-Command railway -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Railway CLI non trouvée. Installe-la depuis https://docs.railway.app/develop/cli" -ForegroundColor Red
    exit 1
}

$envFilePath = ".env"

# 1. Sauvegarde du .env existant
if (Test-Path $envFilePath) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupPath = ".env.bak-$timestamp"
    Copy-Item $envFilePath $backupPath
    Write-Host "🗂️  Backup créé : $backupPath" -ForegroundColor DarkGray
}

# Sauvegarde .env.local si présent
if (Test-Path ".env.local") {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupPathLocal = ".env.local.bak-$timestamp"
    Copy-Item ".env.local" $backupPathLocal
    Write-Host "🗂️  Backup de .env.local : $backupPathLocal" -ForegroundColor DarkGray
}

# 2. Téléchargement des variables Railway vers .env
Write-Host "`n⬇️  Import depuis Railway vers .env..." -ForegroundColor Cyan
$variablesJson = railway variables | ConvertFrom-Json

if (-not $variablesJson.variables) {
    Write-Host "❌ Aucune variable trouvée. Le projet est-il bien lié avec 'railway link' ?" -ForegroundColor Red
    exit 1
}

@()
$envLines = $variablesJson.variables | ForEach-Object {
    "$($_.key)=$($_.value)"
}
$envLines | Set-Content $envFilePath -Encoding UTF8
Write-Host "✅ Fichier .env mis à jour depuis Railway." -ForegroundColor Green

# 3. Envoi de .env local vers Railway
Write-Host "`n⬆️  Export de .env vers Railway..." -ForegroundColor Cyan
$lines = Get-Content $envFilePath | Where-Object {
    ($_ -notmatch '^\s*$') -and ($_ -notmatch '^\s*#')
}

foreach ($line in $lines) {
    if ($line -match '^\s*([^=]+)\s*=\s*(.*)\s*$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        $value = $value -replace '"', '"'  # Échapper les guillemets
        railway variables set "$key=$value" | Out-Null
        Write-Host "→ $key=..." -ForegroundColor Yellow
    }
    else {
        Write-Host "⚠️ Ligne ignorée (format invalide) : $line" -ForegroundColor DarkYellow
    }
}

# 4. Résumé
Write-Host "`n🔐 Variables synchronisées :" -ForegroundColor Cyan
$lines | ForEach-Object {
    if ($_ -match '^\s*([^=]+)\s*=') {
        Write-Host "• $($matches[1])" -ForegroundColor DarkCyan
    }
}

Write-Host "`n✅ Sync terminé avec succès. Vérifie ton projet Railway si besoin 👉 https://railway.app/project" -ForegroundColor Green
