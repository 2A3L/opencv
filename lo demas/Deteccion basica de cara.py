#Importar librerias
import numpy as np
import cv2 
import timeit

#Ruta donde esta instalado el opencv y haarcacade
deteccion = cv2.CascadeClassifier('/home/chiropepitacanela/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt.xml')

#Enviar camara web, 0 Notebook , 2 USB Cam
camara = cv2.VideoCapture(2) #0 Notebook

#Inicializamos el frame
fondo = None;

#Deshabilitamos OpenCL para lograr funcionamiento correcto
cv2.ocl.setUseOpenCL(False)

#Ciclo while hasta break
while(True):
    #Leer frame temporal
    obtener, ventana = camara.read()
    
    #Imagen blanco y negro
    obtencionGris = cv2.cvtColor(ventana, cv2.COLOR_RGB2GRAY)
    obtencionGris = cv2.GaussianBlur(obtencionGris,(21,21),0) #Eliminacion de fondos

    #En caso de error de fondo, envia un fondo automatico hasta leer uno
    if fondo is None:
        fondo = obtencionGris
        continue

    #Diferencia de fondo
    resta = cv2.absdiff(fondo, obtencionGris)

    #Diferencia entre espacios
    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]

    #Eliminar espacios en blanco
    umbral = cv2.dilate(umbral,None, iterations=2)

    #Deteccion de contornos
    contornosimg = umbral.copy()

    #Buscar contornos detectados
    contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #Busqueda de contornos encontrados
    for c in contornos:
        #Eliminamos los contornos pequeños
        if cv2.contourArea(c)<500:
            continue

        #obtenemos el bounds del contorno, el rectangulo mayor que engloba al contorno
        (x, y, w, h) = cv2.boundingRect(c)
        #dibujamos el rextangulo del bounds
        cv2.rectangle(ventana,(x, y),(x + w, y+h),(0, 255, 0),2)
        
    #buscamos las coordenadas de los rostros (si los hay) y guardamos su posicion
    cara = deteccion.detectMultiScale(obtencionGris, 1.3, 5)
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in cara:
        """cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
            img= imagen
            pt1= vertice del rectangulo
            pt2= vertice del rectangulo opuesto a pt1
            rec= especificacion alternativa del rectangulo dibujado
            color= color del rectangulo o brillo(imagen en escala de grises)
            thickness= grosor de lineas que conforman el rectangulo. los valores negativos, 
            como CV_FILLED, significan que la funcion tiene que dibujar un rectangulo relleno
            lineType= tipo de linea
            shift= numero de bits fraccionarios ern las coordenadas del punto
        """
        cv2.rectangle(ventana,(x,y),(x+w,y+h),(125,255,0),2)
 
    #Mostramos la imagen
    cv2.imshow('ventana',ventana)
     
    #con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()