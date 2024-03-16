import React from 'react';
import './display.css'; 
import Loading from '../loading';


const DomainInfoDisplay = ({ domainInfo }) => {
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

    <>
      {host ? <> <div className="domain-info-container">
      {/* Domain Info */}
      <div className="info-section domain-info">
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
        
      </div>

  
      <div className="info-section subdomains">
        <h2>Subdomains</h2>
        {subdomains.map((subdomain, index) => (
          <div key={index} className="subdomain-item">{subdomain+"."+host}</div>
        ))}
      </div>

   
      <div className="info-section external-domains">
        <h2>External Domains</h2>
        {external_domains.length === 0 ? (
          <div>No external domains found</div>
        ) : (
          external_domains.map((externalDomain, index) => (
            <div key={index} className="external-domain-item">{externalDomain}</div>
          ))
        )}
      </div>
    </div></>:<Loading/>  }
    </>
   
  );
};

export default DomainInfoDisplay;
