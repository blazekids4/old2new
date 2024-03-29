import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHandPointRight } from '@fortawesome/free-solid-svg-icons';
import './App.css';
import Quiz from './components/Quiz';

// Import images for M, J, and L
import MImage from './images/M.jpeg';
import JImage from './images/J.jpeg';
import LImage from './images/L.jpeg';
import SImage from './images/S.jpeg';
import DImage from './images/D.jpeg';
import CImage from './images/C.jpeg';


function App() {
  const [balance, setBalance] = useState(100); // Example starting balance
  const [playline, setPlayline] = useState(['C', 'C', 'C', 'C']); // Add a fourth 'C'
  const [spinning, setSpinning] = useState(false);
  const [payout, setPayout] = useState(0);
  const [showQuiz, setShowQuiz] = useState(false);

  // const resetBank = () => {
  //   setBalance(100);
  // }

  const resetBank = () => {
    setShowQuiz(true);
  };

  // useEffect(() => {
  //   if (balance <= 0) {
  //     setShowQuiz(true);
  //   }
  // }, [balance]);

  const handleQuizAnswer = (isCorrect) => {
    if (isCorrect) {
      setBalance(100);
    }
    setShowQuiz(false);
  };

  const handleSpin = () => {
    // Deduct cost of spin and start spinning
    if (balance <= 0) {
      alert("You don't have enough balance to spin!");
      return;
    }
    setBalance(balance - 20);

    setSpinning(true);
  };

  useEffect(() => {
    if (spinning) {
      // Fetch new playline from the backend
      setTimeout(() => {
        fetch(`http://localhost:5000/?player_balance=${balance}`)
          .then((response) => response.json())
          .then((data) => {
            console.log('Data from backend:', data);
            setPlayline(data.playline);
            setPayout(data.payout);
            setBalance(data.balance);
            setSpinning(false);
          })
          .catch((error) => {
            console.error('Error:', error);
            setSpinning(false);
          });
      }, 1000); // Example spinning duration
    }
  }, [spinning, balance]);

  return (
    <div className="App">
      <br />
      <img src="lyons-slots.jpeg" className="logo"  alt="Lyons Logo" />
      <br />
      <h1>Welcome to Lyons Slots!</h1>
      <div className="slot-machine">
      {playline.map((symbol, index) => (
      <div key={index} className={`slot ${spinning ? 'spinning' : ''}`}>
        {symbol === 'M' ? (
          <img src={MImage} alt="M" className="slot-image" />
        ) : symbol === 'J' ? (
          <img src={JImage} alt="J" className="slot-image" />
        ) 
        : symbol === 'S' ? (
          <img src={SImage} alt="S" className="slot-image" />
        )
        : symbol === 'D' ? (
          <img src={DImage} alt="D" className="slot-image" />
        )
        : symbol === 'C' ? (
          <img src={CImage} alt="C" className="slot-image" />
        )
        : symbol === 'L' ? (
          <img src={LImage} alt="L" className="slot-image" />
        ) : (
          symbol
        )}
      </div>
    ))}
      </div>
      <div onClick={handleSpin}>
      <FontAwesomeIcon className="handle-icon rotate-90" icon={faHandPointRight} size="3x" />
      <p className="spin-text">Click to Spin</p>
      </div>

      <div className="spin-results">
        <p className="payout">
          {!spinning && (payout > 0 ? <span className="payout-value">{payout}</span> : <span className="payout-message">"You've Been Clowned! Sorry Spinner, You Ain't A Winner!"</span>)}
        </p>       
      </div>
      <div className="balance">
        <label htmlFor="player_balance">Your Bank:</label>
        <input type="number" id="player_balance" value={balance} readOnly />
      </div>
      {showQuiz && <Quiz onAnswer={handleQuizAnswer} />}
      <button className="button" onClick={resetBank}>Reset Bank</button>    </div>
  );
}

export default App;
