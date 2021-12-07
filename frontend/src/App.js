import React from 'react'
import './App.css';
import Header from './components/Header'
import TextView from './components/TextView'


function App() {
  return (
    <div className ="container">
      <Header title = "OnionGen"/>
      <TextView/>
    </div>
  );
}

export default App;
