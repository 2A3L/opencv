import cv2
import numpy as np

imagen1 = cv2.imread("/home/chiropepitacanela/Documentos/Python en visualcode/foto.png")
imagen2 = cv2.imread("/home/chiropepitacanela/Documentos/Python en visualcode/FotoReconocimiento/foto1.png")


diferencia = cv2.subtract(imagen1, imagen2)


resultado = not np.any(diferencia)


if resultado is True or resultado2 is True or resultado3 is True or resultado4 is True:
	print "Las imagenes son iguales"
else:
	cv2.imwrite("result.png", diferencia)
	print "Incorrecto"
	

#import cv2
#import numpy as np

#ruta1 = "/home/chiropepitacanela/Documentos/Python en visualcode/foto.png"
#ruta2 = "/home/chiropepitacanela/Documentos/Python en visualcode/FotoReconocimiento/foto.png"

#ruta = ("/home/chiropepitacanela/Documentos/Python en visualcode/FotoReconocimiento/foto{}.png")

#termina = True
#i= 0


#while termina:
#	imagen1 = cv2.imread("/home/chiropepitacanela/Documentos/Python en visualcode/foto.png")
#	imagen2 = cv2.imread("/home/chiropepitacanela/Documentos/Python en visualcode/FotoReconocimiento/foto.png")
#
#	diferencia = cv2.subtract(ruta1, ruta2)

#	resultado = not np.any(diferencia)
#	if resultado is True:
#		print "Las imagenes son iguales"
#		termina=False
#	else:
#		#cv2.imwrite("result.png", diferencia)
#		print "Incorrecto"
#		i += 1
#		ruta2 = "/home/chiropepitacanela/Documentos/Python en visualcode/FotoReconocimiento/foto{}.png".format(i)
