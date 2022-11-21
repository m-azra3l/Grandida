import React from 'react';
import { Link } from 'react-router-dom';
import { useLocation } from "react-router-dom";
import "./Album.css";
import Opensea from "../images/opensea.png";
import { ClockCircleOutlined } from "@ant-design/icons";

const Album = () => {
  
    const {state: album} = useLocation();

    /*const albumDetails = [
        {
            "token_address": "0x8a68d4e28515815cd6026416f4b2a4b647796f3e",
            "token_id": "4",
            "amount": "1",
            "contract_type": "ERC721",
            "name": "Shadow",
            "symbol": "shad",
        }
    ]*/
    return (
    <>
    <div className='albumContent'>
        <div className='topBan'>
            <img
                src={album.image}
                alt="albumcover"
                className="albumCover"></img>
            <div className='albumDeets'>
                <div>Album</div>
                <div className='title'>{album.title}</div>
            </div>
        </div>
    </div>
    </>
  )
  }
  
  export default Album;