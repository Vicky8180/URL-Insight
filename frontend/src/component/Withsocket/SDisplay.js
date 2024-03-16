import React, { useState } from 'react';
import '../Display/display.css';
import Loading from '../loading';


const DomainInfoDisplay = ({ domainInfo }) => {
  console.log(domainInfo)
  const {
    city,
    country,
    ip,
    isp,
    latitude,
    longitude,
    organization,
    host,
    subdomains,
    external_domains,
  } = domainInfo;
  return (
    <div className="domain-info-container">
     
      
      {subdomains ? <div className="info-section subdomains">
        <h2>Subdomains</h2>
        {subdomains.map((subdomain, index) => (
          <div key={index} className="subdomain-item">{subdomain}</div>
        ))}
      </div>:<><Loading/></> }

    

     
    </div>
  );
};

export default DomainInfoDisplay;
