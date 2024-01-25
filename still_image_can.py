import cv2

# Load the image
image = cv2.imread('./IMG_2194.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and background
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use Canny edge detection
edges = cv2.Canny(blurred, 30, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area and get the largest one
contours = sorted(contours, key=cv2.contourArea, reverse=True)
largest_contour = contours[0]

# Fit a circle to the largest contour
center, radius = cv2.minEnclosingCircle(largest_contour)
center = tuple(map(int, center))

# Draw the circle on the original image with a green line
cv2.circle(image, center, int(radius), (0, 255, 0), 2)

# Draw the center of the circle in red
cv2.circle(image, center, 5, (0, 0, 255), -1)

# Display the result
cv2.imshow('Circumference Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Note: I tried using the Hough circles function but it didn't make a circumerfance overlay as good as the method I am using right now (radius/minEnclosingCircle function)."""
