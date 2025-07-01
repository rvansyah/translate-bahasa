import streamlit as st

try:
    from googletrans import Translator
    googletrans_ok = True
except ModuleNotFoundError:
    googletrans_ok = False

# Contoh kamus bahasa daerah Indonesia
bahasa_daerah_dict = {
    'jawa': {
        'halo': 'halo',
        'selamat pagi': 'sugeng enjing',
        'terima kasih': 'matur nuwun',
        'bagaimana kabarmu?': 'piye kabarmu?',
    },
    'sunda': {
        'halo': 'halo',
        'selamat pagi': 'wilujeng enjing',
        'terima kasih': 'hatur nuhun',
        'bagaimana kabarmu?': 'kumaha damang?',
    },
    'batak': {
        'halo': 'horas',
        'selamat pagi': 'selamat pagi',
        'terima kasih': 'mauliate',
        'bagaimana kabarmu?': 'bagaimana kabarmu?',
    }
}

def translate_daerah(text, daerah):
    dictionary = bahasa_daerah_dict.get(daerah, {})
    return dictionary.get(text.lower(), '[Terjemahan tidak tersedia]')

st.title("Aplikasi Translate Otomatis Bahasa Dunia & Bahasa Daerah Indonesia")
st.write("""
Aplikasi ini dapat menerjemahkan antar bahasa dunia dengan deteksi otomatis serta beberapa bahasa daerah Indonesia (Jawa, Sunda, Batak).
""")

jenis = st.radio(
    "Pilih jenis terjemahan:", 
    ('Bahasa Dunia (Deteksi Otomatis)', 'Bahasa Daerah Indonesia')
)

if jenis == 'Bahasa Dunia (Deteksi Otomatis)':
    text = st.text_area("Masukkan teks yang ingin diterjemahkan:")
    dest = st.text_input("Kode bahasa tujuan (misal: 'en', 'ar', 'ja'):", value='en')
    if st.button("Terjemahkan"):
        if not googletrans_ok:
            st.error("Modul googletrans belum ter-install. Tambahkan 'googletrans==4.0.0rc1' ke requirements.txt dan deploy ulang.")
        elif text.strip() == "":
            st.warning("Teks tidak boleh kosong.")
        else:
            try:
                translator = Translator()
                result = translator.translate(text, src='auto', dest=dest)
                detected = result.src
                st.info(f"Deteksi bahasa: {detected}")
                st.success(f"Hasil Terjemahan ({detected} → {dest}):")
                st.write(result.text)
            except Exception as e:
                st.error(f"Gagal menerjemahkan: {e}")

elif jenis == 'Bahasa Daerah Indonesia':
    text = st.text_area("Masukkan kalimat (contoh: 'halo', 'selamat pagi', 'terima kasih', 'bagaimana kabarmu?'):")
    daerah = st.selectbox("Pilih bahasa daerah:", list(bahasa_daerah_dict.keys()))
    if st.button("Terjemahkan ke Bahasa Daerah"):
        if text.strip() == "":
            st.warning("Teks tidak boleh kosong.")
        else:
            hasil = translate_daerah(text, daerah)
            st.success(f"Hasil Terjemahan ke {daerah.capitalize()}:")
            st.write(hasil)

st.markdown("---")
st.markdown("**Catatan:** Untuk bahasa daerah, kosakata masih terbatas. Silakan kontribusi untuk menambah kosakata!")
