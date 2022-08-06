import React from "react";
import { Link } from "react-router-dom";

const NavBar = () => {
    return (
        <nav className="nav">
            <Link to="/" className="homepage">Home</Link>
            <ul>
                <li>
                    <Link to="/posts">View Posts</Link>
                </li>
                <li>
                    <Link to="/postform">Add a post</Link>
                </li>
            </ul>
        </nav>
    );
}

export default NavBar;