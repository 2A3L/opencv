# Load the images
img =cv2.imread(MEDIA_ROOT + "/uploads/imagerecognize/armchair.jpg")

# Convert them to grayscale
imgg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# SURF extraction
surf = cv2.FeatureDetector_create("SURF")
surfDescriptorExtractor = cv2.DescriptorExtractor_create("SURF")
kp = surf.detect(imgg)
kp, descritors = surfDescriptorExtractor.compute(imgg,kp)

# Setting up samples and responses for kNN
samples = np.array(descritors)
responses = np.arange(len(kp),dtype = np.float32)

# kNN training
knn = cv2.KNearest()
knn.train(samples,responses)

modelImages = [MEDIA_ROOT + "/uploads/imagerecognize/1.jpg", MEDIA_ROOT + "/uploads/imagerecognize/2.jpg", MEDIA_ROOT + "/uploads/imagerecognize/3.jpg"]

for modelImage in modelImages:

    # Now loading a template image and searching for similar keypoints
    template = cv2.imread(modelImage)
    templateg= cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    keys = surf.detect(templateg)

    keys,desc = surfDescriptorExtractor.compute(templateg, keys)

    for h,des in enumerate(desc):
        des = np.array(des,np.float32).reshape((1,128))

        retval, results, neigh_resp, dists = knn.find_nearest(des,1)
        res,dist =  int(results[0][0]),dists[0][0]


        if dist<0.1: # draw matched keypoints in red color
            color = (0,0,255)

        else:  # draw unmatched in blue color
            #print dist
            color = (255,0,0)

        #Draw matched key points on original image
        x,y = kp[res].pt
        center = (int(x),int(y))
        cv2.circle(img,center,2,color,-1)

        #Draw matched key points on template image
        x,y = keys[h].pt
        center = (int(x),int(y))
        cv2.circle(template,center,2,color,-1)



    cv2.imshow('img',img)
    cv2.imshow('tm',template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
