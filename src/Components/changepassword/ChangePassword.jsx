import React, { useState } from 'react';
import './ChangePassword.css';
import changelogo from '../../Assets/log.png';

const ChangePassword = () => {
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
                    <li className="list-inline-item">Sign up</li>
                    <li className="list-inline-item">Sign in</li>
                </ul>
            </div>

            <div className="change-card container d-flex justify-content-center align-items-center">
                <div className="col-md-4 col-sm-12">
                    <h2 className="text-center text-warning">Change Password</h2>
                    <form onSubmit={handleSubmit}>
                        <h3>Old Password</h3>
                        <input
                            type="password"
                            name="email"
                            placeholder="Enter Old Password"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            className="form-control mb-3"
                        />
                        <h3>New Password</h3>
                        <input
                            type="password"
                            name="password"
                            placeholder="Enter New Password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            className="form-control mb-3"
                        />
                        <h3>Repeat New Password</h3>
                        <input
                            type="password"
                            name="confirmPassword"
                            placeholder="Repeat New Password"
                            value={formData.confirmPassword}
                            onChange={handleChange}
                            required
                            className="form-control mb-3"
                        />
                        <button type="submit" className="btn btn-warning btn-block">Change Password</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default ChangePassword;
