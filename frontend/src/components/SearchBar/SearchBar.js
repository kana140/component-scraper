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
  Input,
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
  setIsLoading,
}) => {
  const getSearchResult = async () => {
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
        <Input
          className="text-area"
          placeholder="Enter SKU to search for products"
          disableUnderline
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
