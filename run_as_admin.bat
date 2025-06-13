@echo off

:: =================================================================
:: Yönetici İzinlerini Kontrol Et ve İstek Gönder
:: =================================================================
REM Yönetici oturumu olup olmadığını kontrol et
net session >nul 2>&1
REM Eğer hata varsa (izin yoksa), script'i yönetici olarak yeniden başlat
if %errorLevel% NEQ 0 (
    echo [ISTEK] Yonetici izinleri isteniyor...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit
)

:: =================================================================
:: Programı Başlat
:: =================================================================
echo [BILGI] Yonetici izinleri onaylandi.
echo [BILGI] Uygulama baslatiliyor...

:: Batch dosyasının bulunduğu dizine git
cd /d "%~dp0"

:: Python script'ini çalıştır
py app.py

echo.
echo [BILGI] Uygulama kapatildi. Kapatmak icin bir tusa basin.
pause >nul
