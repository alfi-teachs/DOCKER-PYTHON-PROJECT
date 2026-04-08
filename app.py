import streamlit as st

st.set_page_config(page_title="Dockerfile Helper", page_icon="🐳", layout="centered")

st.title("🐳 Dockerfile Builder Helper")
st.markdown("Fill details below and **create your Dockerfile manually**")

# Sections
st.header("📦 Base Configuration")
base_image = st.text_input("Base Image", "python:3.11-slim")
workdir = st.text_input("Working Directory", "/app")

st.header("📁 File Handling")
copy_files = st.checkbox("Will you copy all files? (COPY . .)", value=True)

st.header("📦 Dependencies")
use_requirements = st.checkbox("Using requirements.txt?", value=True)

st.header("🌐 Networking")
port = st.text_input("Port to expose", "8000")

st.header("🚀 Execution")
cmd = st.text_input("Start Command", "python app.py")

# Display summary (no Dockerfile generation)
st.header("📋 Your Inputs Summary")

st.write("**Base Image:**", base_image)
st.write("**Working Directory:**", workdir)

if copy_files:
    st.write("✔ You plan to copy files into container")

if use_requirements:
    st.write("✔ You will install dependencies from requirements.txt")

st.write("**Port:**", port)
st.write("**Command:**", cmd)

st.info("💡 Use the above details to manually write your Dockerfile")

# Tips section
st.header("💡 Dockerfile Tips")

st.markdown("""
- Use **FROM** to define base image  
- Use **WORKDIR** to set working directory  
- Use **COPY** to copy files  
- Use **RUN** to install dependencies  
- Use **EXPOSE** for port  
- Use **CMD** or **ENTRYPOINT** to start app  
""")

st.success("✅ You're ready to write your Dockerfile manually!")
