import streamlit as st 
from pathlib import Path
import shutil


st.title("📂 File Organizer")
st.markdown("Upload files, organize them by type, and view their content.")

uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

base_dir = Path("organized_files")
base_dir.mkdir(exist_ok = True)

if uploaded_files:
    moved = 0
    st.markdown("---")
    st.subheader("📁 Organized & Previewed all types of Files")

    for uploaded_file in uploaded_files:
        try:
            ext = Path(uploaded_file.name).suffix.lower().replace(".", "")
            ext_folder = base_dir / (ext if ext else "no_extension")
            ext_folder.mkdir(exist_ok=True)

           
            save_path = ext_folder / uploaded_file.name
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            moved += 1

            
            st.markdown(f"**📄 {uploaded_file.name}**")
            if ext in ["txt", "md", "py", "csv", "json"]:
               
                content = uploaded_file.getvalue().decode("utf-8", errors="ignore")
                st.code(content[:1000] if len(content) > 1000 else content, language=ext)
            elif ext in ["jpg", "jpeg", "png", "gif"]:
                
                st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)
            elif ext in ["pdf"]:
                
                st.info("PDF uploaded. Preview not supported yet.")
            else:
                st.info("Preview not supported for this file type.")

            st.markdown("---")

        except Exception as e:
            st.error(f"Error handling {uploaded_file.name}: {str(e)}")

    st.success(f"{moved} file(s) organized and previewed.")

