import streamlit as st


def show_katagori(katagori_name):
    st.write(" ")

def create_article():
    st.title("Create a New Article")

    # Kolom input untuk judul artikel
    title = st.text_input("Title")

    katagori = st.selectbox("Category", ["Sport", "Art", "Music","Film"])

    if katagori == "Sport":
     show_katagori("Sport")
    elif katagori == "Art":
     show_katagori("Art")
    elif katagori == "Music":
     show_katagori("Music")
    elif katagori == "Film":
     show_katagori("Film")

    # Kolom input untuk isi artikel
    content = st.text_area("Content", height=200)

    # Kolom input untuk informasi penulis
    author_info = st.text_input("Author")

    submitted = st.button("Upload Article")

    if submitted:
        if title and content:
        # Perform article storage process (e.g., into a database or temporary storage)
            st.success("Article successfully saved!")
            st.write(f"Title: {title}")
            st.write(f"Content: {content}")
            st.write(f"Author: {author_info}")
    else:
        st.error("Title and content are required.")

def main():
    create_article()

if __name__ == "__main__":
    main()
