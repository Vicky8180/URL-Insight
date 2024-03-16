import React from 'react';
import '../Display/display.css'; 
import Loading from '../loading';

const DomainInfoDisplay = ({ domainInfo }) => {
  const { external_domains } = domainInfo;

  return (
    <div className="domain-info-container">
      {external_domains ? 
        <div className="info-section external-domains">
          <h2>External Domains</h2>
          {external_domains.map((externalDomain, index) => (
            <div key={index} className="external-domain-item">
             
              <ul>
                {Object.entries(externalDomain).map(([type, values], index) => (
                  <li key={index}>
                    <strong>{type}</strong>: {values.length > 0 ? values.join(', ') : 'None'}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      : <Loading/>}
    </div>
  );
};

export default DomainInfoDisplay;
