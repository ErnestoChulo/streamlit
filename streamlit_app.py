#hola 
import streamlit as st
st.title("CHATBOT DOCUMENTOS")
st.subheader("TU AMIGO CHAT")
st.header("Comienza aqui")
st.text("Este chat te ayudara a revisar documentos PDF para sacar lo mas relevante de ellos")
st.markdown(" > # ** Hola mundo**")#negritas, tamaño
st.markdown("---")
st.markdown("> Bordo") #linea horizontal
st.markdown("[Dame click](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
#st.markdown(![hola](escudo_alemania.png))

#matriz
st.latex(r"\begin{pmatrix}hola&guapo\\co&ca\end{pmatrix}")
#mostrar 
#boton
x = st.button('PICALE')
st.write(x, 'x es', x*x)

#subir archivos
st.markdown("---")
st.header("**Subir Archivos**")
pdf = st.file_uploader("Sube un archivo", type=["pdf", "jpg", "png"])
if pdf is not None:
   pdf_data = pdf.read()
    # Mostrar el PDF en un visor
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image = page.get_pixmap()
        st.image(image, use_column_width=True)

    # Cerrar el archivo PDF
    pdf_document.close()








