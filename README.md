Chronic Kidney Disease Prediction Using Machine Learning
This project predicts Chronic Kidney Disease (CKD) using patient data and machine learning models. The application is built using Streamlit and provides a simple and interactive interface for healthcare professionals to input patient information and receive predictions. The website is hosted on Render for easy accessibility.

Features
User Authentication: Secure login system to protect patient data.
Patient Data Input: Intuitive forms for entering relevant medical information.
CKD Prediction: Leverages a trained machine learning model for accurate predictions.
Results Display: Clear and easy-to-understand output of prediction results.
Web Hosting: Hosted on Render for seamless access.
Live Demo
Visit the live website here: https://ckd-hosting.onrender.com/

Usage (For Local Setup)
Clone the Repository:

bash
Copy code
git clone https://github.com/Shrajoy92/SEED_CKD.git
Navigate to the Project Directory:

bash
Copy code
cd SEED_CKD
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application Locally:

bash
Copy code
streamlit run main.py
Access the Application:

Open your browser and navigate to http://localhost:8501.

Hosting on Render
The application is hosted on Render to make it accessible online. The deployment process includes:

Pushing the code to your GitHub repository.

Linking your repository to Render.

Setting up a Web Service on Render with the start command:

bash
Copy code
streamlit run main.py
Render automatically handles deployment and hosting.

Files and Directories
main.py: The Streamlit application script.
login.py: Handles user authentication and session management.
home.py: Manages the home page and dashboard functionalities.
about.py: Provides information about the application and its purpose.
contact.py: Contains contact information and a form for user inquiries.
test.py: Includes test cases to ensure the application functions correctly.
trained_ckd.sav: The pre-trained machine learning model used for CKD prediction.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

Contact
For questions or support, please open an issue in this repository.
