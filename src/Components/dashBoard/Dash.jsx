import React, { useState } from 'react';
import './dash.css';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import logo from '../../Assets/log.png'
import { BiBell, BiBook, BiBookAdd, BiBookReader, BiFlag, BiNotification, BiSolidDashboard, BiUser } from 'react-icons/bi';
import { PiChalkboardTeacherLight, PiStudent } from 'react-icons/pi';
import { GiGraduateCap, GiTeacher } from 'react-icons/gi';
import { CgChart } from 'react-icons/cg';
import { GoGraph } from 'react-icons/go';
import { MdAssignment, MdClass } from 'react-icons/md';
import { FaChalkboardTeacher, FaLanguage } from 'react-icons/fa';
import ReactCountryFlag from 'react-country-flag'

const Dash = () => {
  const [date, setDate] = useState(new Date());

  return (
    <div className="dashboard">
      
      <div className="sidebar">
        <div className='logo'>
      <img src={logo} alt="" />
      </div>
        <div className="sidebar-item active"><BiSolidDashboard className='dash-icon'/>Dashboard</div>
        <div className="sidebar-item"><GiGraduateCap className='dash-icon'/>Students</div>
        <div className="sidebar-item">Teachers</div>
        <div className="sidebar-item">Courses</div>
        <div className="sidebar-item">Class</div>
        <div className="sidebar-item">Assignment</div>
        <div className="sidebar-item">Attendance</div>
      </div>
      <div className="main-content">
        <div className="header">
          <input type="text" placeholder="Place a search" />
          <div className="user-options">
            <span><ReactCountryFlag countryCode='GB' svg style={{width: '27px',height: '25px',borderRadius: '50%',border: 'none',}} /></span>
            <span><BiBell/></span>
            <span><BiUser/></span>
          </div>
        </div>
      <div className="cards">

        <div className='card'>
          <div className='card-content'>
          <GiGraduateCap className='ic'/>
            <div className='text'>
              <h3>Students</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>

        <div className='card'>
          <div className='card-content'>
          <PiChalkboardTeacherLight className='ic'/>
            <div className='text'>
              <h3>Teachers</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>

        <div className='card'>
          <div className='card-content'>
          <BiBook className='ic'/>
            <div className='text'>
              <h3>Courses</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>

        <div className='card'>
          <div className='card-content'>
          <PiStudent className='ic'/>
            <div className='text'>
              <h3>Assignments</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>

        <div className='card'>
          <div className='card-content'>
          <BiBookAdd className='ic'/>
            <div className='text'>
              <h3>Class</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>

        <div className='card'>
          <div className='card-content'>
          <BiBookAdd className='ic'/>
            <div className='text'>
              <h3>Scheduled Class</h3>
              <h2>10</h2>
            </div>
          </div>
        </div>


      </div>
        <div className="down-items">
        <div className="scheduled-classes">
          <h3>Scheduled Classes</h3>
          
         <table>
          <th>Name</th>
          <th>Date</th>
          <th>Time</th>
          <tr>
          <td>Ngwa Paul</td>
          <td>09/03/24</td>
          <td>9pm</td>
          </tr>
          <tr>
          <td>Kuh James</td>
          <td>09/10/24</td>
          <td>10pm</td>
          </tr>
         </table>
          <div className="see-all">See all</div>
        </div>
        <div className='live'>
          <h3>Add Contents</h3>
        </div>
        <div className="calendar">
          <h3>Calendar</h3>
          <Calendar
            onChange={setDate}
            value={date}
            className="react-calendar"
          />
        </div>
        </div>

      </div>
    </div>
  );
};



export default Dash