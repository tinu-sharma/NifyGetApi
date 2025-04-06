async function downloadVideo() {
    const url = document.getElementById('videoUrl').value;
    const response = await fetch('/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
    });
    const data = await response.json();
    if (data.download_url) {
        document.getElementById('result').innerHTML = 
            `<a href="${data.download_url}" target="_blank">Download Video</a>`;
    } else {
        document.getElementById('result').innerHTML = data.error;
    }
}
