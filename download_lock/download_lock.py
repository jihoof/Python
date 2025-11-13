# Save as Remove-Smoothwall-Windows.ps1 and run as Administrator
Write-Host "== Smoothwall 제거 스크립트 시작 ==" -ForegroundColor Cyan

# 1. 탐지: 설치된 프로그램 (레지스트리에서)
Write-Host "`n-- 1) 설치된 프로그램(레지스트리) 검사 --" -ForegroundColor Yellow
$keys = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*"
)
$foundProducts = @()
foreach ($k in $keys) {
    Get-ItemProperty $k -ErrorAction SilentlyContinue |
    Where-Object { $_.DisplayName -match "Smoothwall|Smooth Wall|Guardian|Filter Agent|Proxy Agent|SSL Inspection" } |
    ForEach-Object {
        $foundProducts += $_
    }
}
if ($foundProducts.Count -eq 0) {
    Write-Host "설치된 Smoothwall 관련 프로그램을 찾지 못했습니다." -ForegroundColor Green
} else {
    Write-Host "발견된 항목:" -ForegroundColor Red
    $foundProducts | Format-Table DisplayName, DisplayVersion, Publisher, UninstallString -AutoSize
}

# 2. 서비스 및 프로세스 검사
Write-Host "`n-- 2) 서비스 및 프로세스 검사 --" -ForegroundColor Yellow
$svcCandidates = Get-Service | Where-Object { $_.Name -match "smoothwall|smooth|guardian|filter|proxy" -or $_.DisplayName -match "smoothwall|guardian|filter|proxy" }
$procCandidates = Get-Process | Where-Object { $_.ProcessName -match "smoothwall|smooth|guardian|filter|proxy" } -ErrorAction SilentlyContinue

if ($svcCandidates) {
    Write-Host "발견된 서비스:" -ForegroundColor Red
    $svcCandidates | Format-Table Name, DisplayName, Status -AutoSize
} else { Write-Host "서비스 없음." -ForegroundColor Green }

if ($procCandidates) {
    Write-Host "발견된 프로세스:" -ForegroundColor Red
    $procCandidates | Format-Table ProcessName, Id, Path -AutoSize
} else { Write-Host "프로세스 없음." -ForegroundColor Green }

# 3. 인증서(신뢰 루트) 검사
Write-Host "`n-- 3) 로컬 컴퓨터의 '신뢰할 수 있는 루트 인증 기관'에 Smoothwall 관련 인증서가 있는지 검사 --" -ForegroundColor Yellow
$store = New-Object System.Security.Cryptography.X509Certificates.X509Store("Root","LocalMachine")
$store.Open('ReadOnly')
$certs = $store.Certificates | Where-Object { $_.Subject -match "Smoothwall|Smooth Wall|Guardian|Proxy" -or $_.Issuer -match "Smoothwall|Guardian|Proxy" }
if ($certs.Count -gt 0) {
    Write-Host "발견된 인증서:" -ForegroundColor Red
    foreach ($c in $certs) {
        Write-Host "Subject: $($c.Subject) | Thumbprint: $($c.Thumbprint)"
    }
    Write-Host "`n인증서를 삭제하시겠습니까? (Y/N): " -NoNewline
    $ans = Read-Host
    if ($ans -match '^[Yy]') {
        $store.Close()
        $store = New-Object System.Security.Cryptography.X509Certificates.X509Store("Root","LocalMachine")
        $store.Open('ReadWrite')
        foreach ($c in $certs) {
            $store.Remove($c)
            Write-Host "삭제: $($c.Subject)"
        }
        $store.Close()
        Write-Host "인증서 삭제 완료." -ForegroundColor Green
    } else { Write-Host "인증서 삭제 취소됨." -ForegroundColor Yellow }
} else { Write-Host "Smoothwall 관련 인증서 없음." -ForegroundColor Green; $store.Close() }

# 4. 발견된 설치 항목 자동 제거 시도 (사용자 동의 필요)
if ($foundProducts.Count -gt 0) {
    Write-Host "`n설치 제거를 시도하려면 'Y' 입력:" -NoNewline
    $r = Read-Host
    if ($r -match '^[Yy]') {
        foreach ($p in $foundProducts) {
            $u = $p.UninstallString
            if ($u) {
                Write-Host "제거 시도: $($p.DisplayName)"
                # UninstallString가 msiexec 인자일 경우 적절히 실행
                if ($u -match "msiexec" ) {
                    Start-Process -FilePath "msiexec.exe" -ArgumentList "$($u -replace '.*msiexec.exe\s*','')" -Wait -NoNewWindow
                } else {
                    # 일반 실행파일 제거 커맨드
                    Start-Process -FilePath "cmd.exe" -ArgumentList "/C `"$u`"" -Wait -NoNewWindow
                }
                Write-Host "완료: $($p.DisplayName)"
            } else {
                Write-Host "UninstallString 없음: $($p.DisplayName)" -ForegroundColor Yellow
            }
        }
    } else { Write-Host "프로그램 제거 단계 건너뜀." -ForegroundColor Yellow }
}

# 5. 서비스 강제 중지 및 제거 (사용자 동의)
if ($svcCandidates.Count -gt 0) {
    Write-Host "`n서비스를 강제로 중지하고 삭제하려면 'Y' 입력:" -NoNewline
    $sans = Read-Host
    if ($sans -match '^[Yy]') {
        foreach ($svc in $svcCandidates) {
            try {
                Stop-Service -Name $svc.Name -Force -ErrorAction Stop
                sc.exe delete $svc.Name | Out-Null
                Write-Host "삭제된 서비스: $($svc.Name)"
            } catch {
                Write-Host "서비스 삭제 실패: $($svc.Name) - $($_.Exception.Message)" -ForegroundColor Red
            }
        }
    } else { Write-Host "서비스 삭제 건너뜀." -ForegroundColor Yellow }
}

Write-Host "`n== 작업 완료: 검사/일부 제거(선택) 종료 ==" -ForegroundColor Cyan
Write-Host "그 외에 'C:\Program Files', 'C:\Program Files (x86)', 'C:\ProgramData' 안의 smooth* 폴더를 수동 확인하세요."
