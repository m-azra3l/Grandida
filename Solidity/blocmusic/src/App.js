import React from 'react';
import { useState } from 'react';
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Album from './pages/Album';
import './App.css';
import { Layout } from 'antd';
import logo from './logo.svg';
import Spotify from "./images/Spotify.png";
import Player from "./components/AudioPlayer";
import { SearchOutlined, DownCircleOutlined } from "@ant-design/icons"; 

const { Header, Footer, Content } = Layout;


const App = () =>{
  
  const [nftAlbum, setNftAlbum] = useState();
  return (
      <Layout>
        <Header style={{
          position: 'sticky',
          top: 0,
          zIndex: 1,
          width: '100%',
        }}><div className="logo" />
        <Link to="/"><img src={Spotify} style={{height:40, width: 40}} alt="Logo" className="logo"></img></Link>
        </Header>
        <Content className="contentWindow">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/album" element={<Album />} />
            </Routes>
          </Content>
          <Footer className="footer">
          {nftAlbum &&
          <Player
            url={nftAlbum}
          />
          }
        </Footer>
      </Layout>
  );
}

export default App;
