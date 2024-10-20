import React from 'react'
import './AdminDashTwo.css'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NavComponent from '../NavComponent/NavComponent';
import { FaChalkboardTeacher, FaGraduationCap } from 'react-icons/fa';
import { BiBook, BiBookAdd } from 'react-icons/bi';
import { GiTeacher } from 'react-icons/gi';
import { PiChalkboardTeacherLight } from 'react-icons/pi';
import GraphChat from '../GraphChat/GraphChat';
import Calenda from '../Calenda/Calenda';
import Chats from '../Chats/Chats';
import Meeting from '../Meeting/Meeting';
import Application from '../Application/Application';
import NextPrev from '../NextPrev/NextPrev';
import NextPrevOne from '../NextPrevOne/NextPrevOne';



const AdminDashTwo= () => {
  return (
    <div>
    <NavComponent/>
    {/* Cards Container */}
    <div className="cards">
              {/* Add your card content here */}
              <div className="card">
                <FaGraduationCap className='icon'/>
                <div className='text'>
                <h3>Students</h3>
                <h4>10</h4>
                </div>
            </div>
            <div className="card">
                <FaChalkboardTeacher className='icon'/>
                <div className='text'>
                <h3>Teachers</h3>
                <h4>10</h4>
                </div>
            </div>
            <div className="card">
                <BiBookAdd className='icon'/>
                <div className='text'>
                <h3>Courses</h3>
                <h4>10</h4>
                </div>
            </div>
            <div className="card">
                <BiBook className='icon'/>
                <div className='text'>
                <h3>Assignments</h3>
                <h4>10</h4>
                </div>
            </div>
            <div className="card">
     
                <GiTeacher className='icon'/>
                <div className='text'>
                <h3>Classes</h3>
                <h4>10</h4>
                </div>
          
            </div>
    
            <div className="card">
                <PiChalkboardTeacherLight className='icon'/>
                <div className='text'>
                <h3>Scheduled Classes</h3>
                <h4>10</h4>
                </div>
            </div>
             {/* Graphs and Calendar components */}
             <div className="graph-calendar">
            <GraphChat/>
            <GraphChat/>
        <Calenda/>
     
      
            </div>
            <div className="meeting-apps">
                    <Meeting/>
                    <Chats/>
                    <Application/>
                    
                    </div>
    
                  <NextPrevOne/>
    
          </div>
    
          </div>
           
  )
}

export default AdminDashTwo