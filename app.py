
pip install streamlit transformers

import streamlit as st
from transformers import pipeline


classifier = pipeline("sentiment-analysis")


def main():
    st.title("Text Classification App")

   
    text_input = st.text_area("Enter Text:", "")

    if st.button("Get Sentiment Prediction"):
        if text_input:
           
            prediction = classifier(text_input)

           
            st.subheader("Prediction:")
            st.write(f"Sentiment: {prediction[0]['label']}")
            st.write(f"Confidence: {prediction[0]['score']:.4f}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
