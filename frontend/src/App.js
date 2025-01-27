import logo from "./logo.svg";
import "./App.css";
import { SearchBar } from "./components/SearchBar/SearchBar";
import { ProductResult } from "./components/ProductResult/ProductResult";
import { Typography } from "@mui/material";
import { useState } from "react";

function App() {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <Typography variant="h1">E-Component Scraper</Typography>
      </header>
      <SearchBar
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        setSearchResult={setSearchResult}
        setIsLoading={setIsLoading}
      ></SearchBar>
      <ProductResult
        products={searchResult}
        isLoading={isLoading}
      ></ProductResult>
    </div>
  );
}

export default App;
