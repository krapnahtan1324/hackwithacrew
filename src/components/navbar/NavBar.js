import React from "react";
import {  Link } from "react-router-dom";

const NavBar = () => {
    return (
        <nav className="nav">
            <a href="/" className="homepage">Home</a>
            <ul>
                <li>
                    <a href="/posts">View Posts</a>
                </li>
                <li>
                    <a href="/postform">Add a post</a>
                </li>
            </ul>
        </nav>
    );
}

export default NavBar;