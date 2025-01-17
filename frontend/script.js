document.getElementById('search-button').addEventListener('click', async () => {
    const ingredient = document.getElementById('ingredient').value.trim();
    
    if (!ingredient) {
        alert("Please enter an ingredient.");
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredient })
    });

    const recipeOutput = document.getElementById('recipe-output');
    recipeOutput.innerHTML = ''; // Clear previous output

    if (response.ok) {
        const recipes = await response.json();
        recipes.forEach(recipe => {
            recipeOutput.innerHTML += `
                <h2>${recipe.name}</h2>
                <h3>Ingredients:</h3>
                <ul>
                    ${recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
                </ul>
                <h3>Instructions:</h3>
                <p>${recipe.instructions}</p>
                <h3>Nutritional Information:</h3>
                <p>Calories: ${recipe.nutritional_info.calories}</p>
                <p>Protein: ${recipe.nutritional_info.protein}g</p>
                <p>Carbs: ${recipe.nutritional_info.carbs}g</p>
                <p>Fat: ${recipe.nutritional_info.fat}g</p>
                <hr>
            `;
        });
    } else {
        const error = await response.json();
        recipeOutput.innerHTML = `<p>${error.message}</p>`;
    }
});