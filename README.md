⚡ Live Network Analysis Dashboard
Python ve modern web teknolojileri kullanılarak geliştirilmiş, gerçek zamanlı ağ trafiğini coğrafi bir harita ve interaktif paneller üzerinde görselleştiren bir siber güvenlik aracı.

![image](https://github.com/user-attachments/assets/ba7cae06-1df7-4223-a738-59b92de41171)

🇹🇷 Türkçe
🚀 Özellikler
* Canlı Harita Görselleştirmesi: Gelen ve giden tüm ağ bağlantılarını, dünya üzerinde canlı ve renkli bir uydu haritasında anlık olarak gösterir.
* İnteraktif Protokol Grafiği: TCP, UDP ve diğer protokollere göre ağ trafiğinin dağılımını gösteren dinamik bir grafik sunar. Grafiğe tıklayarak bağlantıları filtreleme imkanı sağlar.
* Detaylı Bağlantı Bilgisi: Her bağlantı için IP adresi, port numarası, coğrafi konum (ülke/şehir), alan adı (hostname) ve organizasyon (ISP) gibi detaylı bilgiler sunar.
* IP İtibar Kontrolü: Bağlantı kurulan IP adreslerinin bilinen bir hosting veya proxy servisine ait olup olmadığını kontrol ederek "Normal" veya "Şüpheli" olarak işaretler ve görsel olarak uyarır.
* Tam Kontrol: "Durdur/Başlat" butonu ile canlı veri akışını anlık olarak kontrol etme ve "Haritayı Temizle" butonu ile tüm verileri sıfırlama imkanı sunar.
* Dahili Konsol: Tüm ağ aktivitelerini ve sistem mesajlarını terminal yerine doğrudan web arayüzündeki konsol panelinden takip etme olanağı sağlar.
🛠️ Kullanılan Teknolojiler
* Backend: Python, Flask, Flask-SocketIO, Scapy, Requests, Eventlet
* Frontend: HTML5, CSS3, JavaScript, Leaflet.js, Chart.js, Socket.IO-Client
⚙️ Kurulum ve Çalıştırma
Gereksinimler
1. Python 3.8+: Python'un resmi sitesinden indirip kurun.
2. Npcap: scapy kütüphanesinin Windows'ta düzgün çalışabilmesi için gereklidir.
   * Npcap'in resmi indirme sayfasına gidin ve son sürümü indirin.
   * Kurulum sırasında "Support WinPcap API-compatible mode" seçeneğini mutlaka işaretleyin.
Adımlar
1. Bu depoyu klonlayın veya dosyaları indirin.
2. Terminali açıp projenin ana klasörüne gidin ve gerekli Python kütüphanelerini yükleyin. Öncelikle requirements.txt dosyası oluşturmanız tavsiye edilir.
# (İsteğe bağlı, ama iyi bir pratiktir) Gereksinimler dosyasını oluşturun
pip freeze > requirements.txt

# Tüm bağımlılıkları yükleyin
pip install -r requirements.txt

Eğer requirements.txt dosyası oluşturmadıysanız, aşağıdaki komutları tek tek çalıştırın:
pip install flask flask-socketio scapy requests eventlet

3. Projeyi çalıştırmak için run_as_admin.bat dosyasına çift tıklayın. Bu dosya, programın ağı dinleyebilmesi için gerekli olan yönetici izinlerini otomatik olarak isteyecektir.
Program çalıştığında, varsayılan web tarayıcınızda http://127.0.0.1:5000 adresi otomatik olarak açılacaktır.
⚠️ Etik Kullanım Uyarısı
Bu araç, yalnızca eğitim ve yasal test amaçlı geliştirilmiştir. Bu aracı asla size ait olmayan veya test etme izninizin bulunmadığı sistemler üzerinde kullanmayın. İzin alınmadan yapılan tarama işlemleri yasa dışıdır ve siber suç teşkil edebilir.
🇬🇧 English
🚀 Features
   * Live Geo-Map Visualization: Instantly plots incoming and outgoing network connections on a live, satellite-view world map.
   * Interactive Protocol Chart: Displays a dynamic doughnut chart showing the distribution of TCP, UDP, and other protocols. Allows filtering connections by clicking on the chart.
   * Detailed Connection Info: Provides in-depth information for each connection, including IP address, port number, geographical location (country/city), hostname, and organization (ISP).
   * IP Reputation Check: Checks if a connected IP belongs to a known hosting or proxy service, marking it as "Normal" or "Suspicious" with visual cues.
   * Full Control Panel: Features a control panel to pause/resume the live data stream and clear all collected data and map markers with a single click.
   * Embedded Console: Allows monitoring all network activities and system messages directly within the web interface instead of a separate terminal.
🛠️ Tech Stack
   * Backend: Python, Flask, Flask-SocketIO, Scapy, Requests, Eventlet
   * Frontend: HTML5, CSS3, JavaScript, Leaflet.js, Chart.js, Socket.IO-Client
⚙️ Setup and Installation
Prerequisites
   1. Python 3.8+: Download and install from python.org.
   2. Npcap: Required for scapy to function correctly on Windows.
   * Go to the official Npcap download page and get the latest version.
   * During installation, make sure to check the "Support WinPcap API-compatible mode" option.
Steps
   1. Clone this repository or download the files.
git clone [your-repository-url]

   2. Navigate to the project's root directory and install the required Python libraries. It's recommended to create a requirements.txt file first.
# (Optional, but good practice) Create the requirements file
pip freeze > requirements.txt

# Install all dependencies
pip install -r requirements.txt

If you don't have a requirements.txt file, run the following commands one by one:
pip install flask flask-socketio scapy requests eventlet

   3. To run the project, simply double-click the run_as_admin.bat file. This batch file will automatically request the necessary administrator privileges to sniff network traffic.
Once the program starts, your default web browser will automatically open at http://127.0.0.1:5000.
⚠️ Ethical Use Disclaimer
This tool has been developed for educational and legal testing purposes only. NEVER use this tool on systems you do not own or have explicit permission to test. Unauthorized scanning is illegal and constitutes a cybercrime.
