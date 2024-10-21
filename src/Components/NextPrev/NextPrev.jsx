import React from 'react';
import './NextPrev.css';
import { GrFormNextLink } from 'react-icons/gr';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const NextPrev = ({ currentPage }) => {
  const navigate = useNavigate(); // Hook to handle navigation

  const handleNextClick = () => {
    if (currentPage === 'admindashboard')
      {
    navigate('/admin-dashone'); // Navigate to the AdminDashOne component
      } else if (currentPage === '/admin-dashtwo'){
        navigate('/admin-dashthree'); // Navigate to the AdminDashTwo component
      }
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
