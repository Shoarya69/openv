import cv2
import os
from dotenv import load_dotenv

load_dotenv()

cap = cv2.VideoCapture(os.getenv("ip_video"))