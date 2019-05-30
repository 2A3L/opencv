#Importar librerias de openCV
import numpy as np
import cv2
    
#Importar lbrerias casacare rostro y cara
detectar_cara = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_frontalface_alt2.xml')
ojo_derecho = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_righteye_2splits.xml')
ojo_izquerdo = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_lefteye_2splits.xml')

#Capturar video camara ( el 2 es por camara usb, 0 por camara notebook)
cap = cv2.VideoCapture(2)

continuar = True;
#Ciclo while
while continuar:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cara = detectar_cara.detectMultiScale(gray, 1.3, 5)
    print('==== DETECTANDO ROSTRO ====')
    #Ciclo deteccion rostro
    for (x,y,w,h) in cara:
        cv2.rectangle(img,(x,y),(x+w,y+h),(400,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w] 
        
        #Si detecta un rostro, busca ojos
        OjoDerecho = ojo_derecho.detectMultiScale(roi_gray)
        print('\n1. ====  ROSTRO DETECTADO')

        #Ojo derecho
        for (ex,ey,ew,eh) in OjoDerecho:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            OjoIzquerdo = ojo_izquerdo.detectMultiScale(gray, 1.3, 5)
            print('2. ===== OJO DERECHO DETECTADO')
            
            #Ojo izquerdo
            for (ex,ey,ew,eh) in OjoIzquerdo:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                print('3. ====== OJO IZQUERDO DETECTADO')
                
                #Sacar foto
                leido, frame = cap.read()
                if leido == True:
                    cv2.imwrite("foto.png", frame)

                    print("4. ======= Foto tomada correctamente ======")
                    print("\n ================ FIN ===========================")
                    continuar = False
    
    #Desplegar imagen camara
    cv2.imshow('img',img)
    #Presionar escape, para salir
    k = cv2.waitKey(30) & 0xff
    #Re empezar el ciclo
    if k == 27:
        break #volver al inicio

cap.release()
cv2.destroyAllWindows()
