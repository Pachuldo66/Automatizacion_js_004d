"""
Este es un sencillo script que nos permite convertir codigo Python a JavaScript y viceversa. 
El proceso se realiza gracias al modulo 'Jiphy' el cual puedes descargar ejecutando el siguiente comando: pip install jiphy
Es un script muy sencillo, y el cual necesita un poco de optimizacion (Eliminación de elementos irrelevantes e incervibles)
"""
import jiphy
import os

automatizacion_firefox = "Nombre del archivo (py o js) que contiene el codigo que queremos convertir"
automatizacion_firefox_js = "" # Nombre del archivo que contendra el codigo convertido

# Para extraer todo el texto del archivo con el codigo, declramos la funcion "getTextFile"
def getTextFile(automatizacion_firefox):
    with open(automatizacion_firefox, 'r') as File:
        code = File.read()
        File.close()
        return code

# Estas funciones crearan los archivos con su correspondiente extensión
def createCodeFilePy(automatizacion_firefox_js, content):
    with open(automatizacion_firefox_js,'w') as codeFile:
        codeFile.write(content)
        codeFile.close()
    print('Archivo "%s" creado con exito' % automatizacion_firefox_js)

def createCodeFileJS(automatizacion_firefox_js, content):
    with open(automatizacion_firefox_js,'w') as codeFile:
        codeFile.write(content)
        codeFile.close()
    print('Archivo "%s" creado con exito' % automatizacion_firefox_js)

# Esta función convierte coodigo python a javascript
def  convertToPy(automatizacion_firefox):
    code = getTextFile(automatizacion_firefox)
    codePy =jiphy.to.python(code)
    return codePy

# Esta función convierte codigo javascript a python
def convertToJS(automatizacion_firefox):
    code = getTextFile(automatizacion_firefox)
    codeJS = jiphy.to.javascript(code)
    return codeJS

def isExtension(string, ext):
    if string.endswith(ext):
        return string
    else:
        return string + ext

# La función "StartConvertion" inica todo el proceso de conversion
# Y se utilizan ciertas funciones adicionales para evitar malas entradas del usuario
def StartConvertion():
    print('\n')    
    print("********************* Conversión De Codigo - Python y JavaScript *********************")
    automatizacion_firefox = input("Ingresa la ruta del archivo para convertir: ")
    if os.path.exists(automatizacion_firefox):
        if automatizacion_firefox.endswith('.py'):
            archivoConversion = input("Ingrese la ruta y el nombre del nuevo archivo en donde se guardara la conversión: ")
            automatizacion_firefox_js = isExtension(archivoConversion, '.js')
            conJS = convertToJS(automatizacion_firefox)
            createCodeFileJS(automatizacion_firefox_js, conJS)
        elif automatizacion_firefox.endswith('.js'):
            archivoConversion = input("Ingrese la ruta y el nombre del nuevo archivo en donde se guardara la conversión: ")
            automatizacion_firefox = isExtension(archivoConversion, '.py')
            conPy = convertToPy(automatizacion_firefox)
            createCodeFilePy(automatizacion_firefox_js, conPy)
        else:
            print("Debe introducir la ruta de un archivo 'py' o 'js'")
            StartConvertion()
    else:
        print('La ruta "%s" no ha sido encontrada' % automatizacion_firefox)
        StartConvertion()    

StartConvertion()