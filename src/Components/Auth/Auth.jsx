import React, { useState } from 'react';
import Signup from '../signup/Signup';
import Signin from '../signin/Signin';
import ChangePassword from '../changepassword/ChangePassword';

const Auth = () => {
  const [authMode, setAuthMode] = useState('signin'); // 'signin', 'signup', or 'changepassword'

  const toggleAuth = (mode) => {
    setAuthMode(mode);
  };

  return (
    <div>
      {authMode === 'signup' && <Signup onToggleAuth={() => toggleAuth('signin')} />}
      {authMode === 'signin' && <Signin onToggleAuth={() => toggleAuth('signup')} />}
      {authMode === 'changepassword' && <ChangePassword onToggleAuth={() => toggleAuth('signin')} />}
      
      
    </div>
  );
};

export default Auth;
