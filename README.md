# FitAI — AI Fitness Coach

FitAI is a real-time AI-powered fitness coaching application that uses Computer Vision and Machine Learning to track exercises, count repetitions, and analyze body posture using webcam input.

## Features

- Real-time pose detection
- AI squat counter
- Exercise posture tracking
- Live webcam integration
- Streamlit web application
- MediaPipe pose estimation

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Streamlit
- NumPy

## How It Works

The application uses MediaPipe Pose to detect body landmarks from webcam frames. Joint angles are calculated using Computer Vision techniques to count squats and analyze movement accuracy in real time.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/anwesha24bce10681/FitAI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## Future Improvements

- Pushup counter
- Calories burned prediction
- Workout recommendations
- Exercise selection menu
- Progress dashboard
- Voice feedback assistant

## Author

Anwesha Rout