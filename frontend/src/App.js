import  React, { Component } from  'react';
import { BrowserRouter } from  'react-router-dom'
import { Route, Link } from  'react-router-dom'
import PollsList from "./components/PollsList.jsx"
import PollView from "./components/PollView.jsx"
import './App.css';

const BaseLayout  = () => (
<div  className="container-fluid">
    <nav className="navbar navbar-expand-lg navbar-dark bg-orange">
        <a  className="navbar-brand"  href="/">2020 Polls</a>
        <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
        <span  className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse"  id="navbarNavAltMarkup">
        <div  className="navbar-nav">
            <a  className="nav-item nav-link"  href="/polls">Polls Feed</a>
        </div>
    </div>
    </nav>
    <div  className="content">
        <Route  path="/polls"  exact  component={PollsList}  />
        <Route  path="/polls/:pk"  exact  component={PollView}  />
    </div>
</div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;
