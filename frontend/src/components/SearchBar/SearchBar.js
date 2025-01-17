import "./SearchBar.css";
import {
  Typography,
  Box,
  TextField,
  FormControl,
  InputLabel,
  Select,
  OutlinedInput,
  MenuItem,
  SvgIcon,
  IconButton,
} from "@mui/material";
import { useState } from "react";
import FavoriteIcon from "@mui/icons-material/Favorite";
import SearchIcon from "@mui/icons-material/Search";

/* const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 200,
    },
  },
}; */

export const SearchBar = ({
  searchQuery,
  selectedFilter,
  onSearch,
  onClick,
  setSearchQuery,
  setSearchResult,
}) => {
  const getSearchResult = async () => {
    try {
      const response = await fetch(
        // `http://localhost:8000/api/search?q=${searchQuery}`,
        `https://net-component-scraper.onrender.com/api/search?q=${searchQuery}`,
        {
          method: "GET",
        }
      );

      const data = await response.json();
      setSearchResult(data.data);
      console.log("Response from backend:", data);
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  return (
    <Box className="search-bar" display="flex" alignItems="center">
      <Box flex="1" display="flex" alignItems="center">
        <TextField
          className="text-area"
          defaultValue="Part No. TH8056KDC-AAA-014-RE..."
          onInput={(e) => {
            setSearchQuery(e.target.value);
          }}
          sx={{
            "& fieldset": { border: "none" },
          }}
        />
        <IconButton
          type="submit"
          aria-label="search"
          onClick={() => {
            getSearchResult(searchQuery);
            console.log("search clicked");
            console.log(searchQuery);
          }}
        >
          <SearchIcon className="search-icon" fontSize="large" />
        </IconButton>
      </Box>
    </Box>
  );
};
