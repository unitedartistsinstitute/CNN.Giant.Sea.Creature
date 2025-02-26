<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giant Sea Bug Quiz (CNN)</title>
    <style>
        :root {
            --primary: #0077cc;
            --primary-dark: #005fa3;
            --secondary: #2d3748;
            --success: #38a169;
            --danger: #e53e3e;
            --warning: #f6ad55;
            --light: #f7fafc;
            --dark: #1a202c;
            --correct: #c6f6d5;
            --incorrect: #fed7d7;
            --neutral: #edf2f7;
            --font-main: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-main);
            background-color: var(--dark);
            color: var(--light);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--primary);
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
        }

        .subtitle {
            color: var(--light);
            font-size: 1.1rem;
            opacity: 0.8;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--primary-dark);
        }

        .btn-success {
            background-color: var(--success);
            color: white;
        }

        .btn-success:hover {
            background-color: #2f855a;
        }

        .btn-link {
    display: block;  /* Changed from inline-block */
    text-decoration: none;
    margin: 0 auto 20px;  /* Added auto for left/right margins */
    width: fit-content;  /* Makes the button width fit its content */
}

        .card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            position: relative;
        }

        .card-header {
            background-color: var(--secondary);
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .card-body {
            padding: 25px;
            background-color: var(--light);
            color: var(--dark);
        }

        .question-container {
            margin-bottom: 30px;
        }

        .question-text {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .options-container {
            display: grid;
            grid-gap: 15px;
        }

        .option-label {
            position: relative;
            display: block;
            padding: 15px;
            border: 2px solid var(--neutral);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .option-label:hover {
            border-color: var(--primary);
            background-color: #f0f7ff;
        }

        .option-label.correct {
            background-color: var(--correct);
            border-color: var(--success);
        }

        .option-label.incorrect {
            background-color: var(--incorrect);
            border-color: var(--danger);
        }

        .option-radio {
            position: absolute;
            opacity: 0;
            cursor: pointer;
        }

        .option-text {
            display: flex;
            align-items: center;
        }

        .option-letter {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 30px;
            height: 30px;
            border-radius: 50%;
            background-color: var(--neutral);
            color: var(--secondary);
            font-weight: bold;
            margin-right: 15px;
        }

        .option-label:hover .option-letter {
            background-color: var(--primary);
            color: white;
        }

        .option-label.correct .option-letter {
            background-color: var(--success);
            color: white;
        }

        .option-label.incorrect .option-letter {
            background-color: var(--danger);
            color: white;
        }

        .progress-container {
            margin-bottom: 20px;
        }

        .progress-text {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: var(--secondary);
        }

        .progress-bar {
            height: 8px;
            background-color: var(--neutral);
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background-color: var(--primary);
            border-radius: 4px;
            transition: width 0.5s ease;
        }

        .feedback {
            margin: 20px 0;
            padding: 15px;
            border-radius: 8px;
            display: none;
        }

        .feedback.correct {
            background-color: var(--correct);
            color: #276749;
        }

        .feedback.incorrect {
            background-color: var(--incorrect);
            color: #c53030;
        }

        .actions {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 25px;
        }

        .stat-card {
            background-color: var(--neutral);
            border-radius: 8px;
            padding: 15px;
            text-align: center;
        }

        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 5px;
        }

        .stat-label {
            color: var(--secondary);
            font-size: 0.9rem;
        }

        .result-container {
            text-align: center;
            padding: 30px 20px;
        }

        .result-header {
            font-size: 2rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .result-score {
            font-size: 3.5rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 15px;
        }

        .result-message {
            font-size: 1.2rem;
            margin-bottom: 30px;
            color: var(--secondary);
        }

        .timer {
            display: flex;
            align-items: center;
            font-size: 1rem;
            color: var(--light);
        }

        .timer-icon {
            margin-right: 5px;
        }

        .timer-text {
            font-weight: bold;
        }

        .fact-container {
            margin-top: 20px;
            padding: 15px;
            background-color: #ebf8ff;
            border-left: 4px solid var(--primary);
            border-radius: 0 8px 8px 0;
        }

        .fact-title {
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 5px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 10px;
            }
            
            .card-body {
                padding: 15px;
            }
            
            .question-text {
                font-size: 1.1rem;
            }
            
            .option-label {
                padding: 12px;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
        }

        .signature {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9rem;
            color: var(--light);
            opacity: 0.7;
        }

        .signature a {
            color: var(--primary);
            text-decoration: none;
        }

        .signature a:hover {
            text-decoration: underline;
        }

        .animated {
            animation-duration: 0.5s;
            animation-fill-mode: both;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .fadeIn {
            animation-name: fadeIn;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Giant Sea Bug Quiz (CNN)</h1>
            <p class="subtitle">Watch the video then click on the right answers!</p>
        </header>
        
        <a href="https://edition.cnn.com/2025/01/17/science/giant-sea-bug-darth-vader-vietnam/index.html" target="_blank" class="btn btn-primary btn-link">
            Click Here to Watch the CNN Story About this Giant Sea Bug
        </a>

        <div id="intro-screen">
            <div class="card animated fadeIn">
                <div class="card-header">
                    <h2>Ready to Test Your Video Comprehension?</h2>
                </div>
                <div class="card-body">
                    <p>This quiz will test your video comprehension about the recently discovered giant sea bug that has fascinated marine biologists worldwide.</p>
                    
                    <p>You'll face 10 questions about this fascinating creature. Try to answer them all correctly!</p>
                    
                    <div class="fact-container">
                        <p class="fact-title">Did you know?</p>
                        <p>Giant isopods are ancient creatures that have existed for over 160 million years. These remarkable crustaceans can survive in the deep sea without food for up to five years due to their slow metabolism.</p>
                    </div>
                    
                    <div class="actions">
                        <button id="start-btn" class="btn btn-primary">Start Quiz</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="quiz-screen" class="hidden">
            <div class="card animated fadeIn">
                <div class="card-header">
                    <div class="timer">
                        <svg class="timer-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        <span class="timer-text" id="time-display">00:00</span>
                    </div>
                    <div>Question <span id="current-question">1</span> of <span id="total-questions">10</span></div>
                </div>
                <div class="card-body">
                    <div class="progress-container">
                        <div class="progress-text">
                            <span>Progress</span>
                            <span id="progress-percentage">0%</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="progress-bar-fill" style="width: 0%;"></div>
                        </div>
                    </div>

                    <div class="question-container">
                        <div class="question-text" id="question-text">Loading question...</div>
                        <div class="options-container" id="options-container">
                            <!-- Options will be inserted here by JavaScript -->
                        </div>
                    </div>

                    <div class="feedback" id="feedback"></div>

                    <div class="actions">
                        <button id="next-btn" class="btn btn-primary" style="display: none;">Next Question</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="results-screen" class="hidden">
            <div class="card animated fadeIn">
                <div class="card-header">
                    <h2>Quiz Results</h2>
                </div>
                <div class="card-body">
                    <div class="result-container">
                        <h3 class="result-header">Your Score</h3>
                        <div class="result-score"><span id="final-score">0</span>/<span id="max-score">10</span></div>
                        <p class="result-message" id="result-message">You've completed the quiz!</p>
                        
                        <div class="stats">
                            <div class="stat-card">
                                <div class="stat-value" id="correct-answers">0</div>
                                <div class="stat-label">Correct Answers</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-value" id="accuracy-percentage">0%</div>
                                <div class="stat-label">Accuracy</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-value" id="time-taken">00:00</div>
                                <div class="stat-label">Time Taken</div>
                            </div>
                        </div>
                        
                        <div class="fact-container" style="margin-top: 30px;">
                            <p class="fact-title">Interesting Fact</p>
                            <p>Giant isopods are distant relatives of common pill bugs or roly-polies found in gardens, but have adapted to the extreme conditions of the deep ocean environment.</p>
                        </div>
                        
                        <div class="actions">
                            <button id="restart-btn" class="btn btn-primary">Restart Quiz</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="signature">
        &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
    </div>

    <script>
        // Quiz data
        const quizData = [
            {
                question: "Where was the giant sea bug discovered?",
                options: ["Vietnam", "Australia", "Brazil", "Japan"],
                answer: "Vietnam",
                explanation: "The giant sea bug was discovered off the coast of Vietnam by marine biologists during a deep-sea expedition."
            },
            {
                question: "What is the scientific significance of the discovery?",
                options: ["It's a new species", "It's the largest sea bug ever found", "It has unique DNA", "All of the above"],
                answer: "All of the above",
                explanation: "This discovery is significant because it represents a new species with unique DNA and is the largest sea bug ever documented."
            },
            {
                question: "How long can the giant sea bug grow?",
                options: ["10 cm", "20 cm", "30 cm", "40 cm"],
                answer: "30 cm",
                explanation: "The giant sea bug can grow up to 30 cm (about 12 inches) in length, making it one of the largest isopods discovered."
            },
            {
                question: "What is the habitat of the giant sea bug?",
                options: ["Coral reefs", "Deep ocean trenches", "Freshwater lakes", "Mangrove forests"],
                answer: "Deep ocean trenches",
                explanation: "The giant sea bug lives in deep ocean trenches, typically at depths where there is very little light."
            },
            {
                question: "What does the giant sea bug resemble?",
                options: ["A lobster", "A crab", "Darth Vader", "A shrimp"],
                answer: "Darth Vader",
                explanation: "The giant sea bug has been nicknamed the 'Darth Vader bug' because its head shape resembles Darth Vader's helmet from Star Wars."
            },
            {
                question: "What is the primary diet of the giant sea bug?",
                options: ["Plankton", "Small fish", "Dead marine animals", "Seaweed"],
                answer: "Dead marine animals",
                explanation: "The giant sea bug is a scavenger that primarily feeds on dead marine animals that sink to the ocean floor."
            },
            {
                question: "How deep was the giant sea bug found?",
                options: ["500 meters", "1000 meters", "1500 meters", "2000 meters"],
                answer: "1000 meters",
                explanation: "The giant sea bug was discovered at a depth of approximately 1000 meters (about 3,280 feet) below the surface."
            },
            {
                question: "What is the giant sea bug's scientific name?",
                options: ["Bathynomus giganteus", "Gigantocypris muelleri", "Limulus polyphemus", "No official name yet"],
                answer: "No official name yet",
                explanation: "As a newly discovered species, scientists are still working on officially naming and classifying this giant sea bug."
            },
            {
                question: "What is the giant sea bug's role in the ecosystem?",
                options: ["Predator", "Scavenger", "Herbivore", "Parasite"],
                answer: "Scavenger",
                explanation: "The giant sea bug plays an important role as a scavenger in the deep-sea ecosystem, helping to break down dead organisms."
            },
            {
                question: "Why is the discovery important for marine biology?",
                options: ["It shows biodiversity in deep oceans", "It helps understand evolution", "It highlights undiscovered species", "All of the above"],
                answer: "All of the above",
                explanation: "This discovery is important because it demonstrates the rich biodiversity of deep oceans, provides insights into evolution, and reminds us how many species remain undiscovered."
            }
        ];

        // DOM elements
        const introScreen = document.getElementById('intro-screen');
        const quizScreen = document.getElementById('quiz-screen');
        const resultsScreen = document.getElementById('results-screen');
        const startBtn = document.getElementById('start-btn');
        const nextBtn = document.getElementById('next-btn');
        const restartBtn = document.getElementById('restart-btn');
        const questionText = document.getElementById('question-text');
        const optionsContainer = document.getElementById('options-container');
        const currentQuestionDisplay = document.getElementById('current-question');
        const totalQuestionsDisplay = document.getElementById('total-questions');
        const progressBarFill = document.getElementById('progress-bar-fill');
        const progressPercentage = document.getElementById('progress-percentage');
        const feedback = document.getElementById('feedback');
        const finalScore = document.getElementById('final-score');
        const maxScore = document.getElementById('max-score');
        const correctAnswers = document.getElementById('correct-answers');
        const accuracyPercentage = document.getElementById('accuracy-percentage');
        const resultMessage = document.getElementById('result-message');
        const timeDisplay = document.getElementById('time-display');
        const timeTaken = document.getElementById('time-taken');

        // Quiz state
        let currentQuestion = 0;
        let score = 0;
        let answeredQuestions = 0;
        let answered = false;
        let startTime;
        let timerInterval;
        let secondsElapsed = 0;

        // Initialize the quiz
        function initQuiz() {
            totalQuestionsDisplay.textContent = quizData.length;
            maxScore.textContent = quizData.length;
        }

        // Start the quiz
        function startQuiz() {
            introScreen.classList.add('hidden');
            quizScreen.classList.remove('hidden');
            loadQuestion();
            startTimer();
        }

        // Load a question
        function loadQuestion() {
            answered = false;
            
            if (currentQuestion >= quizData.length) {
                endQuiz();
                return;
            }

            const question = quizData[currentQuestion];
            questionText.textContent = `${currentQuestion + 1}. ${question.question}`;
            
            // Update progress indicators
            currentQuestionDisplay.textContent = currentQuestion + 1;
            const progress = ((currentQuestion) / quizData.length) * 100;
            progressBarFill.style.width = `${progress}%`;
            progressPercentage.textContent = `${Math.round(progress)}%`;

            // Clear previous options and feedback
            optionsContainer.innerHTML = '';
            feedback.style.display = 'none';
            nextBtn.style.display = 'none';

            // Add options with letters
            const letters = ['A', 'B', 'C', 'D'];
            question.options.forEach((option, index) => {
                const optionElement = document.createElement('label');
                optionElement.className = 'option-label';
                optionElement.innerHTML = `
                    <input type="radio" name="option" class="option-radio" value="${option}">
                    <div class="option-text">
                        <span class="option-letter">${letters[index]}</span>
                        ${option}
                    </div>
                `;
                optionsContainer.appendChild(optionElement);

                // Add event listener to option
                const radioButton = optionElement.querySelector('input');
                radioButton.addEventListener('change', () => checkAnswer(option, optionElement));
            });
        }

        // Check the answer
        function checkAnswer(selectedOption, selectedLabel) {
            if (answered) return;
            
            answered = true;
            answeredQuestions++;
            
            const question = quizData[currentQuestion];
            const correctAnswer = question.answer;
            const isCorrect = selectedOption === correctAnswer;
            
            // Mark the selected option
            if (isCorrect) {
                selectedLabel.classList.add('correct');
                score++;
                
                feedback.textContent = `Correct! ${question.explanation}`;
                feedback.className = 'feedback correct';
            } else {
                selectedLabel.classList.add('incorrect');
                
                // Find and mark the correct option
                const options = document.querySelectorAll('.option-label');
                options.forEach(option => {
                    const optionValue = option.querySelector('input').value;
                    if (optionValue === correctAnswer) {
                        option.classList.add('correct');
                    }
                });
                
                feedback.textContent = `Incorrect. The correct answer is "${correctAnswer}". ${question.explanation}`;
                feedback.className = 'feedback incorrect';
            }
            
            feedback.style.display = 'block';
            
            // Disable all options
            const options = document.querySelectorAll('.option-radio');
            options.forEach(option => {
                option.disabled = true;
            });
            
            // Show next button only if it's not the last question
            if (currentQuestion < quizData.length - 1) {
                nextBtn.style.display = 'block';
            } else {
                // Automatically proceed to results after a delay on the last question
                setTimeout(() => {
                    endQuiz();
                }, 3000);
            }
        }

        // Move to the next question
        function nextQuestion() {
            currentQuestion++;
            loadQuestion();
        }

        // Format time (seconds to MM:SS)
        function formatTime(seconds) {
            const minutes = Math.floor(seconds / 60);
            const remainingSeconds = seconds % 60;
            return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
        }

        // Start the timer
        function startTimer() {
            startTime = new Date();
            secondsElapsed = 0;
            
            timerInterval = setInterval(() => {
                secondsElapsed++;
                timeDisplay.textContent = formatTime(secondsElapsed);
            }, 1000);
        }

        // Stop the timer
        function stopTimer() {
            clearInterval(timerInterval);
            return secondsElapsed;
        }

        // End the quiz and show results
        function endQuiz() {
            // Stop the timer
            const totalTime = stopTimer();
            
            // Hide quiz screen and show results screen
            quizScreen.classList.add('hidden');
            resultsScreen.classList.remove('hidden');
            
            // Update results
            finalScore.textContent = score;
            correctAnswers.textContent = score;
            
            // Calculate accuracy
            const accuracy = (score / quizData.length) * 100;
            accuracyPercentage.textContent = `${Math.round(accuracy)}%`;
            
            // Set time taken
            timeTaken.textContent = formatTime(totalTime);
            
            // Set result message based on score
            if (score === quizData.length) {
                resultMessage.textContent = "Perfect! You're a giant sea bug expert!";
            } else if (score >= quizData.length * 0.8) {
                resultMessage.textContent = "Great job! Your listening was pretty good!";
            } else if (score >= quizData.length * 0.6) {
                resultMessage.textContent = "Good effort! You got a decent understaning of this CNN story.";
            } else if (score >= quizData.length * 0.4) {
                resultMessage.textContent = "Not bad! You missed some details though.";
            } else {
                resultMessage.textContent = "Keep learning! Consider watching the video again .";
            }
        }

        // Restart the quiz
        function restartQuiz() {
            // Reset quiz state
            currentQuestion = 0;
            score = 0;
            answeredQuestions = 0;
            
            // Hide results screen and show intro screen
            resultsScreen.classList.add('hidden');
            introScreen.classList.remove('hidden');
        }

        // Event listeners
        startBtn.addEventListener('click', startQuiz);
        nextBtn.addEventListener('click', nextQuestion);
        restartBtn.addEventListener('click', restartQuiz);

        // Initialize the quiz
        initQuiz();
    </script>
</body>
</html>
