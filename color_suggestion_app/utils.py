import numpy as np
import cv2
from sklearn.cluster import KMeans
from mtcnn import MTCNN

def detect_face_mtcnn(image):
    detector = MTCNN()
    results = detector.detect_faces(image)
    if results:
        x, y, width, height = results[0]['box']
        x, y = max(x, 0), max(y, 0)
        return (y, y + height, x + width, x)
    return None

def crop_face(image, face_location):
    top, bottom, right, left = face_location
    return image[top:bottom, left:right]

def extract_skin(face_img):
    img_ycrcb = cv2.cvtColor(face_img, cv2.COLOR_RGB2YCrCb)
    mask = cv2.inRange(img_ycrcb, (0, 133, 77), (255, 173, 127))
    skin = cv2.bitwise_and(face_img, face_img, mask=mask)
    return skin

def get_dominant_color(image, n_clusters=2):
    flat_img = image.reshape((-1, 3))
    flat_img = flat_img[np.any(flat_img != [0,0,0], axis=1)]
    if flat_img.shape[0] < 10:
        return [128, 128, 128]
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(flat_img)
    counts = np.bincount(kmeans.labels_)
    dominant = kmeans.cluster_centers_[np.argmax(counts)]
    return [int(x) for x in dominant]

def classify_season(rgb):
    r, g, b = rgb
    if r > 180 and g > 180:
        return "Spring"
    if b > 180:
        return "Winter"
    if r > g and g > b:
        return "Autumn"
    if r < 130 and b > 130:
        return "Summer"
    return "Winter"
