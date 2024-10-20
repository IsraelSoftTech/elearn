import React, { useState } from 'react';
import './Signin.css';
import { FcGoogle } from 'react-icons/fc';
import signinlogo from '../../Assets/log.png';

const Signin = ({ onToggleAuth,onChangePassword }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
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
    // Handle form submission logic
    console.log(formData);
  };

  return (
    <div className="signin-container">
      <div className="signin-header">
        <div className="signin-logo">
          <img src={signinlogo} alt="Logo" />
        </div>
        <ul>
          <button onClick={onToggleAuth} className="toggle-button">Sign Up</button>
          <button className="toggle-button active">Sign In</button>
        </ul>
      </div>

      <div className="signin-card">
        <h2 style={{ color: '#FE7235' }}>Sign in</h2>
        <button className="google-auth">
          <FcGoogle style={{ paddingRight: '1rem', fontSize: '40px' }} />
          Continue with Google Authentication
        </button>
        <p className='divider'>Or</p>
        <form onSubmit={handleSubmit}>
          <h3>Email</h3>
          <input
            type="email"
            name="email"
            placeholder="Enter Email Address"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <h3>Password</h3>
          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <p className="signin-text">
            <button  className="forgot-button">Forgot Password?</button>
            <br />
            Don't have an account?
            <button onClick={onChangePassword}className="change-password-button">Change Password</button>
          </p>
          <button type="submit" className="create-account-btn">Sign In</button>
        </form>
      </div>
    </div>
  );
};

export default Signin;
