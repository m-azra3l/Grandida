import React from 'react';
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Album from './pages/Album';
import './App.css';
import { Layout } from 'antd';
import logo from './logo.svg';
import { SearchOutlined, DownCircleOutlined } from "@ant-design/icons"; 

const { Header, Footer, Content } = Layout;


const App = () =>{
  return (
    <Layout>
      <Header style={{
        position: 'sticky',
        top: 0,
        zIndex: 1,
        width: '100%',
      }}>Header</Header>
      <Content className="contentWindow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/album" element={<Album />} />
          </Routes>
        </Content>
    </Layout>
  );
}

export default App;
