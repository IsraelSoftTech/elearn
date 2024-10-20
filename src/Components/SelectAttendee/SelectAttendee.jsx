import React, { useState } from "react";
import Draggable from "react-draggable";
import './SelectAttendee.css';
import { TbTrash } from "react-icons/tb";
import { BiSearch } from "react-icons/bi";

const SelectAttendee = () => {
    const [open, setOpen] = useState(true);
    const [selectedAttendees, setSelectedAttendees] = useState([
      { name: "Mary Joanah", id: 1 }
    ]);
  
    // Close modal function
    const closeModal = () => {
      setOpen(false);
    };
  
    const removeAttendee = (id) => {
      setSelectedAttendees(selectedAttendees.filter((attendee) => attendee.id !== id));
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
              <div className="modal-tabs">
                <h6 className="tab-btn">Admins | 5</h6>
                <h6 className="tab-btn">Teachers | 15</h6>
              </div>
              <div className="modal-body">
                <div className="search-box"> <BiSearch/>
                  <input type="text" placeholder="Search attendee" />
                </div>
                <table>
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Qualification</th>
                      <th>Course</th>
                    </tr>
               
                  </thead>
                 
                  <tbody>
                    <tr>
                      <td>John Mark Doe</td>
                      <td>Master degree</td>
                      <td>English</td>
                    </tr>
               
                    <tr>
                      <td>John Mark Doe</td>
                      <td>Degree</td>
                      <td>Maths</td>
                    </tr>
                  </tbody>
                </table>
    
                <div className="selected-attendees">
                  <h4>Selected Attendees</h4>
                  {selectedAttendees.map((attendee) => (
                    <div key={attendee.id} className="selected-attendee">
                      {attendee.name}
                      <h6
                        className="remove-attendee-btn"
                        onClick={() => removeAttendee(attendee.id)}
                      >  | <TbTrash className="trash-icon"/>
    
                      </h6>
                    </div>
                  ))}
                </div>
                <div className="btns">
                    <button className="add-everyone-btn">Add Everyone</button>
                    <button className="add-selected-btn">Add Selected</button>
                </div>
              </div>
            </div>
          </Draggable>
        )
      );
    };
    

export default SelectAttendee