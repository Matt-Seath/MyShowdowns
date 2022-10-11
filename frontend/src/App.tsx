import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Header from './components/Header'
// import HomePage from "./components/HomePage";
// import TeamsPage from "./components/TeamsPage";
// import BattlesPage from "./components/BattlesPage";

function App() {
  return (
    <div className="App">
      <Header />
      My App
    </div>
  );
}

export default App;
