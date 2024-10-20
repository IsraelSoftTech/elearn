import React, { useState } from 'react';
import './NavComponent.css';
import logo from '../../Assets/log.png';
import { Link } from 'react-router-dom';
import { MdDashboard } from 'react-icons/md';
import { FaGraduationCap } from 'react-icons/fa';
import { GiTeacher } from 'react-icons/gi';
import { BiBook, BiBookAdd } from 'react-icons/bi';
import Topbar from '../../Components/Topbar/Topbar'; // Import Topbar




const NavComponent = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className={menuOpen ? 'menu-open' : ''}>
      {/* Menu Toggle Button for small screens */}
      <button className="menu-toggle" onClick={toggleMenu}>
        ☰
      </button>

      {/* Overlay when the sidebar is open */}
      <div className={`overlay ${menuOpen ? '' : ''}`} onClick={toggleMenu}></div>

      {/* Sidebar Menu */}
      <div className={`dash-left ${menuOpen ? 'active' : ''}`}>
        <div className="nav-bar">
          <img src={logo} alt="" className='logo' />
          <hr />
          <div className="side-menus">
            <ul>
              <Link to="/admindashboard" className='sider activemenu'>
                <MdDashboard className='sider-icon'/> Dashboard
              </Link>
              <Link to="/students" className='sider'>
                <FaGraduationCap className='sider-icon' /> Students
              </Link>
              <Link to="/teachers" className='sider'>
                <GiTeacher className='sider-icon' /> Teachers
              </Link>
              <Link to="/Courses" className='sider'>
                <BiBook className='sider-icon' /> Courses
              </Link>
              <Link to="/class" className='sider'>
                <GiTeacher className='sider-icon' /> Class
              </Link>
              <Link to="/assignments" className='sider'>
                <BiBookAdd className='sider-icon' /> Assignments
              </Link>
              <Link to="/attendance" className='sider'>
                <GiTeacher className='sider-icon' /> Attendance
              </Link>
            </ul>
          </div>
        </div>
      </div>

      {/* Topbar Component */}
      <Topbar isMenuOpen={menuOpen} />
   

   

     
    </div>
  );
};

export default NavComponent;
