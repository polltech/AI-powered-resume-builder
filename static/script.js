document.getElementById('resume-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        title: document.getElementById('title').value,
        experience: document.getElementById('experience').value,
        skills: document.getElementById('skills').value,
        education: document.getElementById('education').value,
    };

    const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });

    const data = await response.json();
    const resumePreview = document.getElementById('resume-preview');
    resumePreview.innerHTML = data.html;
    resumePreview.innerHTML += '<div class="watermark">Created by PolleResume AI</div>';
    document.getElementById('payment-options').style.display = 'block';
});

document.querySelectorAll('.download-button').forEach(button => {
    button.addEventListener('click', async function() {
        const type = this.dataset.type;
        const response = await fetch(`http://127.0.0.1:5000/download?type=${type}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: document.getElementById('name').value,
                title: document.getElementById('title').value,
                experience: document.getElementById('experience').value,
                skills: document.getElementById('skills').value,
                education: document.getElementById('education').value,
            }),
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = `resume-${type}.pdf`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } else {
            alert('Payment not verified. Please pay to download.');
        }
    });
});
