param(
    [int]$Iterations = 30,
    [string]$PythonExe = ".\\venv\\Scripts\\python.exe",
    [string]$EnergibridgeExe = ".\\energibridge.exe"
)

$ErrorActionPreference = "Stop"

function Invoke-Measurement {
    param(
        [Parameter(Mandatory = $true)][string]$OutputCsv,
        [Parameter(Mandatory = $true)][string]$ScriptName
    )

    & $EnergibridgeExe --output $OutputCsv --summary -- $PythonExe $ScriptName
    if ($LASTEXITCODE -ne 0) {
        throw "Energibridge command failed for $ScriptName (exit code: $LASTEXITCODE)"
    }

    Start-Sleep -Seconds 2
}

if (-not (Test-Path $EnergibridgeExe)) {
    throw "Could not find Energibridge executable at: $EnergibridgeExe"
}

if (-not (Test-Path $PythonExe)) {
    throw "Could not find Python executable at: $PythonExe"
}

$serviceName = "LibreHardwareMonitor"

$serviceQuery = sc.exe query $serviceName 2>&1 | Out-String
if ($serviceQuery -match "FAILED 1060") {
    Write-Host "Creating LibreHardwareMonitor service..."
    sc.exe create $serviceName type= kernel binPath= "$pwd\LibreHardwareMonitor.sys" | Out-Null
}

$serviceStatus = sc.exe query $serviceName 2>&1 | Out-String
if ($serviceStatus -notmatch "RUNNING") {
    Write-Host "Starting LibreHardwareMonitor service..."
    sc.exe start $serviceName | Out-Null
}

Write-Host "Running $Iterations iterations for json and orjson..."

for ($i = 1; $i -le $Iterations; $i++) {
    $jsonOutput = "energy_json_run{0:D2}.csv" -f $i
    $orjsonOutput = "energy_orjson_run{0:D2}.csv" -f $i

    Write-Host "[$i/$Iterations] Measuring read_json.py -> $jsonOutput"
    Invoke-Measurement -OutputCsv $jsonOutput -ScriptName "read_json.py"

    Write-Host "[$i/$Iterations] Measuring read_orjson.py -> $orjsonOutput"
    Invoke-Measurement -OutputCsv $orjsonOutput -ScriptName "read_orjson.py"
}

Write-Host "Finished. Created $Iterations JSON and $Iterations ORJSON measurement files."
