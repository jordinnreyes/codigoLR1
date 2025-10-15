import streamlit as st
from parser_lr1 import analizar_gramatica
from automatas import construir_afd
from utils import limpiar_texto

def app():
    st.title("Proyecto Compiladores: Analizador LR(1)")

    # Entrada de la gramática
    gramatica_input = st.text_area("Ingresa la gramática (formato específico):")

    if st.button("Analizar"):
        if gramatica_input.strip() == "":
            st.warning("Por favor ingresa una gramática válida.")
            return
        
        # Limpiar texto (ejemplo)
        texto_limpio = limpiar_texto(gramatica_input)
        st.write("Texto limpio:")
        st.code(texto_limpio)

        # Llamar función del parser
        resultado_parser = analizar_gramatica(texto_limpio)
        st.write("Resultado del parser:")
        st.code(resultado_parser)

        # Construir AFD a partir del resultado (ejemplo)
        afd = construir_afd(resultado_parser)
        st.write("Automata AFD generado:")
        st.code(afd)

if __name__ == "__main__":
    app()
