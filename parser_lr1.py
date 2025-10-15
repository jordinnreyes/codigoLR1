#aqui lógica de LR(1), gramáticas
def analizar_gramatica(texto):
    terminales = set()
    no_terminales = set()

    for linea in texto.splitlines():
        if '->' not in linea:
            return "Error: Cada producción debe contener '->'"

        izquierda, derecha = linea.split('->')
        izquierda = izquierda.strip()
        derecha = derecha.strip()

        # Asumimos que el lado izquierdo es un solo símbolo no terminal
        # Validamos que sea mayúscula o mayúsculas (ejemplo)
        if not izquierda.isupper():
            return "Error: El símbolo no terminal a la izquierda debe ser mayúscula"

        no_terminales.add(izquierda)

        # Procesar símbolos del lado derecho separados por espacio
        simbolos_derecha = derecha.split()

        for simbolo in simbolos_derecha:
            if simbolo.isupper():
                no_terminales.add(simbolo)
            else:
                terminales.add(simbolo)

    return f"Gramática analizada correctamente.\nTerminales: {sorted(terminales)}\nNo terminales: {sorted(no_terminales)}"
