import React from 'react'
import './Application.css'


// applications
const applications = [
  {

    name: 'John Doe Maxwell',
    role: 'Tutor',
  },
  {
    name: 'Jane Smith',
    role: 'Tutor',
  },
];
const Application = () => {
  return (
    <>
 {/* applications */}
<div className="applications-container">
      <h2>Applications</h2>
      <table className="applications-table">
        <thead>
          <tr>
        
            <th>Name</th>
            <th>Role</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {applications.map((app, index) => (
            <tr key={index}>
              <td>{app.name}</td>
              <td>{app.role}</td>
              <td className="actions">
                <button>🗑️</button>
                <button>👁️</button>
                <button>📅</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <a href="#" className="see-all">See all</a>
    </div>
    </>
  )
}

export default Application