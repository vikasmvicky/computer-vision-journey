import cv2

img1 = cv2.imread("data/dog/dog.jpeg")
img2 = cv2.imread("data/dog/dog1.jpeg")
if img1 is None or img2 is None:
    print("error loading images")
    exit()

orb=cv2.ORB_create()

kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x: x.distance)
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None)
good_matches = [m for m in matches if m.distance < 50]

print("Total matches:", len(matches))
print("Good matches:", len(good_matches))

if len(good_matches) > 30:
    print(" Images are SIMILAR")
else:
    print(" Images are DIFFERENT")
# Show result
cv2.imshow("Matches", result)
cv2.waitKey(0)
cv2.destroyAllWindows()