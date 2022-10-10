import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import HomePage from "./components/HomePage";
// import TeamsPage from "./components/TeamsPage";
// import BattlesPage from "./components/BattlesPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Route path="/">
          <p>This is the Homepage.</p>
        </Route>
        <Route path="/teams">
          <p>This is the Teamspage</p>
        </Route>
        <Route path="/battles">
          <p>This is the Battlespage</p>
        </Route>
      </div>
    </Router>
  );
}

export default App;
