import cv2

# Load the image by using cv2.imread() function
image = cv2.imread('./IMG_2194.jpg')
#Change the image from RGB to grayscale image by using cv2.cvtColor() function
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce background by using cv2.GaussianBlur() function
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use Canny edge detection to detect outer edges using cv2.Canny() function
edges = cv2.Canny(blurred, 30, 150)

# Apply Hough Circles using cv2.HoughCircles() function
circles = cv2.HoughCircles(
    edges,
    cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=30, param2=150, minRadius=0, maxRadius=0
)

# Find contours in the edge-detected image using cv2.findContours() function
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area and get the largest one using sorted() function
contours = sorted(contours, key=cv2.contourArea, reverse=True)
largest_contour = contours[0]

# Fit a circle to the largest contour using radius and cv2.minEnclosingCircle() function
center, radius = cv2.minEnclosingCircle(largest_contour)
center = tuple(map(int, center))

# Draw the circle on the original image with a green line using cv2.circle() function
cv2.circle(image, center, int(radius), (0, 255, 0), 8)

# Draw the center of the circle in red using cv2.circle() function
cv2.circle(image, center, 5, (0, 0, 255), -1)

# Use cv2.imshow() to display the image overlay
cv2.imshow('Circumference Detection', image)
cv2.waitKey(0)
#Turn off the image overlay display after stopping the program using cv2.destroyAllWindows()
cv2.destroyAllWindows()
