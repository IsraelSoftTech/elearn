


import './App.css';

import Dash from './Components/dashBoard/Dash';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Students from './Components/students/Students';
import Teachers from './Components/teachers/Teachers';
import Courses from './Components/courses/Courses';

import Homework from './Components/homework/Homework';
import Attendance from './Components/attendance/Attendance';
import ClassRoom from './Components/ClassRoom/ClassRoom';





function App() {
  return (
 <div className='app'>

  <Router>
    
    <Routes>
      
   
    <Route path="/" element={<Dash />} />
    <Route path="/students" element={<Students />} />
    <Route path="/teachers" element={<Teachers />} />
    <Route path="/courses" element={<Courses />} />
    <Route path="/classroom" element={<ClassRoom />} />
  
    <Route path="/homework" element={<Homework />} />
    <Route path="/attendance" element={<Attendance />} />
   
 
    </Routes>

  </Router>
  </div>
  );
}

export default App;
