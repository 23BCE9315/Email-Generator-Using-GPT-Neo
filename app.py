import streamlit as st
from model_loader import load_model
from email_generator import generate_text

model, tokenizer = load_model()

st.set_page_config(page_title="AI Email Generator", layout="centered")
st.title("\U0001F4E7 AI Personalized Email Generator")
st.markdown("Generate professional emails using GPT-Neo. Fill out the form below.")

with st.form("email_form"):
    recipient = st.text_input("\U0001F464 Recipient's Name")
    event = st.text_input("\U0001F4CC Event Name")
    date = st.date_input("\U0001F4C5 Event Date")
    time = st.time_input("⏰ Event Time")
    location = st.text_input("\U0001F4CD Location")
    instructions = st.text_area("\U0001F4DD Special Instructions (optional)")
    end_note = st.selectbox(
        "\U0001F4E8 Closing Note",
        ["Best Regards", "Thank You", "Yours Sincerely", "Warm Wishes"]
    )

    submitted = st.form_submit_button("Generate Email")

if submitted:
    with st.spinner("\u270D\ufe0f Generating email..."):
        extra_details = (
            f"The event will take place on {date.strftime('%d %B %Y')} at {time.strftime('%I:%M %p')} in {location}. {instructions}"
        )

        email = generate_text(
            model=model,
            tokenizer=tokenizer,
            recipient_name=recipient,
            event_name=event,
            special_instructions=extra_details,
            end_note=end_note
        )

    st.subheader("\u2705 Your Generated Email:")
    st.text_area("\U0001F4E7 Email Body", email, height=300)