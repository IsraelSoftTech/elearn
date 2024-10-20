import React from 'react';
import './Topbar.css';
import { BiAbacus, BiBell } from 'react-icons/bi';
import profile from '../../Assets/profile.png';
import flag from '../../Assets/uk.png';

const Topbar = ({ isMenuOpen }) => {
  return (
    <div className={`search-bar ${isMenuOpen ? 'menu-open' : ''}`}>
      <input type="text" placeholder=" 🔍 Place a Search" />
      <div className="right-search">
        <img src={flag} alt="" className='flag' />
        <BiAbacus />
        <BiBell />
        <img src={profile} alt="" className='profile' />
      </div>
    </div>
  );
};

export default Topbar;
