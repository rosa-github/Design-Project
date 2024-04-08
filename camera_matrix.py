def camera_matrix():
    import os
    import glob
    import cv2
    import numpy as np
    # Defining the dimensions of checkerboard
    CHECKERBOARD = (6,9)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # Creating vector to store vectors of 3D points for each checkerboard image
    objpoints = []
    # Creating vector to store vectors of 2D points for each checkerboard image
    imgpoints = []

    # Defining the world coordinates for 3D points
    objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    prev_img_shape = None

    # Extracting path of individual image stored in a given directory
    images = glob.glob('cherckerboard 2/*.JPG')

    for fname in images:
        try:
            img = cv2.imread(fname)
            if img is None:
                raise FileNotFoundError("Failed to load image: {}".format(fname))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, 
                                                    cv2.CALIB_CB_ADAPTIVE_THRESH + 
                                                    cv2.CALIB_CB_FAST_CHECK + 
                                                    cv2.CALIB_CB_NORMALIZE_IMAGE)
            
            if ret == True:
                objpoints.append(objp)
                
                # Refine the pixel coordinates for given 2D points
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)
                
                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

                # Create a named window with a specific size
                cv2.namedWindow('img', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('img', 800, 600)  # Set the window size to 800x600 pixels


                #cv2.imshow('img', img)
                #cv2.waitKey(500)  # Display the image for 0.5 seconds
        except Exception as e:
            print("Error processing image {}: {}".format(fname, e))
            continue
            
    cv2.destroyAllWindows()

    # Calculate the image size
    h, w = img.shape[:2]


    """
    Performing camera calibration by 
    passing the value of known 3D points (objpoints)
    and corresponding pixel coordinates of the 
    detected corners (imgpoints)
    """
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    img = cv2.imread('cherckerboard 2/GOPR0092.JPG')
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

    return mtx, newcameramtx, dist, w, h, objpoints, rvecs, tvecs, imgpoints