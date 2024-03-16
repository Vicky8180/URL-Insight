import React from 'react';
import '../Display/display.css'; 
import Loading from '../loading';

const DomainInfoDisplay = ({ domainInfo }) => {
  const {  city,
    country,
    ip,
    isp,
    latitude,
    longitude,
    organization,
    host,} = domainInfo;

  return (
    <div className="domain-info-container">
      {domainInfo ? <><div className="info-section domain-info">
        <h2>Domain Info</h2>
        <div className="info-item">
          <strong>Hostname:</strong> {host}
        </div>
        <div className="info-item">
          <strong>City:</strong> {city}
        </div>
        <div className="info-item">
          <strong>Country:</strong> {country}
        </div>
        <div className="info-item">
          <strong>IP Address:</strong> {ip}
        </div>
        <div className="info-item">
          <strong>ISP:</strong> {isp}
        </div>
        <div className="info-item">
          <strong>Latitude:</strong> {latitude}
        </div>
        <div className="info-item">
          <strong>Longitude:</strong> {longitude}
        </div>
        <div className="info-item">
          <strong>Organization:</strong> {organization}
        </div>
        
      </div></>:<><Loading/></>}
    </div>
  );
};

export default DomainInfoDisplay;
