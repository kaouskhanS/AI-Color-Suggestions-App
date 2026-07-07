# 🎨 AI Face Recognition & Dress Color Suggestion App

An AI-powered web application that analyzes a user's facial image to identify skin tone and recommends the most suitable dress color palettes using image processing and color theory. The application helps users make better fashion choices through personalized color suggestions.

---

## 📖 Project Overview

The **AI Face Recognition & Dress Color Suggestion App** uses computer vision and machine learning techniques to analyze facial features and determine the user's skin tone. Based on the detected tone, it recommends clothing colors that complement the user's appearance.

This project combines AI, image processing, and fashion color theory to deliver personalized outfit recommendations.

---

## ✨ Features

- 📷 Upload a facial image
- 🤖 AI-based skin tone detection
- 🎨 Personalized dress color recommendations
- 🌈 Multiple matching color palettes
- ⚡ Fast and lightweight interface
- 💻 User-friendly web application
- 📊 JSON-based color palette management

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### Libraries
- OpenCV
- NumPy
- Pillow
- Scikit-learn
- Pandas

### Data Storage
- JSON

---

## 📂 Project Structure

```
AI-Color-Suggestions-App/
│
├── color_suggestion_app/
│   ├── app.py
│   ├── utils.py
│   ├── palettes.json
│   ├── requirements.txt
│   └── README.md
│
└── LICENSE
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Color-Suggestions-App.git
```

Move into the project folder

```bash
cd AI-Color-Suggestions-App/color_suggestion_app
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running, open your browser and navigate to:

```
http://localhost:8501
```

---

## 🔄 Application Workflow

1. Upload a face image.
2. Detect facial region.
3. Analyze skin tone using AI-based clustering.
4. Match the detected tone with predefined color palettes.
5. Display recommended dress colors.

---

## 📊 Project Modules

- Face Image Upload
- Skin Tone Detection
- Color Analysis
- Dress Color Recommendation
- Palette Management
- User Interface

---

## 📷 Screenshots

You can add screenshots of:

- Home Page
- Image Upload
- Skin Tone Detection
- Recommended Color Palette
- Final Results

Store them in a `screenshots/` folder and reference them here.

---

## 📈 Future Enhancements

- Real-time webcam support
- Makeup color recommendations
- Hairstyle color suggestions
- Jewelry matching
- Seasonal fashion recommendations
- User profile history
- Mobile application
- Dark and Light mode

---

## 📦 Requirements

- Python 3.10+
- Streamlit
- OpenCV
- NumPy
- Pillow
- Scikit-learn
- Pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🎯 Project Objectives

- Analyze facial skin tone using AI.
- Recommend suitable clothing colors.
- Improve fashion decision-making.
- Demonstrate practical applications of computer vision.
- Provide an easy-to-use and interactive user experience.

---

## 💡 How It Works

The application uses image processing to extract facial skin-tone information. It then applies clustering techniques inspired by color analysis to categorize the skin tone and maps the result to curated fashion color palettes stored in `palettes.json`.

---

## 👨‍💻 Author

**S. Kouskhan**

- Aspiring Data Analyst
- Machine Learning Enthusiast
- Python Developer
- AI & Computer Vision Learner

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is developed for educational and learning purposes. Feel free to modify and improve it for personal or academic use.

---

## ⭐ If you like this project

If you found this project useful, please consider giving it a ⭐ on GitHub. It helps support the project and encourages further development.
