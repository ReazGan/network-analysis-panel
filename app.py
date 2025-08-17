from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import webbrowser
import time
import socket
import platform
import logging
import sys 
import ctypes

try:
    from scapy.all import sniff, IP, TCP, UDP
    from scapy.arch.windows import get_windows_if_list
    import requests
except ImportError as e:
    print(f"[HATA] Gerekli bir kütüphane eksik: {e}. Lütfen 'pip install scapy requests' komutu ile yükleyin.")
    sys.exit()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_for_visualizer'
socketio = SocketIO(app, cors_allowed_origins="*")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

ip_cache = {}
hostname_cache = {}
MY_LOCATION = {"city": "İstanbul", "country": "Türkiye", "lat": 41.0082, "lon": 28.9784}
MY_LOCAL_IP = ""
sniffer_thread = None 

def get_my_ip():
    """Makinenin yerel IP adresini alır ve global değişkene atar."""
    global MY_LOCAL_IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        MY_LOCAL_IP = s.getsockname()[0]
    except Exception:
        MY_LOCAL_IP = '127.0.0.1'
    finally:
        s.close()
    print(f"[*] Yerel IP Adresi: {MY_LOCAL_IP} olarak ayarlandı.")

def get_hostname(ip):
    """Verilen bir IP için ters DNS sorgusu yapar."""
    if ip in hostname_cache:
        return hostname_cache[ip]
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        hostname_cache[ip] = hostname
        return hostname
    except (socket.herror, socket.gaierror):
        hostname_cache[ip] = ip
        return ip

def get_geolocation_and_reputation(ip):
    """
    Verilen bir IP adresi için coğrafi konum ve itibar bilgilerini getirir.
    ip-api.com'un 'hosting' ve 'proxy' alanlarını itibar için kullanıyoruz.
    """
    if ip in ip_cache or ip.startswith(('192.168', '10.', '127.')) or ip == MY_LOCAL_IP:
        return None
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,lat,lon,city,country,hosting,proxy,query,org', timeout=2)
        response.raise_for_status()
        data = response.json()
        if data.get('status') == 'success' and data.get('lat') and data.get('lon'):
            reputation = "Şüpheli" if data.get('hosting') or data.get('proxy') else "Normal"
            
            geo_data = {
                'ip': data.get('query'), 
                'lat': data.get('lat'), 
                'lon': data.get('lon'), 
                'city': data.get('city'), 
                'country': data.get('country'),
                'reputation': reputation,
                'org': data.get('org', 'Bilinmiyor')
            }
            ip_cache[ip] = geo_data
            return geo_data
    except requests.exceptions.RequestException:
        pass
    return None

def process_packet(packet):
    """Yakalanan her paketi işler ve verileri ön yüze gönderir."""
    if IP in packet:
        src_ip, dst_ip = packet[IP].src, packet[IP].dst
        if src_ip == MY_LOCAL_IP or dst_ip == MY_LOCAL_IP:
            external_ip = dst_ip if src_ip == MY_LOCAL_IP else src_ip
            geo_data = get_geolocation_and_reputation(external_ip)
            if geo_data:
                proto = "Diğer"
                port = 0
                if TCP in packet:
                    proto = "TCP"
                    port = packet[TCP].dport if src_ip == MY_LOCAL_IP else packet[TCP].sport
                elif UDP in packet:
                    proto = "UDP"
                    port = packet[UDP].dport if src_ip == MY_LOCAL_IP else packet[UDP].sport
                
                hostname = get_hostname(external_ip)
                
                destination_data = {**geo_data, "port": port, "hostname": hostname}
                map_data = {"source": {**MY_LOCATION, "ip": MY_LOCAL_IP}, "destination": destination_data, "protocol": proto}
                
                socketio.emit('new_connection', map_data)
                socketio.sleep(0.05)

def sniff_packets_task():
    """Ağ paketlerini dinleyen fonksiyon (thread görevi)."""
    interface_to_sniff = find_best_interface()
    
    print("[+] Sniffing thread'i başlatıldı.")
    socketio.emit('log_update', {'data': "[*] Ağ trafiği dinleniyor..."})
    try:
        sniff(prn=process_packet, store=0, iface=interface_to_sniff)
    except Exception as e:
        error_msg = f"[HATA] Paket dinleme başarısız: {e}."
        print(error_msg)
        socketio.emit('log_update', {'data': error_msg})
    print("[-] Sniffing thread'i sonlandı.")

def find_best_interface():
    """Windows'ta dinleme yapılacak en iyi ağ arayüzünü (interface) bulur."""
    if platform.system() != "Windows":
        return None
    interfaces = get_windows_if_list()
    for iface in interfaces:
        if MY_LOCAL_IP in iface.get('ips', []):
            print(f"[*] Aktif ağ arayüzü bulundu: {iface.get('name')}")
            return iface.get('name')
    print("[UYARI] Aktif ağ arayüzü otomatik olarak bulunamadı.")
    return None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global sniffer_thread
    print("[+] Web arayüzü bağlandı.")
    socketio.emit('log_update', {'data': "[*] Arayüze başarıyla bağlanıldı."})
    socketio.emit('log_update', {'data': f"[*] Yerel IP Adresiniz: {MY_LOCAL_IP}."})
    if sniffer_thread is None:
        print("[*] Sniffer thread'i başlatılıyor...")
        sniffer_thread = socketio.start_background_task(target=sniff_packets_task)
    else:
        print("[*] Sniffer thread'i zaten çalışıyor.")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
    if platform.system() == "Windows" and not is_admin():
        print("\n[HATA] YÖNETİCİ İZNİ GEREKLİ! Lütfen 'run_as_admin.bat' dosyasını kullanarak çalıştırın.\n")
        sys.exit()

    get_my_ip()
    threading.Timer(1, open_browser).start()
    print("[*] Sunucu http://127.0.0.1:5000 adresinde başlatılıyor... Çıkmak için CTRL+C'ye basın.")
    socketio.run(app, host='127.0.0.1', port=5000)


