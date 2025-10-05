import streamlit as st  # Import the UI toolbox

from summarizer import summarize_text  # Import your AI function from Part 2 (must be in same folder)

# Page title (shows in browser tab and header)
st.title("AI Text Summarizer")

# Subtitle explanation
st.write("Paste a news article or blog post below, and get a 3-sentence summary using Hugging Face AI!")

# Input text box (user pastes article here)
user_input = st.text_area(
    "Enter your text to summarize:",
    height=200,  # Box height in pixels (adjust if you want taller/shorter)
    placeholder="Example: Climate change is one of the most pressing issues of our time..."
)

# Summarize button (only shows summary when clicked)
if st.button("Generate Summary"):
    if user_input:  # Check if user typed something
        # Show loading spinner while AI works
        with st.spinner("Summarizing... (first time may take a minute to load AI model)"):
            summary = summarize_text(user_input)  # Call your AI function
        st.success("Summary generated!")  # Green success message
        st.subheader("3-Sentence Summary:")  # Bold header for output
        st.write(summary)  # Display the AI result
    else:
        st.warning("Please enter some text first!")  # Warning if box is empty

# Footer (extra info at bottom)
st.write("---")  # Horizontal line
st.write("Built with Streamlit and Hugging Face Transformers. For long texts, it summarizes the key points.")