import time 
def pomodora_timer(work_time=25, short_break=5, long_break=15, cycles=4):
      """
    Pomodoro Tekniği Zamanlayıcısı
    - work_time: Çalışma süresi (dakika)
    - short_break: Kısa mola süresi (dakika)
    - long_break: Uzun mola süresi (dakika)
    - cycles: Toplam pomodoro sayısı (bir uzun moladan önce kaç döngü olacak)
    """
    for cycle in range (1,cycles+1):
        print(f"{cycle}. Pomodoro: Çalışma zamanı! ({work_time} dakika)")
        countdown(work_time * 60)  # Çalışma süresi
        else:
            print(f"Uzun mola! ({long_break} dakika)")
            countdown(long_break * 60)  # Uzun mola süresi
def countdown(seconds):
    """
    Geri sayım fonksiyonu, saniye bazlı bir süreyi geri sayar.
    """
    while seconds:
          mins, secs = divmod(seconds, 60)  # Dakika ve saniyeyi ayır
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')  # Aynı satıra yaz
        time.sleep(1)  # 1 saniye bekle
        seconds -= 1
    print("Süre doldu!\n")

# Pomodoro zamanlayıcısını başlat
pomodoro_timer()