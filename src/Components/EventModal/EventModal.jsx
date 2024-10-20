import React from 'react';
import './EventModal.css'; // Link to the CSS file for styling
import { CgClose } from 'react-icons/cg';

const EventModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        {/* Modal header */}
        <div className="modal-header">
          <h3>Staff meeting with all of the newly recruited teachers</h3>
          <span className="close-button" onClick={onClose}><CgClose/></span>
        </div>

        {/* Modal body */}
        <div className="modal-body">
          <div className="event-details">
            <div className="event-type">
              <h3 className="meeting-tag">Meeting</h3>
              <div className="event-time">
                <span className="clock-icon">🕒</span>
                <span className="time">12:30 PM</span>
              </div>
              <div className="event-date">
                <span className="calendar-icon">📅</span>
                <span className="date">11-09-2024</span>
              </div>
            </div>

            <p className="event-description">
              We are going to be having a meeting with all of the newly recruited teachers. This meeting is going to brief these teachers on how the platform works, what is required of them, and much more.
            </p>
            <hr/>

            <div className="attendees-section">
              <span className="attendees-label">Attendees | 20</span>
              <div className="attendees-list">
                <h3 className="attendee-type">Admins | 5</h3>
                <h3 className="attendee-type">Teachers | 15</h3>
              </div>
            </div>
          </div>
        </div>
<hr/>
        {/* Modal footer */}
        <div className="modal-footer">
          <button className="update-button">Update</button>
        </div>
      </div>
    </div>
  );
};

export default EventModal;
