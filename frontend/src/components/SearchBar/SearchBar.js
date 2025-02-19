import "./SearchBar.css";
import { Box, IconButton, Input } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import { useState } from "react";

export const SearchBar = ({
  searchQuery,
  setSearchQuery,
  setSearchResult,
  setIsLoading,
}) => {
  const [searchClicked, setSearchClicked] = useState(false);
  const getSearchResult = async () => {
    // implement handler if search query is empty
    // maybe animation to get them to fill in the empty field
    try {
      setIsLoading(true);
      const apiURL = process.env.REACT_APP_API_URL;
      const response = await fetch(`${apiURL}/api/search?q=${searchQuery}`, {
        method: "GET",
      });

      const data = await response.json();
      setSearchResult(data.data);
      console.log("Response from backend:", data);
      setIsLoading(false);
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };
  return (
    <Box
      className={"search-bar " + (searchClicked ? "animate" : "")}
      display="flex"
      alignItems="center"
    >
      <Box flex="1" display="flex" alignItems="center">
        {/* <IconButton
          type="submit"
          aria-label="search"
 
        > */}
        <SearchIcon className="search-icon" fontSize="large" />
        {/* </IconButton> */}
        <Input
          className="text-area"
          placeholder="Enter part number to search..."
          disableUnderline
          onInput={(e) => {
            setSearchQuery(e.target.value);
          }}
          sx={{
            "& fieldset": { border: "none" },
          }}
        />
        <button
          className="search-button"
          type="submit"
          onClick={() => {
            console.log("search clicked");
            if (searchQuery != "") {
              getSearchResult(searchQuery);
              setSearchClicked(true);
              console.log(searchQuery);
            } else {
              console.log("no search query entered");
            }
          }}
        >
          Search
        </button>
      </Box>
    </Box>
  );
};
