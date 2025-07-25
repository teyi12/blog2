# === sync-env-railway.ps1 ===
Write-Host "🔁 Synchronisation bi-directionnelle Railway ↔ .env" -ForegroundColor Cyan

$envFilePath = ".env"

# 1. Sauvegarde du .env existant
if (Test-Path $envFilePath) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupPath = ".env.bak-$timestamp"
    Copy-Item $envFilePath $backupPath
    Write-Host "🗂️  Backup créé : $backupPath" -ForegroundColor DarkGray
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
        $value = $value -replace '"', '\"'  # Échapper les guillemets
        railway variables set "$key=$value" | Out-Null
        Write-Host "→ $key=..." -ForegroundColor Yellow
    }
    else {
        Write-Host "⚠️ Ligne ignorée (format invalide) : $line" -ForegroundColor DarkYellow
    }
}

Write-Host "`n🎉 Synchronisation Railway <-> .env terminée avec succès." -ForegroundColor Green
