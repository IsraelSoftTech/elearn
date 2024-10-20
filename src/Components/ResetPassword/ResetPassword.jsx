import React, { useState } from 'react'
import changelogo from '../../Assets/log.png';

const ResetPassword = ({ onToggleAuth }) => {
    const [formData, setFormData] = useState({
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
        // Handle form submission logic
        console.log(formData);
    };

  return (

 <div className="change-container">
            <div className="change-header d-flex justify-content-between align-items-center fixed-top">
                <div className="change-logo"><img src={changelogo} alt="" /></div>
                <ul className="list-inline mb-0">
                <button onClick={onToggleAuth} className="toggle-button">Sign Up</button>
                <button className="toggle-button">Sign In</button>
                </ul>
            </div>

            <div className="change-card container d-flex justify-content-center align-items-center">
                <div className="col-md-4 col-sm-12">
                    <h2 className="text-center">Reset Password</h2>
                    <form onSubmit={handleSubmit}>
                        <h3>New Password</h3>
                        <input
                            type="password"
                            name="email"
                            placeholder="Enter Password"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            className="form-control mb-3"
                        />
                        <h3>Repeat New Password</h3>
                        <input
                            type="password"
                            name="password"
                            placeholder="Enter Password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            className="form-control mb-3"
                        />
                     
                        <button type="submit" className="btn-change">Reset Password</button>
                    </form>
                </div>
            </div>
        </div>
  )
}

export default ResetPassword