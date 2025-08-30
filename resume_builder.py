from fpdf import FPDF

# Function to get user input for resume
def get_user_input():
    print("Enter your personal information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")

    summary = input("\nSummary/About You: ")

    # Education
    education = []
    while True:
        print("\nEnter Education Details (or leave degree empty to finish):")
        degree = input("Degree: ")
        if not degree:
            break
        school = input("School/University: ")
        year = input("Year: ")
        education.append({"degree": degree, "school": school, "year": year})

    # Work Experience
    work_experience = []
    while True:
        print("\nEnter Work Experience (or leave job title empty to finish):")
        job_title = input("Job Title: ")
        if not job_title:
            break
        company = input("Company: ")
        start_date = input("Start Date: ")
        end_date = input("End Date: ")
        responsibilities = []
        while True:
            r = input("Responsibility (leave empty to finish): ")
            if not r:
                break
            responsibilities.append(r)
        work_experience.append({
            "job_title": job_title,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities
        })

    # Skills
    skills = []
    print("\nEnter Skills (comma separated):")
    skills_input = input()
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    return {
        "personal_info": {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "address": address
        },
        "summary": summary,
        "education": education,
        "work_experience": work_experience,
        "skills": skills
    }

# Function to generate PDF
def generate_pdf(data, filename="resume.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, f"{data['personal_info']['first_name']} {data['personal_info']['last_name']}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Email: {data['personal_info']['email']} | Phone: {data['personal_info']['phone']}", ln=True)
    pdf.cell(0, 8, f"Address: {data['personal_info']['address']}", ln=True)
    pdf.ln(5)

    # Summary
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 7, data.get("summary", ""))
    pdf.ln(3)

    # Education
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Education", ln=True)
    pdf.set_font("Arial", "", 12)
    for edu in data.get("education", []):
        pdf.cell(0, 7, f"{edu['degree']}, {edu['school']} ({edu['year']})", ln=True)
    pdf.ln(3)

    # Work Experience
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Work Experience", ln=True)
    pdf.set_font("Arial", "", 12)
    for w in data.get("work_experience", []):
        pdf.cell(0, 7, f"{w['job_title']} at {w['company']} ({w['start_date']} - {w['end_date']})", ln=True)
        for r in w.get("responsibilities", []):
            pdf.cell(5)  # indentation
            pdf.cell(0, 7, f"- {r}", ln=True)
    pdf.ln(3)

    # Skills
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Skills", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 7, ", ".join(data.get("skills", [])))

    # Save PDF
    pdf.output(filename)
    print(f"\nResume saved as {filename}")

if __name__ == "__main__":
    user_data = get_user_input()
    generate_pdf(user_data)
