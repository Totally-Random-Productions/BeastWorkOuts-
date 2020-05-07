const exercisesList = document.getElementById('exercisesList');
const searchBar = document.getElementById('searchBar');

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredExercises = exercises.filter((exercise) => {
        return (
            exercise.e.exerciseName.toLowerCase().includes(searchString) ||
            exercise.e.equipment.toLowerCase().includes(searchString) ||
            exercise.e.exerciseType.toLowerCase().includes(searchString) ||
            exercise.e.majorMuscle.toLowerCase().includes(searchString) ||
            exercise.e.minorMuscle.toLowerCase().includes(searchString) ||
        );
    });
    displayExercises(filteredExercises);
});

const displayExercises = (exercises) => {
    const htmlString = exercises
        .map((exercise) => {
            return `
            <li class="exercise">
                <h2>${exercise.name}</h2>
            </li>
        `;
        })
        .join('');
    exerciseList.innerHTML = htmlString;
};