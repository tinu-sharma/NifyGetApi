<script>
document.addEventListener('DOMContentLoaded', () => {
    const downloadBtn = document.querySelector('button');
    const urlInput = document.querySelector('input');

    downloadBtn.addEventListener('click', () => {
        const url = urlInput.value.trim();

        if (!url) {
            alert('कृपया एक URL डालें।');
            return;
        }

        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })  // यहीं से backend को data जाता है
        })
        .then(response => response.json())
        .then(data => {
            if (data.download_url) {
                window.location.href = data.download_url;  // Auto redirect to video
            } else {
                alert(data.error || 'कोई गड़बड़ हो गई है');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('सर्वर से जवाब नहीं मिला।');
        });
    });
});
</script>
