import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';


import GraphChat from './Components/GraphChat/GraphChat';
import Calenda from './Components/Calenda/Calenda';
import Chats from './Components/Chats/Chats';
import AdminDashboard from './Components/AdminDashboard/AdminDashboard';
import NavComponent from './Components/NavComponent/NavComponent';
import Students from './Components/Students/Students';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NextPrev from './Components/NextPrev/NextPrev';
import AdminDashOne from './Components/AdminDashOne/AdminDashOne';
import AdminDashTwo from './Components/AdminDashTwo/AdminDashTwo';



function App() {


  return (

 <div className='app'>

  {/* <Chats/> */}
{/* <Calenda/> */}
{/* <GraphChat/> */}
<Router>
<Routes>

<Route path="/" element={<AdminDashboard />} />
<Route path="/students" element={<Students />} />

<Route path="/" element={<NextPrev />} />
<Route path="/admin-dashone" element={<AdminDashOne />} />
<Route path="/admin-dashtwo" element={<AdminDashTwo />} />

</Routes>

</Router>


  </div>
  );
}

export default App;
