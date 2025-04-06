<script>
    async function downloadVideo() {
        const url = document.getElementById('videoUrl').value;

        const response = await fetch("/download", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })  // URL को JSON format में भेजना ज़रूरी है
        });

        const result = await response.json();
        const output = document.getElementById("result");

        if (result.download_url) {
            output.innerHTML = `<a href="${result.download_url}" target="_blank">Download Link</a>`;
        } else {
            output.innerHTML = `Error: ${result.error}`;
        }
    }
</script>
