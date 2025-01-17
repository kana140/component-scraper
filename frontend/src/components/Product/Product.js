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
  Grid,
} from "@mui/material";
import { useState } from "react";
import FavoriteIcon from "@mui/icons-material/Favorite";
import SearchIcon from "@mui/icons-material/Search";

export const Product = ({ product }) => {
  return (
    <Box className="product" display="flex" alignItems="center">
      <p>{product.manufacturer}</p>
      <p>{product.price}</p>
      <p>{product.stock}</p>
    </Box>
  );
};
