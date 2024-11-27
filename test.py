import numpy as np
import pickle
import streamlit as st

def app():
    # Check if the user is logged in
    if 'username' not in st.session_state or st.session_state.username == '':
        st.warning('Please Login First')
        return  # Exit the function if the user is not logged in

    # Load the trained model
    loaded_model = pickle.load(open(r"C:\\Users\\Shrajoy Sur\\OneDrive\\Desktop\\prediction\\trained_ckd .sav", 'rb'))

    # Function for CKD Prediction
    def ckd_prediction(input_data):
        # Convert input data to a NumPy array
        input_data_as_numpy_array = np.asarray(input_data, dtype=float)  # Ensure all inputs are float

        # Reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Get prediction probabilities
        prediction_probs = loaded_model.predict_proba(input_data_reshaped)

        # Return prediction probabilities
        return prediction_probs[0]

    # Function to calculate lifestyle risk based on user inputs
    def calculate_lifestyle_risk(smoking, drinking, exercise, diet):
        # Assign weights to each lifestyle factor
        weights = {
            "smoking": 0.30,
            "drinking": 0.2,
            "exercise": 0.25,
            "diet": 0.25
        }

        # Map input scales to numerical values
        scale_mapping = {
            "Never": 0,
            "Rarely": 1,
            "Occasionally": 2,
            "Weekly": 3,
            "Daily": 4
        }

        # Convert inputs to numerical values
        smoking_score = scale_mapping[smoking]
        drinking_score = scale_mapping[drinking]
        exercise_score = scale_mapping[exercise]
        diet_score = int(diet)  # Diet is already a numerical scale (0-4)

        # Calculate weighted lifestyle risk
        lifestyle_risk = (
            weights["smoking"] * smoking_score +
            weights["drinking"] * drinking_score +
            weights["exercise"] * exercise_score +
            weights["diet"] * diet_score
        ) / 4  # Normalize to a 0-1 scale

        return lifestyle_risk

    # Function to calculate final risk
    def calculate_final_risk(ckd_model_score, lifestyle_risk, weight_medical=0.7, weight_lifestyle=0.3):
        # Combine risks using weighted sum
        final_risk = (weight_medical * ckd_model_score) + (weight_lifestyle * lifestyle_risk)
        return final_risk * 100  # Convert to percentage

    # Streamlit UI
    st.title('CKD Prediction and Risk Analysis')

    # Input fields for user data
    BMI = st.text_input('Enter your BMI')
    KIM_1 = st.text_input('KIM-1 value (ng/mL)')
    UMOD = st.text_input('UMOD value (ng/mL)')
    NGAL = st.text_input('NGAL value (ng/mL)')
    Albumin = st.text_input('Urine Albumin value (mg/g)')
    Creatinine = st.text_input('Urine Creatinine value (mg/dL)')
    EGF = st.text_input('EGF value (ng/mL)')

    q1 = st.selectbox(
        "How often do you smoke?",
        ["Never", "Rarely", "Occasionally", "Weekly", "Daily"]
    )

    q2 = st.selectbox(
        "How often do you drink?",
        ["Never", "Rarely", "Occasionally", "Weekly", "Daily"]
    )

    q3 = st.selectbox(
        "How often do you exercise?",
        ["Never", "Rarely", "Occasionally", "Weekly", "Daily"]
    )

    q4 = st.selectbox(
        "How balanced is your diet on a scale of 0 (unhealthy) to 4 (healthy)?",
        ["0", "1", "2", "3", "4"]
    )

    # Code for prediction
    if st.button('Show Prediction and Risk Analysis'):
        try:
            # Convert inputs to floats
            input_values = [
                float(BMI),
                float(KIM_1),
                float(UMOD),
                float(NGAL),
                float(Albumin),
                float(Creatinine),
                float(EGF),
            ]

            # Get prediction probabilities
            prediction_probs = ckd_prediction(input_values)
            ckd_model_score = prediction_probs[1]  # Probability of CKD

            # Calculate lifestyle risk
            lifestyle_risk = calculate_lifestyle_risk(q1, q2, q3, q4)

            # Calculate final risk
            final_risk = calculate_final_risk(ckd_model_score, lifestyle_risk)

            # Display results
            st.info(f"Probability of having CKD: {ckd_model_score * 100:.2f}%")
            st.success(f"Combined Progressive Risk Analysis (Medical + Lifestyle): {final_risk:.2f}%")

        except ValueError:
            # Handle invalid input
            st.error('Please enter valid numeric values for all inputs.')
