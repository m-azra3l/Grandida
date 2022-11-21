import React from 'react';
import { Link } from 'react-router-dom';
import { useLocation } from "react-router-dom";
import "./Album.css";
import Opensea from "../images/opensea.png";
import { ClockCircleOutlined } from "@ant-design/icons";

const Album = () => {
  
    const {state: album} = useLocation();
    return (
    <>
    <button onClick={() =>console.log(album)}> HIIII </button>
    </>
  )
  }
  
  export default Album;