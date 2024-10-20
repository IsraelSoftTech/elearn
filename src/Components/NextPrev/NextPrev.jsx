import React from 'react';
import './NextPrev.css';
import { GrFormNextLink } from 'react-icons/gr';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const NextPrev = () => {
  const navigate = useNavigate(); // Hook to handle navigation

  const handleNextClick = () => {
    navigate('/admin-dashone'); // Navigate to the AdminDashOne component
  };

  return (
    <div className='next-prev'>
      <div className="next-card" onClick={handleNextClick}> {/* Handle click event */}
        <GrFormNextLink className='arrow'/>
      </div>
    </div>
  );
};

export default NextPrev;
