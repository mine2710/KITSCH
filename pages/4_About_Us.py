import streamlit as st

st.markdown("<h1 style='text-align: center;'>KITSCH</h1>",unsafe_allow_html=True )
# Mendapatkan lebar halaman


# Membagi layout menjadi beberapa kolom


# Menampilkan teks di kolom tengah

# Menampilkan gambar di kolom 
image1, image2, image3 = st.columns([3,7,1])
with image1:
    st.write("")
with image2:
    st.image("pages/yang asli.png", width=300)
with image3:
    st.write("")
# image_path = "pages/yang_bener.png" 

# st.image(image_path, caption='kitch', use_column_width=True)# Fungsi untuk menampilkan gambar dan teks di tengah
# def centered_text_and_image():
s1, s2= st.columns(2)
with s1:
    st.subheader("Apa, sih, itu Kitsch?")
    st.write("kita ibaratkan objeknya adalah tulisan, di mana tulisan ini tentunya ditulis dengan melibatkan emosi penulisnya. apapun kategori atau genre dari tulisannya, tentu ada emosi yang ikut andil: seperti emosi berupa rasa senang, sedih, semangat yang dirasakan penulis ketika menulis tulisannya. tidak hanya melibatkan emosi penulis, tetapi juga melibatkan emosi pembaca: seperti timbulnya emosi berupa rasa senang apabila pembaca membaca tulisan yang sesuai dengan minat dan hobi mereka")
    st.write("Istilah 'kitsch' atau 'kitsch' merujuk pada gaya seni atau desain yang dianggap sebagai rendah, berlebihan, atau bahkan kurang berkualitas secara estetika. Istilah ini sering digunakan untuk menggambarkan sesuatu yang dianggap sebagai 'berlebihan' atau 'terlalu mencolok' secara artistik, sering kali di luar norma seni yang dianggap sebagai standar tinggi atau memiliki nilai artistik yang tinggi.")
    st.write("kitsch dapat terdiri dari elemen-elemen seperti dekorasi rumah yang berlebihan dalam motif dan aksen, lukisan-lukisan dengan estetika yang terlalu berlebihan atau berwarna-warni, hingga barang-barang hiasan yang dianggap tidak bermakna secara artistik tetapi memiliki daya tarik komersial atau sentimental yang kuat.")
    st.write("Istilah ini bersifat subjektif dan tergantung pada preferensi estetika individu. Apa yang dianggap kitsch oleh satu orang mungkin dianggap menarik atau estetis oleh orang lain. Pemahaman akan kitsch sering kali berkaitan dengan konteks budaya dan perkembangan seni pada suatu periode waktu tertentu.")
with s2:
    st.subheader("Membangun Masyarakat Literasi di Indonesia: Membaca, Menulis, dan Membagikan Pengetahuan")
    st.write("Indonesia adalah negeri yang kaya akan budaya, tetapi tantangan literasi masih menjadi salah satu aspek kritis dalam perkembangan masyarakat. Literasi tidak hanya sebatas kemampuan membaca dan menulis, tetapi juga bagaimana kita memanfaatkan pengetahuan dalam kehidupan sehari-hari. Dalam upaya untuk meningkatkan literasi, langkah-langkah inovatif dan kolaboratif sangatlah penting.")
    st.subheader("Pentingnya Literasi di Masyarakat")
    st.write("Berbagai faktor mempengaruhi tingkat literasi di Indonesia, mulai dari akses terhadap pendidikan, infrastruktur, hingga kebiasaan membaca di kalangan masyarakat. Mengatasi kesenjangan ini memerlukan upaya bersama dari berbagai pihak.")
    st.write("")
    st.write("")
 
     # Membagi layout menjadi tiga kolom

    # Menampilkan teks di kolom tengah
    
    # Menampilkan gambar di kolom tengah
    
# Panggil fungsi untuk menampilkan gambar dan teks di tengah
st.markdown("<h1 style='text-align: center;'>Contact Us:</h1>",unsafe_allow_html=True )

yang1, yang2 = st.columns([3,10])
with yang1:
    st.image('pages/instagram.png',width=90)
    st.image('pages/email.png', width=90)
    st.image('pages/GoOnlineTools-image-downloader.png', width=90)
    


with yang2:
    st.subheader(' ')
    st.subheader('@kitsch.id')
    st.subheader(' ')
    st.subheader(' ')
    st.subheader('kitsch.readwrite@gmail.com')
    st.subheader(' ')
    st.subheader(' ')
    st.subheader('www.kitsch.go.id')

