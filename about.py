import streamlit as st

def app():
    # Set the title of the page
    st.title("About the CKD Prediction App 🩺")

    # Introduction to CKD
    st.markdown(
        """
        ## What is Chronic Kidney Disease (CKD)? 🧑‍⚕️

        Chronic Kidney Disease (CKD) is a long-term condition where the kidneys gradually lose their ability to filter waste and excess fluids from the blood. This slow and progressive decline in kidney function can eventually lead to kidney failure, a condition that requires dialysis or a kidney transplant. CKD can go unnoticed for many years, which is why **early detection** is crucial.

        ### Common Causes of CKD 🏥:
        CKD can be caused by a variety of factors. The most common causes include:
        - **Diabetes 🩸**: High blood sugar levels over time can damage blood vessels in the kidneys.
        - **Hypertension (High Blood Pressure 💉)**: Uncontrolled high blood pressure puts excessive strain on the kidneys, impairing their function.
        - **Genetic Conditions 🧬**: Some genetic conditions, such as polycystic kidney disease, can predispose individuals to CKD.
        - **Chronic Infections 🤒**: Repeated urinary tract infections or kidney infections can damage kidney tissue over time.
        - **Medication Overuse 💊**: Prolonged use of certain medications, such as nonsteroidal anti-inflammatory drugs (NSAIDs), can also cause kidney damage.

        ### Symptoms of CKD 😔:
        - Swelling in your legs, ankles, or feet
        - Fatigue or tiredness
        - Reduced urine output
        - Shortness of breath
        - Nausea and vomiting
        - Blood in urine

        Unfortunately, symptoms of CKD may not appear until kidney function is significantly impaired, which is why regular checkups and early screenings are essential.
        """
    )

    # About the App
    st.markdown(
        """
        ## About This Application 🧑‍💻

        The **CKD Prediction App** is a comprehensive tool designed to assess your risk for Chronic Kidney Disease (CKD) by analyzing both your medical data and lifestyle choices. It combines modern machine learning techniques with your personal health information to give you a holistic understanding of your CKD risk.

        ### Key Features ⚙️:
        - **Accurate CKD Risk Prediction 📊**: The app uses advanced algorithms trained on a large dataset of biochemical markers to predict your likelihood of having CKD.
        - **Lifestyle Risk Assessment 🏋️‍♂️🍏**: It evaluates your lifestyle habits, such as smoking, drinking, exercise, and diet, to provide a complete picture of your health.
        - **Combined Risk Score 🧮**: The app generates a combined risk score by considering both medical and lifestyle factors to help you better understand your overall risk.
        - **Early Detection 🕵️‍♂️**: By recognizing early signs of CKD, you can take proactive steps to slow its progression.

        ### How It Works ⚙️:
        1. **Medical Data 🩺**: The app requires information such as your BMI, KIM-1, UMOD, NGAL, Albumin, Creatinine, and EGF levels to calculate your CKD risk. These markers help to determine how well your kidneys are functioning.
        2. **Lifestyle Input 🍏🍷**: You will also be asked to provide information about your smoking habits, drinking patterns, exercise routines, and diet. These factors can significantly influence kidney health and contribute to your overall risk.
        3. **Risk Calculation 💡**: After processing the inputs, the app provides:
           - **CKD Probability 🏥**: A percentage indicating your likelihood of having CKD.
           - **Lifestyle Risk Score ⚖️**: A score reflecting the impact of your lifestyle choices on your kidney health.
           - **Combined Risk 🧮**: A final score that combines both your medical and lifestyle risks to give you a comprehensive view of your CKD status.

        This holistic approach ensures that you're not just looking at your medical history but also at the day-to-day habits that contribute to your overall health.

        ### Technology Behind the App 💻:
        The app uses machine learning models to analyze the input data. These models have been trained on large datasets that include various medical and lifestyle factors. By utilizing predictive algorithms, the app can provide an accurate assessment of your risk for CKD based on the data you provide.
        """
    )

    # Why Early Detection Matters
    st.markdown(
        """
        ## Why Early Detection of CKD is Crucial ⏳

        **Early detection** of Chronic Kidney Disease is vital because it allows for timely intervention, which can significantly slow down the progression of the disease. In the early stages, CKD can be managed with lifestyle changes and medications, potentially avoiding the need for dialysis or a kidney transplant.

        ### Benefits of Early CKD Detection ✅:
        - **Prevention of Kidney Damage 🚫**: By detecting CKD early, you can take steps to protect your kidneys from further damage.
        - **Better Management of Risk Factors ⚖️**: Early diagnosis allows healthcare providers to address underlying conditions such as high blood pressure and diabetes, which contribute to CKD.
        - **Improved Quality of Life 🌟**: Catching CKD early can help you maintain an active and healthy lifestyle by preventing debilitating symptoms.
        - **Reduced Healthcare Costs 💰**: Addressing CKD early can prevent expensive treatments like dialysis, which are often required when the disease progresses to advanced stages.

        **Remember**, even if you do not show symptoms, regular screenings for CKD are important if you have risk factors like hypertension, diabetes, or a family history of kidney disease.

        ### What You Can Do 🏃‍♀️:
        - **Monitor your health 🩺**: Regular checkups and lab tests can help detect CKD before symptoms appear.
        - **Adopt a healthy lifestyle 🍏**: Managing your weight, quitting smoking 🚭, limiting alcohol intake 🍷, and eating a balanced diet can help protect your kidneys.
        - **Follow medical advice 👨‍⚕️**: If diagnosed with CKD, work closely with your healthcare provider to manage the condition and slow its progression.
        """
    )

    # Disclaimer
    st.markdown(
        """
        ---
        ## Disclaimer ⚠️
        The CKD Prediction App is an educational tool and should not replace medical advice. The results provided by this app are based on algorithms and predictive models that estimate the likelihood of CKD. Please consult with a healthcare professional for a thorough evaluation and diagnosis. 

        The app aims to help individuals become more aware of their health, but it is not intended to diagnose or treat any medical condition. Always seek the guidance of your physician or other qualified health provider with any questions you may have regarding your health.
        """
    )

    # Footer
    st.markdown("---")
    st.markdown("© 2024 CKD Prediction App | Developed with ❤️ using Streamlit.")

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app()
