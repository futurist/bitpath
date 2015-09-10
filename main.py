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

	# find top edge
	c=0;M=0
	if img[i,j] < LOW_THRED:
		while( img[i,j] < LOW_THRED and i<H ):
			i+=1;c+=1
	else:
		while( img[i,j] >= LOW_THRED and i>=0 ):
			i -= 1; c-=1

		# fix by add 1 if looked back, so we stand on right pix
		if c<0 :
			c+=1; i+=1

	curve+=(c,)
	value = (img[i,j],)


	# find LightUp List
	c=0;M=0
	while( i+1<H and img[i,j] < img[i+1,j] ):
		if i>=H: break
		i+=1;c+=1


	curve+=(c,)
	value+=(img[i,j],)



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

	print x,y, '\t', valid, '\t', curve, '\t',sum(imgA),
	if len(imgA) :
		print int(np.mean(imgA)),'\t',  int(np.std(imgA)),
	else:
		print "",
	print  value,  imgA

	return curve, value


def patLine(y,x):

	shapeA = ()
	while( x>=0 and x<=W ):
		curve,value = down(y,x)
		imgA = img[ y+curve[0] : y+sum(curve[:])+1, x]
		valid = sum(curve[1:])
		if not valid :
			break
		else:
			x-=1
			shapeA += ( curve[0], valid, int(sum(imgA)), int(np.mean(imgA)) )

	shapeA = np.array(shapeA).reshape(-1, 4)
	print shapeA[:,2], np.mean( shapeA[:,2] )


# cv2.imwrite('aa2.jpg', np.fromfunction(f, img.shape ,dtype=int)  )

# print img, img.shape, img.ndim, img.size, img.dtype, img.itemsize

row, col = img.shape
print row,col

curRow = 0
curCol = 0

patLine(3,12)

for i in range(row):
	#print i,img[i]
	pass


