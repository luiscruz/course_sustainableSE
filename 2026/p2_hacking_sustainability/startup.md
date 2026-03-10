# Getting Started with Carbon Aware CLI

This guide walks you through everything needed to build and run the [Carbon Aware SDK](https://github.com/Green-Software-Foundation/carbon-aware-sdk) CLI (`caw`) and retrieve CO₂/kWh emissions data for the Netherlands (`westeurope`).

---

## Prerequisites

- **Git**
- **.NET 8 SDK** — version ≥ 8.0.201 (the repo's `global.json` pins `rollForward: latestFeature`)
  - Download: https://dotnet.microsoft.com/download/dotnet/8.0
  - Verify: `dotnet --version`

---

## 1. Clone the Repository

```powershell
git clone https://github.com/Green-Software-Foundation/carbon-aware-sdk.git
cd carbon-aware-sdk
```

The guide assumes all subsequent commands are run from inside the `carbon-aware-sdk/` root unless stated otherwise.

---

## 2. Configure the Data Source

The CLI reads configuration from `appsettings.Development.json` (loaded when `ASPNETCORE_ENVIRONMENT=Development`). A template is provided — copy it and edit it:

```powershell
Copy-Item .\src\CarbonAware.CLI\src\appsettings.Development.json.template `
          .\src\CarbonAware.CLI\src\appsettings.Development.json
```

There are two sensible options depending on whether you have API credentials.

---

### Option A — Offline JSON test data (no credentials required)

This uses a static snapshot of Azure-region emissions included in the repo. Time range is limited to dates in the test file (~Nov 2021 for `westeurope`), but it is enough to verify the tool works end-to-end.

Replace the contents of `appsettings.Development.json` with:

```json
{
  "LocationDataSourcesConfiguration": {
    "LocationSourceFiles": [
      { "DataFileLocation": "azure-regions.json" }
    ]
  },
  "DataSources": {
    "EmissionsDataSource": "test-json",
    "Configurations": {
      "test-json": {
        "Type": "JSON",
        "DataFileLocation": "test-data-azure-emissions.json"
      }
    }
  }
}
```

> **Note:** JSON is not supported as a `ForecastDataSource` — omit that key entirely or the CLI will crash on startup.

---

### Option B — WattTime live API (real-time data, free-tier restricted)

WattTime's free tier only allows the `/index` endpoint (current marginal intensity only). The `/historical` and `/forecast` endpoints that the CLI uses require a paid account.

If you have a WattTime account, use the **v3** base URL (the SDK has been updated to v3 paths):

```json
{
  "LocationDataSourcesConfiguration": {
    "LocationSourceFiles": [
      { "DataFileLocation": "azure-regions.json" }
    ]
  },
  "DataSources": {
    "EmissionsDataSource": "WattTime",
    "ForecastDataSource": "WattTime",
    "Configurations": {
      "WattTime": {
        "Type": "WattTime",
        "Username": "<your-username>",
        "Password": "<your-password>",
        "BaseURL": "https://api.watttime.org/v3/",
        "SignalType": "co2_moer"
      }
    }
  }
}
```

> **⚠️ Important:** Use `https://api.watttime.org/v3/` — the old `https://api2.watttime.org/v2/` URL in the template is no longer valid and returns 403 on all data endpoints.

Sign up: https://www.watttime.org/api-documentation/
Also in testing.ipynb

---

## 3. Build the CLI Binary

From the repo root, publish a self-contained Windows binary:

```powershell
dotnet publish .\src\CarbonAware.CLI\src\CarbonAware.CLI.csproj `
  -c Release -r win-x64 --self-contained `
  -o .\bin\caw
```

For other platforms, replace `win-x64` with `linux-x64` or `osx-x64`.

The binary is named `caw.exe` (Windows) or `caw` (Linux/macOS).

---

## 4. Copy Data Files to the Publish Output

The build does **not** automatically copy the location and emissions data files into the output directory. Do this manually after publishing:

```powershell
# Location name → coordinates mapping (required by all data sources)
Copy-Item .\src\data\location-sources\*.json .\bin\caw\location-sources\json\

# Static test emissions data (only needed for Option A / JSON source)
New-Item -ItemType Directory -Force .\bin\caw\data-sources\json | Out-Null
Copy-Item .\src\data\data-sources\*.json .\bin\caw\data-sources\json\
```

> You only need to do this once per publish. If you republish, repeat this step.

---

## 5. Verify the Binary Works

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"
.\bin\caw\caw.exe -h
```

Expected output:

```
Description:
  A command line tool for accessing data relevant to carbon awareness.

Usage:
  caw [command] [options]

Commands:
  emissions            Emissions command keyword to retrieve emissions data
  emissions-forecasts  Gets emissions forecast data for given locations.
  locations            Returns all the supported locations
```

---

## 6. List Available Locations

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"
.\bin\caw\caw.exe locations | ConvertFrom-Json | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name | Sort-Object
```

The Netherlands corresponds to **`westeurope`** (Azure's Amsterdam datacenter, lat 52.37°N / lon 4.9°E).

---

## 7. Get CO₂/kWh Emissions for the Netherlands

### With JSON test data (Option A)

The test file contains `westeurope` data for dates around November 2021. Query a week of data:

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"
.\bin\caw\caw.exe emissions -l westeurope `
  -s 2021-11-17T00:00:00Z `
  -e 2021-11-24T00:00:00Z
```

Example output (truncated):

```json
[
  {"Location":"westeurope","Time":"2021-11-17T04:45:11+00:00","Rating":65,"Duration":"08:00:00"},
  {"Location":"westeurope","Time":"2021-11-17T12:45:11+00:00","Rating":97,"Duration":"08:00:00"},
  {"Location":"westeurope","Time":"2021-11-17T20:45:11+00:00","Rating":19,"Duration":"08:00:00"},
  ...
]
```

The `Rating` field is in **gCO₂eq/kWh**. `Duration` is the granularity of each data point.

Get the single lowest-carbon moment in that window:

```powershell
.\bin\caw\caw.exe emissions -l westeurope `
  -s 2021-11-17T00:00:00Z -e 2021-11-24T00:00:00Z `
  --best
```

Get the weighted average over the window:

```powershell
.\bin\caw\caw.exe emissions -l westeurope `
  -s 2021-11-17T00:00:00Z -e 2021-11-24T00:00:00Z `
  --average
```

### With WattTime or ElectricityMaps (Options B / C)

With a live API, no date flags are needed — the CLI defaults to a recent window:

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"
.\bin\caw\caw.exe emissions -l westeurope
```

---

## 8. Get Emissions Forecasts for the Netherlands (requires live API)

Forecasts require Option B (WattTime paid) or Option C (ElectricityMaps):

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"

# Current forecast for the Netherlands
.\bin\caw\caw.exe emissions-forecasts -l westeurope

# Forecast with a 60-minute workload window
.\bin\caw\caw.exe emissions-forecasts -l westeurope -w 60

# Forecast filtered to a specific time window
.\bin\caw\caw.exe emissions-forecasts -l westeurope `
  --data-start-at 2026-03-11T08:00:00Z `
  --data-end-at   2026-03-11T20:00:00Z `
  -w 30
```

Example output structure:

```json
[{
  "requestedAt": "2026-03-10T20:00:00+00:00",
  "generatedAt": "2026-03-10T19:55:00+00:00",
  "location": "westeurope",
  "dataStartAt": "2026-03-10T20:00:00Z",
  "dataEndAt": "2026-03-11T20:00:00Z",
  "windowSize": 60,
  "optimalDataPoint": {
    "location": "NL",
    "timestamp": "2026-03-11T03:00:00+00:00",
    "duration": 60,
    "value": 142.5
  },
  "forecastData": [ ... ]
}]
```

---

## Quick Reference

| Goal | Command |
|---|---|
| Help | `.\bin\caw\caw.exe -h` |
| List locations | `.\bin\caw\caw.exe locations` |
| Emissions for NL (window) | `.\bin\caw\caw.exe emissions -l westeurope -s <start> -e <end>` |
| Best (lowest) point in window | `.\bin\caw\caw.exe emissions -l westeurope -s <start> -e <end> --best` |
| Average over window | `.\bin\caw\caw.exe emissions -l westeurope -s <start> -e <end> --average` |
| Current forecast for NL | `.\bin\caw\caw.exe emissions-forecasts -l westeurope` |
| Forecast with workload window | `.\bin\caw\caw.exe emissions-forecasts -l westeurope -w <minutes>` |

All commands require `$env:ASPNETCORE_ENVIRONMENT = "Development"` to be set so the CLI picks up `appsettings.Development.json`.

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `Unknown Location: 'westeurope' not found` | `location-sources/json/` folder is empty in publish output | Re-run the Copy-Item step in §4 |
| `WattTimeClientHttpException 403` on `/historical` or `/forecast` | WattTime free tier only allows `/index` | Upgrade account or switch to ElectricityMaps |
| `WattTimeClientHttpException 403` on `/region-from-loc` | Wrong BaseURL (old v2 URL) | Use `https://api.watttime.org/v3/` |
| `JSON data source is not supported for forecast data` | `ForecastDataSource` set to `test-json` | Remove `ForecastDataSource` key from config when using JSON |
| `ForecastDataSource is not configured` | No forecast source in config | Add WattTime or ElectricityMaps config block |
