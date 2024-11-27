import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import test

cred = credentials.Certificate("ckd-prediction-32924-0142789cacd2.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to :blue[CKD Risk Predictor] :test_tube: ')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def sign_up_with_email_and_password(email, password, username=None):
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            return user.email
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email, password):
        try:
            user = auth.get_user_by_email(email)
            # In a real app, you would verify the password here
            user_info = {
                'email': user.email,
                'username': user.display_name
            }
            return user_info
        except Exception as e:
            st.warning(f'Signin failed: {e}')

    def f(): 
        try:
            userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']

            global Usernm
            Usernm = userinfo['username']

            st.session_state.signedout = True
            st.session_state.signout = True 

            # Switch to the dashboard page after successful login
            #st.switch_page("test.py")
                
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    

    if not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            
            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
               
            

    if st.session_state.signout:
        st.success('Name :' + st.session_state.username)
        st.success('Email id : ' + st.session_state.useremail)
        st.button('Sign out', on_click=t)
        
