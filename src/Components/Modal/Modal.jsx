import React, { useState } from "react";
import { FaTrashAlt } from "react-icons/fa";
import { AiOutlineClose } from "react-icons/ai";
import { BsClock, BsClockFill } from "react-icons/bs";

import './Modal.css'; // Import the styles
import { FiTrash2 } from "react-icons/fi";

const Modal = () => {
    const [isVisible, setIsVisible] = useState(true);
    const [position, setPosition] = useState({ x: 0, y: 0 }); // To track the position of the card
    const [isDragging, setIsDragging] = useState(false); // To track drag state
    const [offset, setOffset] = useState({ x: 0, y: 0 }); // To track mouse offset from the top-left of the card
  
    const attendees = [
      "John Doe Mark",
      "Mary Joanah",
      "John Doe Mark",
      "Mary Joanah",
      "Ngwa Mark",
    ];
  
    const handleClose = () => {
      setIsVisible(false);
    };
  
    // Mouse down event to start dragging
    const handleMouseDown = (e) => {
      setIsDragging(true);
      setOffset({
        x: e.clientX - position.x,
        y: e.clientY - position.y,
      });
    };
  
    // Mouse move event to handle dragging
    const handleMouseMove = (e) => {
      if (isDragging) {
        setPosition({
          x: e.clientX - offset.x,
          y: e.clientY - offset.y,
        });
      }
    };
  
    // Mouse up event to stop dragging
    const handleMouseUp = () => {
      setIsDragging(false);
    };
  
    // If the card is not visible, don't render it
    if (!isVisible) {
      return null;
    }
  
  return (
    <div
      className="meeting-card"
      style={{ left: `${position.x}px`, top: `${position.y}px`}} // Positioning the card dynamically
      onMouseDown={handleMouseDown}
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
    >
      <AiOutlineClose className="close-icon" onClick={handleClose} />

      <div className="meeting-header">
        <h3>Staff meeting with all of the newly recruited teachers</h3>
        <div className="meeting-details">
          <span className="tag">Meeting</span>
          <span className="time">
            <BsClockFill /> 12:30 PM
          </span>
        </div>
      </div>

      <p className="description">
        We are going to be having a meeting with all of the newly recruited
        teachers. This meeting is going to brief these teachers on how the
        platform works, and what is going to be required of them and a lot more.
      </p>

      <div className="attendees-section">
        <p>Attendees | {attendees.length}</p>
        <div className="attendee-kind">
          <h5 className="admin-but">Admins | 5</h5>
          <h5 className="teacher-but">Teachers | {attendees.length - 5}</h5>
        </div>

        <div className="attendees-list">
          {attendees.map((attendee, index) => (
            <div key={index} className="attendee">
              {attendee}   |
              <FiTrash2 className="trash-icon" />
            </div>
          ))}
        </div>
      </div>

      <button className="update-but">Update</button>
    </div>
  )
}

export default Modal