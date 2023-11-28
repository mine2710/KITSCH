import streamlit as st
from streamlit_option_menu import option_menu


def show_content(content_name):
    st.write("Let's send your feedback!!")

# def football_page():
#     st.title("Halaman Sepak Bola")
#     st.write("Ini adalah halaman tentang sepak bola.")

# def musik():
#     st.title("Halaman Bola Basket")
#     st.write("Ini adalah halaman tentang bola basket.")

# def seni():
#     st.title("Halaman Tenis")
#     st.write("Ini adalah halaman tentang tenis.")

# def film():
#     st.title("Halaman Tenis")
#     st.write("Ini adalah halaman tentang tenis.")

def main():
    st.title("Article Category")

    # bola, basket, tennis = st.columns(3)
    # with bola:
    #     if st.button("Sepak bola"):
    #         football_page()
    # with basket:
    #     if st.button("Bola Basket"):
    #         musik()

    # with tennis:
    #     if st.button("Tennis"):
    #         seni()
        
    # Tombol-tombol untuk olahraga
    selected_tab = option_menu(menu_title=None, options=["Sport", "Music", "Film", "Art"],orientation="horizontal",key="nav",)
    if selected_tab == "Sport":
     
     st.subheader("Ketika Mimpi Jadi Kenyataan: Cerita Kemenangan di Kejuaraan Nasional Voli")
     st.write("create: Alvia")
     st.write("Kemenangan tak pernah terasa semanis ketika kamu mengejarnya dengan sepenuh hati. Bagi sebagian besar dari kita, sebuah kejuaraan nasional adalah mimpi terbesar yang hanya bisa diwujudkan oleh para atlet paling berdedikasi. Bagi saya, voli bukan sekadar olahraga. Ia adalah panggung di mana mimpi menjadi kenyataan.")
     st.write("Pengalaman mendebarkan saat berpartisipasi dalam Kejuaraan Nasional Voli masih terpatri kuat dalam ingatan saya. Semua dimulai dari latihan yang tak kenal lelah, keringat yang mengalir, dan semangat yang terus membara. Kami, sebagai tim, telah berkomitmen secara penuh untuk mencapai sesuatu yang lebih dari sekadar trofi. Kami membidik momen yang akan mengukir sejarah bagi kami.")
     st.write("Kompetisi dimulai dengan ketegangan yang tak tertahankan. Setiap servis, setiap smash, dan setiap blok menjadi detik-detik yang menggetarkan hati. Saat pertandingan berlangsung, terlihatlah semangat yang tak terbendung di mata rekan satu tim, di setiap gerakan yang dikerahkan untuk meraih tiap poin. Namun, persaingan bukanlah satu-satunya tantangan; ada tekanan dari ekspektasi dan harapan yang harus diemban. Semua itu menghadirkan tantangan tersendiri.")
     st.write("Namun, di tengah hiruk-pikuk pertandingan, kami menemukan alasan kami berada di sana: cinta pada olahraga ini dan dukungan luar biasa dari tim. Kami merangkul setiap kemenangan, namun juga belajar dari setiap kekalahan. Tiap peluang kami di lapangan adalah kesempatan untuk tumbuh dan menunjukkan apa yang kami bisa.")
     st.write("Dan akhirnya, saat momen yang kami tunggu-tunggu tiba, kami menemukan diri kami berada di puncak. Dalam laga final yang menegangkan, kami berhasil meraih gelar juara. Rasanya tak tergambarkan, suatu kegembiraan yang melebihi kata-kata. Itu bukan hanya kemenangan bagi kami, tetapi juga bagi semangat, dedikasi, dan kerja keras yang kami tanamkan.")
     st.write("Kemenangan itu, lebih dari sekadar trofi besar atau medali emas. Ia adalah cerminan dari perjuangan, pengorbanan, dan tekad yang mengalir dalam darah setiap pemain. Ini adalah pengingat bahwa mimpi yang dikejar dengan semangat tak pernah sia-sia.")
     st.write("Ketika saya melihat kembali perjalanan menuju kejuaraan itu, saya tak hanya melihat kemenangan; saya melihat perjalanan inspiratif kami. Kami bukan hanya menang dalam olahraga, tetapi juga menang dalam memahami arti dari semangat bertanding, kerja tim, dan ketekunan. Dan di atas segalanya, kami menang dalam menginspirasi orang lain untuk bermimpi besar dan bertekad mewujudkannya")
     st.write("Kemenangan nasional dalam voli bukan hanya tentang mengangkat trofi ke atas kepala. Itu tentang mengangkat semangat, tekad, dan mimpi lebih tinggi. Itulah yang membuat olahraga menjadi lebih dari sekadar pertandingan; ia menjadi cerminan dari kekuatan yang ada dalam diri kita untuk mencapai sesuatu yang luar biasa.")
     title = st.text_input("Write your comment")
     content = st.selectbox("Please rate", ["😍", "😐", "😔"])

     if content == "😍":
      show_content("😍")
     elif content == "😐":
      show_content("😐")
     elif content == "😔":
      show_content("😔")

     submitted = st.button("Send")

     if submitted:
        if title and content:
            # Lakukan proses penyimpanan artikel (misalnya, ke database atau penyimpanan sementara)
            st.success("Thank you for your comment!")
            st.write(f"Comment: {title}")
            st.write(f"Your rating: {content}")
            
        else:
            st.error("Write your comment")





    elif selected_tab == "Music":
        
     st.subheader("Kisah Inspiratif di Lapangan Hijau: Dari Cidera Parah hingga Jadi Pelatih")
     st.write("create: Cang S")
     st.write("Setiap langkah di atas lapangan sepak bola memiliki cerita tersendiri. Bagi saya, sepak bola bukan hanya olahraga, tapi juga mimpi yang terpendam. Cidera yang cukup serius menghentikan langkah saya sebagai pemain, namun bukanlah akhir dari cinta dan semangat saya terhadap olahraga ini.")
     st.write("Masa-masa awal saya di lapangan adalah detik-detik yang penuh semangat dan ambisi. Mimpi saya adalah menjadi pemain sepak bola profesional. Namun, sebuah cedera yang cukup serius menghantui perjalanan itu. Saat itu terasa seolah semuanya hancur. Saya dihadapkan pada kenyataan pahit bahwa jalur menuju lapangan hijau sebagai pemain ternyata berakhir di tengah jalan.")
     st.write("Melalui perjuangan yang tidak mudah, saya mulai memahami permainan dari sudut pandang yang berbeda. Saya belajar dari pengalaman saya sebagai pemain, baik yang baik maupun buruk, dan mencoba mentransfer pengetahuan dan semangat itu kepada para pemain muda yang bersemangat. Rasanya membangkitkan semangat baru ketika saya melihat mereka bermain dengan semangat yang sama yang saya miliki dahulu.")
     st.write("Menjadi seorang pelatih membuka mata saya pada sisi lain dari permainan ini. Itu bukan hanya soal teknik atau taktik, tapi juga tentang pembinaan karakter, motivasi, dan kekuatan mental. Saya menemukan kebahagiaan baru dalam membimbing, memberi inspirasi kepada mereka, dan menanamkan semangat juang yang saya bawa dalam diri.")
     st.write("Mungkin, takdir telah mengubah arah mimpi saya menjadi sesuatu yang lebih besar dari sekadar bermain di lapangan. Sekarang, saya tidak lagi mengejar bola di lapangan, tapi saya memimpin, membimbing, dan memotivasi mereka yang bermimpi seperti saya dulu.")
     st.write("Cidera itu bukanlah akhir, melainkan awal dari petualangan baru saya. Menjadi pelatih adalah jawaban dari semangat yang tak pernah padam untuk mencapai sesuatu yang lebih besar. Saya belajar bahwa kadang-kadang, terkadang kegagalan membuka pintu menuju perjalanan baru yang lebih berharga.")
     st.write("Setiap kali saya berdiri di pinggir lapangan, hati saya penuh dengan rasa syukur. Saya masih terlibat dalam olahraga yang saya cintai, tetapi dari perspektif yang berbeda. Perjalanan dari pemain yang cedera hingga menjadi pelatih telah mengajari saya bahwa kegagalan tidak selalu menghentikan kita; terkadang, ia mengarahkan kita pada perjalanan yang lebih bermakna.")
            
     title = st.text_input("Write your comment")
     category = st.selectbox("Please rate", ["😍", "😐", "😔"])

     if category == "😍":
        show_sport_category()
     elif category == "😐":
        show_sport_category()
     elif category == "😔":
        show_sport_category()

     submitted = st.button("Send")
     if submitted:
        if title and content:
                    # Lakukan proses penyimpanan artikel (misalnya, ke database atau penyimpanan sementara)
            st.success("Thank you for your comment!")
            st.write(f"Comment: {title}")
            st.write(f"Your rating: {content}")
                    
        else:
            st.error("Write your comment")


    elif selected_tab == "Art":
        
   
     
     
     
     st.subheader("Seni: Melampaui Batas Dunia dan Menyentuh Jiwa Manusia")
     st.write("create: Adit")
     st.write("Seni tidak hanya sekadar kumpulan lukisan-lukisan indah atau karya-karya musik yang memukau. Seni adalah keajaiban yang meleburkan imajinasi, kreativitas, dan emosi manusia menjadi bentuk-bentuk yang dapat mempesona, menginspirasi, dan menyentuh jiwa. Ia adalah cermin dari keindahan yang ada di sekitar kita, ditransformasikan oleh pandangan dan perasaan manusia menjadi sesuatu yang lebih dari sekadar materi.")
     st.write("PSetiap karya seni, apakah itu lukisan, patung, musik, tari, sastra, atau bentuk seni lainnya, adalah ungkapan dari perasaan, pengalaman, dan visi seseorang. Ia menjadi jendela ke dalam dunia pribadi seniman, mengungkapkan pikiran, konflik, dan kebahagiaan yang mungkin tidak dapat dijelaskan dengan kata-kata.")
     st.write("Keindahan seni terletak pada kemampuannya untuk berbicara dengan segala bahasa dan membangun jembatan antara beragam budaya di dunia ini. Ia tidak mengenal batasan geografis atau bahasa; ia bersifat universal. Saat kita menikmati sebuah karya seni, kita terhubung dengan kesan, emosi, dan makna yang dilukiskan oleh sang seniman.")
     st.write("Seni juga memiliki kekuatan untuk mengubah dan mempengaruhi. Ia adalah medium yang kuat untuk menyampaikan pesan-pesan yang mendalam, merangsang pemikiran, dan memicu perubahan sosial. Melalui seni, kita dapat menyuarakan perasaan, membangkitkan kesadaran, atau bahkan membangun gerakan perubahan.")
     st.write("Namun, di tengah semua keindahan dan kekuatan seni, terdapat kerentanan dan ketidakpastian. Seniman sering kali mengeksplorasi dunia yang tidak pasti, menghadapi tantangan kreatif, dan berjuang untuk diterima atau dipahami oleh audiensnya. Namun, itulah keberanian dan keteguhan hati yang menginspirasi mereka untuk terus melangkah, menciptakan, dan berekspresi.")
     st.write("Seni adalah refleksi dari kehidupan itu sendiri. Ia menghadirkan kegembiraan, kesedihan, kebingungan, dan keindahan yang ada dalam setiap perjalanan manusia. Ia adalah cermin dari pengalaman hidup yang unik untuk setiap individu, dan pada saat yang sama, juga adalah cermin dari pengalaman bersama sebagai umat manusia.")
     st.write("Di dunia yang terus berkembang dan berubah, seni adalah konstan yang abadi. Ia terus bertransformasi, mengikuti perkembangan zaman, teknologi, dan perubahan sosial. Namun, esensi dan keindahannya tetap tak ternilai.")
     st.write("KOleh karena itu, seni adalah suatu keajaiban yang mendalam dan abadi. Ia bukan hanya sekadar gambar atau suara, tetapi juga adalah ungkapan dari hati dan jiwa manusia. Seni adalah bahasa yang universal, menghubungkan kita dengan sisi-sisi terdalam dari diri kita dan dengan dunia di sekitar kita.")
     title = st.text_input("Write your comment")
     content = st.selectbox("Please rate", ["😍", "😐", "😔"])

     if content == "😍":
      show_content("😍")
     elif content == "😐":
      show_content("😐")
     elif content == "😔":
      show_content("😔")

     submitted = st.button("Send")

     if submitted:
        if title and content:
            # Lakukan proses penyimpanan artikel (misalnya, ke database atau penyimpanan sementara)
            st.success("Thank you for your comment!")
            st.write(f"Comment: {title}")
            st.write(f"Your rating: {content}")
            
        else:
            st.error("Write your comment")


    elif selected_tab == "Film":
        
     
     
     
     
     
     st.subheader("Ketika Mimpi Jadi Kenyataan: Cerita Kemenangan di Kejuaraan Nasional Voli")
     st.write("create: Alvia")
     st.write("Kemenangan tak pernah terasa semanis ketika kamu mengejarnya dengan sepenuh hati. Bagi sebagian besar dari kita, sebuah kejuaraan nasional adalah mimpi terbesar yang hanya bisa diwujudkan oleh para atlet paling berdedikasi. Bagi saya, voli bukan sekadar olahraga. Ia adalah panggung di mana mimpi menjadi kenyataan.")
     st.write("Pengalaman mendebarkan saat berpartisipasi dalam Kejuaraan Nasional Voli masih terpatri kuat dalam ingatan saya. Semua dimulai dari latihan yang tak kenal lelah, keringat yang mengalir, dan semangat yang terus membara. Kami, sebagai tim, telah berkomitmen secara penuh untuk mencapai sesuatu yang lebih dari sekadar trofi. Kami membidik momen yang akan mengukir sejarah bagi kami.")
     st.write("Kompetisi dimulai dengan ketegangan yang tak tertahankan. Setiap servis, setiap smash, dan setiap blok menjadi detik-detik yang menggetarkan hati. Saat pertandingan berlangsung, terlihatlah semangat yang tak terbendung di mata rekan satu tim, di setiap gerakan yang dikerahkan untuk meraih tiap poin. Namun, persaingan bukanlah satu-satunya tantangan; ada tekanan dari ekspektasi dan harapan yang harus diemban. Semua itu menghadirkan tantangan tersendiri.")
     st.write("Namun, di tengah hiruk-pikuk pertandingan, kami menemukan alasan kami berada di sana: cinta pada olahraga ini dan dukungan luar biasa dari tim. Kami merangkul setiap kemenangan, namun juga belajar dari setiap kekalahan. Tiap peluang kami di lapangan adalah kesempatan untuk tumbuh dan menunjukkan apa yang kami bisa.")
     st.write("Dan akhirnya, saat momen yang kami tunggu-tunggu tiba, kami menemukan diri kami berada di puncak. Dalam laga final yang menegangkan, kami berhasil meraih gelar juara. Rasanya tak tergambarkan, suatu kegembiraan yang melebihi kata-kata. Itu bukan hanya kemenangan bagi kami, tetapi juga bagi semangat, dedikasi, dan kerja keras yang kami tanamkan.")
     st.write("Kemenangan itu, lebih dari sekadar trofi besar atau medali emas. Ia adalah cerminan dari perjuangan, pengorbanan, dan tekad yang mengalir dalam darah setiap pemain. Ini adalah pengingat bahwa mimpi yang dikejar dengan semangat tak pernah sia-sia.")
     st.write("Ketika saya melihat kembali perjalanan menuju kejuaraan itu, saya tak hanya melihat kemenangan; saya melihat perjalanan inspiratif kami. Kami bukan hanya menang dalam olahraga, tetapi juga menang dalam memahami arti dari semangat bertanding, kerja tim, dan ketekunan. Dan di atas segalanya, kami menang dalam menginspirasi orang lain untuk bermimpi besar dan bertekad mewujudkannya")
     st.write("Kemenangan nasional dalam voli bukan hanya tentang mengangkat trofi ke atas kepala. Itu tentang mengangkat semangat, tekad, dan mimpi lebih tinggi. Itulah yang membuat olahraga menjadi lebih dari sekadar pertandingan; ia menjadi cerminan dari kekuatan yang ada dalam diri kita untuk mencapai sesuatu yang luar biasa.")
     title = st.text_input("Write your comment")
     content = st.selectbox("Please rate", ["😍", "😐", "😔"])

     if content == "😍":
      show_content("😍")
     elif content == "😐":
      show_content("😐")
     elif content == "😔":
      show_content("😔")

     submitted = st.button("Send")

     if submitted:
        if title and content:
            # Lakukan proses penyimpanan artikel (misalnya, ke database atau penyimpanan sementara)
            st.success("Thank you for your comment!")
            st.write(f"Comment: {title}")
            st.write(f"Your rating: {content}")
            
        else:
            st.error("Write your comment")


        
    
    # if st.button("musik"):
    #     musik()
    
    # if st.button("film"):
    #     film()

    # if st.button("seni"):
    #     seni()
if __name__ == "__main__":
    main()
