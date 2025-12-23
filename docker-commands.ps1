# Docker Commands para Inverkids MCP (Windows PowerShell)
# Uso: .\docker-commands.ps1 <comando>

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('help', 'setup', 'build', 'up', 'down', 'restart', 'logs', 'ps', 
                 'dev-build', 'dev-up', 'dev-down', 'dev-logs', 'dev-restart',
                 'shell', 'dev-shell', 'test', 'clean', 'info', 'rebuild', 'prod', 'dev')]
    [string]$Command
)

$ComposeFile = "docker-compose.yml"
$ComposeDevFile = "docker-compose.dev.yml"
$ServiceName = "inverkids-mcp"
$ServiceNameDev = "inverkids-mcp-dev"

function Show-Help {
    Write-Host "Comandos disponibles:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Producción:" -ForegroundColor Yellow
    Write-Host "    setup          - Configuración inicial del proyecto"
    Write-Host "    build          - Construir imagen de producción"
    Write-Host "    up             - Iniciar contenedor de producción"
    Write-Host "    down           - Detener contenedor de producción"
    Write-Host "    restart        - Reiniciar contenedor de producción"
    Write-Host "    logs           - Ver logs de producción"
    Write-Host "    ps             - Ver estado de contenedores"
    Write-Host "    prod           - Build + Up (rápido)"
    Write-Host ""
    Write-Host "  Desarrollo:" -ForegroundColor Yellow
    Write-Host "    dev-build      - Construir imagen de desarrollo"
    Write-Host "    dev-up         - Iniciar contenedor de desarrollo"
    Write-Host "    dev-down       - Detener contenedor de desarrollo"
    Write-Host "    dev-logs       - Ver logs de desarrollo"
    Write-Host "    dev-restart    - Reiniciar contenedor de desarrollo"
    Write-Host "    dev            - Dev Build + Up (rápido)"
    Write-Host ""
    Write-Host "  Utilidades:" -ForegroundColor Yellow
    Write-Host "    shell          - Abrir shell en contenedor de producción"
    Write-Host "    dev-shell      - Abrir shell en contenedor de desarrollo"
    Write-Host "    test           - Ejecutar tests"
    Write-Host "    clean          - Limpiar contenedores y volúmenes"
    Write-Host "    info           - Mostrar información del sistema"
    Write-Host "    rebuild        - Down + Build + Up"
    Write-Host ""
}

switch ($Command) {
    'help' {
        Show-Help
    }
    
    'setup' {
        Write-Host "Configurando proyecto Inverkids MCP..." -ForegroundColor Green
        
        if (-not (Test-Path .env)) {
            Copy-Item .env.example .env
            Write-Host "Archivo .env creado. Por favor, configura las variables." -ForegroundColor Green
        } else {
            Write-Host ".env ya existe." -ForegroundColor Yellow
        }
        
        if (-not (Test-Path logs)) {
            New-Item -ItemType Directory -Force -Path logs | Out-Null
            Write-Host "Directorio de logs creado" -ForegroundColor Green
        }
        
        Write-Host "Setup completado. Ejecuta: .\docker-commands.ps1 build" -ForegroundColor Green
        Write-Host "                   Luego: .\docker-commands.ps1 up" -ForegroundColor Green
    }
    
    'build' {
        Write-Host "Construyendo imagen de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile build
    }
    
    'up' {
        Write-Host "Iniciando contenedor de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile up -d
        Write-Host "Contenedor iniciado. Ver logs con: .\docker-commands.ps1 logs" -ForegroundColor Green
    }
    
    'down' {
        Write-Host "Deteniendo contenedor de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile down
    }
    
    'restart' {
        Write-Host "Reiniciando contenedor de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile restart
    }
    
    'logs' {
        Write-Host "Mostrando logs de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile logs -f $ServiceName
    }
    
    'ps' {
        Write-Host "Estado de contenedores:" -ForegroundColor Cyan
        docker-compose -f $ComposeFile ps
    }
    
    'dev-build' {
        Write-Host "Construyendo imagen de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile build
    }
    
    'dev-up' {
        Write-Host "Iniciando contenedor de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile up -d
        Write-Host "Contenedor de desarrollo iniciado" -ForegroundColor Green
    }
    
    'dev-down' {
        Write-Host "Deteniendo contenedor de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile down
    }
    
    'dev-logs' {
        Write-Host "Mostrando logs de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile logs -f $ServiceNameDev
    }
    
    'dev-restart' {
        Write-Host "Reiniciando contenedor de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile restart
    }
    
    'shell' {
        Write-Host "Abriendo shell en contenedor de producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile exec $ServiceName bash
    }
    
    'dev-shell' {
        Write-Host "Abriendo shell en contenedor de desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile exec $ServiceNameDev bash
    }
    
    'test' {
        Write-Host "Ejecutando tests..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile exec $ServiceName pytest
    }
    
    'clean' {
        Write-Host "Limpiando contenedores y volúmenes..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile down -v
        docker-compose -f $ComposeDevFile down -v
        Write-Host "Limpieza completada" -ForegroundColor Green
    }
    
    'info' {
        Write-Host "Docker Version:" -ForegroundColor Cyan
        docker --version
        Write-Host ""
        Write-Host "Docker Compose Version:" -ForegroundColor Cyan
        docker-compose --version
        Write-Host ""
        Write-Host "Images:" -ForegroundColor Cyan
        docker images | Select-String "inverkids"
        Write-Host ""
        Write-Host "Running Containers:" -ForegroundColor Cyan
        docker ps --filter "name=inverkids"
    }
    
    'rebuild' {
        Write-Host "Reconstruyendo contenedor..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile down
        docker-compose -f $ComposeFile build
        docker-compose -f $ComposeFile up -d
        Write-Host "Reconstrucción completada" -ForegroundColor Green
    }
    
    'prod' {
        Write-Host "Iniciando en modo producción..." -ForegroundColor Cyan
        docker-compose -f $ComposeFile build
        docker-compose -f $ComposeFile up -d
        Write-Host "Producción iniciada. Ver logs con: .\docker-commands.ps1 logs" -ForegroundColor Green
    }
    
    'dev' {
        Write-Host "Iniciando en modo desarrollo..." -ForegroundColor Cyan
        docker-compose -f $ComposeDevFile build
        docker-compose -f $ComposeDevFile up -d
        Write-Host "Desarrollo iniciado. Ver logs con: .\docker-commands.ps1 dev-logs" -ForegroundColor Green
    }
}