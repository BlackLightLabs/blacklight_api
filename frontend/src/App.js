import logo from './logo.svg';
import './App.css';
import {Routes, Route, HashRouter as Router} from 'react-router-dom'

import Header from "./components/Header";
import HomeScreen from "./screens/HomeScreen";
import Background from "./components/Background";
import Footer from "./components/Footer";

function App() {
    return (
        <Router>
            <Header/>
            <Background />
            <main className="py-3">
                <Routes>
                    <Route path="/" element={<HomeScreen/>}/>
                </Routes>
            </main>
            <Footer />
        </Router>
    );
}

export default App;
