def generate_resume_data(data):
    """
    This function simulates an AI model generating a resume.
    In a real application, this would be replaced with a call to an actual AI model.
    """
    return {
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "summary": f"A highly motivated and results-oriented professional with a proven track record of success in the {data['jobTitle']} field.",
        "skills": data["skills"],
        "education": data["education"],
        "experience": f"<ul><li>Generated a professional summary and ATS-optimized bullet points for the {data['jobTitle']} role.</li></ul>"
    }
