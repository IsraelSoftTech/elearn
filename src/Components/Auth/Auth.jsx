import React, { useState } from 'react';
import Signup from '../Signup/Signup';
import Signin from '../Signin/Signin';
import ChangePassword from '../ChangePassword/ChangePassword';
import ResetPassword from '../ResetPassword/ResetPassword';

const Auth = () => {
  const [authMode, setAuthMode] = useState('signin'); // 'signin', 'signup', or 'changepassword'

  const toggleAuth = (mode) => {
    setAuthMode(mode);
  };

  return (
    <div>
      {authMode === 'signup' && <Signup onToggleAuth={() => toggleAuth('signin')} />}
      {authMode === 'signin' && (
        <Signin
          onToggleAuth={() => toggleAuth('signup')}
          onChangePassword={() => toggleAuth('changepassword')} // Pass this to handle change password
        />
      )}
      {authMode === 'changepassword' && (
        <ChangePassword onToggleAuth={() => toggleAuth('signin')} />
      )}
      {authMode === 'reset' && (
        <ResetPassword onToggleAuth={() => toggleAuth('signin')} />
      )}
    </div>
  );
};

export default Auth;
