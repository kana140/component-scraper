import {
  Typography,
  Container,
  TextField,
  FormControl,
  InputLabel,
  Select,
  OutlinedInput,
  MenuItem,
  SvgIcon,
  IconButton,
  Grid,
  Paper,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useState } from "react";
import FavoriteIcon from "@mui/icons-material/Favorite";
import SearchIcon from "@mui/icons-material/Search";
import { Product } from "../Product/Product";

export const ProductResult = ({ products }) => {
  const paginationModel = { page: 0, pageSize: 10 };
  products = products.map((row, index) => ({
    id: index + 1,
    ...row,
  }));

  const columns = [
    {
      field: "manufacturer",
      headerName: "Manufacturer",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "distributor",
      headerName: "Distributor",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "price",
      headerName: "Price",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "stock",
      headerName: "Stock",
      headerAlign: "center",
      flex: 1,
    },
    { field: "website", headerName: "Website", headerAlign: "center", flex: 1 },
    // {
    //   field: "link",
    //   headerName: "Link",
    //   headerAlign: "center",
    //   flex: 1,
    //   renderCell: (params) => (
    //     <a
    //       href={params.value}
    //       target="_blank"
    //       rel="noopener noreferrer"
    //       style={{ textDecoration: "none", color: "blue" }}
    //     >
    //       {params.value}
    //     </a>
    //   ),
    // },
  ];
  return (
    <Container
      className="search-result"
      display={products ? "flex" : "none"}
      alignItems="center"
    >
      {Array.isArray(products) && products.length > 0 ? (
        <Paper
          sx={{
            width: "100%",
            backgroundColor: "#f7fff7",
          }}
        >
          <DataGrid
            rows={products}
            columns={columns}
            initialState={{ pagination: { paginationModel } }}
            pageSizeOptions={[10, 50]}
            sx={{
              border: 0,
              m: 2,
              "& .MuiDataGrid-root": {
                height: "auto", // Expands dynamically
              },
            }}
            getRowId={(row) => row.id}
            onRowClick={(params) => {
              const url = params.row.link;
              if (url) {
                window.open(url, "_blank", "noopener,noreferrer");
              }
            }}
          />
        </Paper>
      ) : (
        <Container>
          <Typography align="center" variant="h6">
            {" "}
            No products found
          </Typography>
          <img src=""></img>
        </Container>
      )}
    </Container>
  );
};
