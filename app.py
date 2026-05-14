import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import mediapipe as mp
import numpy as np

st.title("FitAI - AI Fitness Coach")

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_draw = mp.solutions.drawing_utils

counter = 0
stage = None


def calculate_angle(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1] - b[1],
        c[0] - b[0]
    ) - np.arctan2(
        a[1] - b[1],
        a[0] - b[0]
    )

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


class VideoProcessor:

    def recv(self, frame):

        global counter
        global stage

        img = frame.to_ndarray(format="bgr24")

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = pose.process(rgb)

        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark

            hip = [
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
            ]

            knee = [
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
            ]

            ankle = [
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
            ]

            angle = calculate_angle(hip, knee, ankle)

            cv2.putText(
                img,
                str(int(angle)),
                tuple(np.multiply(knee, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            if angle > 160:
                stage = "up"

            if angle < 90 and stage == "up":
                stage = "down"
                counter += 1

            cv2.putText(
                img,
                f"Squats: {counter}",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            mp_draw.draw_landmarks(
                img,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="fitness",
    video_processor_factory=VideoProcessor
)