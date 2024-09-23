import React, { useState } from 'react';
import './Signup.css';
import { FcGoogle } from 'react-icons/fc';
import signuplogo from '../../Assets/log.png';
import 'bootstrap/dist/css/bootstrap.min.css';

const Signup = ({ onToggleAuth }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <div className="signup-container d-flex flex-column justify-content-center align-items-center vh-100">
      <div className="signup-header d-flex justify-content-between align-items-center fixed-top w-100 p-3 ">
        <div className="signup-logo">
          <img src={signuplogo} alt="Logo" />
        </div>
        <ul className="list-inline mb-0">
          <li className="list-inline-item">
            <button className='active btn btn-link' style={{color: 'orangered',textDecoration: 'none',}}>Sign Up</button>
          </li>
          <li className="list-inline-item">
            <button onClick={onToggleAuth} className='btn btn-link' style={{color: 'orangered',textDecoration: 'none',}}>Sign In</button>
          </li>
        </ul>
      </div>

      <div className="signup-card container d-flex justify-content-center align-items-center">
        <div className="col-md-4 col-sm-12 bg-white p-4 rounded shadow">
          <h2 className="text-center " style={{color: 'orangered',}}>Sign up</h2>
          <button className="google-auth d-flex align-items-center justify-content-center border p-2 mb-3" style={{ color: '#555' }}>
            <FcGoogle style={{ paddingRight: '1rem', fontSize: '40px' }} />
            Continue with Google
          </button>
          <p className="or-text text-center text-muted mb-3">________Or________</p>
          <form onSubmit={handleSubmit}>
            <h3>Name</h3>
            <input
              type="text"
              name="name"
              className="form-control mb-3"
              placeholder="Enter full names"
              value={formData.name}
              onChange={handleChange}
              required
            />
            <h3>Email</h3>
            <input
              type="email"
              name="email"
              className="form-control mb-3"
              placeholder="Enter email"
              value={formData.email}
              onChange={handleChange}
              required
            />
            <h3>Password</h3>
            <input
              type="password"
              name="password"
              className="form-control mb-3"
              placeholder="Enter password"
              value={formData.password}
              onChange={handleChange}
              required
            />
            <h3>Confirm Password</h3>
            <input
              type="password"
              name="confirmPassword"
              className="form-control mb-3"
              placeholder="Repeat password"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
            />
            <p className="signin-text text-center">
              Already have an account? <button onClick={onToggleAuth} className="btn btn-link text-cyan">Sign In</button>
            </p>
            <button type="submit" className="create-account-btn btn btn-warning w-100">Create account</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Signup;
