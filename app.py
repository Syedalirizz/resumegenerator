import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# App Title
st.title("AI-Powered Resumé and Cover Letter Builder")

# Section for Personal Details
st.header("Personal Details")
name = st.text_input("Name")
contact_info = st.text_input("Contact Information (Phone, Email)")
linkedin_profile = st.text_input("LinkedIn Profile URL")

# Section for Career Objective
st.header("Career Objective")
career_objective = st.text_area("Brief Career Objective")

# Section for Work Experience
st.header("Work Experience")
job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")
job_duration = st.text_input("Duration (e.g., Jan 2021 - Present)")
job_accomplishments = st.text_area("Key Accomplishments")

# Section for Education
st.header("Education")
degree = st.text_input("Degree")
university_name = st.text_input("University Name")
graduation_year = st.text_input("Graduation Year")

# Section for Skills
st.header("Skills")
skills = st.text_area("Enter skills separated by commas (e.g., Python, Data Analysis)")

# Section for Target Job
st.header("Target Job")
target_role = st.text_input("Target Job Role")
target_industry = st.text_input("Target Industry")

# Button to generate resumé and cover letter
if st.button("Generate Resumé and Cover Letter"):
    # Placeholder for generated resumé content
    resume_content = f"""
    {name}\n
    {contact_info}\n
    LinkedIn: {linkedin_profile}\n\n
    Career Objective:\n
    {career_objective}\n\n
    Work Experience:\n
    {job_title} at {company_name} ({job_duration})\n
    Key Accomplishments:\n
    {job_accomplishments}\n\n
    Education:\n
    {degree}, {university_name} - {graduation_year}\n\n
    Skills:\n
    {skills}\n
    """
    
    # Display generated resumé
    st.subheader("Generated Resumé")
    st.text(resume_content)

    # Placeholder for generated cover letter content
    cover_letter_content = f"""
    Dear Hiring Manager,\n
    I am writing to express my interest in the {target_role} position in the {target_industry} industry. With my background in {career_objective}, 
    and my experience at {company_name} where I contributed significantly as a {job_title}, I believe I am well-suited for this role.\n\n
    My skills include {skills}, which I am eager to bring to your team. I look forward to the opportunity to further discuss how my background 
    aligns with your goals.\n\n
    Sincerely,\n
    {name}
    """
    
    # Display generated cover letter
    st.subheader("Generated Cover Letter")
    st.text(cover_letter_content)
    
    # PDF generation function
    def create_pdf():
        pdf_buffer = io.BytesIO()
        pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
        pdf_canvas.setFont("Helvetica", 10)

        # Writing resumé content to PDF
        pdf_canvas.drawString(50, 750, "Generated Resumé")
        text = pdf_canvas.beginText(50, 730)
        text.setFont("Helvetica", 10)
        text.setLeading(14)  # Set line spacing
        for line in resume_content.splitlines():
            text.textLine(line)
        pdf_canvas.drawText(text)

        # Adding space for cover letter
        text = pdf_canvas.beginText(50, 400)
        text.setFont("Helvetica", 10)
        text.setLeading(14)
        text.textLine("Generated Cover Letter")
        for line in cover_letter_content.splitlines():
            text.textLine(line)
        pdf_canvas.drawText(text)
        
        pdf_canvas.save()
        pdf_buffer.seek(0)
        return pdf_buffer

    # Button to download PDF
    pdf_data = create_pdf()
    st.download_button("Download Resumé and Cover Letter as PDF", data=pdf_data, file_name="resume_cover_letter.pdf")
