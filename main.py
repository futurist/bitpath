import numpy as np
import cv2

img = cv2.imread('test.jpg',0)
H,W = img.shape
H-=1
W-=1

LOW_THRED = 100
HL_DIFF = 30

minLineHeight = 10
maxLineHeight = min(W, min(H, 50) )

def down(i,j):
	y=i; x=j;
	curve = ()
	value = (img[i,j],)

	# find top edge
	c=0;M=0
	if img[i,j] < LOW_THRED:
		while( img[i,j] < LOW_THRED and i<H ):
			i+=1;c+=1
	else:
		while( img[i,j] >= LOW_THRED and i>=0 ):
			i -= 1; c-=1
	curve+=(c,)


	# find LightUp List
	value+=(img[i,j],)
	c=0;M=0
	while( i+1<H and img[i,j] < img[i+1,j] ):
		if i>=H: break
		i+=1;c+=1


	curve+=(c,)



	# find Highlight List
	c=0;M=0
	# here use dtype="int32" to convert uint8 type to do subtraction
	while( i+1<H and abs( int(img[i,j]) - int(img[i+1,j]) )<HL_DIFF and c<maxLineHeight and img[i+1,j]>LOW_THRED ):
		if i>=H: break
		i+=1;c+=1

	curve+=(c,)
	value+=(img[i,j],)



	# find LightDown List
	c=0;M=999
	while( i+1<H and img[i,j] > img[i+1,j] and img[i+1,j]>LOW_THRED):
		if(img[i+1,j]<M):
			M = img[i+1,j]
		i+=1; c+=1
		if i>=H: break

	if M==999: M=0
	curve+=(c,)
	value+=(M,)


	
	imgA = img[y+curve[0]:y+sum(curve[:])+1, x]
	valid = sum(curve[1:])

	print x,y,valid, curve,value, imgA, sum(imgA),
	if len(imgA) : 
		print np.mean(imgA), np.std(imgA)
	else:
		print

	return curve, value


def patLine(y,x):
	slop = 45	# 30 deg max in left or right
	# curve,value = down(y,x+1)
	curve,value = down(y,x)
	curve,value = down(y,x-1)
	curve,value = down(y,x-2)
	curve,value = down(y,x-3)
	curve,value = down(y,x-4)
	curve,value = down(y,x-5)





# cv2.imwrite('aa2.jpg', np.fromfunction(f, img.shape ,dtype=int)  )

# print img, img.shape, img.ndim, img.size, img.dtype, img.itemsize

row, col = img.shape
print row,col

curRow = 0
curCol = 0

patLine(0,39)

for i in range(row):
	#print i,img[i]
	pass


