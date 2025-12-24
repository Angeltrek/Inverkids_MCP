# Docker Commands para Inverkids MCP HTTP Server (Windows PowerShell)
# Uso: .\docker-commands-http.ps1 <comando>

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('help', 'build', 'up', 'down', 'restart', 'logs', 'test', 'clean')]
    [string]$Command
)

$ComposeFile = "docker-compose.yml"
$ServiceName = "inverkids-mcp-http"

function Show-Help {
    Write-Host "Comandos disponibles para HTTP Server:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "build - Construir imagen HTTP" -ForegroundColor Yellow
    Write-Host "up - Iniciar servidor HTTP" -ForegroundColor Yellow
    Write-Host "down - Detener servidor HTTP" -ForegroundColor Yellow
    Write-Host "restart - Reiniciar servidor HTTP" -ForegroundColor Yellow
    Write-Host "logs - Ver logs del servidor" -ForegroundColor Yellow
    Write-Host "test - Probar endpoints" -ForegroundColor Yellow
    Write-Host "clean - Limpiar contenedores" -ForegroundColor Yellow
    Write-Host ""
}

switch ($Command) {
    'help' {
        Show-Help
    }
    
    'build' {
        Write-Host "Construyendo imagen HTTP..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile build
    }
    
    'up' {
        Write-Host "Iniciando servidor HTTP..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile up -d
        Write-Host "Servidor iniciado en http://localhost:8000" -ForegroundColor Green
        Write-Host "Health check: http://localhost:8000/health" -ForegroundColor Green
        Write-Host "Stream: http://localhost:8000/mcp/stream" -ForegroundColor Green
    }
    
    'down' {
        Write-Host "Deteniendo servidor HTTP..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile down
    }
    
    'restart' {
        Write-Host "Reiniciando servidor HTTP..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile restart
    }
    
    'logs' {
        Write-Host "Mostrando logs..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile logs -f $ServiceName
    }
    
    'test' {
        Write-Host "Probando endpoints..." -ForegroundColor Cyan
        
        Write-Host "`nProbando /health..." -ForegroundColor Yellow
        try {
            $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing
            Write-Host "Health check OK: $($response.Content)" -ForegroundColor Green
        } catch {
            Write-Host "Health check falló: $($_.Exception.Message)" -ForegroundColor Red
        }
        
        Write-Host "`nPara probar el stream, usa:" -ForegroundColor Yellow
        Write-Host "  curl http://localhost:8000/mcp/stream" -ForegroundColor Cyan
    }
    
    'clean' {
        Write-Host "Limpiando..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile down -v
        Write-Host "Limpieza completada" -ForegroundColor Green
    }
}