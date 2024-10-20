import React from 'react'
import './Meeting.css'

const Meeting = () => {
    //   meeting
const datum = [
    { type: 'Staff', description: 'Staff meeting with all of the new recruited teachers...', date: '07-02-20', time: '12 PM' },
    { type: 'Staff', description: 'Staff meeting with all of the new recruited teachers...', date: '07-02-20', time: '12 PM' }
  ];
  return (
    <div>
        {/* Meetings */}
<div className="meetings-container">
      <div className="meetings-header">
        <h2>Meetings</h2>
     
        <table>
            <th>Today</th>
            <th>Week</th>
            <th>Month</th>
        </table>
       
      </div>

      <div className="meetings-table">
        <div className="table-header">
     
        <span className="header-item"></span>
          <span className="header-item">Type</span>
          <span className="header-item">Description</span>
          <span className="header-item">Date</span>
          <span className="header-item">Time</span>
        </div>

        {datum.map((item, index) => (
          <div className="table-row" key={index}>
            <span className="row-item">{item.type}</span>
            <span className="row-item description">{item.description}</span>
            <span className="row-item">{item.date}</span>
            <span className="row-item">{item.time}</span>
          </div>
        ))}

      
         
      <h6>See All</h6>

      </div>
      </div>
    </div>
  )
}

export default Meeting