#######################################################################
################## Detección de multiples objetos #####################
#######################################################################
#----------------------------------------------------------------------

# Importando OpenCV y Numpy
import cv2
import numpy as np



#----------------------------------------------------------------------
# webcam(cam, color_avr)
#	Inicia la cámara y detecta el área de la imágen que se encuentra
#	dentro del rango de valores de detección.
#
# cam   	: Objeto 'VideoCapture' recibido desde la función 'main'
# color_avr : Color promedio del área seleccionada.
# 
#
#
# add(m, num)
# 	Fija las reglas para la suma de un número(num) a todos los elementos 
# 	de una vector(m).
#	
# Si al sumar el número, el resultado excede a 255 se reemplaza por 255.
# Si al sumar el número, el resultado es negativo se reemplza por 0.
# 	
#----------------------------------------------------------------------

def webcam(cam,color_avr):
	kernel=np.ones((5,5),np.uint8)
	def add(m,num):
		output = np.array([0,0,0],np.uint8)
		for i,e in enumerate(m):
			q = e+num
			if q>=0 and q<=255: output[i] = q
			elif q>255: output[i]=255
			else: output[i] = 0
		return output
	rangomax = add(color_avr,15)
	rangomin = add(color_avr,-15)
	while(True):
		ret,frame=cam.read()
		mascara=cv2.inRange(frame,rangomin,rangomax)
		opening=cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)
		contours,hierarchy = cv2.findContours(opening,1,2)
		for cnt in contours:
			if np.size(cnt) > 500:
				x,y,w,h=cv2.boundingRect(cnt)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
				cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,255),-1)
		cv2.imshow("cam",frame)
		k=cv2.waitKey(1) & 0xFF
		if k==27:
			break
	cam.release()
	cv2.destroyAllWindows()

#----------------------------------------------------------------------
# main: función principal
#	Genera la captura de imágenes para poder seleccionar el área a 
#	detectar.
#	
# variables globales: board, p
#
# cam	: Objeto 'VideoCapture', para la captura de imágenes.
# p 	: Si es verdadero(True) se procede con la función 'webcam'.
# board : Se genera una matriz de la misma dimension de imágenes
#		  capturadas.
#
#----------------------------------------------------------------------
def main():
	global board,p
	p = False
	cam = cv2.VideoCapture(1)
	board = np.zeros((int(cam.get(4)),int(cam.get(3)),3),dtype=np.uint8)
	while(True):
		ret,frame=cam.read()
		cv2.namedWindow('board')
		cv2.setMouseCallback('board', paint)
		dst = cv2.addWeighted(frame,1,board,1,0)
		cv2.imshow('board',dst)
		k=cv2.waitKey(1) & 0xFF
		if k==27 or p:
			break
	cv2.destroyAllWindows()
	if xi!=xf and yi!=yf:
		ext = frame[yi:yf,xi:xf] # ext: Se extrae frame  
								 #		desde (xi,yi) a (xf,yf).
		s=np.array([0,0,0])
		for i in range(np.shape(ext)[0]):
			for j in range(np.shape(ext)[1]):
				s+=ext[i][j]
		webcam(cam,s/((i+1)*(j+1)))

if __name__=='__main__':

	main()