const interval = setInterval(function() {
    try {
        // Get the problem statement
        var problems = document.getElementsByClassName("card-title");
        if (problems.length === 0) return;

        // Parse the problem and calculate the answer
        var problemText = problems[0].innerText;
        var parsedProblem = problemText.replace(" x ", "*");
        var splits = parsedProblem.split("*");
        if (splits.length < 2) return;
        
        var answer = parseInt(splits[0]) * parseInt(splits[1]);
        if (isNaN(answer)) return;

        // Get the possible answers
        var buttons = document.getElementsByClassName('card-button');
        if (buttons.length < 4) return;

        // Click the correct answer
        for (var i = 0; i < buttons.length; i++) {
            if (parseInt(buttons[i].innerText) === answer) {
                buttons[i].click();
                break;
            }
        }
    } catch (error) {
        console.error("Error occurred: ", error);
    }
}, 200); // 200 milliseconds = 0.2 seconds
