# Buffer Processor

Este proyecto implementa un sistema básico para cargar y procesar segmentos de datos de entrada en búferes. Es útil para manejar flujos de datos grandes o procesamiento incremental de texto.

## Descripción

El programa utiliza dos funciones principales:

### `cargar_buffer(entrada, inicio, tamano_buffer)`
Carga un segmento de la entrada en un búfer desde la posición inicial especificada hasta completar el tamaño del búfer o alcanzar el final de la entrada. Si no se llena el búfer completamente, se agrega un marcador de fin de archivo (`"eof"`).

#### Parámetros:
- `entrada`: Lista de caracteres a procesar.
- `inicio`: Índice inicial para cargar en el búfer.
- `tamano_buffer`: Tamaño máximo del búfer.

#### Retorna:
- Una lista de caracteres que representa el segmento del búfer.

### `procesar_buffer(entrada, tamano_buffer)`
Procesa el búfer de entrada y extrae los lexemas (palabras separadas por espacios) hasta que se encuentre el marcador `"eof"`.

#### Parámetros:
- `entrada`: Lista de caracteres a procesar.
- `tamano_buffer`: Tamaño máximo del búfer a cargar.

#### Funcionamiento:
1. Implementa dos punteros: `inicio` y `avance`, para simular la lectura del búfer.
2. Carga el búfer desde la entrada.
3. Itera por los caracteres, separando lexemas basados en espacios o el marcador `"eof"`.
4. Cuando el puntero `avance` alcance el final del búfer, recarga los datos desde una entrada simulada.
5. Imprime los lexemas procesados.

## Uso

El siguiente código muestra cómo usar las funciones:

```python
entrada = list("Esto es un ejemplo eof")
tamano_buffer = 10
procesar_buffer(entrada, tamano_buffer)
```

### Salida esperada:
```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
```

## Detalles Técnicos
- El marcador especial `"eof"` indica el final de los datos.
- Los punteros `inicio` y `avance` permiten simular la lectura progresiva del búfer.
- Los búferes se recargan automáticamente cuando el índice de avance alcanza el final del búfer actual.
