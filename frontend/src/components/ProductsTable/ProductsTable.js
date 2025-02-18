import { Typography, Container, Paper, CircularProgress } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useState } from "react";
import FavoriteIcon from "@mui/icons-material/Favorite";
import SearchIcon from "@mui/icons-material/Search";
import { Product } from "../Product/Product";

export const ProductsTable = ({ products }) => {
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
  ];
  return (
    <Paper
      sx={{
        width: "100%",
        // backgroundColor: "",
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
  );
};
