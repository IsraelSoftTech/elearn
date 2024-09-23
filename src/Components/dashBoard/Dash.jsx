import React, { useState } from 'react';
import './dash.css';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import logo from '../../Assets/log.png';
import { BiAbacus, BiBell, BiBook, BiBookAdd, BiBookReader, BiNote, BiSolidDashboard } from 'react-icons/bi';
import { PiChalkboardTeacherLight, PiStudent } from 'react-icons/pi';
import { GiGraduateCap, GiTeacher } from 'react-icons/gi';
import { MdHomeWork } from 'react-icons/md';
import { Link } from 'react-router-dom';
import ReactCountryFlag from 'react-country-flag';
import profile from '../../Assets/profile.png';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend } from 'chart.js';

// Register the components with Chart.js
ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

const Dash = () => {
  const [date, setDate] = useState(new Date());

  // Sample data for the chart
  const data = {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday','Sunday',],
    datasets: [
      {
        label: 'Scheduled Classes',
        data: [20, 60, 80, 100, 100, 80,60],
        fill: true,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.4, 
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
    },
  };

  return (
    <div className="dashboard">
      <div className="sidebar">
        <div className='logo'>
          <img src={logo} alt="" />
          <h2>E-LEARNING SCHOOL</h2>
        </div>

        <Link to="/" className="sidebar-item active">
          <BiSolidDashboard className='dash-icon' /> Dashboard
        </Link>
        <Link to="/students" className="sidebar-item">
          <GiGraduateCap className='dash-icon' /> Students
        </Link>
        <Link to="/teachers" className="sidebar-item">
          <GiTeacher className='dash-icon' /> Teachers
        </Link>
        <Link to="/courses" className="sidebar-item">
          <BiBookReader className='dash-icon' /> Courses
        </Link>
        <Link to="/classroom" className="sidebar-item">
          <GiTeacher className='dash-icon' /> Classes
        </Link>
        <Link to="/homework" className="sidebar-item">
          <MdHomeWork className='dash-icon' /> Assignments
        </Link>
        <Link to="/attendance" className="sidebar-item">
          <BiNote className='dash-icon' /> Attendance
        </Link>
      </div>

      <div className="main-content">
        <div className="header">
          <input type="text" placeholder="Place a search" />
          <div className="user-options">
            <span className='country'>
              <ReactCountryFlag countryCode='GB' svg style={{ width: '45px', height: '45px', border: 'none' }} />
            </span>
            <span><BiAbacus style={{ width: '25px', height: '25px', border: 'none', fontWeight: '100' }} /></span>
            <span><BiBell style={{ width: '30px', height: '30px', border: 'none' }} /></span>
            <span className='profile'><img src={profile} alt="" /></span>
          </div>
        </div>

        <div className="cards">
          <div className='card'>
            <div className='card-content'>
              <GiGraduateCap className='ic' />
              <div className='text'>
                <h3>Students</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>

          <div className='card'>
            <div className='card-content'>
              <PiChalkboardTeacherLight className='ic' />
              <div className='text'>
                <h3>Teachers</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>

          <div className='card'>
            <div className='card-content'>
              <BiBook className='ic' />
              <div className='text'>
                <h3>Courses</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>

          <div className='card'>
            <div className='card-content'>
              <PiStudent className='ic' />
              <div className='text'>
                <h3>Assignments</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>

          <div className='card'>
            <div className='card-content'>
              <BiBookAdd className='ic' />
              <div className='text'>
                <h3>Class</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>

          <div className='card'>
            <div className='card-content'>
              <BiBookAdd className='ic' />
              <div className='text'>
                <h3>Schedules</h3>
                <h2>10</h2>
              </div>
            </div>
          </div>
        </div>

        <div className="down-items">
          <div className="scheduled-classes">
            <h3>Scheduled Classes</h3>

            {/* Curved Statistical Graph */}
            <Line data={data} options={options} />

            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Date</th>
                  <th>Time</th>
                </tr>
              </thead>
              <tbody>
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
              </tbody>
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

export default Dash;
