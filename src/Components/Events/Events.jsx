import React, { useState } from 'react'
import './Events.css'
const Events = () => {
    const [events] = useState([
        {
          title: 'Staff meeting with all of the new ...',
          type: 'Meeting',
          time: '12:30 pm',
        },
        {
          title: 'Staff meeting with all of the new ...',
          type: 'Meeting',
          time: '12:30 pm',
        },
        {
          title: 'Staff meeting with all of the new ...',
          type: 'Meeting',
          time: '12:30 pm',
        },
        {
          title: 'Staff meeting with all of the new ...',
          type: 'Meeting',
          time: '12:30 pm',
        },
      ]);
    
      const handleClose = () => {
        console.log('Modal closed');
      };
  return (
    <div className="modal">
      <div className="modal-content">
        <div className="modal-header">
          <h3>All Events | 10</h3>
          <span className="add-icon">+</span>
        </div>
        <div className="modal-body">
          <div className="event-date">
            <span className="calendar-icon">📅</span>
            <span>11-09-2024</span>
          </div>
          <table className="event-table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Type</th>
                <th>Time</th>
              </tr>
            </thead>
            <tbody>
              {events.map((event, index) => (
                <tr key={index}>
                  <td>{event.title}</td>
                  <td>{event.type}</td>
                  <td>{event.time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="modal-footer">
          <button className="close-button" onClick={handleClose}>Close</button>
        </div>
      </div>
    </div>
  )
}

export default Events