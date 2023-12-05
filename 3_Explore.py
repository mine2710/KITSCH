import streamlit as st
from streamlit_option_menu import option_menu
    
def show_sport_category():
            
    st.title("Category Sport")
    

    selected_tab = option_menu(menu_title=None, options=["Bola Voli", "Sepak Bola", "Batminton", "Lain-lain"],orientation="horizontal",key="nav",)
    if selected_tab == "Bola Voli":
               
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
       
    elif selected_tab == "Sepak Bola":
                
        st.subheader("Kisah Inspiratif di Lapangan Hijau: Dari Cidera Parah hingga Jadi Pelatih")
        st.write("create: Cang S")
        st.write("Setiap langkah di atas lapangan sepak bola memiliki cerita tersendiri. Bagi saya, sepak bola bukan hanya olahraga, tapi juga mimpi yang terpendam. Cidera yang cukup serius menghentikan langkah saya sebagai pemain, namun bukanlah akhir dari cinta dan semangat saya terhadap olahraga ini.")
        st.write("Masa-masa awal saya di lapangan adalah detik-detik yang penuh semangat dan ambisi. Mimpi saya adalah menjadi pemain sepak bola profesional. Namun, sebuah cedera yang cukup serius menghantui perjalanan itu. Saat itu terasa seolah semuanya hancur. Saya dihadapkan pada kenyataan pahit bahwa jalur menuju lapangan hijau sebagai pemain ternyata berakhir di tengah jalan.")
        st.write("Melalui perjuangan yang tidak mudah, saya mulai memahami permainan dari sudut pandang yang berbeda. Saya belajar dari pengalaman saya sebagai pemain, baik yang baik maupun buruk, dan mencoba mentransfer pengetahuan dan semangat itu kepada para pemain muda yang bersemangat. Rasanya membangkitkan semangat baru ketika saya melihat mereka bermain dengan semangat yang sama yang saya miliki dahulu.")
        st.write("Menjadi seorang pelatih membuka mata saya pada sisi lain dari permainan ini. Itu bukan hanya soal teknik atau taktik, tapi juga tentang pembinaan karakter, motivasi, dan kekuatan mental. Saya menemukan kebahagiaan baru dalam membimbing, memberi inspirasi kepada mereka, dan menanamkan semangat juang yang saya bawa dalam diri.")
        st.write("Mungkin, takdir telah mengubah arah mimpi saya menjadi sesuatu yang lebih besar dari sekadar bermain di lapangan. Sekarang, saya tidak lagi mengejar bola di lapangan, tapi saya memimpin, membimbing, dan memotivasi mereka yang bermimpi seperti saya dulu.")
        st.write("Cidera itu bukanlah akhir, melainkan awal dari petualangan baru saya. Menjadi pelatih adalah jawaban dari semangat yang tak pernah padam untuk mencapai sesuatu yang lebih besar. Saya belajar bahwa kadang-kadang, terkadang kegagalan membuka pintu menuju perjalanan baru yang lebih berharga.")
        st.write("Setiap kali saya berdiri di pinggir lapangan, hati saya penuh dengan rasa syukur. Saya masih terlibat dalam olahraga yang saya cintai, tetapi dari perspektif yang berbeda. Perjalanan dari pemain yang cedera hingga menjadi pelatih telah mengajari saya bahwa kegagalan tidak selalu menghentikan kita; terkadang, ia mengarahkan kita pada perjalanan yang lebih bermakna.")
            
        
    elif selected_tab == "Batminton":
                
        st.subheader("Membatasi Mimpi: Ketika Cinta pada Bulutangkis Tergesa-Gesa oleh Kendala")
        st.write("create: Uliano")
        st.write("Pada suatu masa, di sebuah sudut kecil di kota kecil, terdapat seorang anak muda yang memiliki mimpi besar: menjadi pemain bulutangkis yang menginspirasi. Namun, terlepas dari semangatnya yang menyala, ada batasan yang menghentikannya—bukan dari kekurangan bakat atau semangat, melainkan dari orang yang paling dicintainya: orang tuanya.")
        st.write("Tidak bisa dipungkiri bahwa bulutangkis adalah cinta sejati dalam hidupnya. Setiap bulan, setiap minggu, setiap hari, ia rela menghabiskan waktu di lapangan, memukul kok yang berdenting dengan semangat yang tak terbendung. Ia bermimpi berjalan di panggung besar, memenangkan kejuaraan, dan memancarkan semangat juang kepada jutaan orang. Tetapi, mimpi itu dihentikan oleh panggilan dari rumah.")
        st.write("Orang tuanya, dengan hati yang penuh kebaikan, menghentikan langkahnya menuju kejayaan bulutangkis. Mereka menutup pintu setiap kali ia ingin berlatih lebih lama, menghadirkan keraguan dan batasan tentang masa depannya. Alasan mereka adalah keamanan, keberlangsungan, dan 'masuk akal' menurut kacamata mereka.")
        st.write("Namun, terkadang, apa yang masuk akal bagi orang tua belum tentu sesuai dengan hasrat dan panggilan jiwa seseorang. Itu bukan hanya tentang memenangkan trofi atau menjadi terkenal; itu tentang mengejar sesuatu yang membakar api di dalam hati.")
        st.write("Ketika setiap anak muda berusaha menemukan identitas dan tujuannya dalam hidup, dia merasa terperangkap. Antara kewajiban kepada orang tua dan panggilan jiwa yang begitu kuat. Di satu sisi, ada tanggung jawab untuk mematuhi keinginan orang tua yang telah melakukan segalanya untuknya. Di sisi lain, ada impian besar yang tak pernah padam, yang memanggil untuk diwujudkan.")
        st.write("Jika saja dunia bisa melihat betapa bulutangkis bukan sekadar sebuah hobi bagi anak muda ini. Itu adalah lebih dari sekadar sebuah olahraga; itu adalah mimpi yang ingin mempersembahkan semangat, kerja keras, dan kesuksesan. Itu adalah bagian dari dirinya yang ingin diberikan kepada dunia.")
        st.write("Mungkin satu hari, ia akan menemukan jalan untuk menyatukan dunianya yang penuh tanggung jawab dengan hasratnya yang tak terbendung. Mungkin, orang tuanya akan melihat betapa bulutangkis adalah bagian dari jiwanya, bukan hanya kesenangan sesaat. Dan mungkin, pada akhirnya, mimpi yang dibatasi akan menemukan cara untuk terbang bebas, meski jalan menuju sana tidaklah mudah.")
        st.write("Mungkin kisah ini bukan tentang menentang orang tua atau mengecilkan nilai nasihat mereka. Tapi ini tentang menemukan keseimbangan antara kebutuhan kita dan kebahagiaan mereka. Dan pada akhirnya, tentang menemukan jalan kita sendiri menuju apa yang kita yakini. Mimpi itu bisa terlalu kuat untuk ditahan, tapi kadang-kadang, kita harus menemukan caranya untuk membiarkan mimpi itu melayang bebas.")
       
    elif selected_tab == "Lain-lain":
                
        st.subheader("Menuju Puncak di Dunia eSports: Perjalanan Seorang Gamer")
        st.write("create: Syahrul")
        st.write("Di era digital saat ini, kejuaraan eSports telah menjadi panggung bagi para gamer untuk menunjukkan bakat, keterampilan, dan dedikasi mereka. Dalam sorotan terang lampu, di antara jutaan mata yang memperhatikan layar, terdapat kisah-kisah penuh semangat dan perjuangan. Salah satunya adalah perjalanan seorang gamer yang merintis langkahnya menuju kejuaraan eSports.")
        st.write("Bagi banyak orang, permainan video mungkin hanya sebuah hiburan. Tetapi bagi mereka yang mengabdikan hidupnya untuk game, itu adalah panggung penuh tantangan, strategi, dan ketelitian. Dan untuk seseorang yang memasuki dunia eSports, hal tersebut menjadi sesuatu yang lebih besar, sebuah panggung di mana mimpi bisa menjadi kenyataan.")
        st.write("Pertama-tama, ada kesiapan mental yang dibutuhkan. Persiapan mental yang berulang, latihan tanpa henti, dan dedikasi yang tak pernah padam. Jam-jam bermain yang tidak terbatas, memperdalam pemahaman akan mekanisme permainan, dan merumuskan strategi yang dapat melampaui lawan-lawan terbaik.")
        st.write("Tapi perjalanan itu tidak hanya sebatas di atas kursi dengan kontroler di tangan. Ada perjalanan dari turnamen ke turnamen, menantang para pemain elit, dan belajar dari setiap kekalahan. Ada momen tegang di setiap kompetisi, saat di mana tekanan terasa sangat nyata, namun keinginan untuk memenangkan setiap pertandingan tetap membara.")
        st.write("Di balik layar, ada latihan yang disiplin, analisis video permainan, dan diskusi strategi bersama tim. Ada pula kesabaran yang diperlukan untuk tetap berada dalam komunitas yang kompetitif, dan keterampilan dalam mengelola tekanan yang tidak terhindarkan")
        st.write("Dan pada akhirnya, tiba saatnya untuk menapaki panggung besar kejuaraan eSports. Di sini, di depan ribuan bahkan jutaan penonton yang bergumul dalam antusiasme, di sinilah segala pengorbanan, kerja keras, dan ketekunan berbuah hasil. Meskipun hasilnya tidak selalu kemenangan, tetapi pengalaman itu sendiri adalah hadiah yang tak ternilai.")
        st.write("Setiap peserta membawa pulang lebih dari sekadar trofi atau hadiah uang. Mereka membawa pulang pengalaman yang tak terlupakan, koneksi dengan komunitas yang sama, dan keyakinan bahwa perjuangan mereka adalah bagian dari membangun sebuah peradaban digital yang baru.")
        st.write("Kisah-kisah ini, dari gamer yang memulai dari ruang kamar hingga panggung kejuaraan eSports, adalah bukti akan kegigihan, dedikasi, dan semangat manusia untuk mencapai sesuatu yang lebih. Dunia eSports telah menjadi bukti bahwa kecintaan pada permainan video bisa menjadi sesuatu yang jauh lebih besar—sebuah kompetisi, seni, dan perayaan dari keahlian dan semangat yang luar biasa.")
       






def show_art_category():
    st.title("Category Art")
    

    selected_tab = option_menu(menu_title=None, options=["Lukisan", "Tarian", "Bahasa", "Lain-lain"],orientation="horizontal",key="nav",)
    if selected_tab == "Lukisan":
            
            
            
            
        st.subheader("Mahakarya Seni yang Melampaui Batas: Lukisan Termahal di Dunia")
        st.write("create: Aden")
        st.write("Seni telah mempesona manusia selama berabad-abad, dan lukisan seringkali menjadi karya yang paling menakjubkan dan bernilai di dunia seni. Di antara lukisan-lukisan yang memikat hati, ada yang menjadi perbincangan karena bukan hanya keindahannya, tetapi juga karena nilai materinya yang luar biasa tinggi. Dan dalam lelang seni, tercatat sejarah ketika salah satu mahakarya melampaui semua ekspektasi dan menjadi lukisan termahal yang pernah terjual.")
        st.write("Lukisan ini, bukan hanya sekadar karya seni biasa. Ia adalah jendela ke dalam pikiran seorang seniman yang meramu segala detail dengan keindahan dan pengertian yang luar biasa. Ia adalah manifestasi dari pikiran yang kreatif, ekspresi emosi, dan teknik yang tiada tara.")
        st.write("Keistimewaan lukisan ini bukan hanya berasal dari indahnya, tetapi dari cerita yang tersembunyi di balik sapuan kuasnya. Setiap goresan memiliki makna, setiap warna memiliki cerita, dan setiap detail memiliki kekayaan yang tak ternilai.")
        st.write("Di balik harganya yang fantastis, ada perdebatan tentang apakah nilai sebenarnya dari sebuah karya seni yang tergantung pada harga yang dianggapnya. Bagi beberapa orang, ini adalah bukti bahwa seni dapat menjadi investasi yang menguntungkan, sedangkan bagi yang lain, ini adalah pernyataan tentang ketidaksetaraan dalam akses terhadap seni yang membingungkan.")
        st.write("Namun, di tengah semua diskusi ini, tidak dapat dipungkiri bahwa nilai karya seni tidak hanya diukur dalam angka. Lukisan ini adalah warisan budaya, potongan sejarah yang dilestarikan untuk generasi mendatang. Ia adalah pilar dari peradaban, manifestasi budaya, dan cerminan dari jiwa manusia yang ingin mengekspresikan dirinya melalui medium yang paling indah.")
        st.write("Bagi mereka yang menghargai seni, lukisan ini bukan hanya sebuah investasi atau alat status sosial. Ia adalah keindahan yang menginspirasi, cerita yang mencerahkan, dan pembawa emosi yang mendalam. Ia adalah saksi bisu dari kisah manusia, sebuah karya seni yang melebihi batas-batas waktu dan ruang.")
        st.write("Dalam dunia yang terus berkembang dan berubah, lukisan ini tetap menjadi simbol dari apa yang manusia capai, apa yang mereka cintai, dan apa yang mereka hargai. Ia tetap menjadi perwujudan keindahan, kreativitas, dan hasrat manusia untuk menciptakan sesuatu yang tak terlupakan.")
        st.write("Sehingga, meskipun dihargai dengan angka fantastis, nilai sejati dari lukisan ini mungkin tidak pernah bisa diukur. Karena nilai sejati dari seni tidaklah dihitung dalam angka, tetapi terletak pada kesan yang meninggalkan, inspirasi yang memberikan, dan keindahan yang menggugah.")
  

    elif selected_tab == "Tarian":
            

                

        st.subheader("Kisah Inspiratif di Lapangan Hijau: Dari Cidera Parah hingga Jadi Pelatih")
        st.write("create: Cang S")
        st.write("Setiap langkah di atas lapangan sepak bola memiliki cerita tersendiri. Bagi saya, sepak bola bukan hanya olahraga, tapi juga mimpi yang terpendam. Cidera yang cukup serius menghentikan langkah saya sebagai pemain, namun bukanlah akhir dari cinta dan semangat saya terhadap olahraga ini.")
        st.write("Masa-masa awal saya di lapangan adalah detik-detik yang penuh semangat dan ambisi. Mimpi saya adalah menjadi pemain sepak bola profesional. Namun, sebuah cedera yang cukup serius menghantui perjalanan itu. Saat itu terasa seolah semuanya hancur. Saya dihadapkan pada kenyataan pahit bahwa jalur menuju lapangan hijau sebagai pemain ternyata berakhir di tengah jalan.")
        st.write("Melalui perjuangan yang tidak mudah, saya mulai memahami permainan dari sudut pandang yang berbeda. Saya belajar dari pengalaman saya sebagai pemain, baik yang baik maupun buruk, dan mencoba mentransfer pengetahuan dan semangat itu kepada para pemain muda yang bersemangat. Rasanya membangkitkan semangat baru ketika saya melihat mereka bermain dengan semangat yang sama yang saya miliki dahulu.")
        st.write("Menjadi seorang pelatih membuka mata saya pada sisi lain dari permainan ini. Itu bukan hanya soal teknik atau taktik, tapi juga tentang pembinaan karakter, motivasi, dan kekuatan mental. Saya menemukan kebahagiaan baru dalam membimbing, memberi inspirasi kepada mereka, dan menanamkan semangat juang yang saya bawa dalam diri.")
        st.write("Mungkin, takdir telah mengubah arah mimpi saya menjadi sesuatu yang lebih besar dari sekadar bermain di lapangan. Sekarang, saya tidak lagi mengejar bola di lapangan, tapi saya memimpin, membimbing, dan memotivasi mereka yang bermimpi seperti saya dulu.")
        st.write("Cidera itu bukanlah akhir, melainkan awal dari petualangan baru saya. Menjadi pelatih adalah jawaban dari semangat yang tak pernah padam untuk mencapai sesuatu yang lebih besar. Saya belajar bahwa kadang-kadang, terkadang kegagalan membuka pintu menuju perjalanan baru yang lebih berharga.")
        st.write("Setiap kali saya berdiri di pinggir lapangan, hati saya penuh dengan rasa syukur. Saya masih terlibat dalam olahraga yang saya cintai, tetapi dari perspektif yang berbeda. Perjalanan dari pemain yang cedera hingga menjadi pelatih telah mengajari saya bahwa kegagalan tidak selalu menghentikan kita; terkadang, ia mengarahkan kita pada perjalanan yang lebih bermakna.")
            
            

           

    elif selected_tab == "Bahasa":
                
        st.subheader("Membatasi Mimpi: Ketika Cinta pada Bulutangkis Tergesa-Gesa oleh Kendala")
        st.write("create: Uliano")
        st.write("Pada suatu masa, di sebuah sudut kecil di kota kecil, terdapat seorang anak muda yang memiliki mimpi besar: menjadi pemain bulutangkis yang menginspirasi. Namun, terlepas dari semangatnya yang menyala, ada batasan yang menghentikannya—bukan dari kekurangan bakat atau semangat, melainkan dari orang yang paling dicintainya: orang tuanya.")
        st.write("Tidak bisa dipungkiri bahwa bulutangkis adalah cinta sejati dalam hidupnya. Setiap bulan, setiap minggu, setiap hari, ia rela menghabiskan waktu di lapangan, memukul kok yang berdenting dengan semangat yang tak terbendung. Ia bermimpi berjalan di panggung besar, memenangkan kejuaraan, dan memancarkan semangat juang kepada jutaan orang. Tetapi, mimpi itu dihentikan oleh panggilan dari rumah.")
        st.write("Orang tuanya, dengan hati yang penuh kebaikan, menghentikan langkahnya menuju kejayaan bulutangkis. Mereka menutup pintu setiap kali ia ingin berlatih lebih lama, menghadirkan keraguan dan batasan tentang masa depannya. Alasan mereka adalah keamanan, keberlangsungan, dan 'masuk akal' menurut kacamata mereka.")
        st.write("Namun, terkadang, apa yang masuk akal bagi orang tua belum tentu sesuai dengan hasrat dan panggilan jiwa seseorang. Itu bukan hanya tentang memenangkan trofi atau menjadi terkenal; itu tentang mengejar sesuatu yang membakar api di dalam hati.")
        st.write("Ketika setiap anak muda berusaha menemukan identitas dan tujuannya dalam hidup, dia merasa terperangkap. Antara kewajiban kepada orang tua dan panggilan jiwa yang begitu kuat. Di satu sisi, ada tanggung jawab untuk mematuhi keinginan orang tua yang telah melakukan segalanya untuknya. Di sisi lain, ada impian besar yang tak pernah padam, yang memanggil untuk diwujudkan.")
        st.write("Jika saja dunia bisa melihat betapa bulutangkis bukan sekadar sebuah hobi bagi anak muda ini. Itu adalah lebih dari sekadar sebuah olahraga; itu adalah mimpi yang ingin mempersembahkan semangat, kerja keras, dan kesuksesan. Itu adalah bagian dari dirinya yang ingin diberikan kepada dunia.")
        st.write("Mungkin satu hari, ia akan menemukan jalan untuk menyatukan dunianya yang penuh tanggung jawab dengan hasratnya yang tak terbendung. Mungkin, orang tuanya akan melihat betapa bulutangkis adalah bagian dari jiwanya, bukan hanya kesenangan sesaat. Dan mungkin, pada akhirnya, mimpi yang dibatasi akan menemukan cara untuk terbang bebas, meski jalan menuju sana tidaklah mudah.")
        st.write("Mungkin kisah ini bukan tentang menentang orang tua atau mengecilkan nilai nasihat mereka. Tapi ini tentang menemukan keseimbangan antara kebutuhan kita dan kebahagiaan mereka. Dan pada akhirnya, tentang menemukan jalan kita sendiri menuju apa yang kita yakini. Mimpi itu bisa terlalu kuat untuk ditahan, tapi kadang-kadang, kita harus menemukan caranya untuk membiarkan mimpi itu melayang bebas.")
            
           

    elif selected_tab == "Lain-lain":
                
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
            

           



def show_music_category():
    st.title("Category Music")
    

    selected_tab = option_menu(menu_title=None, options=["Musik Barat", "Lagu Kpop", "Lagu Daerah", "Lain-lain"],orientation="horizontal",key="nav",)
    if selected_tab == "Musik Barat":
        
        
        
        
       
        st.subheader("Niki: Melodi Eklektik dari Talenta Asia yang Mendunia")
        st.write("create: Niki")
        st.write("Di tengah industri musik yang terus berkembang, ada bintang muda yang menembus batas-batas geografis, membawa melodi yang merayap ke hati pendengarnya dengan kehalusan yang menakjubkan. Dia adalah Niki, seorang penyanyi berbakat yang telah merajut jaringan penggemar di seluruh dunia dengan suara unik dan energi yang menggetarkan.")
        st.write("Lahir dan dibesarkan di Asia, Niki tumbuh dalam aliran yang kaya akan berbagai genre musik. Pengaruh ini tercermin dalam karya-karyanya yang eklektik, sebuah perpaduan harmonis antara elemen-elemen pop, R&B, dan electro-pop. Di dalam setiap lirik dan melodi yang ia ciptakan, terdapat kekuatan emosional yang mampu menembus ke dalam hati pendengarnya.")
        st.write("Kesuksesan Niki tidak hanya terbatas pada perbatasan negara asalnya; ia telah menarik perhatian dunia melalui karyanya yang autentik dan pengaruh global. Lagu-lagu ciptaannya telah mencapai jutaan pendengar di platform musik digital, memperoleh pengakuan atas kualitas artistiknya yang mengagumkan.")
        st.write("Satu hal yang membedakan Niki adalah kemampuannya untuk mengekspresikan emosi dengan cara yang sangat mendalam. Dari lagu-lagu yang penuh semangat hingga lagu-lagu yang lebih melankolis, setiap nada yang ia ciptakan terasa seperti jendela ke dalam dunianya yang penuh warna.")
        st.write("Selain bakat musiknya yang luar biasa, Niki juga menciptakan identitasnya sendiri sebagai seorang musisi dengan gaya dan pesona yang menginspirasi. Dari gaya fashion yang unik hingga pernyataan-pernyataan kejujuran di media sosial, ia menjadi teladan bagi generasi muda yang ingin mengejar mimpi mereka di dunia seni.")
        st.write("Keberhasilan Niki dalam menghadirkan musik yang menggugah perasaan telah mengukir jalur bagi musisi muda di Asia untuk mengejar impian mereka. Ia memberikan inspirasi bahwa terlepas dari asal-usulnya, bakat dan dedikasi dapat membawa seseorang meraih puncak dalam industri yang kompetitif.")
        st.write("Kesuksesan Niki juga menggarisbawahi fakta bahwa musik adalah bahasa universal yang mampu mengatasi segala batasan. Ia telah membawa keindahan musik Asia ke panggung dunia, memperkaya keragaman dan membangun pengertian antara budaya-budaya yang berbeda di seluruh dunia.")
            

           

    elif selected_tab == "Lagu Kpop":
                
        st.subheader("Kisah Inspiratif di Lapangan Hijau: Dari Cidera Parah hingga Jadi Pelatih")
        st.write("create: Cang S")
        st.write("Setiap langkah di atas lapangan sepak bola memiliki cerita tersendiri. Bagi saya, sepak bola bukan hanya olahraga, tapi juga mimpi yang terpendam. Cidera yang cukup serius menghentikan langkah saya sebagai pemain, namun bukanlah akhir dari cinta dan semangat saya terhadap olahraga ini.")
        st.write("Masa-masa awal saya di lapangan adalah detik-detik yang penuh semangat dan ambisi. Mimpi saya adalah menjadi pemain sepak bola profesional. Namun, sebuah cedera yang cukup serius menghantui perjalanan itu. Saat itu terasa seolah semuanya hancur. Saya dihadapkan pada kenyataan pahit bahwa jalur menuju lapangan hijau sebagai pemain ternyata berakhir di tengah jalan.")
        st.write("Melalui perjuangan yang tidak mudah, saya mulai memahami permainan dari sudut pandang yang berbeda. Saya belajar dari pengalaman saya sebagai pemain, baik yang baik maupun buruk, dan mencoba mentransfer pengetahuan dan semangat itu kepada para pemain muda yang bersemangat. Rasanya membangkitkan semangat baru ketika saya melihat mereka bermain dengan semangat yang sama yang saya miliki dahulu.")
        st.write("Menjadi seorang pelatih membuka mata saya pada sisi lain dari permainan ini. Itu bukan hanya soal teknik atau taktik, tapi juga tentang pembinaan karakter, motivasi, dan kekuatan mental. Saya menemukan kebahagiaan baru dalam membimbing, memberi inspirasi kepada mereka, dan menanamkan semangat juang yang saya bawa dalam diri.")
        st.write("Mungkin, takdir telah mengubah arah mimpi saya menjadi sesuatu yang lebih besar dari sekadar bermain di lapangan. Sekarang, saya tidak lagi mengejar bola di lapangan, tapi saya memimpin, membimbing, dan memotivasi mereka yang bermimpi seperti saya dulu.")
        st.write("Cidera itu bukanlah akhir, melainkan awal dari petualangan baru saya. Menjadi pelatih adalah jawaban dari semangat yang tak pernah padam untuk mencapai sesuatu yang lebih besar. Saya belajar bahwa kadang-kadang, terkadang kegagalan membuka pintu menuju perjalanan baru yang lebih berharga.")
        st.write("Setiap kali saya berdiri di pinggir lapangan, hati saya penuh dengan rasa syukur. Saya masih terlibat dalam olahraga yang saya cintai, tetapi dari perspektif yang berbeda. Perjalanan dari pemain yang cedera hingga menjadi pelatih telah mengajari saya bahwa kegagalan tidak selalu menghentikan kita; terkadang, ia mengarahkan kita pada perjalanan yang lebih bermakna.")
            
            

           

    elif selected_tab == "Lagu Daerah":
                
        st.subheader("Membatasi Mimpi: Ketika Cinta pada Bulutangkis Tergesa-Gesa oleh Kendala")
        st.write("create: Uliano")
        st.write("Pada suatu masa, di sebuah sudut kecil di kota kecil, terdapat seorang anak muda yang memiliki mimpi besar: menjadi pemain bulutangkis yang menginspirasi. Namun, terlepas dari semangatnya yang menyala, ada batasan yang menghentikannya—bukan dari kekurangan bakat atau semangat, melainkan dari orang yang paling dicintainya: orang tuanya.")
        st.write("Tidak bisa dipungkiri bahwa bulutangkis adalah cinta sejati dalam hidupnya. Setiap bulan, setiap minggu, setiap hari, ia rela menghabiskan waktu di lapangan, memukul kok yang berdenting dengan semangat yang tak terbendung. Ia bermimpi berjalan di panggung besar, memenangkan kejuaraan, dan memancarkan semangat juang kepada jutaan orang. Tetapi, mimpi itu dihentikan oleh panggilan dari rumah.")
        st.write("Orang tuanya, dengan hati yang penuh kebaikan, menghentikan langkahnya menuju kejayaan bulutangkis. Mereka menutup pintu setiap kali ia ingin berlatih lebih lama, menghadirkan keraguan dan batasan tentang masa depannya. Alasan mereka adalah keamanan, keberlangsungan, dan 'masuk akal' menurut kacamata mereka.")
        st.write("Namun, terkadang, apa yang masuk akal bagi orang tua belum tentu sesuai dengan hasrat dan panggilan jiwa seseorang. Itu bukan hanya tentang memenangkan trofi atau menjadi terkenal; itu tentang mengejar sesuatu yang membakar api di dalam hati.")
        st.write("Ketika setiap anak muda berusaha menemukan identitas dan tujuannya dalam hidup, dia merasa terperangkap. Antara kewajiban kepada orang tua dan panggilan jiwa yang begitu kuat. Di satu sisi, ada tanggung jawab untuk mematuhi keinginan orang tua yang telah melakukan segalanya untuknya. Di sisi lain, ada impian besar yang tak pernah padam, yang memanggil untuk diwujudkan.")
        st.write("Jika saja dunia bisa melihat betapa bulutangkis bukan sekadar sebuah hobi bagi anak muda ini. Itu adalah lebih dari sekadar sebuah olahraga; itu adalah mimpi yang ingin mempersembahkan semangat, kerja keras, dan kesuksesan. Itu adalah bagian dari dirinya yang ingin diberikan kepada dunia.")
        st.write("Mungkin satu hari, ia akan menemukan jalan untuk menyatukan dunianya yang penuh tanggung jawab dengan hasratnya yang tak terbendung. Mungkin, orang tuanya akan melihat betapa bulutangkis adalah bagian dari jiwanya, bukan hanya kesenangan sesaat. Dan mungkin, pada akhirnya, mimpi yang dibatasi akan menemukan cara untuk terbang bebas, meski jalan menuju sana tidaklah mudah.")
        st.write("Mungkin kisah ini bukan tentang menentang orang tua atau mengecilkan nilai nasihat mereka. Tapi ini tentang menemukan keseimbangan antara kebutuhan kita dan kebahagiaan mereka. Dan pada akhirnya, tentang menemukan jalan kita sendiri menuju apa yang kita yakini. Mimpi itu bisa terlalu kuat untuk ditahan, tapi kadang-kadang, kita harus menemukan caranya untuk membiarkan mimpi itu melayang bebas.")
            

           

    elif selected_tab == "Lain-lain":
            
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
            

           


def show_film_category():
    st.title("Category Film")
    

    selected_tab = option_menu(menu_title=None, options=["Romance", "Senang", "Sedih", "Lain-lain"],orientation="horizontal",key="nav",)
    if selected_tab == "Romance":
            
            
                
                
        st.subheader("Mengungkap Keindahan Kisah Cinta dalam Dunia Film: Romantis dan Mengharukan")
        st.write("create: Mine")
        st.write("Kisah cinta selalu menjadi tema yang tak pernah lekang oleh waktu. Dalam dunia film, genre romantis menjadi pencerminan yang indah dari keajaiban percintaan manusia. Bukan sekadar tentang kisah asmara, film-film romantis seringkali menggambarkan perjalanan emosional yang menggetarkan hati penonton.")
        st.write("Dari 'Casablanca' hingga 'The Notebook', film-film ini telah berhasil membius kita dengan kekuatan cerita yang memilukan dan mengharukan. Bukan hanya sekadar alur cerita yang menarik, tetapi juga kekuatan penghayatan karakter dan chemistry di antara para pemain yang membuat film-film romantis ini begitu memikat.")
        st.write("Salah satu daya tarik utama dari genre ini adalah kemampuannya untuk menghadirkan seutas harapan di tengah-tengah kehidupan yang sering kali keras dan kompleks. Dalam setiap adegannya, film-film romantis mengajak kita memimpikan kisah cinta yang abadi, meyakini bahwa cinta sejati adalah kekuatan yang mampu mengatasi segala rintangan.")
        st.write("Tidak hanya itu, keindahan visual dan latar yang dipilih dalam film-film romantis juga turut menjadi bagian yang tak terpisahkan. Dari suasana kota Paris yang romantis hingga pedesaan yang tenang, setiap latar memberikan nuansa yang mendalam pada cerita yang disampaikan.")
        st.write("Namun, tidak selalu tentang akhir yang bahagia. Film-film romantis juga terkadang menghadirkan tragedi cinta yang meninggalkan kesan mendalam pada penonton. Di balik cerita yang penuh keindahan, film-film ini juga mampu mengajarkan banyak hal tentang kehidupan dan makna sejati dari cinta.")
        st.write("Kemenangan itu, lebih dari sekadar trofi besar atau medali emas. Ia adalah cerminan dari perjuangan, pengorbanan, dan tekad yang mengalir dalam darah setiap pemain. Ini adalah pengingat bahwa mimpi yang dikejar dengan semangat tak pernah sia-sia.")
        st.write("Dalam era modern, film-film romantis terus berkembang dengan berbagai pendekatan baru. Kisah cinta tidak lagi hanya terbatas pada formula klise, tetapi juga menggali berbagai tema yang lebih kompleks, menyajikan cerita cinta yang realistis dan relevan bagi generasi saat ini.")
        st.write("Sebagai penutup, film romantis bukan hanya sekadar hiburan. Mereka adalah cerminan dari kerumitan emosi manusia, keindahan hubungan antarmanusia, serta kekuatan cinta yang mampu mengatasi segala batasan. Film-film romantis tetap menjadi tempat yang nyaman bagi para penonton untuk merenungkan, menginspirasi, dan terkadang, bahkan menggugah hati mereka.")
                

                
    elif selected_tab == "Senang":
                
        st.subheader("Kisah Inspiratif di Lapangan Hijau: Dari Cidera Parah hingga Jadi Pelatih")
        st.write("create: Cang S")
        st.write("Setiap langkah di atas lapangan sepak bola memiliki cerita tersendiri. Bagi saya, sepak bola bukan hanya olahraga, tapi juga mimpi yang terpendam. Cidera yang cukup serius menghentikan langkah saya sebagai pemain, namun bukanlah akhir dari cinta dan semangat saya terhadap olahraga ini.")
        st.write("Masa-masa awal saya di lapangan adalah detik-detik yang penuh semangat dan ambisi. Mimpi saya adalah menjadi pemain sepak bola profesional. Namun, sebuah cedera yang cukup serius menghantui perjalanan itu. Saat itu terasa seolah semuanya hancur. Saya dihadapkan pada kenyataan pahit bahwa jalur menuju lapangan hijau sebagai pemain ternyata berakhir di tengah jalan.")
        st.write("Melalui perjuangan yang tidak mudah, saya mulai memahami permainan dari sudut pandang yang berbeda. Saya belajar dari pengalaman saya sebagai pemain, baik yang baik maupun buruk, dan mencoba mentransfer pengetahuan dan semangat itu kepada para pemain muda yang bersemangat. Rasanya membangkitkan semangat baru ketika saya melihat mereka bermain dengan semangat yang sama yang saya miliki dahulu.")
        st.write("Menjadi seorang pelatih membuka mata saya pada sisi lain dari permainan ini. Itu bukan hanya soal teknik atau taktik, tapi juga tentang pembinaan karakter, motivasi, dan kekuatan mental. Saya menemukan kebahagiaan baru dalam membimbing, memberi inspirasi kepada mereka, dan menanamkan semangat juang yang saya bawa dalam diri.")
        st.write("Mungkin, takdir telah mengubah arah mimpi saya menjadi sesuatu yang lebih besar dari sekadar bermain di lapangan. Sekarang, saya tidak lagi mengejar bola di lapangan, tapi saya memimpin, membimbing, dan memotivasi mereka yang bermimpi seperti saya dulu.")
        st.write("Cidera itu bukanlah akhir, melainkan awal dari petualangan baru saya. Menjadi pelatih adalah jawaban dari semangat yang tak pernah padam untuk mencapai sesuatu yang lebih besar. Saya belajar bahwa kadang-kadang, terkadang kegagalan membuka pintu menuju perjalanan baru yang lebih berharga.")
        st.write("Setiap kali saya berdiri di pinggir lapangan, hati saya penuh dengan rasa syukur. Saya masih terlibat dalam olahraga yang saya cintai, tetapi dari perspektif yang berbeda. Perjalanan dari pemain yang cedera hingga menjadi pelatih telah mengajari saya bahwa kegagalan tidak selalu menghentikan kita; terkadang, ia mengarahkan kita pada perjalanan yang lebih bermakna.")
                
                
    elif selected_tab == "sedih":
                
        st.subheader("Membatasi Mimpi: Ketika Cinta pada Bulutangkis Tergesa-Gesa oleh Kendala")
        st.write("create: Uliano")
        st.write("Pada suatu masa, di sebuah sudut kecil di kota kecil, terdapat seorang anak muda yang memiliki mimpi besar: menjadi pemain bulutangkis yang menginspirasi. Namun, terlepas dari semangatnya yang menyala, ada batasan yang menghentikannya—bukan dari kekurangan bakat atau semangat, melainkan dari orang yang paling dicintainya: orang tuanya.")
        st.write("Tidak bisa dipungkiri bahwa bulutangkis adalah cinta sejati dalam hidupnya. Setiap bulan, setiap minggu, setiap hari, ia rela menghabiskan waktu di lapangan, memukul kok yang berdenting dengan semangat yang tak terbendung. Ia bermimpi berjalan di panggung besar, memenangkan kejuaraan, dan memancarkan semangat juang kepada jutaan orang. Tetapi, mimpi itu dihentikan oleh panggilan dari rumah.")
        st.write("Orang tuanya, dengan hati yang penuh kebaikan, menghentikan langkahnya menuju kejayaan bulutangkis. Mereka menutup pintu setiap kali ia ingin berlatih lebih lama, menghadirkan keraguan dan batasan tentang masa depannya. Alasan mereka adalah keamanan, keberlangsungan, dan 'masuk akal' menurut kacamata mereka.")
        st.write("Namun, terkadang, apa yang masuk akal bagi orang tua belum tentu sesuai dengan hasrat dan panggilan jiwa seseorang. Itu bukan hanya tentang memenangkan trofi atau menjadi terkenal; itu tentang mengejar sesuatu yang membakar api di dalam hati.")
        st.write("Ketika setiap anak muda berusaha menemukan identitas dan tujuannya dalam hidup, dia merasa terperangkap. Antara kewajiban kepada orang tua dan panggilan jiwa yang begitu kuat. Di satu sisi, ada tanggung jawab untuk mematuhi keinginan orang tua yang telah melakukan segalanya untuknya. Di sisi lain, ada impian besar yang tak pernah padam, yang memanggil untuk diwujudkan.")
        st.write("Jika saja dunia bisa melihat betapa bulutangkis bukan sekadar sebuah hobi bagi anak muda ini. Itu adalah lebih dari sekadar sebuah olahraga; itu adalah mimpi yang ingin mempersembahkan semangat, kerja keras, dan kesuksesan. Itu adalah bagian dari dirinya yang ingin diberikan kepada dunia.")
        st.write("Mungkin satu hari, ia akan menemukan jalan untuk menyatukan dunianya yang penuh tanggung jawab dengan hasratnya yang tak terbendung. Mungkin, orang tuanya akan melihat betapa bulutangkis adalah bagian dari jiwanya, bukan hanya kesenangan sesaat. Dan mungkin, pada akhirnya, mimpi yang dibatasi akan menemukan cara untuk terbang bebas, meski jalan menuju sana tidaklah mudah.")
        st.write("Mungkin kisah ini bukan tentang menentang orang tua atau mengecilkan nilai nasihat mereka. Tapi ini tentang menemukan keseimbangan antara kebutuhan kita dan kebahagiaan mereka. Dan pada akhirnya, tentang menemukan jalan kita sendiri menuju apa yang kita yakini. Mimpi itu bisa terlalu kuat untuk ditahan, tapi kadang-kadang, kita harus menemukan caranya untuk membiarkan mimpi itu melayang bebas.")
                
    elif selected_tab == "Lain-lain":
                
        st.subheader("Ketika Mimpi Jadi Kenyataan: Cerita Kemenangan di Kejuaraan Nasional Voli")
        st.write("create: Alvia")
        st.write("Kemenangan tak pernah terasa semanis ketika kamu mengejarnya dengan sepenuh hati. Bagi sebagian besar dari kita, sebuah kejuaraan nasional adalah mimpi terbesar yang hanya bisa diwujudkan oleh para atlet paling berdedikasi. Bagi saya, voli bukan sekadar olahraga. Ia adalah panggung di mana mimpi menjadi kenyataan.")
        st.write("Pengalaman mendebarkan saat berpartisipasi dalam Kejuaraan Nasional Voli masih terpatri kuat dalam ingatan saya. Semua dimulai dari latihan yang tak kenal lelah, keringat yang mengalir, dan semangat yang terus membara. Kami, sebagai tim, telah berkomitmen secara penuh untuk mencapai sesuatu yang lebih dari sekadar trofi. Kami membidik momen yang akan mengukir sejarah bagi kami.")
        st.write("Kompetisi dimulai dengan ketegangan yang tak tertahankan. Setiap servis, setiap smash, dan setiap blok menjadi detik-detik yang menggetarkan hati. Saat pertandingan berlangsung, terlihatlah semangat yang tak terbendung di mata rekan satu tim, di setiap gerakan yang dikerahkan untuk meraih tiap poin. Namun, persaingan bukanlah satu-satunya tantangan; ada tekanan dari ekspektasi dan harapan yang harus diemban. Semua itu menghadirkan tantangan tersendiri.")
        st.write("Namun, di tengah hiruk-pikuk pertandingan, kami menemukan alasan kami berada di sana: cinta pada olahraga ini dan dukungan luar biasa dari tim. Kami merangkul setiap kemenangan, namun juga belajar dari setiap kekalahan. Tiap peluang kami di lapangan adalah kesempatan untuk tumbuh dan menunjukkan apa yang kami bisa.")
        st.write("Dan akhirnya, saat momen yang kami tunggu-tunggu tiba, kami menemukan diri kami berada di puncak. Dalam laga final yang menegangkan, kami berhasil meraih gelar juara. Rasanya tak tergambarkan, suatu kegembiraan yang melebihi kata-kata. Itu bukan hanya kemenangan bagi kami, tetapi juga bagi semangat, dedikasi, dan kerja keras yang kami tanamkan.")
        st.write("Kemenangan itu, lebih dari sekadar trofi besar atau medali emas. Ia adalah cerminan dari perjuangan, pengorbanan, dan tekad yang mengalir dalam darah setiap pemain. Ini adalah pengingat bahwa mimpi yang dikejar dengan semangat tak pernah sia-sia.")
        st.write("Ketika saya melihat kembali perjalanan menuju kejuaraan itu, saya tak hanya melihat kemenangan; saya melihat perjalanan inspiratif kami. Kami bukan hanya menang dalam olahraga, tetapi juga menang dalam memahami arti dari semangat bertanding, kerja tim, dan ketekunan. Dan di atas segalanya, kami menang dalam menginspirasi orang lain untuk bermimpi besar dan bertekad mewujudkannya")
 

def main():
    st.title("Category")

    selected_category = st.sidebar.radio("Choose a category", ["Sport", "Art", "Music", "Film"])

    if selected_category == "Sport":
        show_sport_category()
    elif selected_category == "Art":
        show_art_category()
    elif selected_category == "Music":
        show_music_category()
    elif selected_category == "Film":
        show_film_category()





if __name__ == "__main__":
    main()

