import React, { useState } from 'react'
import './Calenda.css'
import Calendar from 'react-calendar';
const Calenda = () => {
    // calendar
const [value, setValue] = useState(new Date());
  return (
    <div style={{background:'white-smoke',width:'100%',borderRadius:'5px'}}>
{/* calenda */}
<div className="calendar-container">
      <Calendar
        onChange={setValue}
        value={value}
      />
 
    </div>
    </div>
  )
}

export default Calenda