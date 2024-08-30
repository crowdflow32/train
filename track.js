// Change colors dynamically after some seconds
function changeCoachColors() {
    const coaches = document.querySelectorAll('.coach .card');
    coaches.forEach((coach, index) => {
        if (index !== 0 && index !== coaches.length - 1) {
            // Apply different colors based on index
            if (index % 4 === 0) {
                coach.style.backgroundColor = 'red'; // Extreme
            } else if (index % 4 === 1) {
                coach.style.backgroundColor = 'orange'; // High
            } else if (index % 4 === 2) {
                coach.style.backgroundColor = '#b2ddfd'; // Normal
            } else {
                coach.style.backgroundColor = 'greenyellow'; // Low
            }
        }
    });
}

// Run the color change function every 5 seconds
setInterval(changeCoachColors, 5000);

// Initial color setup
changeCoachColors();

// Function to change coach colors dynamically
function changeCoachColors() {
    const coaches = document.querySelectorAll('.coach .card');
    coaches.forEach((coach, index) => {
        if (index !== 0 && index !== coaches.length - 1) {
            // Apply different colors based on index and time
            const time = new Date().getSeconds(); // Get current seconds
            const colorIndex = (index + time) % 4; // Vary colors dynamically

            // Assign colors based on colorIndex
            if (colorIndex === 0) {
                coach.style.backgroundColor = 'red'; // Extreme
            } else if (colorIndex === 1) {
                coach.style.backgroundColor = 'orange'; // High
            } else if (colorIndex === 2) {
                coach.style.backgroundColor = '#b2ddfd'; // Normal
            } else {
                coach.style.backgroundColor = 'greenyellow'; // Low
            }
        }
    });
}

// Run the color change function every second
setInterval(changeCoachColors, 3000);

// Initial color setup
changeCoachColors();
