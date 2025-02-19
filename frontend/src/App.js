import logo from "./logo.svg";
import "./App.css";
import { SearchBar } from "./components/SearchBar/SearchBar";
import { ProductResult } from "./components/ProductResult/ProductResult";
import { Typography } from "@mui/material";
import { useState } from "react";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";

function App() {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="App">
      <div className="App-header">Forseti</div>
      <div className="background">
        <div
          style={{
            color: "white",
            position: "absolute",
            bottom: "50%",
            left: "25%",
            fontWeight: "bold",
            textAlign: "center",
          }}
        >
          {" "}
          Scrapes data from major electronic component websites including
          FindChips, OctoPart, OemsTrade and ICSource.
        </div>
        <SearchBar
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
          setSearchResult={setSearchResult}
          setIsLoading={setIsLoading}
        ></SearchBar>
        <div className="check-boxes">
          <CheckCircleIcon fontSize="large" />
        </div>
      </div>
      <ProductResult
        products={searchResult}
        isLoading={isLoading}
        searchQuery={searchQuery}
      ></ProductResult>
    </div>
  );
}

export default App;
