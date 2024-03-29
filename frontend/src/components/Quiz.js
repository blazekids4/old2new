import React, { useState } from 'react';
import './Quiz.css'; // import your CSS file

function Quiz({ onAnswer }) {
  const [answer, setAnswer] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onAnswer(answer.trim() !== ''); // any non-empty answer is acceptable
  };

  return (
    <form onSubmit={handleSubmit} className="quiz-form">
      <label className="quiz-question">
        What is one thing you are grateful for that happened in the last 24 hours?
        <input type="text" value={answer} onChange={(e) => setAnswer(e.target.value)} className="quiz-input" />
      </label>
      <input type="submit" value="Submit" className="quiz-submit" />
    </form>
  );
}

export default Quiz;