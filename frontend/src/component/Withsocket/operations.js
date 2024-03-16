import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import './operation.css';
import SDisplay from "./SDisplay"
import ExternalDisplay from "./externalDisplay"
import InfoDisplay from "./InfoDisplay"
import Loading from '../loading';

const socket = io('http://localhost:5000'); 

const ButtonComponent = ({url}) => {
  const [message, setMessage] = useState();
  const [domaincheck, setDomain]=useState(false)
  const [externalcheck, setExternal]=useState(false)
  const [info_domain, setInfoDomain]=useState(false)
  const handleClick = (buttonName) => {
    socket.emit('info_domain', url);
    console.log("info_domain")
    setDomain(false);
    setExternal(false)
    setInfoDomain(true)

  };
  
  const handleSubDomain = (buttonName) => {
    socket.emit('getsubdomain', url);
    console.log("getsubdomain")
    setDomain(true);
    setExternal(false)
    setInfoDomain(false)
  };

  const handleExternal = (buttonName) => {
    socket.emit('getexternaldomains', url);
    console.log("getexternaldomains")
    setDomain(false);
    setExternal(true)
    setInfoDomain(false)
  };
  useEffect(() => {
    socket.on('connect', () => {
      console.log('Socket connected');
    });

    socket.on('messageFromServer', (msg) => {
      setMessage(msg);
      console.log(msg)
    });

    return () => {
      socket.off('connect');
      socket.off('messageFromServer');
    };
  }, []);



  return (
    <>
      <div className="button-container">
      <button onClick={() => handleClick('Button 1')} className="button">Get_info</button>
      <button onClick={handleExternal} className="button">External</button>
      <button onClick={handleSubDomain} className="button">Subdomains</button>
    </div>
      {domaincheck && message && externalcheck===false && info_domain===false ? <><SDisplay   domainInfo={message}/></>:<></>}
      {domaincheck===false && message && externalcheck && info_domain===false ? <ExternalDisplay   domainInfo={message}/>:<></>}
      {domaincheck===false && message && externalcheck===false && info_domain? <InfoDisplay   domainInfo={message}/>:<></>}

    </>


  
  );
};

export default ButtonComponent;
