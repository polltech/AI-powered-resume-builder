let resumeData = {};

document.getElementById('resume-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        skills: document.getElementById('skills').value,
        education: document.getElementById('education').value,
        experience: document.getElementById('experience').value,
        jobTitle: document.getElementById('job-title').value,
    };

    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });

    resumeData = await response.json();

    const resumePreview = document.getElementById('resume-preview');
    resumePreview.innerHTML = `
        <div class="watermark">Unlock to Download</div>
        <h2>${resumeData.name}</h2>
        <p>${resumeData.email} | ${resumeData.phone}</p>
        <h3>Professional Summary</h3>
        <p>${resumeData.summary}</p>
        <h3>Skills</h3>
        <p>${resumeData.skills}</p>
        <h3>Education</h3>
        <p>${resumeData.education}</p>
        <h3>Work Experience</h3>
        <div>${resumeData.experience}</div>
    `;

    document.getElementById('payment-buttons').style.display = 'block';
});

paypal.Buttons({
    createOrder: function(data, actions) {
        const template = document.getElementById('template').value;
        const price = template === 'classic' ? '0.00' : '1.99';
        if (price === '0.00') {
            return;
        }
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: price
                }
            }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            alert('Transaction completed by ' + details.payer.name.given_name);
            document.getElementById('resume-preview').classList.remove('watermarked');
            const downloadButton = document.createElement('button');
            downloadButton.textContent = 'Download PDF';
            downloadButton.addEventListener('click', async () => {
                const response = await fetch('/download', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(resumeData)
                });
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'resume.pdf';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            });
            document.getElementById('payment-buttons').innerHTML = '';
            document.getElementById('payment-buttons').appendChild(downloadButton);
        });
    }
}).render('#payment-buttons');
