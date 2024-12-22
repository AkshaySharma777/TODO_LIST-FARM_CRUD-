import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {
  return (
    <div className="App">
      Hello World!
      <h1 className='text-bg-primary'>FARM STACK</h1>
      <div className="App list-group-item justify-content-center align-items-center mx-auto mt-2" style={{"width": "400px", "backgroundColor": "white"}}></div>
    </div>
  );
}

export default App;
