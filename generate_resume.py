def generate_resume_html(data):
    """
    Simulates AI-powered resume generation and returns it as an HTML string.
    """
    # In a real app, you'd use a language model to generate this content.
    # For now, we'll just format the input data.

    experience_html = "".join(f"<li>{item}</li>" for item in data['experience'].split('\n') if item)
    skills_html = ", ".join(data['skills'].split(','))
    education_html = "".join(f"<li>{item}</li>" for item in data['education'].split('\n') if item)

    html_content = f"""
        <h2>{data['name']}</h2>
        <p><em>{data['title']}</em></p>
        <hr>
        <h3>Work Experience</h3>
        <ul>{experience_html}</ul>
        <h3>Skills</h3>
        <p>{skills_html}</p>
        <h3>Education</h3>
        <ul>{education_html}</ul>
    """
    return html_content
