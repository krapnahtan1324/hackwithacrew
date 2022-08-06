import {React, Component } from 'react';
import { Route, Routes } from 'react-router-dom';
import NavBar from './components/navbar/NavBar';
import ViewPosts from './pages/ViewPosts';
import AddPost from './pages/AddPost';
import Home from './pages/Home';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar/>
        <div className='container'>
          <Routes>
            <Route path='/' element={ <Home/> }/>
            <Route path='/posts' element={ <ViewPosts/> }/>
            <Route path='/postform' element={ <AddPost/> }/>
          </Routes>
        </div>
      </div>
    );
  }
}

export default App;
