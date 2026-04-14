document.addEventListener("mouseup", () => {
    const selectedText = window.getSelection().toString();

    if (selectedText.length > 20) {
        chrome.storage.local.set({ selectedText: selectedText });
    }
});