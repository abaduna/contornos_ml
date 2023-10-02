import cv2

img = cv2.imread('Fig.png') #importo la imagen

#Binarizar la imagen
imgCanny= cv2.Canny(img,10,50)

#encontrar los contornos

contornos,jerarquia =cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("el contenido de contornos es: ",len(contornos))


#dibujamos los contornos

cv2.drawContours(img,contornos,-1,(255,0,0),3) #entra la imagen , la colecion de punto, cual escribir -1 recore todo , el color,grosor


cv2.imshow("imagen", img) #la muestro
cv2.imshow("canny", imgCanny) #la muestro
cv2.waitKey(5000)

cv2.destoyAllWindows()