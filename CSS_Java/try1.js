function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed');
}

let currentSection = 1;
const totalSections = 4;

function updateStepper(sectionNumber) {
    // Update progress line width
    const progressLine = document.querySelector('.progress-line');
    const progressPercentage = ((sectionNumber - 1) / (totalSections - 1)) * 100;
    progressLine.style.width = `calc(${progressPercentage}% - 40px)`;

    // Update step states
    document.querySelectorAll('.step').forEach((step, index) => {
        const stepNumber = index + 1;
        if (stepNumber < sectionNumber) {
            step.classList.add('completed');
            step.classList.remove('active');
        } else if (stepNumber === sectionNumber) {
            step.classList.add('active');
            step.classList.remove('completed');
        } else {
            step.classList.remove('completed', 'active');
        }
    });
}

function showSection(sectionNumber) {
    // Hide all sections
    document.querySelectorAll('.form-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Show current section
    document.querySelector(`.form-section[data-section="${sectionNumber}"]`).classList.add('active');
    
    // Update stepper
    updateStepper(sectionNumber);
    
    // Update buttons
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    const saveButton = document.querySelector('.save-button');
    
    prevButton.style.display = sectionNumber === 1 ? 'none' : 'block';
    nextButton.style.display = sectionNumber === totalSections ? 'none' : 'block';
    saveButton.style.display = sectionNumber === totalSections ? 'block' : 'none';
}

function nextSection() {
    if (currentSection < totalSections) {
        currentSection++;
        showSection(currentSection);
    }
}

function previousSection() {
    if (currentSection > 1) {
        currentSection--;
        showSection(currentSection);
    }
}

function saveForm() {
    // Add your save functionality here
    alert('Form saved successfully!');
}

// Initialize the form
document.addEventListener('DOMContentLoaded', () => {
    showSection(1);
});

// import 'spinalviewer.js';