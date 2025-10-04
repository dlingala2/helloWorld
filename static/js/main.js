// (Comment 1) Change text on button click
const buttonToChangeText = document.getElementById("buttonToChangeText");
const changeParameter = document.getElementById("changeParameter");
if (buttonToChangeText && changeParameter) {
    buttonToChangeText.addEventListener("click", () => {
        changeParameter.textContent = "Yay! This paragraph changed has changed.";
    });
}
// (Comment 2) Handle name form -> "Hello, {name}!"
const greetForm = document.getElementById("greetForm");
if (greetForm) {
    greetForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const input = document.getElementById("nameInput");
        const output = document.getElementById("greetOutput");
        const name = (input.value || "").trim();
        if (!name) {
            input.classList.add("is-invalid");
            output.textContent = "";
            return;
        }
        input.classList.remove("is-invalid");
        output.textContent = `Hello, ${name}!`;
    });
}

// (Comment 3) Create list items for favorite foods using a JS loop
const foodsList = document.getElementById("foodsList");
if (foodsList) {
    ["Pizza", "Sushi", "Red Velvet Cake"].forEach(food => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = food;
        foodsList.appendChild(li);
    });
}
// (Comment 4) Read checked courses and alert what was selected
const coursesForm = document.getElementById("coursesForm");
if (coursesForm) {
    coursesForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const chosen = Array.from(
            coursesForm.querySelectorAll('input[type="checkbox"]:checked')
        ).map(cb => cb.value);
        alert(
            chosen.length ?
            `You have taken: ${chosen.join(", ")}` :
            "You did choose any courses. Please choose at least one course."
        );
    });
}