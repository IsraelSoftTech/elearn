import React from 'react'
import './cards.css'
import { FaGraduationCap } from 'react-icons/fa'
import { GiTeacher } from 'react-icons/gi'
import { BiBook } from 'react-icons/bi'

const cards = () => {
  return (
    <div className="cards">
         <div className="card">
            <FaGraduationCap className='icon'/>
            <div className='text'>
            <h3>Students</h3>
            <h4>10</h4>
            </div>
        </div>
      
        <div className="card">
            <GiTeacher className='icon'/>
            <div className='text'>
            <h3>Teachers</h3>
            <h4>10</h4>
            </div>
        </div>
        <div className="card">
            <BiBook className='icon'/>
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
            <h3>Class</h3>
            <h4>10</h4>
            </div>
        </div>
        
        <div className="card">
            <GiTeacher className='icon'/>
            <div className='text'>
            <h3>Scheduled Class</h3>
            <h4>10</h4>
            </div>
        </div>
   
    </div>
  )
}

export default cards