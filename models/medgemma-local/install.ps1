param(
    [ValidateSet("auto","cuda","mps","cpu")][string]$Backend = "auto",
    [switch]$Apply,
    [string]$TorchIndex = "https://download.pytorch.org/whl/cu126"
)
$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
Set-Location $root
$cmd = @("models/medgemma-local/install.py", "--backend", $Backend, "--torch-index", $TorchIndex)
if ($Apply) { $cmd += "--apply" }
py -3.11 @cmd
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
