document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("inputText");
    const resultDiv = document.getElementById("result");

    // Auto-fill selected text
    chrome.storage.local.get("selectedText", (data) => {
        if (data.selectedText) {
            input.value = data.selectedText;
        }
    });

    // Voice Input (FINAL FIXED)
    document.getElementById("voiceBtn").addEventListener("click", () => {

        if (!('webkitSpeechRecognition' in window)) {
            resultDiv.innerText = "❌ Voice not supported in this browser";
            return;
        }

        const recognition = new webkitSpeechRecognition();

        recognition.lang = "en-US";
        recognition.continuous = false;
        recognition.interimResults = false;

        resultDiv.innerText = "🎤 Listening... Speak now";

        recognition.start();

        recognition.onresult = function(event) {
            const text = event.results[0][0].transcript;
            input.value = text;
            resultDiv.innerText = "✅ Voice captured";
        };

        recognition.onerror = function(event) {
            console.error("Voice error:", event.error);

            if (event.error === "not-allowed") {
                resultDiv.innerText = "❌ Microphone permission denied";
            } else if (event.error === "no-speech") {
                resultDiv.innerText = "❌ No speech detected";
            } else if (event.error === "audio-capture") {
                resultDiv.innerText = "❌ Microphone not found";
            } else if (event.error === "network") {
                resultDiv.innerText = "❌ Network error (check internet)";
            } else {
                resultDiv.innerText = "❌ Voice error: " + event.error;
            }
        };

        recognition.onend = function() {
            console.log("Voice recognition ended");
        };
    });

    // Analyze Button
    document.getElementById("analyzeBtn").addEventListener("click", async () => {

        const text = input.value;

        if (!text || text.trim().length === 0) {
            resultDiv.innerText = "⚠️ Enter or speak text";
            return;
        }

        resultDiv.innerText = "⏳ Analyzing...";

        try {
            const response = await fetch("http://127.0.0.1:5000/analyze", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();

            if (data.error) {
                resultDiv.innerText = "❌ " + data.error;
                return;
            }

            resultDiv.innerHTML = `
                <p><b>Result:</b> ${data.label}</p>
                <p><b>Confidence:</b> ${data.confidence}%</p>
                <hr>
                <p>Length: ${data.features.length}</p>
                <p>Unique Words: ${data.features.unique_words}</p>
                <p>Repetition: ${data.features.repetition_ratio}</p>
            `;

        } catch (error) {
            resultDiv.innerText = "❌ Backend not running!";
        }
    });

});