import Search from "./component/Search/search"
import './App.css';
import Display from "./component/Display/display"
import SDisplay from "./component/Withsocket/SDisplay"

function App() {

const domain={

  "city":988,
    "country":"hujids",
    "ip":"847.4747.33.3",
    "isp":"nice if of",
    "latitude":577439934.33,
    "longitude":4343435.,
    "organization":"google.ocom",
    "ip_address":"8488484.4.4.",
    "server_host":"me pythond",
    "subdomains":["vickyc yadav", "lelo"],
    "external_domains":["njj","nnoceee", "niice"],
}


  return (
    <div className="App">
    <Search/>
    {/* <SDisplay/> */}

    {/* <Display domainInfo={domain}/> */}
    </div>
  );
}

export default App;
