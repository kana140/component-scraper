import logo from "./logo.svg";
import "./App.css";
import { SearchBar } from "./components/SearchBar/SearchBar";
import { ProductResult } from "./components/ProductResult/ProductResult";
import { Typography } from "@mui/material";
import { useState } from "react";

function App() {
  /*   async function getProducts() {
    console.log("retrieving products");
    const requestBody = { input: searchQuery, label: selectedFilter };
    console.log(searchQuery, selectedFilter);
    setIsLoading(true);
    try {
      const response = await axios.post(
        "http://localhost:3001/search-results",
        requestBody
      );
      // Handle the response as needed
      console.log("Products retrieved:", response.data.data);
      setProducts(response.data.data);
      setProductsLoaded(true);
      setIsLoading(false);
    } catch (error) {
      // Handle errors if the request fails
      console.error("Error retrieving products:", error.message);
    }
  } */
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <Typography variant="h1">E-Component Scraper</Typography>
      </header>
      {/* <p> Scrapes websites such as net component, blah, blah, blah</p> */}
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
