
############################################ IMPORT LIBRARIES ################################################
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import requests
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

##############################################################################################################
################################################ SIDEBAR #####################################################
##############################################################################################################

######################## Contact Me link ################################
st.sidebar.markdown(
    """<a style='display: block; text-align: right;' href="https://github.com/AparGarg99"><b>Contact Me</b></a>
    """,
    unsafe_allow_html=True,
)

######################## READ IMAGE #####################################
st.sidebar.warning("""Please upload image OR Enter Image URL""")
uploaded_file = st.sidebar.file_uploader("Upload image", type=['png', 'jpg'])
url=st.sidebar.text_input('Enter image url','')
try:
	if uploaded_file is not None and url=='':
	    image = Image.open(uploaded_file)
	 

	elif uploaded_file is None and url!='':
		image = Image.open(requests.get(url, stream=True).raw)

	else:
		sample_url='https://user-images.githubusercontent.com/54896849/108807008-46b3d900-75c9-11eb-98fe-ce1b8242fc56.jpg'
		image = Image.open(requests.get(sample_url, stream=True).raw)

except:
	st.error("Invalid URL...try again !!")
	sample_url='https://user-images.githubusercontent.com/54896849/108807008-46b3d900-75c9-11eb-98fe-ce1b8242fc56.jpg'
	image = Image.open(requests.get(sample_url, stream=True).raw)

image=np.array(image)

######################## Take User Input #########################

st.sidebar.title('User Input Parameters')

######################### RESCALE ################################
st.sidebar.header('Rescale Image')
scale_percent = st.sidebar.selectbox('', sorted(list(range(10,110,10)),reverse=True),index=8)
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#st.write('After Resize: ',image.shape)

########################## CROP ##################################
st.sidebar.header('Crop Image')
x1 = st.sidebar.slider('From Left',0, image.shape[1]-2, 0, key='Crop1')
x2 = st.sidebar.slider('From Right',x1+1, image.shape[1], image.shape[1], key='Crop2')

y1 = st.sidebar.slider('From Top',0, image.shape[0]-2, 0, key='Crop3')
y2 = st.sidebar.slider('From Bottom',y1+1, image.shape[0], image.shape[0], key='Crop4')

image =image[y1:y2, x1:x2]
#st.write('After Crop: ',image.shape)

########################### BLUR ##################################
st.sidebar.header('Smoothen/Blur Image')

choose_blur=st.sidebar.selectbox('Choose Method', ['None','Averaging Filter','Gaussian Filter','Median Filter',
									'Denoising (Advance Method)','Bilateral Filtering (Advance Method)'])

if(choose_blur=='Averaging Filter'):
	blur = st.sidebar.slider('ksize',1, 99,1,2)
	image = cv2.blur(image,(blur, blur))

elif(choose_blur=='Gaussian Filter'):
	blur = st.sidebar.slider('ksize',1, 99,1,2)
	image = cv2.GaussianBlur(image, (blur, blur), 0)

elif(choose_blur=='Median Filter'):
	blur = st.sidebar.slider('ksize',1, 99,1,2)
	image = cv2.medianBlur(image,blur)

elif(choose_blur=='Denoising (Advance Method)'):
	den = st.sidebar.slider('searchWindowSize',0,30,0,key='den')
	image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, den)

elif(choose_blur=='Bilateral Filtering (Advance Method)'):
	diam=st.sidebar.slider('d (Diameter of each pixel neighborhood)',0,100,0)
	sigma_col=st.sidebar.slider('sigmaColor/sigmaSpace',0,100,0)
	image = cv2.bilateralFilter(image, diam, sigma_col, sigma_col)

############################# ROTATE ##################################
st.sidebar.header('Rotate Image')
rotate = st.sidebar.slider('degree',0,360,0)
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, rotate, 1.0)
image = cv2.warpAffine(image, M, (w, h))

############################ GRAYSCALING #############################
st.sidebar.header('GrayScale Image')
gscale=st.sidebar.checkbox('Yes')
if(gscale):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

############################ THRESHOLDING ##############################
if(gscale):
	st.sidebar.markdown('#### Image Thresholding')
	thresh=st.sidebar.selectbox('Choose Method', ['None','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV',
														'ADAPTIVE_MEAN', 'ADAPTIVE_GAUSSIAN','OTSU'])

	if(thresh=='BINARY'):
		ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	elif(thresh=='BINARY_INV'):
		ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
	elif(thresh=='TRUNC'):
		ret, image = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
	elif(thresh=='TOZERO'):
		ret, image = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
	elif(thresh=='TOZERO_INV'):
		ret, image = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
	elif(thresh=='ADAPTIVE_MEAN'):	
		image = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
	elif(thresh=='ADAPTIVE_GAUSSIAN'):
		image = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	elif(thresh=='OTSU'):	
		ret, image = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

########################  Contrast Manipulation #######################
if(gscale):
	st.sidebar.markdown('#### Contrast Manipulation (Gamma Transformation)')
	
	gamma=st.sidebar.selectbox('Choose gamma value', np.round(np.arange(0.2, 3.2, 0.2),1).tolist(),index=4)
	image = np.array(255*(image / 255) ** gamma, dtype = 'uint8') 

######################### Edge Detection ###############################
if(gscale):
	st.sidebar.markdown('#### Edge Detection')		
	ed=st.sidebar.selectbox('Choose Method', ['None','LAPLACIAN','SOBELX','SOBELY','CANNY'])

	ed_map={
	'LAPLACIAN':cv2.Laplacian(image,cv2.CV_8U),
	'SOBELX':cv2.Sobel(image,cv2.CV_8U,1,0,ksize=3),
	'SOBELY':cv2.Sobel(image,cv2.CV_8U,0,1,ksize=3),
	}

	if(ed not in ['None','CANNY']):
		image=ed_map[ed]

	elif(ed=='CANNY'):
		threshold1=st.sidebar.slider('threshold1',0,300,50,50)
		threshold2=st.sidebar.slider('threshold2',threshold1,400,threshold1,50)
		image = cv2.Canny(image,threshold1,threshold2)

######################## SHOW INTENSITY HISTOGRAM #########################
if(gscale):
	st.sidebar.markdown('#### Show Intensity distribution')
	showhist=st.sidebar.checkbox('Yes',key='hist')
	if(showhist):
		plt.figure(figsize=(5,3))
		plt.xlabel('Pixel values')
		plt.ylabel('No. of pixels')
		plt.hist(image.ravel(),256,[0,256]) 

######################## Morphological Transformations ####################
st.sidebar.header('Morphological Transformations')
mt = st.sidebar.selectbox('Choose Method',['None','Erosion','Dilation','Opening','Closing','Morphological Gradient','Top Hat','Black Hat'])
if(mt!='None'):
	k=st.sidebar.slider('kernal size',3,9,3,2)
	kernel=np.ones((k,k),np.uint8)
	mt_map={'Erosion':cv2.erode(image,kernel,iterations = 1),
			'Dilation':cv2.dilate(image,kernel,iterations = 1),
			'Opening':cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel),
			'Closing':cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel),
			'Morphological Gradient':cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel),
			'Top Hat':cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel),
			'Black Hat':cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)}
	image = mt_map[mt]


######################## BOUNDING BOX #####################################
st.sidebar.header('Bounding Box on Image')
bbox_x1 = st.sidebar.slider('From Left',0, image.shape[1]-2, 0)
bbox_x2 = st.sidebar.slider('From Right',bbox_x1+1, image.shape[1], image.shape[1])

bbox_y1 = st.sidebar.slider('From Top',0, image.shape[0]-2, 0)
bbox_y2 = st.sidebar.slider('From Bottom',bbox_y1+1, image.shape[0], image.shape[0])

thickness = st.sidebar.slider('Choose Thickness',0, 50,0,1)

#color = st.sidebar.selectbox('Color',['Black','Blue','Green','Red','White'])
#color_map={'Black':(0,0,0),'Red':(255,0,0),'Green':(0,255,0),'Blue':(0,0,255),'White':(255,255,255)}
#cv2.rectangle(image, (bbox_x1, bbox_y1), (bbox_x2, bbox_y2), color_map[color], thickness)

color=st.sidebar.color_picker('Choose colour ')
rgb_color=st.sidebar.text_input('Enter RGB values','0 0 0')
rgb=tuple([int(i) for i in rgb_color.split()])

cv2.rectangle(image, (bbox_x1, bbox_y1), (bbox_x2, bbox_y2), rgb, thickness)

##############################################################################################################
################################################ MAIN PAGE ###################################################
##############################################################################################################

######################## OpenCV Image #####################################

st.image('https://user-images.githubusercontent.com/54896849/108690271-2da31d80-7520-11eb-901f-ff6211508d79.PNG',use_column_width=True)

######################## ABOUT THE APP #####################################
expander_bar = st.beta_expander("About App")
expander_bar.markdown('''
	There is a plethora of tutorials on OpenCV on the internet, but none of them provide real-time testing functionality. This app aids in real-time analysis of basic image processing functions in OpenCV.
	[Source Code](https://github.com/AparGarg99/Tutorials/tree/master/streamlit_frontend_tutorial/app7_opencv_tutorial)

	**Advantages**:
	*	A better understanding of function outputs.
	*	A better understanding of the effect of change in parameter values on the output image.
	*	A better understanding of the effect of one image processing method on top of another.
	
		''')

######################## VISUALIZATIONS #####################################
for i in range(3):
	st.write('')

st.image(image)
st.pyplot()