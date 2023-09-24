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

