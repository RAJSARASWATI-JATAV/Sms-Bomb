# SMS-POWERBOMB Bug Fix Verification Script
# This script tests all the fixes applied

Write-Host "🔧 SMS-POWERBOMB Bug Fix Verification" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

$rootPath = Split-Path -Parent $PSScriptRoot

# Test 1: Backend .env CORS format
Write-Host "✓ Test 1: Checking backend .env CORS format..." -ForegroundColor Yellow
$envPath = Join-Path $rootPath "backend\.env"
if (Test-Path $envPath) {
    $corsLine = Get-Content $envPath | Select-String "CORS_ORIGINS="
    if ($corsLine -match "CORS_ORIGINS=http://localhost:5173,http://localhost:3000") {
        Write-Host "  ✅ CORS format is correct (comma-separated)" -ForegroundColor Green
    } else {
        Write-Host "  ❌ CORS format is incorrect" -ForegroundColor Red
        Write-Host "  Found: $corsLine" -ForegroundColor Red
    }
} else {
    Write-Host "  ⚠️  .env file not found" -ForegroundColor Yellow
}
Write-Host ""

# Test 2: Backend config.py has validator
Write-Host "✓ Test 2: Checking backend config.py for CORS validator..." -ForegroundColor Yellow
$configPath = Join-Path $rootPath "backend\config.py"
if (Test-Path $configPath) {
    $configContent = Get-Content $configPath -Raw
    if ($configContent -match "field_validator.*parse_cors_values") {
        Write-Host "  ✅ CORS validator found in config.py" -ForegroundColor Green
    } else {
        Write-Host "  ❌ CORS validator not found" -ForegroundColor Red
    }
} else {
    Write-Host "  ⚠️  config.py not found" -ForegroundColor Yellow
}
Write-Host ""

# Test 3: Frontend vite.config has code splitting
Write-Host "✓ Test 3: Checking frontend vite.config for code splitting..." -ForegroundColor Yellow
$viteConfigPath = Join-Path $rootPath "frontend\vite.config.ts"
if (Test-Path $viteConfigPath) {
    $viteContent = Get-Content $viteConfigPath -Raw
    if ($viteContent -match "manualChunks") {
        Write-Host "  ✅ Code splitting configured in vite.config.ts" -ForegroundColor Green
        if ($viteContent -match "react-vendor") {
            Write-Host "  ✅ React vendor chunk configured" -ForegroundColor Green
        }
        if ($viteContent -match "ui-vendor") {
            Write-Host "  ✅ UI vendor chunk configured" -ForegroundColor Green
        }
        if ($viteContent -match "chart-vendor") {
            Write-Host "  ✅ Chart vendor chunk configured" -ForegroundColor Green
        }
    } else {
        Write-Host "  ❌ Code splitting not configured" -ForegroundColor Red
    }
} else {
    Write-Host "  ⚠️  vite.config.ts not found" -ForegroundColor Yellow
}
Write-Host ""

# Test 4: Check backend dependencies
Write-Host "✓ Test 4: Checking backend dependencies..." -ForegroundColor Yellow
$backendReqPath = Join-Path $rootPath "backend\requirements.txt"
if (Test-Path $backendReqPath) {
    $reqContent = Get-Content $backendReqPath -Raw
    $deps = @("fastapi", "uvicorn", "sqlalchemy", "aiosqlite", "pydantic-settings")
    $allFound = $true
    foreach ($dep in $deps) {
        if ($reqContent -match $dep) {
            Write-Host "  ✅ $dep found" -ForegroundColor Green
        } else {
            Write-Host "  ❌ $dep missing" -ForegroundColor Red
            $allFound = $false
        }
    }
    if ($allFound) {
        Write-Host "  ✅ All critical dependencies present" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  requirements.txt not found" -ForegroundColor Yellow
}
Write-Host ""

# Test 5: Check CLI dependencies
Write-Host "✓ Test 5: Checking CLI dependencies..." -ForegroundColor Yellow
$cliReqPath = Join-Path $rootPath "cli\requirements.txt"
if (Test-Path $cliReqPath) {
    $cliReqContent = Get-Content $cliReqPath -Raw
    $cliDeps = @("aiohttp", "requests", "scikit-learn", "numpy")
    $allFound = $true
    foreach ($dep in $cliDeps) {
        if ($cliReqContent -match $dep) {
            Write-Host "  ✅ $dep found" -ForegroundColor Green
        } else {
            Write-Host "  ❌ $dep missing" -ForegroundColor Red
            $allFound = $false
        }
    }
    if ($allFound) {
        Write-Host "  ✅ All CLI dependencies present" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  CLI requirements.txt not found" -ForegroundColor Yellow
}
Write-Host ""

# Summary
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "🎉 Verification Complete!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Start backend: cd backend; python main.py" -ForegroundColor White
Write-Host "2. Start frontend: cd frontend; npm run dev" -ForegroundColor White
Write-Host "3. Start CLI: cd cli; python main.py" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see QUICKSTART_FIXED.md" -ForegroundColor Cyan