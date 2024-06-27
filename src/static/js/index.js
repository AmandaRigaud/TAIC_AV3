userInput.addEventListener('input', function() {
    const userInput = document.getElementById('userInput');
    const submitButton = document.getElementById('submitButton');
    
    if (userInput.value === "") {
        submitButton.disabled = true;
    } else {
        submitButton.disabled = false;
    }
});

document.getElementById('submitButton').addEventListener('click', function() {
    const userInput = document.getElementById('userInput');
    const submitButton = document.getElementById('submitButton');

    console.log('Button clicked');

    submitButton.setAttribute('disabled', true);
    userInput.setAttribute('disabled', true);
    submitButton.innerHTML = 'Criando...';

    // console.log("Cliiiiiiiick!")

    // for (let i = 1; i <= 20; i++) {
    //     console.log(`Item ${i}`);
    //     // Aqui você pode adicionar qualquer lógica que precise ser executada para cada item
    // }
    
    fetch(`/get/${encodeURIComponent(userInput.value)}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const mediaContainer = document.getElementById('responseContainer');
            
            const audio = document.createElement('audio');
            audio.controls = true;
            audio.src = data.audio;
            audio.className = 'audio-item';

            const image = document.createElement('img');
            image.src = data.image_url;
            image.className = 'img-item';
            
            mediaContainer.appendChild(audio);
            mediaContainer.appendChild(image);
            
            submitButton.removeAttribute('disabled');
            userInput.removeAttribute('disabled');
            userInput.value = "";
            submitButton.textContent = 'Historiar!';
        })
        .catch(error => {
            console.error('Error:', error);
        });

});