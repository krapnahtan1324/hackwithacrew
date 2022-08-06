import {React, Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NavBar from './components/navbar/NavBar';
import ViewPosts from './pages/ViewPosts';
import AddPost from './pages/AddPost';
import Home from './pages/Home';
import './App.css';

class App extends Component {
  render() {
    let component
    switch (window.location.pathname) {
      case '/':
        component = <Home/>
        break
      case '/posts':
        component = <ViewPosts/>
        break
      case '/postform':
        component = <AddPost/>
        break
    }
    return (
      <div className="App">
        <NavBar/>
        {component}
      </div>
    );
  }
}

export default App;
