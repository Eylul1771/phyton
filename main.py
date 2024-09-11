# Gerekli kütüphaneleri yükleme
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import random

# NLTK veri setlerini indirme
nltk.download('punkt')
nltk.download('wordnet')

# Lemmatizer'ı başlatma
lemmer = WordNetLemmatizer()

# Fonksiyon: Lemmatization (kelimeleri köklerine indirme)
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

# Fonksiyon: Noktalama işaretlerini kaldırma ve kelimelere bölme
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Örnek sohbet metni
sohbet_metni = """
Merhaba! Sana nasıl yardımcı olabilirim? Nasılsın? Ben iyiyim, teşekkür ederim. 
Bugün hava güzel mi? Hava durumu hakkında konuşalım. 
Python programlama dili çok popülerdir. Neler öğrenmek istiyorsun?
"""

# Metni cümlelere bölme
sent_tokens = nltk.sent_tokenize(sohbet_metni)

# Basit bir cevap verme fonksiyonu
def yanit_ver(kullanici_girdisi):
    kullanici_girdisi = kullanici_girdisi.lower()
    girisler = ("merhaba", "selam", "nasılsın", "naber", "görüşürüz", "hoşça kal", "teşekkür ederim", "sağol")
    yanitlar = ["Merhaba! Sana nasıl yardımcı olabilirim?", 
                "Selam! Nasıl yardımcı olabilirim?", 
                "İyiyim, teşekkür ederim! Sen nasılsın?", 
                "Merhaba! Bir şey mi sormak istedin?", 
                "Görüşmek üzere!", 
                "Hoşça kal! Yardımcı olabileceğim başka bir şey var mı?", 
                "Rica ederim!", 
                "Teşekkürler, sana nasıl yardımcı olabilirim?"]
    
    for i, kelime in enumerate(girisler):
        if kelime in kullanici_girdisi:
            return yanitlar[i]
    return None

# Gelişmiş yanıt fonksiyonu: cosine similarity kullanarak en uygun cevabı bulma
def en_iyi_cevap(kullanici_girdisi):
    sent_tokens.append(kullanici_girdisi)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    skor = flat[-2]
    
    if skor == 0:
        return "Üzgünüm, seni anlayamadım."
    else:
        return sent_tokens[idx]

# Gelişmiş chatbot fonksiyonu
def chatbot():
    print("Chatbot: Merhaba! Bana soru sorabilirsin. (Çıkmak için 'çık' yaz)")
    while True:
        kullanici_girdisi = input("Sen: ")
        if kullanici_girdisi.lower() == 'çık':
            print("Chatbot: Görüşmek üzere!")
            break
        else:
            # Öncelikle sabit cevaplar kontrol edilir
            cevap = yanit_ver(kullanici_girdisi)
            if cevap:
                print(f"Chatbot: {cevap}")
            else:
                # Eğer sabit bir cevap yoksa, gelişmiş yanıt fonksiyonu kullanılır
                print(f"Chatbot: {en_iyi_cevap(kullanici_girdisi)}")
                sent_tokens.remove(kullanici_girdisi)

# Chatbot'u başlatma
chatbot()
