import streamlit as st
from rembg import remove
from PIL import Image
import io
from streamlit_image_comparison import image_comparison

# පිටුවේ Layout එක සැකසීම
st.set_page_config(page_title="AI Background Remover", layout="centered")

st.markdown("<h1 style='text-align: center;'>🖼️ AI Background Remover</h1>", unsafe_allow_status=True)
st.write("ඕනෑම Format එකක photo එකක් upload කර HD තත්ත්වයෙන් පසුබිම ඉවත් කරගන්න.")

# File Uploader
uploaded_file = st.file_uploader("ඡායාරූපයක් තෝරන්න...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # රූපය විවෘත කිරීම
    input_image = Image.open(uploaded_file)
    
    with st.spinner('පසුබිම ඉවත් කරමින් පවතී...'):
        # Background එක ඉවත් කිරීම
        output_image = remove(input_image)
        
        # Before vs After Slider එක පෙන්වීම
        st.subheader("සැසඳීම (Before vs After)")
        image_comparison(
            img1=input_image,
            img2=output_image,
            label1="මුල් රූපය",
            label2="පසුබිම රහිත රූපය",
            width=700,
        )

        # Download Button එක
        buf = io.BytesIO()
        output_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="HD රූපය Download කරගන්න",
            data=byte_im,
            file_name="bg_removed_hd.png",
            mime="image/png"
        )