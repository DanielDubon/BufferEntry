def cargar_buffer(entrada, inicio, tamano_buffer):
    """
    Carga un segmento de la entrada en el búfer desde la posición de inicio
    hasta completar el tamaño del búfer o llegar al final de la entrada.
    """
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(entrada, tamano_buffer):
    """
    Procesa el búfer de entrada y extrae lexemas separados por espacios o el carácter especial 'eof'.
    """
    inicio = 0
    avance = 0
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexema = []

    while "eof" not in buffer or avance < len(buffer):
        char = buffer[avance]
        avance += 1

        # Si encontramos un espacio o el centinela, procesamos el lexema
        if char == " " or char == "eof":
            if lexema:  # Si el lexema no está vacío
                print("Lexema procesado:", "".join(lexema))
                lexema = []

            # Si el centinela eof es encontrado, se rompe el bucle
            if char == "eof":
                break
        else:
            lexema.append(char)

        # Recargar el búfer al final cuando avance llego al final del bufer
        if avance == len(buffer):
            inicio += tamano_buffer
            buffer = cargar_buffer(entrada, inicio, tamano_buffer)
            avance = 0


entrada = list("Esto es un ejemplo eof")
tamano_buffer = 10


procesar_buffer(entrada, tamano_buffer)
