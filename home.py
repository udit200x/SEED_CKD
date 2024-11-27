import streamlit as st


def app():
    
  
    # Set the title with a larger, bolder heading
    st.title("🩺 **Chronic Kidney Disease (CKD) Prediction App** 🌿")

    # Introduction with a focus on prevention and awareness
    st.markdown(
        """
        ## Welcome to the CKD Prediction App!  
        Chronic Kidney Disease (CKD) is a serious health condition that affects millions of people worldwide.  
        With our app, you can **assess your risk** based on **medical and lifestyle factors**. Our goal is to raise awareness about kidney health and provide insights into your health journey.

        🌱 **Let's prevent CKD together!**
        
        ### 📊 Features:
        - **Medical Risk Assessment:** Predict the likelihood of CKD based on biochemical markers.
        - **Lifestyle Evaluation:** Understand how your habits (like smoking, drinking, and exercise) affect your kidney health.
        - **Holistic Risk Score:** A combined score that helps guide your healthcare decisions.

        ---
        ### 🎯 Why is CKD Prevention Important?
        - **Early detection** is key to preventing kidney failure.
        - Lifestyle changes can make a huge difference in managing your risk.
        - Take control of your health with **simple, actionable steps**!

        **Prevention is always better than cure!**
        """
    )

    # Add a space before an important call to action
    st.markdown("---")
    
    # Inspirational Quote with enhanced formatting
    st.markdown(
        """
        ## 📝 *"The greatest wealth is health."*  
        — **Virgil**  
        """
    )

    # A section with facts about CKD
    st.markdown("### 🔍 **Did You Know?**")
    st.write(
        """
        - **CKD affects 1 in 10 adults worldwide**, and it often goes undetected until it reaches an advanced stage.
        - It is a leading cause of **kidney failure** and **dialysis**.
        - **Controlling blood pressure, maintaining a healthy weight,** and **regular exercise** can significantly reduce the risk of CKD.
        """
    )

    # A call to action for preventive actions
    st.markdown("### 🚶‍♂️ **How to Prevent CKD**")
    st.write(
        """
        - **Maintain a healthy lifestyle**: Eat a balanced diet, exercise regularly, and stay hydrated.
        - **Monitor your kidney health**: Get regular checkups and keep track of your kidney function.
        - **Avoid smoking and excessive drinking**: These lifestyle factors can accelerate kidney damage.
        """
    )

    # Motivational section
    st.markdown("---")
    st.markdown("### 🌟 **Keep Going! Every Step Counts!**")
    st.markdown(
        """
        Small efforts today can lead to a healthier tomorrow.  
        **Let's take care of our kidneys, together.**  
        """
    )

    # Footer with a simple, encouraging note
    st.markdown("---")
    st.markdown("© 2024 CKD Prediction App | Made with ❤️ by the CKD Team")

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app()
