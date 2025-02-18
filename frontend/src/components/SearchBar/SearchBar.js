import "./SearchBar.css";
import { Box, IconButton, Input } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";

export const SearchBar = ({
  searchQuery,
  setSearchQuery,
  setSearchResult,
  setIsLoading,
}) => {
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
    <Box className="search-bar" display="flex" alignItems="center">
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
      </Box>
      <button
        className="search-button"
        type="submit"
        onClick={() => {
          getSearchResult(searchQuery);
          console.log("search clicked");
          console.log(searchQuery);
        }}
      >
        Search
      </button>
    </Box>
  );
};
