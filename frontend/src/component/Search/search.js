import React, { useState } from 'react';
import './search.css'; 
import axios from "axios";
import Display from "../Display/display";
import Operations from "../Withsocket/operations"
import Loading from '../loading';



function isValidUrl(url) {
    
    const urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;
  
    
    return urlRegex.test(url);
  }


const UrlSearchComponent = () => {
    const [url, setUrl] = useState('');
    const [check, setCheck] = useState(false);
    const [check2, setCheck2] = useState(true);
    const [socketcheck, setSocketcheck] = useState(true);
    const [responseData, setResponseData] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleUrlChange = (event) => {
            setUrl(event.target.value);
      
        
    };

    const handleSocket=()=>{
       
        if(isValidUrl(url)){
            setSocketcheck(false)
            setCheck(false)
        }else {
   alert("Not valid url")
   return
        }
    }

    const handleSearch = async () => {
     
        if (!url.trim()) {
            setError('Please enter a valid URL');
         
            return;
        }
          if(isValidUrl(url)){
            try {
              
                const response = await axios.post('http://localhost:5000/api/analyze', {
                    "url": url
                });
    
                console.log(response.data)
                setResponseData(response.data);
                setCheck(true);
                setCheck2(false);
                setSocketcheck(true)
            } catch (error) {
                setError('Failed to fetch data. Please try again later.');
                console.error('Error fetching data:', error);
            }
          }else {
            alert("not valid url")
            return;
          }
        // Reset error and loading state
        setError(null);
        setLoading(true);

        

        setLoading(false);
    };

  
    const domain = responseData ? {
        "city": responseData.domain_info?.data.city || '',
        "country": responseData.domain_info?.data.country || '',
        "ip": responseData.domain_info?.data.ip || '',
        "isp": responseData.domain_info?.data.isp || '',
        "latitude": responseData.domain_info?.data.latitude || '',
        "longitude": responseData.domain_info?.data.longitude || '',
        "organization": responseData.domain_info?.data.organization || '',
        "host": responseData.domain_info?.hostname || '',
        "subdomains": responseData.subdomains || [],
        "external_domains": responseData.external_domains || [],
    } : {};

    return (
        <>
            {check2 ? (
                <div className="url-search-container">
                    <h1>Search url Information</h1>
                    <input
                        type="text"
                        placeholder="Enter URL..."
                        value={url}
                        onChange={handleUrlChange}
                        className="url-input"
                    />
                    <button onClick={handleSearch} className="search-button">Search</button>
                    <button  onClick={handleSocket} className="search-button">Socket</button>
                </div>
            ) : (
                <div className="url-search-container" style={{ marginTop: "50px" }}>
                    <input
                        type="text"
                        placeholder="Enter URL..."
                        value={url}
                        onChange={handleUrlChange}
                        className="url-input"
                    />
                    <button onClick={handleSearch} className="search-button">Search</button>
                    <button  onClick={handleSocket} className="search-button">Socket</button>
                </div>

            )}

            {check && socketcheck? <Display domainInfo={domain} /> : null}
            {check===false && socketcheck===false? <Operations url={url}/> : null}
        </>
    );
};

export default UrlSearchComponent;
