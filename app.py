import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))


def predict_strength(cement, slag, ash, water, superplastic, coarseagg, fineagg, age):
    input = np.array([[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]]).astype(np.float64)
    prediction = model.predict(input)
    return float(prediction)

def main():
    st.title("Nal & Neel")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Concrete Strength Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    cement = st.text_input("Cement (kg/m^3)", "")
    slag = st.text_input(" Blast furnace slag (kg/m^3 )", "")
    ash = st.text_input("Flyash (kg/m^3)", "")
    water = st.text_input("Water (kg/m^3)", "")
    superplastic = st.text_input("Superplastisizer (kg/m^3)", "")
    coarseagg = st.text_input("Coarse Aggregate (kg/m^3)", "")
    fineagg = st.text_input(" Fine Aggregate (kg/m^3)", "")
    age = st.text_input("Age (days)", "")
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Concrete is strong enough!</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Concrete is not strong enough!</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_strength(cement, slag, ash, water, superplastic, coarseagg, fineagg, age)
        st.success('Predicted Concrete Strength is {} Mpa'.format(output))

        if output < 17:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
