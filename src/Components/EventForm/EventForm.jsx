import React, { useState } from "react";
import Draggable from "react-draggable";
import "./EventForm.css"; // For the styling

const EventForm = () => {
    const [open, setOpen] = useState(true);

    // Close modal function
    const closeModal = () => {
      setOpen(false);
    };
  
    return (
        open && (
          <Draggable>
            <div className="modal-container">
              <div className="modal-header">
                <h2>Add an event</h2>
                <button className="close-btn" onClick={closeModal}>
                  &times;
                </button>
              </div>
              <div className="modal-body">
                <label htmlFor="type">Type</label>
                <select id="type" defaultValue="Meeting">
                  <option value="Meeting">Meeting</option>
                  <option value="Event">Event</option>
                  <option value="Reminder">Reminder</option>
                </select>
    
                <label htmlFor="title">Title *</label>
                <input id="title" type="text" required />
    
                <label htmlFor="description">Description *</label>
                <textarea id="description" required />
    
                <label>Attendees    <button className="add-attendee-btn">+</button></label>
                <div className="attendees">
                  <span>All attendees will be notified when the event is created</span>
                </div>
              </div>
    
              <div className="modal-footer">
                <button className="create-btn">Create event</button>
              </div>
            </div>
          </Draggable>
        )

  );
};

export default EventForm;
