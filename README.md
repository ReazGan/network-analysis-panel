Gelişmiş Ağ Analiz Paneli
Bu proje, Python ve modern web teknolojileri kullanılarak geliştirilmiş, gerçek zamanlı ağ trafiğini coğrafi bir harita ve interaktif paneller üzerinde görselleştiren bir siber güvenlik aracıdır.

🚀 Özellikler
Canlı Harita Görselleştirmesi: Gelen ve giden tüm ağ bağlantılarını, dünya üzerinde canlı ve renkli bir uydu haritasında anlık olarak gösterir.

İnteraktif Protokol Grafiği: TCP, UDP ve diğer protokollere göre ağ trafiğinin dağılımını gösteren dinamik bir grafik sunar. Grafiğe tıklayarak bağlantıları filtreleme imkanı sağlar.

Detaylı Bağlantı Bilgisi: Her bağlantı için IP adresi, port numarası, coğrafi konum (ülke/şehir), alan adı (hostname) ve organizasyon (ISP) gibi detaylı bilgiler sunar.

IP İtibar Kontrolü: Bağlantı kurulan IP adreslerinin bilinen bir hosting veya proxy servisine ait olup olmadığını kontrol ederek "Normal" veya "Şüpheli" olarak işaretler ve görsel olarak uyarır.

Tam Kontrol: "Durdur/Başlat" butonu ile canlı veri akışını anlık olarak kontrol etme ve "Haritayı Temizle" butonu ile tüm verileri sıfırlama imkanı sunar.

Dahili Konsol: Tüm ağ aktivitelerini ve sistem mesajlarını terminal yerine doğrudan web arayüzündeki konsol panelinden takip etme olanağı sağlar.

🛠️ Kullanılan Teknolojiler
Backend: Python, Flask, Flask-SocketIO, Scapy, Requests

Frontend: HTML5, CSS3, JavaScript, Leaflet.js, Chart.js, Socket.IO-Client

Kurulum ve Çalıştırma
Gereksinimler
Python 3: Python'un resmi sitesinden indirip kurun.

Npcap: scapy kütüphanesinin Windows'ta düzgün çalışabilmesi için gereklidir.

Npcap'in resmi indirme sayfasına gidin ve son sürümü indirin.

Kurulum sırasında "Support WinPcap API-compatible mode" seçeneğini mutlaka işaretleyin.

Adımlar
Bu depoyu klonlayın veya dosyaları indirin.

Terminali açıp projenin ana klasörüne gidin ve gerekli Python kütüphanelerini yükleyin:

pip install -r requirements.txt

(Eğer requirements.txt dosyası yoksa, aşağıdaki komutları tek tek çalıştırın):

pip install flask flask-socketio scapy requests eventlet

Projeyi çalıştırmak için run_as_admin.bat dosyasına çift tıklayın. Bu dosya, programın ağı dinleyebilmesi için gerekli olan yönetici izinlerini otomatik olarak isteyecektir.

Program çalıştığında, varsayılan web tarayıcınızda http://127.0.0.1:5000 adresi otomatik olarak açılacaktır.

⚠️ Etik Kullanım Uyarısı
Bu araç, yalnızca eğitim ve yasal test amaçlı geliştirilmiştir. Bu aracı asla size ait olmayan veya test etme izninizin bulunmadığı sistemler üzerinde kullanmayın. İzin alınmadan yapılan tarama işlemleri yasa dışıdır ve siber suç teşkil edebilir.